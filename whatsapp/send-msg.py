"""

author: @endormi

Automated text sender for Whatsapp

"""

from selenium import webdriver
import time


browser = webdriver.Chrome(r'file/to/chromedriver/if/needed/otherwise/remove/r')
browser.get('https://web.whatsapp.com')

name = ''
message = ''

time.sleep(1)

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
send_msg = browser.find_element_by_class_name('_13mgZ')
send_msg.send_keys(message)
btn = browser.find_element_by_class_name('_3M-N-')
btn.click()
