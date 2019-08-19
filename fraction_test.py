import math
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12) + Fraction(2,3))
        # get whole number after addition
        self.assertEqual(Fraction(1), Fraction(1,2) + Fraction(1,2))
        # get fraction after addition with whole number
        self.assertEqual(Fraction(9,4), Fraction(2) + Fraction(1,4))

    def test_mul(self):
        self.assertEqual(Fraction(2,3), Fraction(1)*Fraction(2,3))
        self.assertEqual(Fraction(2,9), Fraction(1,3)* Fraction(2,3))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        inf = Fraction(1, 0)
        n_inf_one = Fraction(-1, 0)
        n_inf_two = Fraction(-1201023012, 0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        # -1/0 == -1201023012/0 neg_infinity == neg_infinity
        self.assertTrue(n_inf_one == n_inf_two)
        # neg_infinity != infinity
        self.assertFalse(n_inf_one == inf)
        # infinity != normal fraction
        self.assertFalse(inf == f)

    def test_sub(self):
        self.assertEqual(Fraction(1,4), Fraction(2, 4)-Fraction(1, 4))
    
    def test_gt(self):
        self.assertTrue(Fraction(1) > Fraction(1,2))
        self.assertFalse(Fraction(1) > Fraction(1))
    
    def test_neg(self):
        self.assertEqual(Fraction(1, 2), -Fraction(-1, 2))
        self.assertEqual(Fraction(1, -2), -Fraction(1, 2))