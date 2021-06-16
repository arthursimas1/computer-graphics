from typing import Optional
import wx


class Scene:
    count = 0
    wx_app = None

    def __init__(self, k_ambient: Optional[float] = .1):
        """
        Scene constructor.
        """

        Scene.count += 1
        self.id = Scene.count

        self.objects = []
        self.light_sources = []
        self.k_ambient = k_ambient; assert 0 <= k_ambient <= 1

        if not Scene.wx_app:
            Scene.wx_app = wx.App()

    def add_object(self, obj) -> None:
        """
        Adds an object to the scene.

        :param obj: Object to be added to the scene.
        :return:
        """

        self.objects.append(obj)

    def add_light_source(self, ls) -> None:
        """
        Adds a light source to the scene.

        :param ls: Light source to be added to the scene.
        :return:
        """

        self.light_sources.append(ls)

    @staticmethod
    def main_loop() -> None:
        """
        Open the app windows.
        """
        Scene.wx_app.MainLoop()
