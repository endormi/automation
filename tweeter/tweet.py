"""

author: @endormi
Automated tweeter

"""

from selenium import webdriver
import time


"""
Install browser driver:
https://www.seleniumhq.org/download/
"""

browser = webdriver.Chrome(r'file/to/driver/if/needed')
browser.get('https://twitter.com/login')


user = input("Username: ")
username = f'{user}'
password = input("Password: ")
__password__ = f'{password}'
tweet = input("Tweet: ")
__tweet__ = f'{tweet}'

user = browser.find_element_by_class_name('js-username-field')
user.send_keys(username)
pw = browser.find_element_by_class_name('js-password-field')
pw.send_keys(__password__)
log_in = browser.find_element_by_class_name('EdgeButtom--medium')
log_in.click()
time.sleep(1)
start_tweeting = browser.find_element_by_class_name('r-e7q0ms')
start_tweeting.click()
time.sleep(1)
tweet_content = browser.find_element_by_class_name('notranslate')
tweet_content.send_keys(__tweet__)
time.sleep(1)
tweet_button = browser.find_element_by_class_name('r-1n0xq6e')
tweet_button.click()
