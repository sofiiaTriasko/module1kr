from math import sqrt

from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_area(self):
        return self._sides[0] ** 2

    def _calculate_perimeter(self):
        return 4 * self._sides[0]

    def _calculate_diagonals(self):
        return (self._sides[0] * sqrt(2),)

    def _calculate_angles(self):
        return (90, 90, 90, 90)
