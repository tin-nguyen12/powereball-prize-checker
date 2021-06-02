#! python3

import requests
import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

#Takes in a string variable and extracts the integer only
def getPrizeMoney(amount):
    return int(re.findall("\d+", amount)[0])

driver = webdriver.Chrome('C:/Users/ngutt094/Google Drive/Miscellaneous/Programming/Python/Powerball Check/powereball-prize-checker/chromedriver.exe') 
driver.get("https://www.thelott.com/")

#Ensures that the page opens
time.sleep(5) 

#Gets the html source of the dynamic website
html = driver.page_source

#Closes the browser and driver
driver.close()
driver.quit()

#Converts the html into something easier read
soup = BeautifulSoup(html, "html.parser")

#Extracts the necessary element
powerballSection = soup.find_all('li', class_='au-target powerball state-sa')

#Searches through and looks for the section where the prize pool is mentioned
for section in powerballSection:
    amount = getPrizeMoney(section.find('div',class_='au-target jackpot').getText())

#If the amonut is above this number (i.e. 40 (40 million)) then an email is sent to the designated email address
if amount > 40:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('tinothynguyen12@gmail.com', 'ysoomdieepmngezw')
    conn.sendmail('tinothynguyen12@gmail.com', 'tinothynguyen@gmail.com', 'Subject: Powerball Alert!!\n\nA prize pool of %d million has been announced!' % amount)
    conn.quit()

