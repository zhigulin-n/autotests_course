from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return str(int(x) + int(y))


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text

# ls = browser.find_element_by_css_selector("[class='custom-select']").click()
select = Select(browser.find_element_by_css_selector("[class='custom-select']"))
select.select_by_value(calc(x, y))
button = browser.find_element_by_css_selector('.btn-default').click()

time.sleep(20)
browser.quit()
