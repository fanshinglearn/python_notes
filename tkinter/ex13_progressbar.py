# Progressbar進度條
import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.geometry('300x100')

def running():
    for i in range(100):
        pb["value"] = i+1
        root.update()
        time.sleep(0.03)

pb = ttk.Progressbar(root, length=150,
                 mode="determinate", orient='horizontal')
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0

b = tk.Button(root, text="Running",command=running)
b.pack(pady=18)

root.mainloop()