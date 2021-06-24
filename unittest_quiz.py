import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_first(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get('http://suninjuly.github.io/registration1.html')
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']").send_keys('1')
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']").send_keys('2')
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']").send_keys('3')
        browser.find_element_by_class_name("btn").click()
        result_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual('Congratulations! You have successfully registered!', result_text, 'Ожидаемый текст не совпал с фактическим')

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        value1 = browser.find_element_by_xpath('//div[@class=\'first_block\']//input[@class=\'form-control first\']')
        value1.send_keys('nick')
        value2 = browser.find_element_by_xpath('//div[@class=\'first_block\']//input[@class=\'form-control second\']')
        value2.send_keys('zhig')
        value3 = browser.find_element_by_xpath('//div[@class=\'first_block\']//input[@class=\'form-control third\']')
        value3.send_keys('123@gmail.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Ожидаемый текст не совпал с фактическим')

if __name__ == "__main__":
    unittest.main()