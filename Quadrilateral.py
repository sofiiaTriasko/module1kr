from abc import ABC, abstractmethod
import uuid
from math import sqrt, degrees, acos


class Quadrilateral(ABC):
    def __init__(self, vertices):
        self._type = self.__class__.__name__
        self._id = uuid.uuid4()
        self._vertices = tuple(vertices)
        self._sides = self._calculate_sides()
        self._perimeter = self._calculate_perimeter()
        self._area = self._calculate_area()
        self._diagonals = self._calculate_diagonals()
        self._angles = self._calculate_angles()

    @abstractmethod
    def _calculate_sides(self):
        sides = []
        for i in range(4):
            j = (i + 1) % 4
            side = sqrt((self._vertices[i][0] - self._vertices[j][0])**2 + (self._vertices[i][1] - self._vertices[j][1])**2)
            sides.append(side)
        return sides

    @abstractmethod
    def _calculate_perimeter(self):
        return sum(self._sides)

    @abstractmethod
    def _calculate_area(self):
        area = 0
        n = len(self._vertices)
        for i in range(n):
            j = (i + 1) % n
            area += self._vertices[i][0] * self._vertices[j][1]
            area -= self._vertices[j][0] * self._vertices[i][1]
        return abs(area) / 2

    @abstractmethod
    def _calculate_diagonals(self):
        d1 = sqrt((self._vertices[0][0] - self._vertices[2][0])**2 + (self._vertices[0][1] - self._vertices[2][1])**2)
        d2 = sqrt((self._vertices[1][0] - self._vertices[3][0])**2 + (self._vertices[1][1] - self._vertices[3][1])**2)
        return (d1, d2)

    @abstractmethod
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

    def is_type(self, type_name):
        return type_name.lower() in self._type.lower()

    def compare_area(self, other):
        return self._area - other._area

    def compare_perimeter(self, other):
        return self._perimeter - other._perimeter

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def get_vertices(self):
        return self._vertices

    def get_sides(self):
        return self._sides

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonals(self):
        return self._diagonals

    def get_angles(self):
        return self._angles
