from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cool_and_util as u
import inputs
import constants as c
SLEEP_TIME = 1000

# Set up the webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # For Chrome, you can use webdriver.Firefox() for Firefox

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Wait for the page to load and find the username and password input fields
username_field = WebDriverWait(driver, SLEEP_TIME).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password_field = WebDriverWait(driver, SLEEP_TIME).until(
    EC.presence_of_element_located((By.ID, "password"))
)

# Enter your LinkedIn username and password
username_field.send_keys("gmartinialan@gmail.com")
password_field.send_keys("liAa!1234567in")

# Find and click the login button
login_button = WebDriverWait(driver, SLEEP_TIME).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entrar')]"))
)
login_button.click()

# Wait for the home page to load after successful login
WebDriverWait(driver, SLEEP_TIME).until(
    EC.url_contains("https://www.linkedin.com/feed/")
)

print("Successfully logged in to LinkedIn!")

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3880183128&f_AL=true&f_WT=2&keywords=Engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER')

# Wait until the jobss appear. Jobs list: document.querySelector("#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div > ul")
WebDriverWait(driver, SLEEP_TIME).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, c.JOB_LIST))
)

jobs_list = u.get_job_list(driver, By)

time.sleep(3)

u.scroll_to_the_bottom(driver, By)

# Get the job information. class: jobs-search__job-details--wrapper
job_info = driver.find_element(By.CSS_SELECTOR, ".jobs-search__job-details--wrapper")

#Click in the easy apply
easy_apply = driver.find_element(By.XPATH, r"//span[@class='artdeco-button__text' and text()='Easy Apply']")

easy_apply.click()
time.sleep(1)
# Wait until next is clickable
u.wait_until_next_and_click(driver)
u.wait_until_next_and_click(driver)


#Check options jobs-easy-apply-form-section__grouping
options = driver.find_elements(By.CSS_SELECTOR, ".jobs-easy-apply-form-section__grouping")


radios = []
texts = []
selects = []
options = driver.find_elements(By.CSS_SELECTOR, ".jobs-easy-apply-form-section__grouping")

for option in options:
    if inputs.RadioLinkedinInput(option).check_is_radio_type():
        radios.append(inputs.RadioLinkedinInput(option))
        print("Radio")
    elif inputs.TextLinkedinInput(option).check_is_text_type():
        texts.append(inputs.TextLinkedinInput(option))
        print("Text")
    elif inputs.SelectLinkedinInput(option).check_is_select_type():
        selects.append(inputs.SelectLinkedinInput(option))
        print("Select")
    else:
        print("Not found")
