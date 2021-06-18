from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    value1 = browser.find_element_by_name('first_name')
    value1.send_keys("Nikita")
    value2 = browser.find_element_by_name('last_name')
    value2.send_keys("Yung")
    value3 = browser.find_element_by_class_name('city')
    value3.send_keys("Kursk")
    value3 = browser.find_element_by_id('country')
    value3.send_keys("Russia")
    button = browser.find_element_by_class_name('btn-default')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
