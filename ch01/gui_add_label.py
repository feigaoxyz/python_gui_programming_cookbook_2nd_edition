import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

ttk.Label(win, text="A label").grid(column=0, row=0)
tk.Label(win, text="default theme").grid(column=1, row=0)

win.mainloop()
