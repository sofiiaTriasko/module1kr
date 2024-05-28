import unittest
from math import sqrt

from Quadrilateral import Quadrilateral


class ConcreteQuadrilateral(Quadrilateral):
    def _calculate_sides(self):
        return super()._calculate_sides()

    def _calculate_perimeter(self):
        return super()._calculate_perimeter()

    def _calculate_area(self):
        return super()._calculate_area()

    def _calculate_diagonals(self):
        return super()._calculate_diagonals()

    def _calculate_angles(self):
        return super()._calculate_angles()

class TestQuadrilateral(unittest.TestCase):
    def setUp(self):
        self.vertices_square = [(0, 0), (1, 0), (1, 1), (0, 1)]
        self.square = ConcreteQuadrilateral(self.vertices_square)

    def test_type(self):
        self.assertEqual(self.square.get_type(), 'ConcreteQuadrilateral')

    def test_id(self):
        another_square = ConcreteQuadrilateral(self.vertices_square)
        self.assertNotEqual(self.square.get_id(), another_square.get_id())

    def test_sides_length(self):
        expected_sides =[1.0, 1.0, 1.0, 1.0]
        self.assertEqual(self.square.get_sides(), expected_sides)

    def test_perimeter(self):
        self.assertEqual(self.square.get_perimeter(), 4)

    def test_area(self):
        self.assertEqual(self.square.get_area(), 1)

    def test_diagonals(self):
        expected_diagonals = (sqrt(2), sqrt(2))
        self.assertEqual(self.square.get_diagonals(), expected_diagonals)

    def test_angles(self):
        expected_angles = [90.0, 90.0, 90.0, 90.0]
        self.assertEqual(self.square.get_angles(), expected_angles)

    def test_compare_area(self):
        another_square = ConcreteQuadrilateral(self.vertices_square)
        self.assertEqual(self.square.compare_area(another_square), 0)

    def test_compare_perimeter(self):
        another_square = ConcreteQuadrilateral(self.vertices_square)
        self.assertEqual(self.square.compare_perimeter(another_square), 0)

if __name__ == '__main__':
    unittest.main()
