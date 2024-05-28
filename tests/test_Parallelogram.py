import unittest
from cmath import sqrt

from Parallelogram import Parallelogram


class TestParallelogram(unittest.TestCase):
    def setUp(self):
        # Example vertices for a simple parallelogram (base and height are 1 unit, side slants at 45 degrees)
        self.vertices = [(0, 0), (2, 0), (3, 1), (1, 1)]
        self.parallelogram = Parallelogram(self.vertices)

    def test_sides(self):
        expected_sides = [2, sqrt(2).real, 2, sqrt(2).real]  # Calculated based on the vertices setup
        calculated_sides = self.parallelogram._calculate_sides()
        for calculated_side, expected_side in zip(calculated_sides, expected_sides):
            self.assertAlmostEqual(calculated_side, expected_side, places=5)

    def test_perimeter(self):
        expected_perimeter = 2 * (sqrt(2).real + 2)  # Calculate expected perimeter
        self.assertAlmostEqual(self.parallelogram._calculate_perimeter(), expected_perimeter, places=5)

    def test_area(self):
        expected_area = 2  # Base * Height for the given vertices
        self.assertAlmostEqual(self.parallelogram._calculate_area(), expected_area, places=5)

    def test_diagonals(self):
        expected_diagonal1 = sqrt(10).real  # Distance between vertices 0 and 2
        expected_diagonal2 = sqrt(
            2).real  # Distance between vertices 1 and 3 (not 3.1622776601683795 which is sqrt(10))
        diagonals = self.parallelogram._calculate_diagonals()
        self.assertAlmostEqual(diagonals[0].real, expected_diagonal1, places=5)
        self.assertAlmostEqual(diagonals[1].real, expected_diagonal2, places=5)

    def test_angles(self):
        expected_angles = (45, 135, 45, 135)  # Expected angles for a simple parallelogram setup
        calculated_angles = self.parallelogram._calculate_angles()
        self.assertAlmostEqual(calculated_angles[0], expected_angles[0], places=5)
        self.assertAlmostEqual(calculated_angles[1], expected_angles[1], places=5)
        self.assertAlmostEqual(calculated_angles[2], expected_angles[2], places=5)
        self.assertAlmostEqual(calculated_angles[3], expected_angles[3], places=5)

if __name__ == '__main__':
    unittest.main()
