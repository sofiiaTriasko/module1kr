import unittest
from math import sqrt

# Assuming the Rhombus class is correctly imported
from Rhombus import Rhombus

class TestRhombus(unittest.TestCase):
    def setUp(self):
        self.vertices = [(0, 0), (2, 2), (4, 0), (2, -2)]
        self.rhombus = Rhombus(self.vertices)

    def test_area(self):
        expected_diagonals = self.rhombus._calculate_diagonals()
        expected_area = (expected_diagonals[0] * expected_diagonals[1]) / 2
        self.assertAlmostEqual(self.rhombus._calculate_area(), expected_area, places=5)

    def test_angles(self):
        expected_angles = (60, 120, 60, 120)
        self.assertEqual(self.rhombus._calculate_angles(), expected_angles)

if __name__ == '__main__':
    unittest.main()
