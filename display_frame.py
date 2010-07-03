#!/usr/bin/env python

import wx
from wx.lib.wxcairo import ContextFromDC

class GraphicsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        
    def OnSize(self, evt):
        self.Refresh()
        
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.Clear()
        w,h = dc.GetSizeTuple()
        print w,h
        cr = ContextFromDC(dc)
        cr.scale(w,h)
        cr.set_source_rgb(0, 0, 0)
        cr.move_to(0, 0)
        cr.line_to(1, 1)
        cr.move_to(1, 0)
        cr.line_to(0, 1)
        cr.set_line_width(0.2)
        cr.stroke()

        cr.rectangle(0, 0, 0.5, 0.5)
        cr.set_source_rgba(1, 0, 0, 0.80)
        cr.fill()

        cr.rectangle(0, 0.5, 0.5, 0.5)
        cr.set_source_rgba(0, 1, 0, 0.60)
        cr.fill()

        cr.rectangle(0.5, 0, 0.5, 0.5)
        cr.set_source_rgba(0, 0, 1, 0.40)
        cr.fill()


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
    
        