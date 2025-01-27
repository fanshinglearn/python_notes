from tkinter import *
root = Tk()

# T1 = Text(root, height=10, width=30, wrap='none')
# T1 = Text(root, height=10, width=30, wrap='char')
T1 = Text(root, height=10, width=30, wrap='word')
T1.insert(END, '哭阿\n我要怎麼畢業')
T1.insert(INSERT, '\n吐了')
T1.insert(INSERT, '\n吐了')
T1.insert(INSERT, '\n吐了')
T1.insert(INSERT, '在Tkinter中，Button的command函式應該寫在程式碼的任何位置，只要它在該Button被創建之前就被定義即可。在你提供的程式碼中，btn_hit()函式是在Button被創建之前被定義的，因此這是正確的位置。當按下該Button時，它會呼叫btn_hit()函式來執行相應的動作。如果你有多個Button，每個Button都有自己的command函式，你可以將這些函式定義在Button之前的任何位置。請確保在定義Button之前已經定義了所有的command函式。')
T1.insert(2.9, 'QAQ')
T1.pack(fill=BOTH, expand=True)

Sx1 = Scrollbar(root, orient=HORIZONTAL)
Sy1 = Scrollbar(root)

Sx1.pack(side=BOTTOM, fill=X)
Sy1.pack(side=RIGHT, fill=Y)

Sx1.config(command=T1.xview)
Sy1.config(command=T1.yview)

T1.config(xscrollcommand=Sx1.set, yscrollcommand=Sy1.set)


root.mainloop()