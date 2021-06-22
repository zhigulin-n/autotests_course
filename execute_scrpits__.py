from selenium import webdriver
from math import log, sin
import time

def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))
browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_class_name('btn-primary'))
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_class_name('btn-primary').click()
time.sleep(30)
browser.quit()

