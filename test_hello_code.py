import unittest
from hello_code import hello

class Test(unittest.TestCase):
    def test_hello_code(self):
        self.assertAlmostEqual(hello("Tshepo"),"Hello Tshepo!")
        self.assertAlmostEqual(hello("Yanga"),"Hello Yanga!")
        self.assertAlmostEqual(hello("Zweli"),"Hello Zweli!")
