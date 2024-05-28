from math import sqrt, degrees, atan2

from Trapezoid import Trapezoid


class RightTrapezoid(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_sides(self):
        sides = []
        num_vertices = len(self._vertices)
        for i in range(num_vertices):
            next_index = (i + 1) % num_vertices
            side = sqrt((self._vertices[i][0] - self._vertices[next_index][0]) ** 2 +
                        (self._vertices[i][1] - self._vertices[next_index][1]) ** 2)
            sides.append(side)
        return sides

    def _calculate_angles(self):
        # Assuming right angles are at vertices[0] and vertices[1]
        angles = [90, 90]

        # Calculate the other two angles using the law of cosines or vector approach
        # For simplicity, use atan2 to find angles relative to horizontal
        dx1 = self._vertices[2][0] - self._vertices[1][0]
        dy1 = self._vertices[2][1] - self._vertices[1][1]
        dx2 = self._vertices[3][0] - self._vertices[2][0]
        dy2 = self._vertices[3][1] - self._vertices[2][1]

        angle3 = degrees(atan2(dy1, dx1) - atan2(dy2, dx2))
        angle4 = 360 - sum(angles) - angle3  # Ensure total 360 degrees

        angles.append(abs(angle3))
        angles.append(abs(angle4))
        return tuple(angles)
