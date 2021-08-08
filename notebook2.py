
import wx

class PanelOne(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)
        
        self.SetSizer(sizer)

class NestedPanel(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create some nested tabs on the first tab
        nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        nestedTabOne = PanelOne(nestedNotebook)
        nestedTabTwo = PanelOne(nestedNotebook)
        nestedNotebook.AddPage(nestedTabOne, "NestedTabOne")
        nestedNotebook.AddPage(nestedTabTwo, "NestedTabTwo")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)
                
        self.SetSizer(sizer)


########################################################################
class NestedNotebookDemo(wx.Notebook):
    """
    Notebook class
    """
    
    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP 
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             )
        
        # Create the first tab and add it to the notebook
        tabOne = NestedPanel(self)
        self.AddPage(tabOne, "Email Search")
    
        
        # Create and add the second tab
        tabTwo = PanelOne(self)
        self.AddPage(tabTwo, "Text Search")
        
        
        
        
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
        
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        #print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        #print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()

        
########################################################################
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""        
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Notebook Tutorial",
                          size=(600,400)
                          )
        panel = wx.Panel(self)


        notebook = NestedNotebookDemo(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)

        self.db_hbox = wx.BoxSizer(wx.HORIZONTAL)
        

        self.btn_connect = wx.Button(panel, label='Connect to DB')
        #self.btn_connect.Bind(wx.EVT_BUTTON,self
        self.st_db = wx.StaticText(panel, label='     Not connected to database')
        #self.st_db.SetFont(font)
        self.db_hbox.Add(self.btn_connect, flag=wx.RIGHT|wx.ALIGN_CENTER, border=8) 
        self.db_hbox.Add(self.st_db, flag=wx.RIGHT|wx.ALIGN_CENTER, border=8) 
        sizer.Add(self.db_hbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=8)
        

         #
        # set up Assets Label
        #
        assets_label_hbox = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Assets Found')
        #st2.SetFont(font)
        assets_label_hbox.Add(st2)
        sizer.Add(assets_label_hbox, flag=wx.LEFT | wx.TOP, border=8)
        sizer.Add((-1, 10))

        #
        # setup text control for assets 
        #
        textctrl_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.assets_tc = wx.TextCtrl(panel,style=wx.TE_MULTILINE)
        self.assets_tc.SetEditable(False)
        textctrl_hbox.Add(self.assets_tc, proportion=1, flag=wx.EXPAND)
        sizer.Add(textctrl_hbox, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=8)

        #
        # setup text control for checkboxes 
        #
        cboxes_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.cmdb_cb = wx.CheckBox(panel, label='CMDB')
        #self.cmdb_cb.SetFont(font)
        self.cmdb_cb.SetValue(True)
        self.cmdb_cb.Disable()
        cboxes_hbox.Add(self.cmdb_cb)
        self.jamf_cb = wx.CheckBox(panel, label='JAMF')
        #self.jamf_cb.SetFont(font)
        self.jamf_cb.SetValue(True)
        self.jamf_cb.Disable()
        cboxes_hbox.Add(self.jamf_cb, flag=wx.LEFT, border=8)
        sizer.Add(cboxes_hbox, flag=wx.LEFT, border=8)
        

        sizer.Add((-1, 25))
        panel.SetSizer(sizer)
        self.Layout()
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = DemoFrame()
    app.MainLoop()