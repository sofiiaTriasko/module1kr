import unittest
from math import sqrt

# Assuming the Square class is correctly imported
from Square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        # Define a square using vertices that form a square of side length 2
        # Vertices are (0,0), (2,0), (2,2), and (0,2)
        self.vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
        self.square = Square(self.vertices)

    def test_perimeter(self):
        # Perimeter of a square with side length 2 should be 8
        self.assertEqual(self.square._calculate_perimeter(), 8)

    def test_area(self):
        # Area of a square with side length 2 should be 4 (2*2)
        self.assertEqual(self.square._calculate_area(), 4)

    def test_diagonals(self):
        # Diagonal of a square with side length 2 should be 2*sqrt(2)
        expected_diagonal = 2 * sqrt(2)
        self.assertEqual(self.square._calculate_diagonals(), (expected_diagonal,))

    def test_angles(self):
        # All angles in a square should be 90 degrees
        expected_angles = (90, 90, 90, 90)
        self.assertEqual(self.square._calculate_angles(), expected_angles)

if __name__ == '__main__':
    unittest.main()
