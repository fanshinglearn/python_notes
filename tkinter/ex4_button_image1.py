# Label 2
import tkinter

root = tkinter.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")

# 按鈕按一次顯示+1
text=tkinter.Label(root, text="Hello\@^0^@/",font=("Bauhaus 93",20,"bold"))

count=0
def clickHello():
    global count
    count=count + 1
    text.config(text="Click Hello " + str(count) + " times")
B=tkinter.Button(root, text="Hello", command=clickHello,font=("Bauhaus 93",20,"bold"))

text.pack()
B.pack()

# 加入jpg圖片
from PIL import Image,ImageTk
image=Image.open("test.jpg")
test=ImageTk.PhotoImage(image)
text=tkinter.Label(root,image=test)
text.pack() 

# Separator分隔線
from tkinter.ttk import Separator
sep=Separator(root,orient=tkinter.HORIZONTAL) #分隔線
sep.pack(fill='x',padx=7)

root.mainloop()
