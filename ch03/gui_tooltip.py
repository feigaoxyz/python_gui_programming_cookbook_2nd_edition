import tkinter as tk
from tkinter import ttk, scrolledtext


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tip_window = None

        self.id = None
        self.wait_time = 500

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide_tip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.show_tip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show_tip(self, event=None):
        """Display text in a tooltip window.
        """
        x = y = 0
        x, y, cx, cy = self.widget.bbox('insert')  # get size of widget
        x += self.widget.winfo_rootx() + 25  # calculate to display tooltip
        y += self.widget.winfo_rooty() + 20  # below and to the right

        self.tip_window = tw = tk.Toplevel(self.widget)  # create new tooltip window

        self.tip_window.wm_overrideredirect(True)  # remove all Window Manager (wm) decorations
        # tw.wm_overrideredirect(False)  # uncomment to see the effect
        self.tip_window.wm_geometry("+%d+%d" % (x, y))  # create window size

        label = tk.Label(
            self.tip_window,
            text=self.text,
            justify=tk.LEFT,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            wraplength=100,
        )
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


win = tk.Tk()
win.title("Python GUI")

tab_control = ttk.Notebook(win)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

# tab_control.pack(
#     expand=1,
#     fill="both"  # pack to make visible
# )
tab_control.grid(
    row=0, column=0
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

button_tip = ToolTip(button, 'This is a Button widget.')


def spin_cb():
    scroll.insert(
        tk.INSERT,
        spin.get() + '\n',
    )


spin = tk.Spinbox(
    mighty,
    values=(1, 3, 5, 11),
    width=5,
    borderwidth=8,  # borderwidth
    command=spin_cb,
    relief=tk.SUNKEN,  # default
)
spin.grid(
    row=2, column=0
)

spin_tip = ToolTip(spin, "This is a Spinbox")

spin2 = tk.Spinbox(
    mighty,
    values=(0, 50, 100),
    width=5,
    border=20,
    command=spin_cb,
    # relief=tk.RIDGE,
    # relief=tk.FLAT,
    # relief=tk.RAISED,
    relief=tk.GROOVE,
    # relief=tk.SUNKEN,  # default
)
spin2.grid(
    row=2, column=1
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

scroll_tip = ToolTip(scroll, "This is a ScrolledText.")

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

tab1_tip = ToolTip(tab1, "Tab 1 tooltip")

other_button = ttk.Button(
    win,
    text="other button"
)
other_button.grid(
    column=0
)
other_button_tip = ToolTip(other_button, "Other button")

# set cursor focus
# name_entry.focus()

# start GUI
win.mainloop()
