import time
import constants as c
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_job_list(driver, By):
    return driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div > ul")


def get_job_item(driver, By, index_job=0):
    jobs_list = get_job_list(driver, By)

    click_target = jobs_list.find_elements(By.CSS_SELECTOR, "li > div > div")[index_job]
    return click_target
    
def click_in_each_item(job_list, driver, By):
    lis = job_list.find_elements(By.CSS_SELECTOR, "li")

    for i, item in enumerate(lis):
        job = get_job_item(driver, By, i)
        job.click()
        time.sleep(1)

# Function that finds a list and scroll the list until the end
def scroll_to_the_bottom(driver, By):
    SCROLL_PAUSE_TIME = 0.5

    # Get scrollable item
    scrollable_item = driver.find_element(By.CSS_SELECTOR, c.SCROLLABLE_ITEM)

    # Get current height of the scrollable item
    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_item)

    while True:
        # Scroll down to bottom
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_item)

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_item)
        if new_height == last_height:
            break
        last_height = new_height


def wait_until_next_and_click(driver):
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, c.NEXT_BUTTON))
    )
    WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, c.NEXT_BUTTON))
    )

    next_button = driver.find_element(By.XPATH, c.NEXT_BUTTON)
    next_button.click()

# Class that holds each form question in a page
# class = jobs-easy-apply-form-section__grouping
# Title -> class > div > div > div > div
#
        


# If is a select with only yes or no, answer yes

# If the question is open, send to openai, but only if there is nothing already written to it.

# If the button is review, the next is submit.

