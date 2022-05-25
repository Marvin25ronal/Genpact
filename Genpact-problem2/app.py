import wx
from controller import Controller


class window(wx.Frame):
    def __init__(self, parent, title):
        super(window, self).__init__(parent, title=title, size=(500, 200))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        nameLbl = wx.StaticText(panel, -1, "Name:")
        name = wx.TextCtrl(panel, -1, "Marvin Ronaldo Martínez Marroquín")
        name.Disable()
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        pathLbl = wx.StaticText(panel, -1, "Path:")
        path = wx.TextCtrl(panel, -1, "Select Folder....")
        path.Disable()
        self.pathInput=path

        srcBtb = wx.Button(panel, -1, "Select Folder")
        
        

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)

        pathSizer = wx.FlexGridSizer(cols=3, hgap=5, vgap=5)
        pathSizer.AddGrowableCol(1)
        pathSizer.Add(pathLbl, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        pathSizer.Add(path, 0, wx.EXPAND)
        pathSizer.Add(srcBtb, 0, wx.EXPAND)

        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(pathSizer, 0, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(mainSizer)

        self.Bind(wx.EVT_BUTTON, self.OpenFileChooser, srcBtb)

        self.SetTitle("Genpact")
        self.Centre()

    def OpenFileChooser(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
            self.pathInput.SetValue(dlg.GetPath())
            controller = Controller(self.path)
            controller.AnalizeFolder()
            
        dlg.Destroy()


if __name__ == "__main__":
    app = wx.App()
    window(None, title="Genpact")
    app.MainLoop()
