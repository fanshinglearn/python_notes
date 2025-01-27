# Notebook
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

root = tk.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x100')

def msg():
    messagebox.showinfo("Go", "gogogo")

notebook=ttk.Notebook (root)

f1= tk.Frame()
f2= tk.Frame()

l=tk.Label(f1, text="Hello") 
l.pack(padx=10, pady=10)

b=tk.Button (f2, text="Go", command=msg) 
b.pack(padx=10, pady=10)

notebook.add(f1, text="First") 
notebook.add(f2, text="Second") 
notebook.pack (padx=10, pady=10, fill='both', expand=True)

root.mainloop()