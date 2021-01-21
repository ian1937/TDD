import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestBase(unittest.TestCase):
    # I open "localhost:5000" on the browser
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('localhost:5000')

    # I close the browser
    def tearDown(self):
        self.browser.quit()

    def input_data(self, data):
        input = self.browser.find_element_by_name('name')
        input.send_keys(data)
        submit = self.browser.find_element_by_name('submit')
        submit.click()


class TestMainPage(TestBase):
    # The browser shows me a HTML page
    def test_page_loads_up(self):
        self.assertIn('Product', self.browser.title)

    # The page has an input that says 'New Product'
    # I then input my new product
    # Then I press a button that says 'Submit'
    # The page reloads and my new product is now listed on the page
    def test_submit_and_data_retrieval(self):
        self.input_data('First Item')
        time.sleep(3)
        self.assertIn('First Item', self.browser.page_source)

    # It's still asking me for more items
    # I input another one
    # The page reloads again and added another product with the one before
    def test_submit_another_data(self):
        current_page = self.browser.page_source
        self.input_data('Second Item')
        time.sleep(3)
        self.assertNotEqual(current_page, self.browser.page_source)
        self.assertIn('Second Item', self.browser.page_source)

    # I tried inserting a blank data
    # It told me "Data Required"
    def test_submit_blank_data(self):
        current_page = self.browser.page_source
        self.input_data('')
        time.sleep(3)
        self.assertEqual(current_page, self.browser.page_source)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
