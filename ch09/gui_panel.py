import wx


class GUI(wx.Panel):
    def __init__(self, parent: wx.Frame):
        wx.Panel.__init__(self, parent)

        parent.CreateStatusBar()

        menu = wx.Menu()
        menu.Append(wx.ID_ABORT, 'About', 'wxPython GUI')
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, 'Exit', 'Exit the GUI')

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu, 'File')

        parent.SetMenuBar(menu_bar)

        button = wx.Button(self, label='Print', pos=(0, 60))
        self.Bind(wx.EVT_BUTTON, self.print_button, button)

        self.text_box = wx.TextCtrl(self, size=(280, 50), style=wx.TE_MULTILINE)

    def print_button(self, event):
        self.text_box.AppendText('The Print Button has been clicked!')


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(300, 180))
    GUI(frame)
    frame.Show()
    app.MainLoop()
