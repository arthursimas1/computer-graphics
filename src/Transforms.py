from math import cos, sin
import numpy as np


def rotate_x(vertex, rad: float):
    """
    Rotate a vertex by a given angle in radians around X axis.

    Transformation matrix used:
    [[ 1,       0,          0, 0 ],
     [ 0, cos(rad), -sin(rad), 0 ],
     [ 0, sin(rad),  cos(rad), 0 ],
     [ 0,        0,         0, 1 ]]

    :param vertex: Vertex to be transformed.
    :param rad: Radians to rotate a vertex.
    :return: Vertex after rotation.
    """

    trans_matrix = np.array([[1,        0,         0, 0],
                             [0, cos(rad), -sin(rad), 0],
                             [0, sin(rad),  cos(rad), 0],
                             [0,        0,         0, 1]])

    return np.matmul(trans_matrix, vertex)


def rotate_y(vertex, rad: float):
    """
    Rotate a vertex by a given angle in radians around Y axis.

    Transformation matrix used:
    [[  cos(rad), 0, sin(rad), 0 ],
     [         0, 1,        0, 0 ],
     [ -sin(rad), 0, cos(rad), 0 ],
     [         0, 0,        0, 1 ]]

    :param vertex: Vertex to be transformed.
    :param rad: Radians to rotate a vertex.
    :return: Vertex after rotation.
    """

    trans_matrix = np.array([[ cos(rad), 0, sin(rad), 0],
                             [        0, 1,        0, 0],
                             [-sin(rad), 0, cos(rad), 0],
                             [        0, 0,        0, 1]])

    return np.matmul(trans_matrix, vertex)


def rotate_z(vertex, rad: float):
    """
    Rotate a vertex by a given angle in radians around Z axis.

    Transformation matrix used:
    [[ cos(rad), -sin(rad), 0, 0 ],
     [ sin(rad),  cos(rad), 0, 0 ],
     [        0,         0, 1, 0 ],
     [        0,         0, 0, 1 ]]

    :param vertex: Vertex to be transformed.
    :param rad: Radians to rotate a vertex.
    :return: Vertex after rotation.
    """

    trans_matrix = np.array([[cos(rad), -sin(rad), 0, 0],
                             [sin(rad),  cos(rad), 0, 0],
                             [       0,         0, 1, 0],
                             [       0,         0, 0, 1]])

    return np.matmul(trans_matrix, vertex)


def scale(vertex, factor_x: float, factor_y: float, factor_z: float):
    """
    Scale each vertex coordinate by a given factor.

    Transformation matrix used:
    [[ factor_x,         0,        0, 0 ],
     [        0,  factor_y,        0, 0 ],
     [        0,         0, factor_z, 0 ],
     [        0,         0,        0, 1 ]]

    :param vertex: Vertex to be transformed.
    :param factor_x: Scaling factor for the X coordinate.
    :param factor_y: Scaling factor for the Y coordinate.
    :param factor_z: Scaling factor for the Z coordinate.
    :return: Vertex after scaling.
    """

    trans_matrix = np.array([[factor_x,         0,        0, 0],
                             [       0,  factor_y,        0, 0],
                             [       0,         0, factor_z, 0],
                             [       0,         0,        0, 1]])

    return np.matmul(trans_matrix, vertex)


def translate(vertex, delta_x: float, delta_y: float, delta_z: float):
    """
    Translate each vertex coordinate by a given delta.

    Transformation matrix used:
    [[ 1, 0, 0, delta_x ],
     [ 0, 1, 0, delta_y ],
     [ 0, 0, 1, delta_z ],
     [ 0, 0, 0,       1 ]]

    :param vertex: Vertex to be transformed.
    :param delta_x: Delta amount to translate the X coordinate.
    :param delta_y: Delta amount to translate the Y coordinate.
    :param delta_z: Delta amount to translate the Z coordinate.
    :return: Vertex after translation.
    """

    trans_matrix = np.array([[1, 0, 0, delta_x],
                             [0, 1, 0, delta_y],
                             [0, 0, 1, delta_z],
                             [0, 0, 0,       1]])

    return np.matmul(trans_matrix, vertex)
