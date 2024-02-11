from coe_test.Q4_TwoCharacters import alternate
import unittest

class TwoCharactersTest(unittest.TestCase):
    def test_beabeefeab_(self):
        s = 'beabeefeab'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 5)

    def test_a_(self):
        s = 'a'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 0)
    
    def test_ab_(self):
        s = 'ab'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)
    
    def test_asvkugfiugsalddlasguifgukvsa_(self):
        s = 'asvkugfiugsalddlasguifgukvsa'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 0)

    def test_asdcbsdcagfsdbgdfanfghbsfdab_(self):
        s = 'asdcbsdcagfsdbgdfanfghbsfdab'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 8)
    
    def test_aaaaa_(self):
        s = 'aaaaa'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 0)

    def test_kanjicool555_(self):
        s = 'kanjicool555'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)

    def test_KaNjIcool404_(self):
        s = 'KaNjIcool404'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 3)

    def test_KANjiC00l_(self):
        s = 'KAN-ji-C00l '
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 3)

    def test_KANjC0_(self):
        s = '#KaN_j!-C0*1'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)