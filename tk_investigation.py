# tk_investigation.py
import tkinter as tk
from tkinter import messagebox

from sqlite_investigation import get_names

#names = ["Alice", "Bob" ,"Carol", "Dan"]
names = get_names()

root = tk.Tk()
root.title("Python Desktop Application")
root.geometry("600x400")

def on_click():
    messagebox.showinfo("Information", "you clicked the button")

button = tk.Button(root, text="Press Me", command=on_click)
button.place(x=10, y=10)

listbox = tk.Listbox(root, height=10)
listbox.place(x=10, y=40)

for name in names:
    listbox.insert(tk.END, name)

root.mainloop()



