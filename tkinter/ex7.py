import tkinter as tk

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x300')

# get()方法

def GET():
    if Z.get() == "":
        Z.set("cuteluluWindow")
    else:
        Z.set("")

Z = tk.StringVar() #字串變數

L= tk.Label (root, textvariable=Z,fg="#FFAAD5",bg="#7AFEC6", font=("Algerian","16","bold"),width=25,height=2)
L.pack()

btn = tk.Button(root,text="Click Me",relief="sunken",command=GET)
btn.pack()

root.mainloop()

# trace()方法
def write(*args):
    print(" changing data ：",zE.get())

zE = tk.StringVar()#字串變數
entry = tk.Entry(root,textvariable=zE)
entry.pack()
zE.trace("w",write) #"w"就是寫入

root.mainloop()

# read方法
def callbackW(*args):#*args可以直接傳遞參數內容，因為目前還不需要傳遞參數
    zl.set(zE.get())

def callbackR(*args):
    print(" 資料被讀取了 ")

def read():
    print(" read the data :",zE.get())

zE = tk.StringVar()#字串變數
entry = tk.Entry(root,textvariable=zE)
entry.pack()
zE.trace("w",callbackW)#如有更改執行這行callbackW
zE.trace("r",callbackR)#如有讀取執行這行callbackR

zl = tk.StringVar()#字串變數
lab = tk.Label(root,textvariable=zl)
zl.set(" 顯示於此 ")
lab.pack(pady=5,padx=10)

btn = tk.Button(root,text=" read ",command=read)
btn.pack(pady=10)

root.mainloop()