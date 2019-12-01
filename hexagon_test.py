import unittest
from Hexagon import Hexagon


class TestHexagon(unittest.TestCase):

    def test_hexagon_perimeter(self):
        self.assertEqual(6.0, Hexagon(1.0).perimeter)
        self.assertEqual(12.0, Hexagon(2.0).perimeter)

    def test_hexagon_area(self):
        self.assertEqual(2.598076211353316, Hexagon(1.0).area)
        self.assertEqual(10.392304845413264, Hexagon(2.0).area)


if __name__ == '__main__':
    unittest.main()
