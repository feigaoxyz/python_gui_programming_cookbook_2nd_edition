import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# create instance
win = tk.Tk()

# add a title
win.title("Python GUI")

# create a container frame to hold all other widgets
mighty = ttk.LabelFrame(
    win,
    text=' Mighty Python '
)
mighty.grid(
    row=0, column=0,
    padx=8, pady=4
)

name_label = ttk.Label(
    mighty, text="Enter a name:"
).grid(
    row=0, column=0
)

name = tk.StringVar()

name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(row=1, column=0)

number_label = ttk.Label(
    mighty, text="Choose a number:"
).grid(row=0, column=1)

number = tk.StringVar()

number_chosen = ttk.Combobox(
    mighty, width=12, textvariable=number
)
number_chosen['state'] = 'readonly'  # restrict user to pre-defined values
number_chosen.grid(row=1, column=1)

# number_chosen.configure(values=(1, 2, 4, 42, 100))
number_chosen['values'] = [1, 2, 4, 42, 100]
number_chosen.current(3)


# button widget callback
def click_me():
    variables = [name, number]
    text = ', '.join([str(v.get()) for v in variables])
    action.configure(text=text)


action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(row=1, column=2)

check_dis = tk.IntVar()
check1 = ttk.Checkbutton(mighty, text="Disabled", variable=check_dis, state='disabled')
check1.state(['selected'])  # check1.select() for tk.Checkbutton
check1.grid(row=4, column=0, sticky=tk.W)

check_un = tk.IntVar()
check2 = ttk.Checkbutton(mighty, text='Unchecked', variable=check_un)
check2.grid(row=4, column=1, sticky=tk.W)
check2.state(['!selected'])  # check2.deselect() for tk.Checkbutton

check_en = tk.IntVar()
check3 = ttk.Checkbutton(mighty, text="Enabled", variable=check_en)
check3.grid(row=4, column=2, sticky=tk.W)
check_en.set(1)  # check3.state(['selected']) for ttk or check3.select() for tk

# ScrolledText widget
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(
    mighty,
    width=scroll_w, height=scroll_h,
    wrap=tk.WORD
)
scr.grid(
    row=5, column=0,
    columnspan=3,
    sticky='WE'
)

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
    cur_rad = ttk.Radiobutton(mighty, text=colors[col],
                              variable=rad_var, value=col,
                              command=rad_call
                              ).grid(row=6, column=col, sticky=tk.W)

# create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a Frame ')
buttons_frame.grid(row=7, column=1)

# place labels into the container element
for col in range(3):
    ttk.Label(
        buttons_frame,  # notice the parent
        text=f'Label {col+1}'
    ).grid(
        row=0, column=col,
        sticky=tk.W
    )

# creating a Menu Bar
menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

# create menu and add menu items
file_menu = tk.Menu(  # create File menu
    menu_bar,
    tearoff=0  # remove the dashed line appears above the first menu item in a menu
)
file_menu.add_command(label="New")  # add item to File menu
file_menu.add_separator()
file_menu.add_command(label='Exit')

# add File menu to menu bar and give it a label
menu_bar.add_cascade(label='File', menu=file_menu)

# set cursor focus
name_entered.focus()

# Start GUI
win.mainloop()
