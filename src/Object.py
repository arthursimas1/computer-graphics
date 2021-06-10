from typing import Optional
import numpy as np
import math
import Transforms


class Object:
    def __init__(self, path: Optional[str] = None):
        """
        3D Object constructor.

        :param path: Filepath to an .obj 3D object (optional).
        """

        self.vertexes = []
        self.faces = []
        self.transformation_matrix = np.array([[1., 0., 0., 0.],
                                               [0., 1., 0., 0.],
                                               [0., 0., 1., 0.],
                                               [0., 0., 0., 1.]])

        if path:
            self.from_file(path)

    def from_file(self, path) -> None:
        """
        Loads a 3D Object from an .obj.

        :param path: Filepath to an .obj 3D object.
        """
        self.vertexes = []
        self.faces = []

        x_max = float('-inf')
        x_min = float('inf')

        y_max = float('-inf')
        y_min = float('inf')

        z_max = float('-inf')
        z_min = float('inf')

        with open(path, 'r') as fp:
            for line in fp.readlines():
                line_type, *elements = line.split()

                if line_type == 'v':
                    x = float(elements[0])
                    y = float(elements[1])
                    z = float(elements[2])

                    x_max = max(x_max, x)
                    x_min = min(x_min, x)

                    y_max = max(y_max, y)
                    y_min = min(y_min, y)

                    z_max = max(z_max, z)
                    z_min = min(z_min, z)

                    self.vertexes.append(np.array([[x], [y], [z], [1]]))
                elif line_type == 'f':
                    self.faces.append(list(map(lambda f: int(f) - 1, elements)))

        # center around the coordinate (0, 0, 0)
        self.translate(-(x_max + x_min) / 2, -(y_max + y_min) / 2, -(z_max + z_min) / 2)

        # normalize the axes in the range [-0.5, 0.5]
        self.scale(1 / max(x_max - x_min, y_max - y_min, z_max - z_min))

    def copy(self) -> 'Object':
        """
        Copies itself into a new object, without having to read the .obj file again.

        :return: Copied object.
        """

        new_obj = Object()
        new_obj.vertexes = self.vertexes
        new_obj.faces = self.faces

        return new_obj

    def rotate_x(self, deg: float) -> None:
        """
        Rotate the object by a given angle in degrees around X axis.

        :param deg: Degrees to rotate the object.
        """

        self.transformation_matrix = Transforms.rotate_x(self.transformation_matrix, math.radians(deg))

    def rotate_y(self, deg: float) -> None:
        """
        Rotate the object by a given angle in degrees around Y axis.

        :param deg: Degrees to rotate the object.
        """

        self.transformation_matrix = Transforms.rotate_y(self.transformation_matrix, math.radians(deg))

    def rotate_z(self, deg: float) -> None:
        """
        Rotate the object by a given angle in degrees around Z axis.

        :param deg: Degrees to rotate the object.
        """

        self.transformation_matrix = Transforms.rotate_z(self.transformation_matrix, math.radians(deg))

    def scale(self, factor: float) -> None:
        """
        Scale the object by a given factor.

        :param factor: Scaling factor.
        """

        self.transformation_matrix = Transforms.scale(self.transformation_matrix, factor, factor, factor)

    def translate(self, delta_x: float, delta_y: float, delta_z: float) -> None:
        """
        Translate the object by a given delta.

        :param delta_x: Delta amount to translate the X coordinate.
        :param delta_y: Delta amount to translate the Y coordinate.
        :param delta_z: Delta amount to translate the Z coordinate.
        """

        self.transformation_matrix = Transforms.translate(self.transformation_matrix, delta_x, delta_y, delta_z)
