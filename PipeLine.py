import requests
import sqlite3
from datetime import date

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

  '''
  This Pipeline is responsible for extracting, transformating, and loading data 
  into the database created during instantiation when a link a fed into it.
  '''
class Pipeline():
  ''' 
  Constrctor of the Pipeine
  '''
    def __init__(self):
        self.date = ''.join(str(date.today()).split('-'))
        self.con = sqlite3.connect('Data.db')
        self.curr = self.con.cursor()
        self.createTable()
  
  '''
  This function creates a table in a database.
  If the table exists, it won't create a new table
  '''
    def createTable(self):
        # print('''CREATE TABLE IF NOT EXISTS Directory_'''+self.date+'''(Name VARCHAR, ID INT PRIMARY KEY)''')
        self.curr.execute("CREATE TABLE IF NOT EXISTS NewsBias (News text, link text, bias text, agree integer, disagree integer, ratio real);")
        self.con.commit()
  
  '''
  This function process each block of data and inserts them into the table in the database
  '''
    def processItem(self, item):
        self.curr.execute("INSERT OR IGNORE INTO NewsBias  VALUES (?, ?, ?, ?, ?, ?)", [item['News'], item['link'], item['bias'], item['agree'], item['disagree'], item['ratio']])
        self.con.commit()

  '''
  This function extracts the html strucuture of the page
  and divides them into rows using Selenium, Chrome websriver,
  and Beautiful Soup
  '''
    def extract(self, link):
        browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        browser.get(link)
        r = scrollDown(browser, 125)
        # r = requests.get(link)
        # self.site = BS(r.content, 'html.parser')
        self.site = BS(r.page_source, 'html.parser')
        # print(self.parsed_site)
        self.rows = self.site.select('tbody tr')
    
    '''
    This function transforms the HTML data into readable data
    '''
    def transform(self):
        for row in self.rows:
            news.append(row.select_one('a').text.strip())
            newslink.append('https://www.allsides.com' + row.select_one('a')['href'])
            bias.append(row.select('a')[1]['href'].split('/')[-1].split('-'))
            a = int(row.select_one('.community-feedback .agree').text)
            d = int(row.select_one('.community-feedback .disagree').text)
            agree.append(a)
            disagree.append(d)
            ratio.append(a/d)
    
    '''
    This function loads the transformed data 
    into the table of the database
    '''
    def load(self):
        for n, l, b, a, d, r in zip(news, newslink, bias, agree, disagree, ratio):
            data = {'News': n, 'link': l, 'bias': '|'.join(b), 'agree': a, 'disagree': d, 'ratio': r}
            self.processItem(data)
        self.con.close()

pipe = Pipeline()
pipe.extract('https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B2%5D=2&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title=')
pipe.transform()
pipe.load()
