import unittest

from main import *


class MyTestCase(unittest.TestCase):
    def test_computeR2D2PopulationStep1(self):
        self.assertEqual(computeR2D2Population(2), [10,10,10])

    def test_computeR2D2PopulationStep2(self):
        self.assertEqual(computeR2D2Population(2), [60,5,3])

    def test_computeR2D2PopulationStep3(self):
        self.assertEqual(computeR2D2Population(3), [26, 30, 1])


if __name__ == '__main__':
    unittest.main()
