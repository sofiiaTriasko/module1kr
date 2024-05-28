from math import acos, degrees
from cmath import sqrt

from Quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._sides = self._calculate_sides()
        self._angles = self._calculate_angles()

    def _calculate_perimeter(self):
        return 2 * (self._sides[0] + self._sides[1])

    def _calculate_area(self):
        x1, y1 = self._vertices[0]
        x2, y2 = self._vertices[1]
        x3, y3 = self._vertices[2]
        x4, y4 = self._vertices[3]
        return abs(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1)) / 2

    def _calculate_diagonals(self):
        diagonal1 = sqrt((self._vertices[0][0] - self._vertices[2][0])**2 + (self._vertices[0][1] - self._vertices[2][1])**2)
        diagonal2 = sqrt((self._vertices[1][0] - self._vertices[3][0])**2 + (self._vertices[1][1] - self._vertices[3][1])**2)
        return (diagonal1, diagonal2)

    def _calculate_sides(self):
        sides = []
        num_vertices = len(self._vertices)
        for i in range(num_vertices):
            x1, y1 = self._vertices[i]
            x2, y2 = self._vertices[(i + 1) % num_vertices]
            side_length = sqrt((x2 - x1)**2 + (y2 - y1)**2).real
            sides.append(side_length)
        return sides

    def _calculate_angles(self):
        def angle_between(v1, v2):
            dot_p = v1[0] * v2[0] + v1[1] * v2[1]
            mag_v1 = sqrt(v1[0]**2 + v1[1]**2).real
            mag_v2 = sqrt(v2[0]**2 + v2[1]**2).real
            cos_angle = dot_p / (mag_v1 * mag_v2)
            clamped_cos_angle = max(-1, min(1, cos_angle))
            angle_rad = acos(clamped_cos_angle)
            return degrees(angle_rad)

        v1 = (self._vertices[1][0] - self._vertices[0][0], self._vertices[1][1] - self._vertices[0][1])
        v2 = (self._vertices[2][0] - self._vertices[1][0], self._vertices[2][1] - self._vertices[1][1])
        angle1 = angle_between(v1, v2)
        angle2 = 180 - angle1
        return (angle1, angle2, angle1, angle2)
