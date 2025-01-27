# 點擊按鈕更改label內容
from tkinter import *
root = Tk()

def msg_show():
    L1['text'] = '>w<'
    L1['bg'] = 'lightblue'
    L1['fg'] = 'blue'

L1 = Label(root, text='owo')
B1 = Button(root, text='Hit', command=msg_show)
B2 = Button(root, text='Exit', command=root.destroy)

L1.pack()
B1.pack()
B2.pack()

root.mainloop()