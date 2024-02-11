from coe_test.Q5_GridChallenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_grid_1(self):
        grid = ["abc", "ade", "efg"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_2(self):
        grid = ["xxx", "yyy", "zzz"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_3(self):
        grid = ["AB", "CD", "EF"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_4(self):
        grid = ["qwe", "asd", "zxc"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_grid_5(self):
        grid = ["jkl", "uio", "rty"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_grid_6(self):
        grid = ["tgbrfv", "yhnrfv", "ujmrfv"]
        self.assertEqual(gridChallenge(grid), "NO")
