import tkinter as tk
from tkinter import ttk

win = tk.Tk()


def click_me():
    action.configure(text='Hello, ' + name.get())
    action.configure(state='disabled')


ttk.Label(win, text="Enter a name:").grid(row=0, column=0)

name = tk.StringVar()

name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(row=0, column=1)
name_entered.focus()

action = ttk.Button(win, text="Greeting",
                    command=click_me)
action.grid(row=1, column=0)

win.mainloop()
