# Button
import tkinter

root = tkinter.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x300')

B1=tkinter.Button(root,text='Normal Button',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             state=tkinter.NORMAL,#設定按鈕的狀態
             cursor='heart')
B2=tkinter.Button(root,text='Disabled Button',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             state=tkinter.DISABLED)#設定按鈕的狀態
B3=tkinter.Button(root,text='Active Button',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             state=tkinter.ACTIVE)#設定按鈕的狀態

B1.pack()
B2.pack()
B3.pack()

photo=tkinter.PhotoImage(file='shiro.gif')
B4=tkinter.Button(root,image=photo,text='Love',compound='top')#設定文字在圖的top
B4.pack()

root.mainloop()