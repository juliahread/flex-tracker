from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
'''
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
driver = webdriver.PhantomJS()
url = 'https://cards.cuc.claremont.edu'
driver.get(url)
url ='login.php?cid=35&'
driver.find_element_by_xpath('//a[@href="'+url+'"]').click()

skey = driver.find_element_by_name('skey').get_attribute("value")
driver.find_element_by_id("loginphrase").send_keys('muddflextracker@gmail.com')
driver.find_element_by_id("password").send_keys('GTW3RJ3DFR')
cookies = driver.get_cookies()

driver.find_elements_by_class_name('jsa_submit-form')[0].click()
driver.close()
#cookies1 = driver.get_cookies()
cookie = {}
for i in cookies:
    cookie[i['name']] = i['value']
#print(cookies1)
#print(cookies)
url = 'https://cards.cuc.claremont.edu/statementdetail.php?cid=35&skey=%s&format=csv&startdate=2018-10-01&enddate=2018-10-31&acct=21'%skey
time.sleep(1)
r = requests.get( url, cookies = cookie)
print(r.text)
#time.sleep(10)
#cookies = driver.get_cookies()
#print(cookies)
'''
url = 'statementnew.php?cid=35&amp;acctto=21'
#<a href="statementnew.php?cid=35&amp;acctto=21">View More</a>
driver.find_elements_by_xpath("//*[contains(text(), 'View More')]")[0].click()
driver.find_elements_by_xpath("//*[contains(text(), 'CSV')]")[0].click()
'''