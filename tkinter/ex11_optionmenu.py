# 下拉式選單
import tkinter as tk

root = tk.Tk()

root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x300')

def get():
    print("You select ",var.get())

sets=("cellphone","computer","book")
var =tk.StringVar(root) 
var.set("book")

opm=tk.OptionMenu(root, var, *sets)
opm.pack()

b=tk.Button(root,text="Get",command=get)
b.pack(pady=10)

root.mainloop()