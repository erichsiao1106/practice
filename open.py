import  wx
import notebook
import codecs
import hero
import grid

 

# app=wx.App()
# win=hero.MyFrame1(None)
# win.Show()
# app.MainLoop()

# app=wx.App()
# win=notebook.MyFrame1(None)
# win.Show()
# app.MainLoop()

app=wx.App()
win=grid.MyFrame1(None)
win.Show()
app.MainLoop()

# r=self.m_filePicker1.GetPath()
# 		wx.MessageBox(r)
# 		with codecs.oprn(r,"r","utf8") as f:
# 			self.m_textCtrl1.SetValue(f.read())

# wx.MessageBox(self.m_hyperlink1.GetURL())

import wx

def main():
    # 建立應用
    app = wx.App()

    frame = wx.Frame(
        parent=None,    # 父層元件（已是頂層視窗，故無父層元件）
        id=wx.ID_ANY,
        title='Hello'   # 視窗標題
    )
    frame.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()