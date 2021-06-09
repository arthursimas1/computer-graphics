import wx
import numpy as np
import Transforms
import math


class Camera(wx.Panel):
    count = 0

    def __init__(self, scene):
        """
        Camera constructor.

        :param scene: Scene instance where the camera should be placed.
        """

        Camera.count += 1
        self.id = Camera.count

        frame = wx.Frame(None, title=f'Computer Graphics Test (Scene {scene.id}, Camera {self.id})')
        wx.Panel.__init__(self, frame)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_KEY_DOWN, self.key_down)
        frame.Show()

        self.scene = scene
        self.position = np.array([[0.],
                                  [0.],
                                  [0.],
                                  [1.]])
        self.look_at = np.array([[1., 0., 0., 0.],
                                 [0., 1., 0., 0.],
                                 [0., 0., 1., 0.],
                                 [0., 0., 0., 1.]])

        self.step_delta_constant = 10
        self.step_deg_constant = 1

    def key_down(self, evt):
        re_render = True
        mod = evt.GetModifiers()
        key = evt.GetKeyCode()

        if mod == wx.MOD_NONE:
            if key == wx.WXK_RIGHT:
                self.translate(self.step_delta_constant, 0, 0)
            elif key == wx.WXK_LEFT:
                self.translate(-self.step_delta_constant, 0, 0)
            elif key == wx.WXK_UP:
                self.translate(0, 0, self.step_delta_constant)
            elif key == wx.WXK_DOWN:
                self.translate(0, 0, -self.step_delta_constant)
            else:
                re_render = False
        elif mod == wx.MOD_SHIFT and key == wx.WXK_UP:
            self.translate(0, -self.step_delta_constant, 0)
        elif mod == wx.MOD_SHIFT and key == wx.WXK_DOWN:
            self.translate(0, self.step_delta_constant, 0)
        elif mod == wx.MOD_CONTROL:
            if key == wx.WXK_RIGHT:
                self.rotate_y(self.step_deg_constant)
            elif key == wx.WXK_LEFT:
                self.rotate_y(-self.step_deg_constant)
            elif key == wx.WXK_UP:
                self.rotate_x(self.step_deg_constant)
            elif key == wx.WXK_DOWN:
                self.rotate_x(-self.step_deg_constant)
            else:
                re_render = False
        elif mod == wx.MOD_CONTROL | wx.MOD_SHIFT and key == wx.WXK_RIGHT:
            self.rotate_z(self.step_deg_constant)
        elif mod == wx.MOD_CONTROL | wx.MOD_SHIFT and key == wx.WXK_LEFT:
            self.rotate_z(-self.step_deg_constant)
        else:
            re_render = False

        if re_render:
            self.Refresh()

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

    def translate(self, delta_x: float, delta_y: float, delta_z: float) -> None:
        """
        Translate the camera by a given delta.

        :param delta_x: Delta amount to translate the X coordinate.
        :param delta_y: Delta amount to translate the Y coordinate.
        :param delta_z: Delta amount to translate the Z coordinate.
        """

        self.look_at = Transforms.translate(self.look_at, delta_x, delta_y, delta_z)
