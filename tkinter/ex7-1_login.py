# 文字方塊Entry 輸入帳密
import tkinter as tk
root=tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x300')

def Info():
    root1 = tk.Tk()
    root1.title('cutelulu')
    root1.configure(bg="#7AFEC6")
    root1.geometry('300x300')
    if En.get()=='cutelulu' and En1.get()=='8888':#用get獲得帳密去判斷能不能登入
      l=tk.Label(root1, text='Login successful！', bg="#7AFEC6",fg='#FFD306',
                 font=("Viner Hand ITC",15,"bold"),anchor='c',width=50,height=10)
      l.pack()
    else:
      l=tk.Label(root1,text='Login Error！', bg="#7AFEC6",fg='#CE0000',
                 font=("Viner Hand ITC",15,"bold"),width=50,height=10,anchor='c')
      l.pack()

label=tk.Label(root,text='Account',bg='#DDA0DD',fg="#8B008B",
            font=("Algerian",15,"bold"),anchor='c')
label.grid(row=0)
En=tk.Entry(root)
En.grid(row=0,column=1)

label1=tk.Label(root,text='Password',bg='#DDA0DD',fg="#8B008B",
            font=("Algerian",15,"bold"),anchor='c')
label1.grid(row=1)
En1=tk.Entry(root,show='*')#隱藏密碼
En1.grid(row=1,column=1)

b=tk.Button(root,text='Exit',anchor='c',width=6,height=1,command=root.quit)#quit可以讓pyhon shell結束
b.grid(row=2,column=0)
b1=tk.Button(root,text='Login',anchor='c',width=6,height=1,command=Info)
b1.grid(row=2,column=1)

root.mainloop()