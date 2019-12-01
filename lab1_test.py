import unittest
from lab1_module import *


class TestLab1(unittest.TestCase):

    def test_max_of_vector(self):
        self.assertEqual(3, max_of_vector([1, 2, 3]))
        self.assertEqual(-1, max_of_vector([-1, -2, -3]))

    def test_min_of_vector(self):
        self.assertEqual(1, min_of_vector([1, 2, 3]))
        self.assertEqual(-3, min_of_vector([-1, -2, -3]))

    def test_sum_positive_vector(self):
        self.assertEqual(8, sum_positive_vector([-1, -2, 3, 5]))
        self.assertEqual(6, sum_positive_vector([1, 2, 3, -1]))

    def test_count_positive_vector(self):
        self.assertEqual(2, count_positive_vector([-1, -2, 3, 5]))
        self.assertEqual(3, count_positive_vector([1, 2, 3, -1]))

    def test_lab1_task1(self):
        self.assertEqual(3.3, lab1_task1([-1, -2, 0.5], [1, 2, 0.5], [-3, -2, 1]))

    def test_lab1_func1(self):
        self.assertEqual(1.0, func1(0))

    def test_lab1_func2(self):
        self.assertEqual(2.5, func2(0))
        self.assertEqual(3.5, func2(1))


if __name__ == '__main__':
    unittest.main()
