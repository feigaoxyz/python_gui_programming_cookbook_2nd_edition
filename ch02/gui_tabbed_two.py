import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

tab_control = ttk.Notebook(win)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

tab_control.pack(
    expand=1,
    fill="both"  # pack to make visible
)

# start GUI
win.mainloop()
