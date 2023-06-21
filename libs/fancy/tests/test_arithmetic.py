import unittest

from cyberlib_fancy.arithmetic import add3


class TestArithmetic(unittest.TestCase):
    def test_add3(self):
        result = add3(1, 2, 3)

        self.assertEqual(6, result)
