# 滑鼠事件
# 鍵盤事件
import tkinter as tk

root = tk.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x150')

def key(event):
    print ("pressed",repr(event.char))

def cursors(event):
    frame.focus_set() #取得物件焦點
    print ("clicked at", event.x, event.y)

L=tk.Label(root,text="click your cursor first",
            font=("Algerian",15,"bold"),bg='#ADFEDC',fg='#00CACA')
L.pack()

frame = tk.Frame(root, width=300, height=150,bg="#7AFEC6")
frame.bind("<Key>", key)
frame.bind("<Button-1>", cursors)
frame.pack()

root.mainloop()