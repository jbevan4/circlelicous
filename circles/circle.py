"""Circlelicous ltd.
The be all and end all of circle analytics
"""
from math import pi, radians, sqrt, tan


class Circle:
    """an advanced circle class"""

    version = '99'

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        """Radius of a circle"""
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

    def area(self):
        perimeter = self.__perimeter()
        calculated_radius = perimeter / pi / 2
        return calculated_radius ** 2 * pi

    def perimeter(self):
        return self.radius * 2 * pi

    @classmethod
    def from_bbd(cls, bbd):
        return cls(radius=bbd / 2 / sqrt(2))

    @staticmethod
    def angle_to_grade(angle):
        return tan(radians(angle)) * 100

    __perimeter = perimeter
