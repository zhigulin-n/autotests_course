import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stepik.org/lesson/25969/step/12")
driver.implicitly_wait(5)
textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click()
