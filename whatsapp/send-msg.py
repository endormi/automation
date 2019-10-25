"""

author: @endormi

Automated text sender for Whatsapp

"""

from selenium import webdriver


"""
Install browser driver:
https://www.seleniumhq.org/download/
"""

browser = webdriver.Chrome(r'file/to/chromedriver/if/needed/otherwise/remove/r')
browser.get('https://web.whatsapp.com')

name = ''
message = ''

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
message_content = browser.find_element_by_class_name('_13mgZ')
message_content.send_keys(message)
send_message = browser.find_element_by_class_name('_3M-N-')
send_message.click()
