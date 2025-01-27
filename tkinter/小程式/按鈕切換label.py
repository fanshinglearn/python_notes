# 點擊按鈕切換label內容
from tkinter import *
root = Tk()

def btn_hit():
    global msg_on
    msg_on = not msg_on
    x.set('owo' if msg_on else '>w<')

msg_on = False
x = StringVar()

L1 = Label(root, textvariable=x)
B1 = Button(root, text='Hit', command=btn_hit)
B2 = Button(root, text='Exit', command=root.destroy)

L1.pack()
B1.pack()
B2.pack()

root.mainloop()