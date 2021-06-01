import requests
import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

def getPrizeMoney(amount):
    return int(re.findall("\d+", amount)[0])

url = "https://www.thelott.com/"

driver = webdriver.Chrome('./chromedriver') 
driver.get(url)

time.sleep(5) 

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

powerballSection = soup.find_all('li', class_='au-target powerball state-sa')

for section in powerballSection:
    amount = getPrizeMoney(section.find('div',class_='au-target jackpot').getText())

if amount > 40:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('tinothynguyen12@gmail.com', 'ysoomdieepmngezw')
    conn.sendmail('tinothynguyen12@gmail.com', 'tinothynguyen@gmail.com', 'Subject: Powerball Alert!!\n\nA prize pool of %d million has been announced!' % amount)
    conn.quit()

else:
    driver.close()
    driver.quit()


