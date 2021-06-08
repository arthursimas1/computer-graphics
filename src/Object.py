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

        with open(path, 'r') as fp:
            for line in fp.readlines():
                line_type, *elements = line.split()

                if line_type == 'v':
                    np_vertex = np.array([[float(elements[0])],
                                          [float(elements[1])],
                                          [float(elements[2])],
                                          [1]])
                    self.vertexes.append(np_vertex)
                elif line_type == 'f':
                    self.faces.append(list(map(lambda x: int(x) - 1, elements)))

    def copy(self) -> 'Object':
        """
        Copies itself into a new object, without having to read the .obj file again.

        :return: Copied object.
        """

        new_obj = Object()
        new_obj.vertexes = self.vertexes
        new_obj.faces = self.faces

        return new_obj

    def scale(self, factor: float) -> None:
        """
        Scale the object by a given factor.

        :param factor: Scaling factor.
        """

        self.transformation_matrix = Transforms.scale(self.transformation_matrix, factor)

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
