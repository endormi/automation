"""

author: @endormi

Automated login form testing and generate report

"""

from selenium import webdriver
import unittest
import HtmlTestRunner
import time


"""
Install browser driver:
https://selenium.dev/downloads/
"""


class login_form_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(r'file/to/driver/if/needed/otherwise/remove/r')
        cls.browser.maximize_window()

    def test_login_github(self):
        time.sleep(1)
        self.browser.get('https://github.com/login')
        self.browser.find_element_by_id('login_field').send_keys('username')
        self.browser.find_element_by_id('password').send_keys('password')
        self.browser.find_element_by_class_name('btn-block').click()

    def test_login_so(self):
        time.sleep(1)
        self.browser.get('https://stackoverflow.com/')
        self.browser.find_element_by_link_text('Log in').click()
        self.browser.find_element_by_id('email').send_keys('username')
        self.browser.find_element_by_id('password').send_keys('password')
        self.browser.find_element_by_id('submit-button').click()

    def test_login_twitter(self):
        time.sleep(1)
        self.browser.get('https://twitter.com/login')
        self.browser.find_element_by_class_name('js-username-field').send_keys('username')
        self.browser.find_element_by_class_name('js-password-field').send_keys('password')
        self.browser.find_element_by_class_name('EdgeButtom--medium').click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.browser.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output/path'))
