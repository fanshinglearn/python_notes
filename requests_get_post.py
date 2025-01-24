# 阿嬤都會

import requests

url = 'https://t4.qy0.ru/data/t/1813/47/1670061836489.jpg'

r = requests.get(url)
print(r.text)

# 下載檔案 r=網址
with open('123.jpg', mode='wb') as file:
    file.write(r.content)

# 上傳資料???
# https://httpbin.org/
params = {
    'page' : '2',
    'count' : '5'
}
data = {
    'name' : 'white',
    'age' : 23
}
r = requests.get(url, params=params, data=data)
r = requests.post(url, params=params, json=data)
print(r.text)

# 上傳圖片
with open('123.jpg', mode='rb') as file:
    image = { 'upload_image' : file.read()}
    r = requests.post(url, params=params, data=image)
    print(r.text)

# User-Agent
header = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
r = requests.get(url, headers=header)
print(r.text)

# 帳號密碼 等5秒
r = requests.get(url, auth=('123', '123'), timeout=5)
print(r.text)