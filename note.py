# 程式執行時間
import time
start_time = time.time()

pass

end_time = time.time()
execution_time = end_time - start_time

# 測試程式
if __name__ == '__main__':
    pass

# 沒有資料夾創建一個
import os
if not os.path.isdir('123'):
    os.mkdir('123')

# 使用瀏覽器打開網頁
import webbrowser
webbrowser.open('https://www.google.com.tw/?hl=zh_TW')

# 打開文件
import os
os.chdir('test_excel')
os.startfile('output.xlsx')
# 不使用chdir (反斜線)
os.startfile('test_excel\output.xlsx')

# 下載圖片
import requests
url = 'https://img.gamewith.jp/assets/images/games/covers/301e45348532fecf2a52b45c896853d1.png'
img = requests.get(url)
with open('test.png', 'wb') as file:
    file.write(img.content)


# 圖片像素
from PIL import Image
image = Image.open('test.jpg')
width, height = image.size

# 獲得位元組大小
import os
bytes_size = os.path.getsize('test.jpg')
    
# requests
# 找不到標籤時 可以印出前一個標籤內容 可能檢查的Html和爬取的Html中的 class 不同