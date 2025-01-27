# 實作選項鈕
import tkinter as tk

root = tk.Tk()
root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x200')

def Selection ():
    print(schools [var.get()]) 

schools = {0:"國小",1:"國中",2:"高中",3:"大學",4:"碩士/博士"}


var = tk.IntVar()

var.set(0)
l = tk.Label(root, text="最高學歷" ,fg="#8B008B", bg="#7AFEC6", width=30)
l.pack()

for val, school in schools.items():
    R=tk.Radiobutton (root,text=school,variable=var, value=val,command=Selection)
    R.pack()

root.mainloop()

# 多選
import tkinter as tk

root = tk.Tk()
root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('350x200')

def fruitselect():
    selection = " "
    for i in checkboxes:
        if checkboxes[i].get() ==True:
            selection = selection + fruits[i] + "\t"
        print (selection)

l=tk.Label (root, text="Choise your favirot fruit. ", fg="#FFAAD5", bg="#7AFEC6",font=("Ravie",10,"bold"),width=30)
l.grid(row=0)

fruits = {0:"Strawberry",1: "Peach",2:"mango",3:"Cherry"}#矩陣內的內容

checkboxes = {}

for i in range (len (fruits)):
    checkboxes[i] = tk.BooleanVar()#布林值變數
    Cb = tk.Checkbutton(root, text=fruits[i], variable=checkboxes[i])
    Cb.grid (row=i+1)

btn = tk.Button (root, text="DOWN" ,width=10, command=fruitselect)

btn.grid(row=i+2)

root.mainloop()