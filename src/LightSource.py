from typing import List, Optional
import Transforms
import numpy as np


class LightSource:
    def __init__(self, position: List[float], intensity: Optional[float] = 1.):
        """
        Light Source constructor.

        :param position: Where it should be placed at the scene.
        :param intensity: Intensity constant.
        """

        self.position = np.array(position)
        self.intensity = intensity; assert 0 <= intensity <= 1

    def copy(self) -> 'LightSource':
        """
        Copies itself into a new light source.

        :return: Copied light source.
        """

        new_obj = LightSource(self.position.copy(), self.intensity)

        return new_obj

    def translate(self, delta_x: float, delta_y: float, delta_z: float) -> None:
        """
        Translate the light source by a given delta.

        :param delta_x: Delta amount to translate the X coordinate.
        :param delta_y: Delta amount to translate the Y coordinate.
        :param delta_z: Delta amount to translate the Z coordinate.
        """

        self.position = Transforms.translate(self.position, delta_x, delta_y, delta_z)
