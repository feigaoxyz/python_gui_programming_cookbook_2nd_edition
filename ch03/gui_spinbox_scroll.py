import tkinter as tk
from tkinter import ttk, scrolledtext

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
name_label = ttk.Label(mighty, text="Enter a name:")
name_label.grid(
    row=0, column=0,
    sticky='W'
)

number_label = ttk.Label(
    mighty, text="Choose a number:",
)
number_label.grid(
    row=0, column=1,
    sticky='W',
)

name_var = tk.StringVar()
name_entry = ttk.Entry(
    mighty,
    textvariable=name_var,
    width=12
)
name_entry.grid(
    row=1, column=0,
    sticky='W'
)

number_var = tk.StringVar()
number_combo = ttk.Combobox(
    mighty,
    width=12,
    textvariable=number_var
)
number_combo.grid(
    row=1, column=1,
    sticky='WE'
)
number_combo['values'] = (1, 2, 4, 42, 100)
number_combo.current(3)
number_combo.state(['readonly'])


def click_callback():
    button.configure(
        text="{}, {}".format(name_var.get(), number_var.get())
    )


button = ttk.Button(
    mighty,
    text="Click Me!",
    command=click_callback
)
button.grid(
    row=1, column=2
)


def spin_cb():
    scroll.insert(
        tk.INSERT,
        spin.get() + '\n',
    )


spin = tk.Spinbox(
    mighty,
    from_=0,
    to=10,
    width=5,
    bd=3,  # borderwidth
    command=spin_cb,
)
spin.grid(
    row=2, column=0
)

scroll = scrolledtext.ScrolledText(
    mighty,
    width=30,
    height=10,
)
scroll.grid(
    row=3, column=0, columnspan=3,
    sticky='ewsn'
)

mighty2 = ttk.LabelFrame(
    tab2,
    text=" The Snake "
)
mighty2.grid(
    row=0, column=0,
    padx=8, pady=4
)

check_dis_var = tk.IntVar()
check_dis = ttk.Checkbutton(
    mighty2,
    text="Disabled",
    variable=check_dis_var,
    state='disabled'
)
check_dis.grid(
    row=2, column=0
)
check_dis.state(['selected'])

check_un_var = tk.IntVar()
check_un = ttk.Checkbutton(
    mighty2,
    text="UnChecked",
    variable=check_un_var
)
check_un.grid(
    row=2, column=1
)
check_un.state(['!selected'])

check_en_var = tk.IntVar()
check_en = ttk.Checkbutton(
    mighty2,
    text="Enabled",
    variable=check_en_var
)
check_en.grid(
    row=2, column=2
)
check_en_var.set(1)

colors = ['Blue', 'Gold', 'Red']
color_var = tk.IntVar()
color_var.set(99)


def radio_callback():
    try:
        mighty2.configure(text=colors[color_var.get()])
    except IndexError:
        pass


for col in range(3):
    radio_button = ttk.Radiobutton(
        mighty2,
        text=colors[col],
        value=col,
        variable=color_var,
        command=radio_callback,
    )
    radio_button.grid(
        row=4, column=col,
        sticky='E'
    )

label_frame = ttk.LabelFrame(
    mighty2,
    text="Labels in a Frame"
)
label_frame.grid(
    row=5, column=0,
    columnspan=2
)

for col in range(3):
    ttk.Label(
        label_frame,
        text=f"Label {col}"
    ).grid(
        row=0, column=col
    )

# set cursor focus
name_entry.focus()

# start GUI
win.mainloop()
