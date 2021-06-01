import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.thelott.com/"

driver = webdriver.Chrome('./chromedriver') 
driver.get(url)

time.sleep(5) 

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

powerballSection = soup.find_all('li', class_='au-target powerball state-sa')

