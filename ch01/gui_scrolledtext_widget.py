import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()


def click_me():
    variables = [name, number, check_dis, check_un, check_en]
    text = ', '.join([str(v.get()) for v in variables])
    action.configure(text=text)


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

check_dis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=check_dis, state='disabled')
check1.select()
check1.grid(row=4, column=0, sticky=tk.W)

check_un = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=check_un)
check2.grid(row=4, column=1, sticky=tk.W)
check2.deselect()

check_en = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=check_en)
check3.grid(row=4, column=2, sticky=tk.W)
check3.select()

color_blue = "blue"
color_red = 'red'
color_gold = 'gold'


def rad_call():
    # Radiobutton callback
    rad_sel = rad_var.get()
    if rad_sel == 1:
        win.configure(background=color_blue)
    elif rad_sel == 2:
        win.configure(background=color_red)
    elif rad_sel == 3:
        win.configure(background=color_gold)


# create three Radiobuttons using one variable
rad_var = tk.IntVar()

rad1 = tk.Radiobutton(win, text=color_blue, variable=rad_var, value=1, command=rad_call)
rad1.grid(row=5, column=0, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=color_red, variable=rad_var, value=2, command=rad_call)
rad2.grid(row=5, column=1, sticky=tk.W, columnspan=3)

rad3 = ttk.Radiobutton(win, text=color_gold, variable=rad_var, value=3, command=rad_call)
rad3.grid(row=5, column=2, sticky=tk.W, columnspan=3)

# ScrolledText widget
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Start GUI
win.mainloop()
