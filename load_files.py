from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
browser.find_element_by_css_selector("[name='firstname']").send_keys('nick')
browser.find_element_by_css_selector("[name='lastname']").send_keys('zhig')
browser.find_element_by_css_selector("[name='email']").send_kesys('zhig@mail.ru')
browser.find_element_by_css_selector("[name='file']").send_keys(os.path.abspath('text.txt'))
browser.find_element_by_class_name('btn-primary').click()
time.sleep(30)
browser.quit()


