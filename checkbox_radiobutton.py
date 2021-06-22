from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    x_element = browser.find_element_by_id('input_value')
    text = browser.find_element_by_id('answer')
    text.send_keys(calc(x_element.text))
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    submit = browser.find_element_by_css_selector('.btn-default')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
