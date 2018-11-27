from selenium import webdriver
import requests
import time
import datetime
import psycopg2
import sys
sys.path.append('../')
from database.config import config
import dateutil.parser
import pytz
from operator import attrgetter
from flex_backend.models import *

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
        time.sleep(10)

    def getCSV(self):
        today = datetime.date.today().isoformat()
        print(today)
        url = 'https://cards.cuc.claremont.edu/statementdetail.php?cid=35&skey=%s&format=csv&startdate=2015-09-01&enddate=%s&acct=21'%(self.skey, today)
        r = requests.get( url, cookies = self.cookies)
        print(r.text)
        self.data = r.text.split('\n')[1:-1]

    def updateFlex(self):
        '''Before calling this function, getCSV() should be called.'''
        #login = config()
        #conn = psycopg2.connect(**login)
        #curs = conn.cursor()
        #date = max(p,key=attrgetter("date"))
        #sql = "SELECT date FROM flex_backend_flex_transaction WHERE user_id = {} ORDER BY date asc LIMIT 1".format(self.id)
        #curs.execute(sql)
        #date = curs.fetchall()[0][0]

        date = max(flex_transaction.objects.filter(user_id = self.id), key=attrgetter("date")).date
        print(self.data[0].split(','))
        current = float(self.data[0].split(',')[3])
        flex = flex_info.objects.get(user_id=self.id)
        flex.current_flex = current
        flex.save()
        for i in self.data:
            j = i.split(',')
            print(j)
            j[0] = dateutil.parser.parse(j[0])
            timezone = pytz.timezone("America/Los_Angeles")
            j[0] = timezone.localize(j[0])
            #j[0] = j[0].replace(tzinfo=date.tzinfo)

            if j[0] > date:
                new = flex_transaction(user_id=self.id, date=j[0], location=j[1].split(" - ")[0], transaction_type=j[1].split(" - ")[1], transaction_amount=float(j[2]), balance=float(j[3]))
                new.save()
                #sql = "INSERT INTO flex_backend_flex_transaction (user_id, date, location, transaction_type, transaction_amount, balence) VALUES ({}, '{}', '{}', '{}', {}, {}) ".format(int(self.id), j[0], j[1].split(" - ")[0].replace("'", "''"), j[1].split(" - ")[1], float(j[2]), float(j[3]))
                #curs.execute(sql)

                #conn.commit()
                #curs.close()
                #conn.close()

#p = flex_transaction.objects.all(). .get(user_id = 8, ) .filter() access_key__isnull = False 

#max(p,key=attrgetter("date"))

def main():
    allFlex = flex_info.objects.exclude(access_key = '')
    for i in allFlex:
        flex = FlexScrapper(i.user_id, i.access_key)
        flex.getCookies()
        flex.getCSV()
        flex.updateFlex()

if __name__ == "__main__":
    main()
