from Camera import Camera
from Object import Object
from Scene import Scene
import wx

if __name__ == '__main__':
    s = Scene()

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj')
    s.add_object(obj1)

    # obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj')
    # s.add_object(obj2)

    app = wx.App()
    frame = wx.Frame(None, title=f'Computer Graphics Test')

    cam = Camera(frame, s)

    frame.Show()
    app.MainLoop()
