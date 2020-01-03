"""

author: @endormi

Automated search testing
Generates report and displays current url

"""

import unittest
from selenium import webdriver
import time
import pyautogui
import HtmlTestRunner


"""
Install browser driver:
https://selenium.dev/downloads/
"""


class ChromeSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(r'file/to/driver/if/needed/otherwise/remove/r')
        cls.browser.maximize_window()

    def test_search_github(self):
        self.browser.get("https://www.github.com")
        time.sleep(1)
        self.browser.find_element_by_class_name('form-control').send_keys('Python')
        time.sleep(1)
        pyautogui.typewrite(["enter"])
        print(self.browser.current_url)

    def test_search_so(self):
        self.browser.get("https://stackoverflow.com/")
        time.sleep(1)
        self.browser.find_element_by_class_name('js-search-field').send_keys('Python')
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        print(self.browser.current_url)

    def test_search_amazon(self):
        self.browser.get("https://amazon.com/")
        time.sleep(1)
        self.browser.find_element_by_id('twotabsearchtextbox').send_keys('Python')
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        print(self.browser.current_url)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.browser.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output/path'))
