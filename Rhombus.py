from math import sqrt
from Parallelogram import Parallelogram

class Rhombus(Parallelogram):
    def __init__(self, vertices):
        # First calculate diagonals to ensure they are available for area calculation
        self._diagonals = self._calculate_initial_diagonals(vertices)
        super().__init__(vertices)

    def _calculate_initial_diagonals(self, vertices):
        # Temporary method to calculate diagonals for constructor usage
        d1 = sqrt((vertices[0][0] - vertices[2][0])**2 + (vertices[0][1] - vertices[2][1])**2)
        d2 = sqrt((vertices[1][0] - vertices[3][0])**2 + (vertices[1][1] - vertices[3][1])**2)
        return (d1, d2)

    def _calculate_sides(self):
        # Assuming each side of the rhombus has the same length
        side = sqrt((self._vertices[0][0] - self._vertices[1][0])**2 + (self._vertices[0][1] - self._vertices[1][1])**2)
        return [side] * 4

    def _calculate_area(self):
        # Now safe to use _diagonals as they are initialized
        return (self._diagonals[0] * self._diagonals[1]) / 2

    def _calculate_diagonals(self):
        # Properly assign diagonals based on already initialized vertices
        return self._calculate_initial_diagonals(self._vertices)

    def _calculate_angles(self):
        # Simplified; actual implementation may differ
        angle = 60
        return (angle, 180 - angle, angle, 180 - angle)
