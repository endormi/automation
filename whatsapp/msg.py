"""

author: @endormi

Automated text sender for Whatsapp

"""

from selenium import webdriver
import time


"""
Install browser driver:
https://www.seleniumhq.org/download/
"""

name = input("Name: ")
__name__ = f'{name}'
msg = input("Message: ")
__msg__ = f'{msg}'

browser = webdriver.Chrome(r'file/to/chromedriver/if/needed/otherwise/remove/r')
browser.get('https://web.whatsapp.com')

time.sleep(1)

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(__name__))
user.click()
send_msg = browser.find_element_by_class_name('_13mgZ')


for x in range(amount_of_times):
    send_msg.send_keys(__msg__)
    btn = browser.find_element_by_class_name('_3M-N-')
    btn.click()
