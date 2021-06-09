import wx
import numpy as np
import Transforms
import math


class Camera(wx.Panel):
    def __init__(self, frame, scene):
        """
        Camera constructor.

        :param frame: wx.Frame instance to insert a wx.Panel.
        :param scene: Scene instance where the camera should be placed.
        """

        wx.Panel.__init__(self, frame)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.scene = scene
        self.position = np.array([[0.],
                                  [0.],
                                  [0.],
                                  [1.]])
        self.look_at = np.array([[1., 0., 0., 0.],
                                 [0., 1., 0., 0.],
                                 [0., 0., 1., 0.],
                                 [0., 0., 0., 1.]])

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
            vt = []
            for i in range(len(obj.vertexes)):
                vt.append(np.matmul(self.look_at, np.matmul(obj.transformation_matrix, obj.vertexes[i])))

            vt.sort(key=lambda v: v[2][0])

            for v in vt:
                # data[Y][X]
                data[round(v[1][0])][round(v[0][0])] = min(round(v[2][0]), 255)

        bmp = wx.Bitmap.FromBuffer(w, h, data)
        return bmp

    def translate(self, delta_x: float, delta_y: float, delta_z: float) -> None:
        """
        Translate the camera by a given delta.

        :param delta_x: Delta amount to translate the X coordinate.
        :param delta_y: Delta amount to translate the Y coordinate.
        :param delta_z: Delta amount to translate the Z coordinate.
        """

        self.look_at = Transforms.translate(self.look_at, delta_x, delta_y, delta_z)

    def rotate_x(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around X axis.

        :param deg: Degrees to rotate the camera.
        """

        self.look_at = Transforms.rotate_x(self.look_at, math.radians(deg))

    def rotate_y(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around Y axis.

        :param deg: Degrees to rotate the camera.
        """

        self.look_at = Transforms.rotate_y(self.look_at, math.radians(deg))

    def rotate_z(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around Z axis.

        :param deg: Degrees to rotate the camera.
        """

        self.look_at = Transforms.rotate_z(self.look_at, math.radians(deg))
