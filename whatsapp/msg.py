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
msg = input("Message: ")
amount_of_times = int(input("How many times do you want to send the message? (use numbers) "))

browser = webdriver.Chrome(r'file/to/chromedriver/if/needed/otherwise/remove/r')
browser.get('https://web.whatsapp.com')

time.sleep(1)

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
send_msg = browser.find_element_by_class_name('_13mgZ')

for x in range(amount_of_times):
    send_msg.send_keys(msg)
    btn = browser.find_element_by_class_name('_3M-N-')
    btn.click()
