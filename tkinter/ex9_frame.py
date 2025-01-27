# Frame框架
import tkinter as tk

root = tk.Tk()

root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('270x100')

'''上半部框架設定'''
frameUpper=tk.Frame (root, bg="#FFC1E0")#上半部分
frameUpper.pack()

btnyellow = tk.Button (frameUpper, text="yellow",fg="yellow")#黃色按鈕
btnyellow.pack (side='left', padx=10)

btnnavy = tk.Button (frameUpper, text="navy", fg="navy")#深藍色按鈕
btnnavy.pack (side='left', pady=10)

btncyan = tk.Button (frameUpper, text="cyan",fg="cyan")#天藍色按鈕
btncyan.pack (side = 'left', padx = 10, pady = 10)

'''下半部框架設定'''
frameLower = tk.Frame (root, bg="#EE82EE")#下半部分
frameLower.pack()

btnviolet = tk.Button (frameLower, text="violet", fg="violet")#紫色按鈕
btnviolet.pack(side='left', padx=10,pady=10)

btnmoccasin = tk.Button (frameLower, text="moccasin",fg="moccasin")#橙色按鈕
btnmoccasin.pack (side = 'left', padx = 10, pady = 10)

root.mainloop()

# LabelFrame
lF=tk.LabelFrame(root,text="Choise your favirot fruit.",fg="#FFAAD5", bg="#7AFEC6",font=("Ravie",10,"bold"),width=30)
lF.pack(ipadx=5,ipady=5,pady=10)

# Toplevel
# 這個空件會產稱一個獨立的視窗出來，會有自己的標題欄和邊框。
T1 = tk.Toplevel()

T1.title("Toplevel")
T1.geometry("300x180")
T1.configure(bg="skyblue")
T1.iconbitmap('star.ico')

l=tk.Label (T1, text = 'This is Toplevel',bg='skyblue',fg='mediumblue')
l.pack()