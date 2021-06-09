import wx


class Scene:
    count = 0
    wx_app = None

    def __init__(self):
        """
        Scene constructor.
        """

        Scene.count += 1
        self.id = Scene.count

        self.objects = []

        if not Scene.wx_app:
            Scene.wx_app = wx.App()

    def add_object(self, obj) -> None:
        """
        Adds an object to the scene.

        :param obj: Object to be added to the scene.
        :return:
        """

        self.objects.append(obj)

    @staticmethod
    def main_loop() -> None:
        """
        Open the app windows.
        """
        Scene.wx_app.MainLoop()
