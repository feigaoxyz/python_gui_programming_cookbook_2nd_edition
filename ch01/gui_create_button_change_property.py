import tkinter as tk
from tkinter import ttk

win = tk.Tk()

a_label = ttk.Label(win, text="A label")
a_label.grid(row=0, column=0)


def click_me():
    button.configure(text="I have been clicked")
    a_label.configure(foreground='red', text='A red label')


button = ttk.Button(win, text="Click me", command=click_me)
button.grid(row=0, column=1)

win.mainloop()
