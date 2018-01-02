import wx

BACKGROUND_COLOR = (240, 240, 240, 255)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()

    def exitGUI(self, event):
        self.Destroy()

    def createWidgets(self):
        self.CreateStatusBar()
        self.createMenu()
        self.createNotebook()

    def createMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_NEW, 'New', 'Create something new')
        menu.AppendSeparator()
        _exit = menu.Append(wx.ID_EXIT, 'Exit', 'Exit wxPython GUI')
        self.Bind(wx.EVT_MENU, self.exitGUI, _exit)

        menu_about = wx.Menu()
        menu_about.Append(wx.ID_ABOUT, 'About', 'wxPython GUI')

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu, 'File')
        menu_bar.Append(menu_about, 'Help')
        self.SetMenuBar(menu_bar)

    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, 'Widgets')
        notebook.SetBackgroundColour(BACKGROUND_COLOR)

        # layout
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)


class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFilesFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()

    def createWidgetsFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, 'Widgets Frame', size=(285, -1))
        self.staticBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def createManageFilesFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, 'Manage Files', size=(285, -1))
        self.staticBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def addWidgets(self):
        self.addCheckBoxes()
        self.addRadioButtons()
        self.addStaticBoxWithLabels()
        self.addTextCtrl()
        self.addButtons()

    def addCheckBoxes(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)

        chk1 = wx.CheckBox(self.panel, label='Disabled')
        chk1.SetValue(True)
        chk1.Disable()
        boxSizerH.Add(chk1)

        chk2 = wx.CheckBox(self.panel, label='UnChecked')
        boxSizerH.Add(chk2, flag=wx.LEFT, border=10)

        chk3 = wx.CheckBox(self.panel, label='Toggle')
        chk3.SetValue(True)
        boxSizerH.Add(chk3, flag=wx.LEFT, border=10)

        self.staticBoxSizerV.Add(boxSizerH, flag=wx.LEFT, border=10)
        self.staticBoxSizerV.Add((0, 8))

    def addRadioButtons(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add((2, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Blue', style=wx.RB_GROUP))
        boxSizerH.Add((33, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Gold'))
        boxSizerH.Add((45, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Red'))

        self.staticBoxSizerV.Add(boxSizerH, 0, wx.ALL, 8)

    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='Browse to File...'))
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(174, -1), value='Z:'))

        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH1.Add(wx.Button(self.panel, label='Copy File To:'))
        boxSizerH1.Add(wx.TextCtrl(self.panel, size=(174, -1), value='Z:/Backup'))

        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)

        self.staticBoxSizerMgrV.Add(boxSizerV, 1, wx.ALL)

    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.staticBoxSizerV, 1, wx.ALL)
        boxSizerV.Add(self.staticBoxSizerMgrV, 1, wx.ALL)

        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)

    def addStaticBoxWithLabels(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)

        # first column of boxSizerH
        ## first row of staticBoxSizerV
        staticBox = wx.StaticBox(self.panel, -1, 'Labels within a Frame')
        staticBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

        ## second row of staticBoxSizerV
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        staticText1 = wx.StaticText(self.panel, -1, 'Choose a number:')
        boxSizerV.Add(staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText(self.panel, -1, 'Label 2')
        boxSizerV.Add(staticText2, 0, wx.ALL)

        ## third row of staticBoxSizerV
        staticBoxSizerV.Add(boxSizerV, 0, wx.ALL)

        boxSizerH.Add(staticBoxSizerV)

        boxSizerH.Add(wx.ComboBox(self.panel, size=(70, -1)))
        boxSizerH.Add(wx.SpinCtrl(self.panel, size=(50, -1), style=wx.BORDER_RAISED))

        # add local boxSizer to main frame
        self.staticBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    def addTextCtrl(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(275, -1), style=wx.TE_MULTILINE))
        self.staticBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    def addButtons(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='All Time Zones'))
        boxSizerH.Add(wx.Button(self.panel, label='Local Zone'))
        boxSizerH.Add(wx.Button(self.panel, label='New York'))
        self.staticBoxSizerV.Add(boxSizerH, 1, wx.ALL)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, title='Python GUI using wxPython', size=(350, 450))
    # Widgets(frame)
    # frame.Show()
    app.MainLoop()
