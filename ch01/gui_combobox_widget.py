import tkinter as tk
from tkinter import ttk

win = tk.Tk()


def click_me():
    action.configure(text='{}, {}'.format(name.get(), number.get()))


action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(row=1, column=2)

ttk.Label(win, text="Enter a name:").grid(row=0, column=0)

name = tk.StringVar()

name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(row=1, column=0)
name_entered.focus()

ttk.Label(win, text="Choose a number:").grid(row=0, column=1)

number = tk.StringVar()

number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['state'] = 'readonly'  # restrict user to pre-defined values
number_chosen.grid(row=1, column=1)

# number_chosen.configure(values=(1, 2, 4, 42, 100))
number_chosen['values'] = [1, 2, 4, 42, 100, 'a', 'bcd']
number_chosen.current(3)

win.mainloop()
