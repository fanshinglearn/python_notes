from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH = r'C:\Users\USER\Desktop\app\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# 網址
# driver.get('https://www.wnacg.org/')
driver.get('https://www.wnacg.org/albums-index-cate-9.html')

# 執行一連串動作
action = ActionChains(driver)

button = driver.find_element('')

# 動作
action.click(button)
action.move_to_element()

# 執行 搭配for
action.perform()

# 刪除多餘文字
button.text.replace('您目前擁有', '').replace('技術點', '')


