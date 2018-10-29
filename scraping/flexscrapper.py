from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import datetime

'''
Other Option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("download.default_directory=/home")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("-incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
'''
'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="/usr/local/bin/geckodriver")
'''

class FlexScrapper():
    """
    Class for scrapping the cards.cuc webpage
    """

    def __init__(self, userToken):
        """
        Inits with unique user ID/token which is used to log into their data
        """
        self.token = userToken
        self.cookies = {}
        self.skey = ''
        self.data = ''

    def getCookies(self):
        url = 'https://cards.cuc.claremont.edu/login.php'
        driver = webdriver.PhantomJS()
        driver.get(url)
        self.skey = driver.find_element_by_name('skey').get_attribute("value")
        driver.find_element_by_id("loginphrase").send_keys('muddflextracker@gmail.com')
        driver.find_element_by_id("password").send_keys(self.token)
        cookies = driver.get_cookies()
        driver.find_elements_by_class_name('jsa_submit-form')[0].click()
        cookie = {}
        for i in cookies:
            cookie[i['name']] = i['value']
        self.cookies = cookie


    def getCSV(self):
        today = datetime.date.today().isoformat()
        url = 'https://cards.cuc.claremont.edu/statementdetail.php?cid=35&skey=%s&format=csv&startdate=2015-09-01&enddate=%s&acct=21'%(self.skey, today)
        r = requests.get( url, cookies = self.cookies)
        self.data = r.text


