"""

author: @endormi

Automated file downloader using Selenium

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


"""
Install browser driver:
https://selenium.dev/downloads/
"""

options = Options()
options.add_experimental_option('prefs', {
  "download.default_directory": r'directory/you/choose',
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

browser = webdriver.Chrome(options=options, executable_path=r'file/to/driver/if/needed/otherwise/remove/r')
browser.get('https://chromedriver.chromium.org/')
time.sleep(1)
link = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td[2]/div/div[3]/div/table/tbody/tr/td/div/div[4]/ul/li[1]/a')
link.click()
dl_file = browser.find_element_by_xpath('/html/body/table/tbody/tr[6]/td[2]/a')
dl_file.click()
