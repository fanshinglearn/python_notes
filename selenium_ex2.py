from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 等待網頁跑完
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = r'C:\Users\USER\Desktop\app\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# 網址
# driver.get('https://www.wnacg.org/')
driver.get('https://www.wnacg.org/albums-index-cate-9.html')

# 搜尋確認
search = driver.find_element('name', 'q')
search.clear()
search.send_keys('loli')
search.send_keys(Keys.RETURN)

# 等待網頁跑完
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'span12')))

# 點進去標題
link = driver.find_element(By.LINK_TEXT, 'Donna Loli - Ankha')
link.click()

# 上一頁 下一頁
driver.back()
driver.forward()

# 印出標題內容
# titles = driver.find_elements('class name', 'title')
titles = driver.find_elements(By.CLASS_NAME, 'title')

for title in titles:
    print(title.text)

time.sleep(3)
driver.quit()

