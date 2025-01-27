import tkinter

# 新視窗
root = tkinter.Tk()
# root.mainloop()

# 顯示視窗寬高
print(root.winfo_screenmmwidth())
print(root.winfo_screenmmheight())

# 設定視窗大小
root.geometry("350x200+200+300")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 300
height = 150
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f'{width}x{height}+{x}+{y}')

# 設定視窗標題
root.title(':P')

# 視窗背景顏色
root.configure(bg='aqua')
root.configure(bg='#a074c4')

# 視窗圖示
root.iconbitmap('loli.ico')

# 視窗最大 & 最小
root.maxsize(500,500)
root.minsize(100,100)

# 是否能改變視窗大小
root.resizable(True,True)
root.resizable(0,0)

# 最小化視窗 & 最大化視窗
root.iconify()
root.state('zoomed')

root.mainloop()