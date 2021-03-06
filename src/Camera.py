import wx
import numpy as np
import Transforms
import math
import Rasterization


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
        self.view_transformation = np.array([[1., 0., 0., 0.],
                                             [0., 1., 0., 0.],
                                             [0., 0., 1., 0.],
                                             [0., 0., 0., 1.]])

        self.bmp = None
        self.update_bmp = True
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
            self.translate(0, self.step_delta_constant, 0)
        elif mod == wx.MOD_SHIFT and key == wx.WXK_DOWN:
            self.translate(0, -self.step_delta_constant, 0)
        elif mod == wx.MOD_CONTROL:
            if key == wx.WXK_RIGHT:
                self.rotate_y(-self.step_deg_constant)
            elif key == wx.WXK_LEFT:
                self.rotate_y(self.step_deg_constant)
            elif key == wx.WXK_UP:
                self.rotate_x(-self.step_deg_constant)
            elif key == wx.WXK_DOWN:
                self.rotate_x(self.step_deg_constant)
            else:
                re_render = False
        elif mod == wx.MOD_CONTROL | wx.MOD_SHIFT and key == wx.WXK_RIGHT:
            self.rotate_z(-self.step_deg_constant)
        elif mod == wx.MOD_CONTROL | wx.MOD_SHIFT and key == wx.WXK_LEFT:
            self.rotate_z(self.step_deg_constant)
        else:
            re_render = False

        if re_render:
            self.update_bmp = True
            self.Refresh()

    def on_size(self, evt):
        self.update_bmp = True
        self.Refresh()

    def on_paint(self, evt):
        w, h = self.GetClientSize()
        dc = wx.PaintDC(self)
        dc.Clear()
        if self.update_bmp:
            self.bmp = self.generate_bitmap(w, h)
            self.update_bmp = False
        dc.DrawBitmap(self.bmp, 0, 0)

    def generate_bitmap(self, w, h):
        camera_coord = np.array(list(map(lambda x: -x[-1], self.view_transformation))[:3])
        z_buffer = np.full((h, w), float('inf'), np.float64)
        data = np.full((h, w, 3), 0, np.uint8)  # data[Y][X] = (R, G, B)

        trans = self.view_transformation
        #trans = Transforms.perspective(trans, math.radians(90), w/h, 0, 1000)  # FIXME
        trans = Transforms.translate(trans, w/2, h/2, 0)

        for obj in self.scene.objects:
            trans_obj = np.matmul(trans, obj.transformation_matrix)
            vertexes = np.matmul(trans_obj, obj.vertexes).round(decimals=0).astype(int, copy=False)

            for triangle_index in range(len(obj.faces)):
                Rasterization.draw_triangle_vertices(data, z_buffer, (h, w), camera_coord, obj, self.scene, vertexes, triangle_index)

        print(f'Scene#{self.scene.id}, Camera#{self.id}: rendered')

        return wx.Bitmap.FromBuffer(w, h, data)

    def rotate_x(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around X axis.

        :param deg: Degrees to rotate the camera.
        """

        self.view_transformation = Transforms.rotate_x(self.view_transformation, math.radians(-deg))

    def rotate_y(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around Y axis.

        :param deg: Degrees to rotate the camera.
        """

        self.view_transformation = Transforms.rotate_y(self.view_transformation, math.radians(-deg))

    def rotate_z(self, deg: float) -> None:
        """
        Rotate the camera by a given angle in degrees around Z axis.

        :param deg: Degrees to rotate the camera.
        """

        self.view_transformation = Transforms.rotate_z(self.view_transformation, math.radians(-deg))

    def translate(self, delta_x: float, delta_y: float, delta_z: float) -> None:
        """
        Translate the camera by a given delta.

        :param delta_x: Delta amount to translate the X coordinate.
        :param delta_y: Delta amount to translate the Y coordinate.
        :param delta_z: Delta amount to translate the Z coordinate.
        """

        self.view_transformation = Transforms.translate(self.view_transformation, -delta_x, -delta_y, -delta_z)
