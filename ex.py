import pyautogui
import time

# 滑鼠移到左上角安全停止
pyautogui.FAILSAFE = True

# 每個動作間隔0.5秒
pyautogui.PAUSE = 0.5

#螢幕大小
size = pyautogui.size()
print(size)

#鼠標座標
mouse_pos = pyautogui.position()
print(mouse_pos)

#判斷點是否在螢幕內
print(pyautogui.onScreen(100,100))

#移動到座標10,10
pyautogui.moveTo(10,10,duration=1)

#移動到螢幕正中央
pyautogui.moveTo(size.width/2,size.height/2,duration=1)

#鼠標相對移動
pyautogui.moveRel(0,100,duration=1)

#上一次的位置
last_pos = pyautogui.position()
try:
    while True:
        #新位置
        new_pos = pyautogui.position()
        if last_pos != new_pos:
            print(new_pos)
            last_pos = new_pos
except KeyboardInterrupt:
    print('\nExit')

#鼠標的移動加點擊
lol_pos = pyautogui.locateOnScreen('1.png')
print(lol_pos)
goto_pos = pyautogui.center(lol_pos)
pyautogui.click()

# 輸入
pyautogui.typewrite('cat')
pyautogui.typewrite('\nmeow',0.25)
pyautogui.typewrite(['enter','g','o','o','d','left','left','left','backspace','G','end','.'],0.25)

# 記事本打出時間
pyautogui.press('f5')

# ctrl + A + C
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

# 貼上
pyautogui.hotkey('ctrl','v')

import keyboard
import pydirectinput

# LOL 輸入使用 keyboard.write 比較快
def say(txt):
    pydirectinput.press('enter')
    keyboard.write(txt)
    pydirectinput.press('enter')

# 等到按下 0
keyboard.wait('0')

