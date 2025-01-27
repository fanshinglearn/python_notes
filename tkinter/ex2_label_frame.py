# Label 標籤
import tkinter

# 視窗基本設定
root = tkinter.Tk()
root.title(':P')
root.geometry('400x200')

# 要注意一個視窗中不能同時使用 pack 與 grid 排版, 但 place 卻可以與 pack 或 grid 同時使用 !!!!!

# pack()用法
L1=tkinter.Label(root,text='I am Label',bg='#DDA0DD',fg="#8B008B",
            font=("Viner Hand ITC",18,"bold"), width=15)

L1.pack()
L1.pack(side='bottom')#下往上排
L1.pack(side='right',padx='10',ipadx='20')#由右排到左，左右間隔10，文字跟標籤邊界間隔20
L1.pack(anchor='s',side='right',padx=10,pady=10)#從右開始南方位置

# grid()方法
L1.grid(row=0,column=0,columnspan=2)#網格方法
L1.grid(row=0,column=1,rowspan=2)#網格方法
L1.grid(row=1,column=0)#網格方法

# sticky 參數的組合使用:
# sticky=N+S:拉長高度使控件在頂端和底端對齊
# sticky=W+E:拉長寬度度使控件在左邊和右邊對齊
# sticky=N+S+E:拉長高度使控件在頂端和底端對齊且同時切齊右邊
# sticky=N+S+W:拉長高度使控件在頂端和底端對齊且同時切齊左邊
# sticky=N+S+W+E:拉長高度使控件在頂端和底端對齊且同時切齊左右兩邊
L1.grid(row=0,column=0,columnspan=2,sticky=tkinter.E+tkinter.W)#網格方法

L1.place(x=0,y=0,height=100,width=200)#位置在(0,0)，高100寬200
L1.place(x=100,y=100,height=200,width=200)#位置在(100,100)，高200寬200
L1.place(x=250,y=250,height=150,width=200)#位置在(150,150)，高150寬200

# 圖片
song=tkinter.PhotoImage(file="Ferris wheel.gif")
L1=tkinter.Label(root,image=song)

L1.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

F1=tkinter.Frame(root, borderwidth=5, relief="ridge", width=90, height=50)
L1=tkinter.Label(F1, text="Welcome")
F2=tkinter.Frame(root, borderwidth=5, relief="ridge", width=90, height=50)
L2=tkinter.Label(F2, text="Welcome")

F1.pack()
F2.pack()
L1.place(x=10, y=10, bordermode="outside")#在父容器外
L2.place(x=10, y=10, bordermode="inside")#在父容器內

root.mainloop()