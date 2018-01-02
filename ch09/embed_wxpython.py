from tkinter import ttk, scrolledtext, Tk, StringVar, WORD

win = Tk()
win.title('Python GUI')
a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)

ttk.Label(win, text='Enter a name:').grid(column=0, row=0)
name = StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
number = StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 42, 1024)
number_chosen.current(0)
number_chosen.grid(column=1, row=1)

scr = scrolledtext.ScrolledText(win, width=30, height=10, wrap=WORD)
scr.grid(column=0, row=2, sticky='WE', columnspan=3)

name_entered.focus()


def wx_app():
    import wx
    app = wx.App()

    frame = wx.Frame(None, -1, 'wxPython GUI', size=(200, 150))
    frame.SetBackgroundColour('white')
    frame.CreateStatusBar()

    menu = wx.Menu()
    menu.Append(wx.ID_ABOUT, 'About', 'wxPython GUI')
    menu_bar = wx.MenuBar()
    menu_bar.Append(menu, 'File')
    frame.SetMenuBar(menu_bar)

    frame.Show()
    app.MainLoop()


def action_cb():
    wx_app()


action = ttk.Button(win, text='Call wxPython GUI', command=action_cb)
action.grid(column=2, row=1)

win.mainloop()
