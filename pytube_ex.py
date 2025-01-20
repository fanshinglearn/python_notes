from pytube import YouTube
yt = YouTube('https://youtu.be/nU9TUouN3W4')

print(yt.watch_url)             # 網址
print(yt.video_id)              # id

print(yt.title)                 # 標題
print(yt.thumbnail_url.split('?')[0])         # 縮圖網址
print(yt.views)                 # 觀看數
print(yt.length)                # 長度 ( 秒 )

print(yt.author)                # 頻道EX/pytube_ex
print(yt.channel_url)           # 頻道網址

print(yt.publish_date)          # 上傳時間
print(yt.publish_date.year)
print(yt.publish_date.month)
print(yt.publish_date.day)

print(yt.streams)               # (15.0.0會報錯)
# 下載影片 15.0.0 有bug

from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLNE0caHGV5enmvBVaSlsQ-VR0wHGHdY2g')  # 讀取影片清單

print(playlist.playlist_id)     # id
print(playlist.playlist_url)    # 網址

print(playlist.video_urls)      # 播放清單影片網址
print(playlist.videos)          # yt 物件

print(playlist.title)           # 播放清單標題
print(playlist.length)          # 影片總數
print(playlist.views)           # 觀看次數
print(playlist.last_updated)    # 上次更新時間(可能出錯)

print(playlist.owner)           # 播放清單擁有者
print(playlist.owner_id)        # 播放清單擁有者頻道id
print(playlist.owner_url)       # 播放清單擁有者頻道網址
