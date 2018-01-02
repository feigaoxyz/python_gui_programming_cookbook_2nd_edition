import wx


class GUI(wx.Frame):
    def __init__(self, parent, title, size=(200, 100)):
        wx.Frame.__init__(self, parent, title=title, size=size)

        self.SetBackgroundColour('white')

        self.CreateStatusBar()

        menu = wx.Menu()

        menu.Append(wx.ID_ABORT, "About", 'wxPython GUI')
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, 'Exit', ' Exit the GUI')

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu, 'File')
        self.SetMenuBar(menu_bar)

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    # GUI(None, "Python GUI using wxPython", (300, 150))
    app.MainLoop()
