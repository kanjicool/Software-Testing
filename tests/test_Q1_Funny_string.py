from coe_test.Q1_FunnyString import FunnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_bacxz_is_funny(self):
        s = 'acxz'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Funny')

    def test_give_hjlnp_is_funny(self):
        s = 'hjlnp'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Funny')

    def test_give_djnsyzxszry_is_funny(self):
        s = 'djnsyzxszryqworuxpqvqwquvotzsqvoupwvztzupowtqnvpxqyrwutzuys'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Not Funny')

    def test_give_rvovprxzvwrxpwpzsltzutxztrxqxt_is_not_funny(self):
        s = 'rvovprxzvwrxpwpzsltzutxztrxqxt'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Funny')

    def test_give_ceiosyrtztvnqsuozrxvtqywqwyrxtnjh_is_not_funny(self):
        s = 'ceiosyrtztvnqsuozrxvtqywqwyrxtnjh'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Not Funny')

    def test_give_ysklstz10_is_funny(self):
        s = 'ysklstzvzumrwqrywysxqxzuowryvnumrxpsysywytztvptwo'
        is_FunnyString = FunnyString(s)
        self.assertEqual(is_FunnyString, 'Not Funny')

