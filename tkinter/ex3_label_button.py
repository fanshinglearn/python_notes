# Label 的語法
import tkinter

# 視窗基本設定
root = tkinter.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('400x200')

gif=tkinter.PhotoImage(file="shiro.gif")

# 標籤各種參數
text=tkinter.Label(root, text='I am Label', #建立標籤
              height=7,width=25, #設定標籤高度為7寬度為25
              fg="#FF8000",bg="#02DF82", #更改前景與背景的顏色
              font=("Bauhaus 93",18,"bold","italic","underline"), #設定字型
              anchor='se', #設定標籤位置
              cursor='draped_box', #設定滑鼠移到標籤上後會變成星星圖案
              wraplength=40, #40像素後自動換行
              justify="right", #文字靠右
              compound="center", # 同時有圖像與文字時，定義圖像與文字的位置
              padx=15,pady=20, #左右間隔5，上下間隔10
              image=gif) #加入Gif動態圖片

# compound()參數
# left:圖在文字左側
# right:圖在文字右側
# top:圖在文字上面
# bottom:圖在文字下方面
# center:文字覆蓋在圖像上

text.pack()

# 不同形狀的按鈕
R1 = tkinter.Button(root, text ="FLAT", relief="flat") #建立flat標籤
R2 = tkinter.Button(root, text ="RAISED", relief="raised") #建立raised標籤 常見?
R3 = tkinter.Button(root, text ="SUNKEN", relief="sunken") #建立sunken標籤
R4 = tkinter.Button(root, text ="GROOVE", relief="groove") #建立groove標籤
R5 = tkinter.Button(root, text ="RIDGE", relief="ridge") #建立ridge標籤

R1.grid() 
R2.grid() 
R3.grid() 
R4.grid() 
R5.grid() 

# 各種不同的像素圖
# 如果bitmap參數跟image參數同時存在，bimap參數會沒有用!!!
B1=tkinter.Label(root,bitmap="error")    #建立error位元圖
B2=tkinter.Label(root,bitmap="hourglass") #建立hourglass位元圖
B3=tkinter.Label(root,bitmap="info")     #建立info位元圖
B4=tkinter.Label(root,bitmap="questhead") #建立questhead位元圖
B5=tkinter.Label(root,bitmap="question") #建立question位元圖
B6=tkinter.Label(root,bitmap="warning") #建立warning位元圖
B7=tkinter.Label(root,bitmap="gray12") #建立gray12位元圖
B8=tkinter.Label(root,bitmap="gray25") #建立gray25位元圖
B9=tkinter.Label(root,bitmap="gray50") #建立gray50位元圖
B10=tkinter.Label(root,bitmap="gray75") #建立gray75位元圖

B1.grid(row=0,column=0)
B2.grid(row=1,column=0)
B3.grid(row=1,column=1)
B4.grid(row=0,column=2)
B5.grid(row=2,column=2)
B6.grid(row=0,column=3)
B7.grid(row=2,column=1)
B8.grid(row=3,column=1)
B9.grid(row=4,column=3)
B10.grid(row=4,column=2)

root.mainloop()