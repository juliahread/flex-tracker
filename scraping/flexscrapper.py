from selenium import webdriver
import requests
import time
import datetime
import psycopg2
import sys
sys.path.append('../')
from database.config import config
import dateutil.parser

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

    def __init__(self, userId, userToken):
        """
        Inits with unique user ID/token which is used to log into their data
        """
        self.token = userToken
        self.cookies = {}
        self.skey = ''
        self.data = ''
        self.id = userId

    def getCookies(self):
        url = 'https://cards.cuc.claremont.edu/login.php'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("download.default_directory=/home")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("-incognito")
        driver = webdriver.Chrome(chrome_options=chrome_options)
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
        self.data = r.text.split('\n')[1:]

    def updateFlex(self):
        '''Before calling this function, getCSV() should be called.'''
        login = config()
        conn = psycopg2.connect(**login)
        curs = conn.cursor()

        sql = "SELECT date FROM flex_backend_flex_transaction WHERE user_id = {} LIMIT 1".format(self.id)
        curs.execute(sql)
        date = curs.fetchall()[0][0]
        for i in self.data:
            j = i.split(',')
            j[0] = dateutil.parser.parse(j[0])
            j[0] = j[0].replace(tzinfo=date.tzinfo)

            if j[0] > date:
                sql = "INSERT INTO flex_backend_flex_transaction (user_id, date, location, transaction_type, transaction_amount, balence) VALUES ({}, '{}', '{}', '{}', {}, {}) ".format(int(self.id), j[0], j[1].split(" - ")[0].replace("'", "''"), j[1].split(" - ")[1], float(j[2]), float(j[3]))
                curs.execute(sql)

                conn.commit()
                curs.close()
                conn.close()
