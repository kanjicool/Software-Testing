from coe_test.Q2_AlternatingCharacters import alternatingCharacters 
import unittest

class alternatingCharactersTest(unittest.TestCase):
    def test_give_AAAA_is_4_in_deletions(self):
        s = "AAAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 3)

    def test_give_AAABBB_is_5_in_deletions(self):
        s = "AAABBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 4)

    def test_give_ABABBABAAB_is_8_in_deletions(self):
        s = "ABABBABAAB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 2)

    def test_give_AAAABAABBB_is_13_in_deletions(self):
        s = "AAAABAABBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 6)

    def test_give_ABABABABABABBBAA_is_3_in_deletions(self):
        s = "ABABABABABABBBAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 3)

    def test_give_ABABABAB_is_2_in_deletions(self):
        s = "ABABABAB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 0)

    def test_give_ABABABABABABABAA_is_1_in_deletions(self):
        s = "ABABABABABABABAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 1)

    def test_give_BAABAAABAAAB_is_2_in_deletions(self):
        s = "BAABAAABAAABBBAABAAAAABABAAAABABBAABBBABBAAAABABBABAAAAABBABAABBBBAAAABBAABABAAAABABABBBABAAABBBBBBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 51)

    
    def test_give_BBBBBBBBBBABBB_is_2_in_deletions(self):
        s = "BBBBBBBBBBABBBBBBBBBBBBBBBBBBBBBBBBBABBBBBBBABBBBBBABBABAABBBBBABBBBBABBBBBBBABBBBBABBBBBBBABBAABBAB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 73)

    
    def test_give_BABBBBBBBB_is_2_in_deletions(self):
        s = "BABBBBBBBBBBABBBBBBBBABBBBBAABBBABBBBAABBBBBBABBBBBBBBBABBBBBBBBBBBBBABBBBBBBAABBBBBBABBBBBBABBABBBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 73)