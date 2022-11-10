import unittest
from find_pairs import pairs_finder


class TestPairFinder(unittest.TestCase):
    """test for find_pairss() function"""

    def test_example(self):
        data = [1,9,5,0,20,-4,12,16,7]
        self.assertEqual(pairs_finder(data, 12), [(-4,16), (0,12), (5, 7)])

if __name__ == "__main__":
    unittest.main()