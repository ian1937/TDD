import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestMainPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('localhost:5000')

    def tearDown(self):
        self.browser.quit()

    # I open "localhost:5000" on the browser
    # The browser shows me a HTML page
    def test_page_loads_up(self):
        self.assertIn('To-Do', self.browser.title)

    # The page has an input that says 'Your To-Do'
    # I then input my to-do plan
    # Then I press a button that says 'Submit'
    def test_submit_and_data_retrieval(self):
        input = self.browser.find_element_by_name('input')
        input.send_keys('Say Hello')
        submit = self.browser.find_element_by_name('input')
        submit.click()
        time.sleep(3)
        self.assertIn('Say Hello', self.browser.page_source)

    # The page reloads and my to-do is now listed on the page
    # It's still asking me for more To-Do
    # I input another one
    # The page reloads again and added another to-do with the one before


if __name__ == '__main__':
    unittest.main(warnings='ignore')
