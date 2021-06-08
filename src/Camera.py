from types import SimpleNamespace
import wx
import numpy as np
import Transforms
import math


class Camera(wx.Panel):
    def __init__(self, frame, scene):
        wx.Panel.__init__(self, frame)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.scene = scene
        self.position = [0, 0, 0]
        self.look_at = [[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]]

        for obj in self.scene.objects:
            obj.vertexes.sort(key=lambda v: v[2])

    def on_size(self, evt):
        self.Refresh()

    def on_paint(self, evt):
        w, h = self.GetClientSize()
        dc = wx.PaintDC(self)
        dc.Clear()
        bmp = self.get_bitmap(w, h)
        dc.DrawBitmap(bmp, 0, 0)

    def get_bitmap(self, w, h):
        data = np.zeros((h, w, 3), np.uint8)

        for obj in self.scene.objects:
            for vt in obj.vertexes:
                # data[Y][X]
                vt = Transforms.scale(vt, 40)[:-1]
                vt = Transforms.translate(list(map(lambda x: x[0], vt)), 50, -400, 0)[:-1]
                data[round(vt[1][0])][round(vt[0][0])] = min(round(vt[2][0]), 255)

        bmp = wx.Bitmap.FromBuffer(w, h, data)
        return bmp
