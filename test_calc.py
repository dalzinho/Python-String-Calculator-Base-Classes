from unittest import TestCase
from Calc import Calc

class TestCalc(TestCase):

    def test_pass_empty_string_get_0(self):
        calc = Calc()
        self.assertEqual(0, calc.add(""))
