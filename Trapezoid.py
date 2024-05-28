from math import sqrt, degrees, acos, cos
from Quadrilateral import Quadrilateral

class Trapezoid(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_sides(self):
        sides = []
        for i in range(4):
            j = (i + 1) % 4
            side = sqrt((self._vertices[i][0] - self._vertices[j][0])**2 + (self._vertices[i][1] - self._vertices[j][1])**2)
            sides.append(side)
        return sides

    def _calculate_perimeter(self):
        return sum(self._sides)

    def _calculate_area(self):
        a, b, c, d = self._sides
        semi_perimeter_1 = (a + b + d) / 2
        area_triangle_1 = sqrt(semi_perimeter_1 * (semi_perimeter_1 - a) * (semi_perimeter_1 - b) * (semi_perimeter_1 - d))
        height = 2 * area_triangle_1 / a
        return (a + c) * height / 2

    def _calculate_diagonals(self):
        a, b, c, d = self._sides
        diagonal_AC = sqrt(a**2 + c**2 - 2 * a * c * cos(self._calculate_angle(b, d, a)))
        diagonal_BD = sqrt(b**2 + d**2 - 2 * b * d * cos(self._calculate_angle(a, c, b)))
        return (diagonal_AC, diagonal_BD)

    def _calculate_angles(self):
        angles = []
        for i in range(4):
            j = (i + 1) % 4
            k = (i + 2) % 4
            v1 = (self._vertices[j][0] - self._vertices[i][0], self._vertices[j][1] - self._vertices[i][1])
            v2 = (self._vertices[k][0] - self._vertices[j][0], self._vertices[k][1] - self._vertices[j][1])
            dot_product = v1[0] * v2[0] + v1[1] * v2[1]
            mag_v1 = sqrt(v1[0]**2 + v1[1]**2)
            mag_v2 = sqrt(v2[0]**2 + v2[1]**2)
            cos_angle = dot_product / (mag_v1 * mag_v2)
            angle_rad = acos(cos_angle)
            angles.append(degrees(angle_rad))
        return angles

    def _calculate_angle(self, side1, side2, opposite_side):
        return acos((side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2))
