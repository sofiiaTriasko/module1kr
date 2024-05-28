import unittest
from math import sqrt

from Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.vertices = [(0, 0), (2, 0), (2, 3), (0, 3)]
        self.rectangle = Rectangle(self.vertices)

    def test_perimeter(self):
        self.assertEqual(self.rectangle._calculate_perimeter(), 10)

    def test_area(self):
        self.assertEqual(self.rectangle._calculate_area(), 6)

    def test_diagonals(self):
        expected_diagonal = sqrt(2**2 + 3**2)
        self.assertEqual(self.rectangle._calculate_diagonals(), (expected_diagonal,))

    def test_angles(self):
        expected_angles = (90, 90, 90, 90)
        self.assertEqual(self.rectangle._calculate_angles(), expected_angles)

if __name__ == '__main__':
    unittest.main()
