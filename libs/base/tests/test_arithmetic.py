import unittest

from cyberlib_base.arithmetic import add2


class TestArithmetic(unittest.TestCase):
    def test_add2(self):
        result = add2(1, 2)

        self.assertEqual(3, result)
