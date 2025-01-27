# Menu功能表
import tkinter as tk

root = tk.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x100')

filemenu=tk.Menu(root)
root.config(menu=filemenu)
mb1=tk.Menu(filemenu)
mb2=tk.Menu(filemenu)

mb1.add_command(label='Add')
mb1.add_command(label='Save')
mb2.add_command(label='Run')
mb2.add_command(label='Help')

filemenu.add_cascade(label='File',menu=mb1)
filemenu.add_cascade(label='Edit',menu=mb2)

root.mainloop()