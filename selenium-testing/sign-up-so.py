"""

author: @endormi

Automated stack overflow sign up form testing and generate report

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

    def test_signup_so(self):
        time.sleep(1)
        self.browser.get('https://stackoverflow.com/')
        self.browser.find_element_by_link_text('Sign up').click()
        self.browser.find_element_by_id('display-name').send_keys('username')
        self.browser.find_element_by_id('email').send_keys('example@gmail.com')
        self.browser.find_element_by_id('password').send_keys('password')
        self.browser.find_element_by_id('opt-in').click()
        time.sleep(1)
        self.browser.find_element_by_id('submit-button').click()

    def test_signup_with_gmail_auth(self):
        time.sleep(1)
        self.browser.get('https://stackoverflow.com/')
        self.browser.find_element_by_link_text('Sign up').click()
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/button[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys('username')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('password')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()

    def test_signup_with_github_auth(self):
        time.sleep(1)
        self.browser.get('https://stackoverflow.com/')
        self.browser.find_element_by_link_text('Sign up').click()
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/button[2]').click()
        self.browser.find_element_by_id('login_field').send_keys('username')
        self.browser.find_element_by_id('password').send_keys('password')
        self.browser.find_element_by_class_name('btn-block').click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.browser.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output/path'))
