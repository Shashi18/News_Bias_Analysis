import requests
import sqlite3
from datetime import date
import pipeline

# !pip install selenium
# !apt-get update 
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
# !pip install pyvirtualdisplay
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

#!pip3 install requests requests selectorlib
#!pip install beautifulsoup4
from bs4 import BeautifulSoup as BS
news = []
newslink = []
bias = []
agree = []
disagree = []
ratio = []

def scrollDown(browser, numberOfScrollDowns):
    body = browser.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return browser
