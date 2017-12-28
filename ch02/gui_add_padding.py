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

# ScrolledText widget
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(row=5, column=0, columnspan=3)

colors = ['Blue', 'Gold', 'Red']


def rad_call():
    # Radiobutton callback
    rad_sel = rad_var.get()
    try:
        win.configure(background=colors[rad_sel])
    except IndexError:
        pass


# create three Radiobuttons using one variable
rad_var = tk.IntVar()

# we selects a non-existing index value for rad_var
rad_var.set(99)

# create all three Radiobutton widgets within in one loop
for col in range(3):
    cur_rad = ttk.Radiobutton(win, text=colors[col],
                              variable=rad_var, value=col,
                              command=rad_call
                              ).grid(row=6, column=col, sticky=tk.W)

# create a container to hold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
buttons_frame.grid(
    row=7, column=0,
    padx=20, pady=40  # add padding space around widget
)

# place labels into the container element
for col in range(3):
    ttk.Label(
        buttons_frame,  # notice the parent
        text=f'Label {col+1}'
    ).grid(
        row=col, column=0,
        sticky=tk.W
    )

# set cursor focus
name_entered.focus()

# Start GUI
win.mainloop()
