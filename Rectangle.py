from math import sqrt

from Quadrilateral import Quadrilateral

class Rectangle(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_sides(self):
        # Розрахунок довжин сторін, припускаючи, що вершини передані у послідовному порядку
        sides = []
        num_vertices = len(self._vertices)
        for i in range(num_vertices):
            next_index = (i + 1) % num_vertices
            side_length = sqrt((self._vertices[i][0] - self._vertices[next_index][0])**2 +
                               (self._vertices[i][1] - self._vertices[next_index][1])**2)
            sides.append(side_length)
        return sides

    def _calculate_perimeter(self):
        return 2 * (self._sides[0] + self._sides[1])

    def _calculate_area(self):
        # Припускаємо, що перші дві сторони - це довжина і ширина
        return self._sides[0] * self._sides[1]

    def _calculate_diagonals(self):
        return (sqrt(self._sides[0]**2 + self._sides[1]**2),)

    def _calculate_angles(self):
        # Усі кути прямокутника — 90 градусів
        return (90, 90, 90, 90)
