import os
import tkinter as tk
from queue import Queue
from threading import Thread
from time import sleep
from tkinter import Menu, filedialog
from tkinter import Spinbox
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import ttk

import Queues as bq
import ToolTip as tt

GLOBAL_CONST = 42
FILEDIR = os.path.dirname(__file__)
NETDIR = FILEDIR + '/Backup'
if not os.path.exists(NETDIR):
    os.makedirs(NETDIR, exist_ok=True)


# =====================================================
class OOP():
    def __init__(self):  # Initializer method
        # Create instance
        self.win = tk.Tk()

        self.gui_queue = Queue()

        # Add a title       
        self.win.title("Python GUI")
        self.create_widgets()
        self.default_file_entries()

    def default_file_entries(self):
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, FILEDIR)
        if len(FILEDIR) > self.entry_len:
            self.file_entry.config(width=len(FILEDIR) + 3)
            self.file_entry.config(state='readonly')

        self.netw_entry.delete(0, 'end')
        self.netw_entry.insert(0, NETDIR)
        if len(NETDIR) > self.entry_len:
            self.netw_entry.config(width=len(NETDIR) + 3)

    # Modified Button Click Function
    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' +
                                   self.number_chosen.get())
        # self.create_thread()
        bq.write_to_scrol(self)

    def use_queues(self, num_loop=5):
        while True:
            print(self.gui_queue.get())

    def create_thread(self, num_loop=10):
        self.run_thread = Thread(
            target=self.method_in_a_thread,
            args=(num_loop,),
        )
        self.run_thread.setDaemon(True)
        self.run_thread.start()

        write_thread = Thread(
            target=self.use_queues,
            args=(num_loop,),
            daemon=True)
        write_thread.start()

    def method_in_a_thread(self, num_of_loop=5):
        print('Hi, how are you?')
        for idx in range(num_of_loop):
            sleep(2)
            self.scrol.insert('insert', f'{idx}\n')
        print('method_in_thread:', self.run_thread.is_alive())

    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')

    # GUI Callback  
    def checkCallback(self, *ignored_args):
        # only enable one checkbutton
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

        # Radiobutton Callback

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.mighty2.configure(text='Blue')
        elif radSel == 1:
            self.mighty2.configure(text='Gold')
        elif radSel == 2:
            self.mighty2.configure(text='Red')

        # update progressbar in callback loop

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i  # increment progressbar
            self.progress_bar.update()  # have to call update() in loop
        self.progress_bar["value"] = 0  # reset/clear progressbar

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

        #####################################################################################

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tabControl)  # Create a tab
        tabControl.add(tab1, text='Tab 1')  # Add the tab
        tab2 = ttk.Frame(tabControl)  # Add a second tab
        tabControl.add(tab2, text='Tab 2')  # Make second tab visible

        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        ########################################
        # Tab 1
        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        # Modify adding a Label using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)

        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        # Adding a Spinbox widget
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin)  # using range
        self.spin.grid(column=0, row=2, sticky='W')  # align left

        # Using a scrolled Text control    
        scrol_w = 40
        scrol_h = 10  # increase sizes
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

        for child in mighty.winfo_children():  # add spacing to align widgets within tabs
            child.grid_configure(padx=4, pady=2)

        ########################################
        # Tab Control 2
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)

        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=0, sticky=tk.W)

        # trace the state of the two checkbuttons
        chVarUn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())
        chVarEn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())

        # First, we change our Radiobutton global variables into a list
        colors = ["Blue", "Gold", "Red"]

        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()

        # Next we are selecting a non-existing index value for radVar
        self.radVar.set(99)

        # Now we are creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar,
                                    value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)  # row=6
            # And now adding tooltips
            tt.create_ToolTip(curRad, 'This is a Radiobutton control')

        # Add a Progressbar to Tab 2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0,
                                                                                                 sticky='W')
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1,
                                                                                                    sticky='W')
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2,
                                                                                                 sticky='W')
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3,
                                                                                                        sticky='W')

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=2, pady=2)

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

        # create manage files frame
        mng_files_frame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mng_files_frame.grid(
            row=4, column=0,
            sticky='WE',
            padx=10, pady=5
        )

        # button callback
        def get_filename_cb():
            print('hello from get_filename_cb')
            file_dir = os.path.dirname(__file__)
            filename = filedialog.askopenfilename(
                parent=self.win,
                initialdir=file_dir
            )
            if filename:
                file.set(filename)

        # add widgets to Manage File Frame
        lb = ttk.Button(
            mng_files_frame,
            text="Browse to File...",
            command=get_filename_cb
        )
        lb.grid(
            row=0, column=0,
            sticky=tk.W
        )

        file = tk.StringVar()
        self.entry_len = scrol_w
        self.file_entry = ttk.Entry(
            mng_files_frame,
            width=self.entry_len,
            textvariable=file
        )
        self.file_entry.grid(
            row=0, column=1, sticky=tk.W
        )

        log_dir = tk.StringVar()
        self.netw_entry = ttk.Entry(
            mng_files_frame,
            width=self.entry_len,
            textvariable=log_dir
        )
        self.netw_entry.grid(
            row=1, column=1, sticky=tk.W
        )

        def copy_file():
            import shutil
            src = self.file_entry.get()
            file = src.split('/')[-1]
            dst = self.netw_entry.get() + '/' + file
            try:
                shutil.copy(src, dst)
                msg.showinfo('Copy File to Network',
                             'Success: File copied.')
            except FileNotFoundError as err:
                msg.showerror('Copy File to Network',
                              '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as err:
                msg.showerror('Copy File to Network',
                              '*** Failed to copy file! ***\n\n' + str(err))

        cb = ttk.Button(
            mng_files_frame,
            text='Copy File to: ',
            command=copy_file
        )
        cb.grid(row=1, column=0, sticky='e')

        for child in mng_files_frame.winfo_children():
            child.grid_configure(padx=6, pady=6)

        ########################################
        # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Display a Message Box
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')

            # Add another Menu to the Menu Bar and an item

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)  # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Change the main windows icon
        self.win.iconbitmap('pyc.ico')

        # It is not necessary to create a tk.StringVar() 
        # strData = tk.StringVar()
        strData = self.spin.get()
        print("Spinbox value: " + strData)

        # call function
        # self.usingGlobal()

        # self.name_entered.focus()
        tabControl.select(1)

        ########################################
        # Add Tooltips -----------------------------------------------------
        # Add a Tooltip to the Spinbox
        tt.create_ToolTip(self.spin, 'This is a Spinbox control')

        # Add Tooltips to more widgets
        tt.create_ToolTip(self.name_entered, 'This is an Entry control')
        tt.create_ToolTip(self.action, 'This is a Button control')
        tt.create_ToolTip(self.scrol, 'This is a ScrolledText control')


# ======================
# Start GUI
# ======================
oop = OOP()

# Running methods in Threads
run_thread = Thread(target=oop.method_in_a_thread)

oop.win.mainloop()
