
#coding=utf-8
 
import wx
import time
 
class MyFrame(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Multi-mode testing hot patch tool",size = (800,600))
        panel = wx.Panel(self)
        list1 = ["this is a longer choice","this is an even longer choice" ,"this is a short choice"]
        list2 = ["RRU1", "RRU2", "RRU3"]
        #ListBox class instance
        self.listbox1 = wx.ListBox(panel,-1,(50,80),(200, 60),list1,wx.LB_SINGLE) #wx.LB_SINGLE can only select a single
        self.listbox2 = wx.ListBox(panel, -1,(50, 150), (200, 60), list2, wx.LB_MULTIPLE)#Multiple choice
        #CheckListBox class instance
        self.listbox3 = wx.CheckListBox(panel,-1,pos=(300,80),size=(200, 400),choices=list1, style=wx.LB_HSCROLL)
                 #Choice class instance
        # self.listbox4 = wx.Choice(panel,-1,(300,200),(200, 40),list2)
        # self.listbox4.Bind(wx.EVT_CHOICE,self.One_Play)
        #          #Progress bar display
        # self.gauge1 = wx.Gauge(panel,-1,100,(50, 250), (200, 60))
        # self.value = 1
        # self.gauge1.SetValue(self.value)
        #          #Binding wx idle events to the progress bar
        # self.Bind(wx.EVT_IDLE,self.Gauge_Test)
        #          #Slider
        # self.slider = wx.Slider(panel,-1,10,10,100,(300, 350), (200, 60))
        # self.slider.Bind(wx.EVT_SCROLL,self.Slider_Test)
 
    def Gauge_Test(self,event):
        if self.value < 100:
            self.value += 1
            time.sleep(0.3)
            self.gauge1.SetValue(self.value)
 
    def Slider_Test(self,event):
        value = self.slider.GetValue()
        #print "now value is:",value
 
    def One_Play(self,event):
        pass
                # print "Did you choose this time:",self.listbox4.GetStringSelection()
 
    def Two_Play(self,event):
        pass
                 #print "Have you selected this time:", self.listbox2.GetSelections()
 
 
 
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()