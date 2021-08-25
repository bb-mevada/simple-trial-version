import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Trial Version')
root.geometry('400x400+100+100')

with open('validity.txt','r+') as f:
    timer = f.readline()
    try:
        if int(timer) <= 3 and int(timer)>0:
            root.mainloop()
            f.seek(0)
            f.write(str(int(timer)-1))
        else:
            messagebox.showerror('Error','Sorry! The trial has been expired...')
    except ValueError:
        messagebox.showerror('Error','Sorry! The trial has been expired...')