# 文字方塊
from tkinter import *
root = Tk()
# root.geometry('300x150+400+200')

def printinfo():
    print(f'Account: {E1.get()}')
    print(f'Password: {E2.get()}')
    E1.delete(0, END)
    E2.delete(0, END)

L1 = Label(root, text='Account')
L2 = Label(root, text='Password')

L1.grid(row=0)
L2.grid(row=1)

E1 = Entry(root)
E2 = Entry(root, show='*')
E1.insert(0, 'Ken')
E1.insert(2, '.....')
E2.insert(1, 'pwd')

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)

B1 = Button(root, text='Print', command=printinfo)
B2 = Button(root, text='Exit', command=root.destroy)

B1.grid(row=2, column=0, sticky=W, pady=10)
B2.grid(row=2, column=1, sticky=W, pady=10)


root.mainloop()