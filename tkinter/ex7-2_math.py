# 文字方塊Entry 數學公式
import tkinter as tk
root=tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x300')

def math():
    out.configure(text = 'Answer: '+ str(eval(equ.get())))
              
label =tk.Label(root, text="Enter your math question:",bg="#7AFEC6",fg='#FFAAD5',font=("Ravie",10,"bold"))
label.pack()

equ = tk.Entry(root)#輸入要算的東西
equ.pack()

out = tk.Label(root,bg="#7AFEC6",fg='#FF5151',font=("Ravie",15,"bold"))#儲存計算結果
out.pack()

btn = tk.Button(root,text="count",command=math)#執行鈕
btn.pack()

root.mainloop()