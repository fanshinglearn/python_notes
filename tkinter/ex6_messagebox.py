import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x200')

# Message 的功能
mes = '謝謝大家點進來看我的文章，有任何問題都歡迎留言討喔~❤❤❤'
msg =tk.Message(root,text=mes,font=("Algerian",18,"bold"),bg='#ADFEDC',fg='#00CACA')
msg.pack()

# tkinter messagebox 基本用法

# 一般訊息
messagebox.showinfo('My messagebox','Hola')

# 警告訊息
messagebox.showwarning('My messagebox','Oops!')

# 錯誤訊息
messagebox.showerror('My messagebox','Error!!!')

# 問問題對話框，確定或取消
messagebox.askokcancel('My messagebox','Cancel or not ?')
messagebox.askquestion('My messagebox','Are you sure you want to leave ?')

# 問問題對話框，是或否或取消
messagebox.askyesnocancel('My messagebox','是或否或取消?')

# 重試或取消對話框
messagebox.askretrycancel('My messagebox','重試或取消?')

root.mainloop()
