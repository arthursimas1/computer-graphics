from Camera import Camera
from Object import Object
from Scene import Scene
import wx

if __name__ == '__main__':
    s = Scene()

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj')
    obj1.scale(30)
    s.add_object(obj1)

    # obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj')
    # s.add_object(obj2)

    frame = wx.Frame(None, title=f'Computer Graphics Test')

    cam = Camera(frame, s)
    cam.rotate_y(45)
    cam.rotate_z(45)
    cam.translate(100, -100, 0)

    frame.Show()
    Scene.main_loop()
