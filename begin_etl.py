import requests
import sqlite3
from datetime import date
import Pipeline

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

pipe = Pipeline()
pipe.extract('https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B2%5D=2&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title=')
pipe.transform()
pipe.load()
