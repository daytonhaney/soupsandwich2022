import unittest
from math import pi 
from test_unit import circle_area 

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test 
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0,0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
