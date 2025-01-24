from selenium import webdriver
import time

PATH = r'C:\Users\USER\Desktop\app\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html')
print(driver.title)
driver.quit()
