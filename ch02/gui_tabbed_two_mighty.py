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

# LabelFrame using tab1 as parent
mighty = ttk.LabelFrame(tab1, text=" Mighty Python ")
mighty.grid(
    row=0, column=0,
    padx=8, pady=4
)

# Label using mighty as parent
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(
    row=0, column=0,
    sticky='W'
)

# start GUI
win.mainloop()
