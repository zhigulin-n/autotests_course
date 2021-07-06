from selenium import webdriver
import time
import math
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_test(browser, link):
    browser.get(link)
    browser.find_element_by_css_selector('textarea').send_keys(str(math.log(int(time.time() + 19.8))))
    browser.find_element_by_css_selector('[class="submit-submission"]').click()
    text = browser.find_element_by_css_selector('[class="smart-hints__hint"]').text
    assert text == 'Correct!', text
