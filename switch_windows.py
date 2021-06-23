from selenium import webdriver
import time
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
browser.find_element_by_class_name('btn-primary').click()
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
browser.find_element_by_class_name('btn-primary').click()

time.sleep(30)
browser.quit()
