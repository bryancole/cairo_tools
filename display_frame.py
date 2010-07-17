#!/usr/bin/env python

import wx
from wx.lib.wxcairo import ContextFromDC
import cairo_tools
import numpy

def gen_data():
    x = numpy.linspace(0.1,0.9,20)
    x0 = x.copy()
    while True:
        y = 0.5 + 0.4*numpy.sin(x*20) #+ numpy.random.random(500)*0.01
        yield x0,y
        x += 0.003
        
def gen_path(s):
    cr = (yield)
    cr.new_path()
    cr.line_to(-s, -s)
    cr.line_to(-s, s)
    cr.line_to(s, s)
    cr.line_to(s, -s)
    cr.close_path()
    path = cr.copy_path()
    cr.new_path()
    while True:
        yield path

class GraphicsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        
        self.SetBackgroundColour(wx.NamedColor("white"))
        
        self.data = gen_data()
        self.path = gen_path(0.01)
        self.path.next()
        self.timer.Start(100)
        
    def OnTimer(self, evt):
        self.Refresh()
        
    def OnSize(self, evt):
        self.Refresh()
        
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        #dc.Clear()
        w,h = dc.GetSizeTuple()
        dc.SetPen(wx.RED_PEN)
        cr = ContextFromDC(dc)
        cr.scale(w,h)
        cr.set_source_rgb(1, 0, 1)
        cr.set_line_width(0.002)
        path = self.path.send(cr)
        x,y = self.data.next()
    
        #dc.DrawLines(numpy.array([x*w,y*h]).T)
        cairo_tools.polyline(cr,x,y)
        cairo_tools.stamp_at(cr, path, x, y)
        cr.stroke()


class DisplayFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Graphics Deisplay")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.display_panel = GraphicsPanel(self)
        self.SetSize((600,400))
        sizer.Add(self.display_panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()
        
if __name__=="__main__":
    app = wx.App()
    frame = DisplayFrame(None)
    frame.Show()
    app.MainLoop()
    
        