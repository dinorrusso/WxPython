import wx
import wx.grid 

class TestTable(wx.grid.PyGridTableBase):
    def _init_(self):

        wx.grid.PyGridTableBase._init_(self)

        self.odd=wx.grid.GridCellAttr() 
        self.odd.SetBackgroundColour("sky blue")

        self.odd.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.even=wx.grid.GridCellAttr() 
        self.even.SetBackgroundColour("sea green")

        self.even.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

    def GetNumberRows(self):
        return 50

    def GetNumberCols(self): 
        return 50

    def IsEmptyCell(self, row, col):
        return self.data.get((row, col)) is not None 
    
    def GetValue(self, row, col):
        value = self.data.get((row, col)) 
        if value is not None:
            return value 
        else:
            pass

    def SetValue(self, row, col, value): 
        self.data[(row,col)] = value 

    def GetAttr(self, row, col, kind):
        attr.IncRef()
        return attr 

class TestFrame(wx.Frame):

    wx.Frame._init_(self, None, title="Grid Table", size=(640,480))

    grid = wx.grid.Grid(self)

    table = TestTable()

    grid.SetTable(table, True) 


app = wx.PySimpleApp() 
frame = TestFrame() 
frame.Show() 
app.MainLoop()