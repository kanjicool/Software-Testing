from coe_test.Q3_CaesarCipher import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_give_k_is_3_if_s_is_lower(self):
        s = 'kanjicool'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'ndqmlfrro')

    def test_give_k_is_3_if_s_is_upper(self):
        s = 'KANJICOOL'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'NDQMLFRRO')

    
    def test_give_k_is_87_if_s_is_lower(self):
        s = 'www.abc.xy'
        k = 87
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'fff.jkl.gh')

    def test_give_k_is_3_if_s_is_int(self):
        s = '159357lcfd'
        k = 98
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '159357fwzx')

    def test_give_k_is_3_if_s_is_upper_and_lower(self):
        s = 'middle-Outz'
        k = 2
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'okffng-Qwvb')

    def test_give_k_is_3_if_s_is_special(self):
        s = '+-*/@#$%^&'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '+-*/@#$%^&')

    def test_give_k_is_62_if_s_is_all(self):
        s = '!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U'
        k = 62
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E')

    def test_give_k_is_3_if_s_is_empty(self):
        s = ''
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '')