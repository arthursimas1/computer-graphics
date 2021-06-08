class Scene:
    def __init__(self):
        """
        Scene constructor.
        """

        self.objects = []

    def add_object(self, obj) -> None:
        """
        Adds an object to the scene.

        :param obj: Object to be added to the scene.
        :return:
        """

        self.objects.append(obj)
