from selenium.webdriver.common.by import By
from openai_controller import ask_gpt


class LinkedinInput:
    def __init__(self, form_section_grouping) -> None:
        self.form_section_grouping = form_section_grouping

    def check_is_type(self, type):
        try:
            # Get the inputs
            input_elements = self.form_section_grouping.find_elements(By.TAG_NAME, "input")

            if len(input_elements) == 0:
                return False

            # Check if is radio
            is_all_radio = [
                input_element.get_attribute('type') == type for input_element in input_elements
            ]

            print("is_all", is_all_radio)

            return all(is_all_radio)
        except:
            return False


class RadioLinkedinInput(LinkedinInput):
    def check_is_radio_type(self):
        return  self.check_is_type("radio")

    def get_question(self):
        return self.form_section_grouping.find_element(By.TAG_NAME, "legend").text

    def get_input_options(self):
        return self.form_section_grouping.find_elements(By.TAG_NAME, "input")

    def click_in_input_with_value(self, value):
        for input in self.get_input_options():
            if input.get_attribute("value") == value:
                input.find_element(
                        By.XPATH, ".."
                    ).find_element(
                            By.TAG_NAME, 'label'
                        ).click()

                break

    def fill_input(self):
        for yes_possibilitie in ["yes", "Yes", "YES", "y", "Y", 'Sí']:
            try:
                self.click_in_input_with_value(yes_possibilitie)
            except:
                continue
            

class TextLinkedinInput(LinkedinInput):
    def check_is_text_type(self):
        return  self.check_is_type("text")

    def get_question(self):
        return self.form_section_grouping.find_element(By.TAG_NAME, "label").text

    def get_input(self):
        return self.form_section_grouping.find_element(By.TAG_NAME, "input")

    def write_to_input(self, text):
        input = self.get_input()
        input.clear()
        input.send_keys(text)

    def check_if_is_empty(self):
        return self.get_input().get_attribute("value") == ""

    def fill_input(self):
        question = self.get_question()

        words_to_check = [
            "years", "year", "ano",
            "experience", "experiência",
            "tempo", "work", "trabalho",
            "com", "with", "em", "de",
            ]

        if any([word in question.lower() for word in words_to_check]):
            self.write_to_input('1')
            return
        
        if not self.check_if_is_empty():
            return

        response = ask_gpt(self.get_question())
        self.write_to_input(response)
        

class SelectLinkedinInput(LinkedinInput):
    def check_is_select_type(self):
        try:
            # Get the inputs
            input_elements = self.form_section_grouping.find_elements(By.TAG_NAME, "select")

            return len(input_elements) > 0
        except:
            return False

    def get_question(self):
        select = self.form_section_grouping.find_element(By.TAG_NAME, "select")
        select_father = select.find_element(By.XPATH, "..")
        label = select_father.find_element(By.TAG_NAME, "label")
        label_first_span = label.find_element(By.TAG_NAME, "span")
        return label_first_span.text

    def get_all_options_as_array(self):
        select = self.form_section_grouping.find_element(By.TAG_NAME, "select")
        options = select.find_elements(By.TAG_NAME, "option")
        return [option for option in options]

    def select_option(self, option):
        options = self.get_all_options_as_array()
        for option_element in options:
            if option_element.text == option:
                option_element.click()
                break

    def fill_input(self):
        all_options = [
            option.text for option in self.get_all_options_as_array()
        ]

        print("all options are", all_options)
        text = self.get_question() + "options are:" + ' '.join(all_options)
        response = ask_gpt(text)
        print("select question is", self.get_question())
        print("response for select is", response)
        self.select_option(response)

