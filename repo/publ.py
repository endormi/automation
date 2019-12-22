"""

author: @endormi

Automated public repository creation

"""

from selenium import webdriver
import time


"""
Install browser driver:
https://www.seleniumhq.org/download/
"""

browser = webdriver.Chrome(r'file/to/chromedriver/if/needed/otherwise/remove/r')
browser.get('https://github.com/login')
browser.maximize_window()

user = ''
pw = ''
repo = ''
desc = ''

username = browser.find_element_by_id('login_field')
username.send_keys(user)
password = browser.find_element_by_id('password')
password.send_keys(pw)
log_in = browser.find_element_by_class_name('btn-block')
log_in.click()
new_repo = browser.find_element_by_link_text('New')
new_repo.click()
repo_name = browser.find_element_by_id('repository_name')
repo_name.send_keys(repo)
repo_desc = browser.find_element_by_id('repository_description')
repo_desc.send_keys(desc)
init = browser.find_element_by_id('repository_auto_init')
init.click()
time.sleep(1)

"""
Additional for marketplace apps:
app = browser.find_element_by_name('quick_install[your_name][number]')
app.click()
"""

create_repo = browser.find_element_by_class_name('first-in-line')
create_repo.click()
