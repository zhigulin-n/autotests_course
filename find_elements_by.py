from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    elements = browser.find_elements_by_css_selector('input[type]')
    for element in elements:
        element.send_keys('test')
    button = browser.find_element_by_css_selector('.btn-default')
    button.click()

finally:
    time.sleep(30)
    browser.quit()