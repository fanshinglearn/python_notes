from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 等待網頁跑完
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import os
import wget

PATH = r'C:\Users\USER\Desktop\app\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# 網址
# driver.get('https://www.wnacg.org/')
driver.get('https://www.wnacg.org/albums-index-cate-9.html')


# 等待輸入帳號密碼
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

# 清空欄位
username.clear()
password.clear()

# 輸入密碼
username.send_keys('fanshing')
password.send_keys('12345678')

# 確認
login = driver.find_element(By.XPATH, '//qwe')
login.click()

# 搜尋框
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'search')))

# 搜尋 cat
keyword = '#cat'
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

# 等搜尋完畢
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ffac')))



path = os.path.join(keyword)
os.mkdir(path)

# 往下滑5次
for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrolllHeight);')
    time.sleep(5)

# 找出圖片
imgs = driver.find_element(By.CLASS_NAME, 'q')

# 創建名為 keyword 的資料夾
path = os.path.join(keyword)
os.mkdir(path)

# 下載圖片
count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + 'jpg')
    wget.download(img.get_attribute('src'), save_as)
    count += 1
    # print(img.get_attribute('src'))


time.sleep(3)
driver.quit()

