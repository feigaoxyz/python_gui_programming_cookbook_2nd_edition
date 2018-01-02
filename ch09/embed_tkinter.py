import wx

app = wx.App()

frame = wx.Frame(None, -1, title='wxPython GUI', size=(270, 180))
frame.SetBackgroundColour('white')
frame.CreateStatusBar()

menu = wx.Menu()
menu.Append(wx.ID_ABOUT, 'About', 'wxPython GUI')
menu_bar = wx.MenuBar()
menu_bar.Append(menu, 'File')
frame.SetMenuBar(menu_bar)


def tkinter_app():
    import tkinter as tk
    win = tk.Tk()
    win.title('Python GUI')
    win.mainloop()


def tkinter_embed(event):
    tkinter_app()


text_box = wx.TextCtrl(frame, size=(250, 50), style=wx.TE_MULTILINE)
button = wx.Button(frame, label='Call tkinter GUI', pos=(0, 60))
frame.Bind(wx.EVT_BUTTON, tkinter_embed, button)

frame.Show()
app.MainLoop()
