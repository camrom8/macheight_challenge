import unittest
from find_pairs import pairs_finder


class TestPairFinder(unittest.TestCase):
    """test for find_pairss() function"""

    def test_example(self):
        data = [1,9,5,0,20,-4,12,16,7]
        self.assertEqual(pairs_finder(data, 12), [(-4,16), (0,12), (5, 7)])

    def test_consecutive(self):
        # find pairs for  positive number in range of -20 to 20
        data_1 = [x for x in range(-20, 21)]
        expected_output_pos = [(-10, 20), (-9, 19), (-8, 18), (-7, 17), (-6, 16), (-5, 15), (-4, 14),
                               (-3, 13), (-2, 12), (-1, 11), (0, 10), (1, 9), (2, 8), (3, 7), (4, 6)]
        print(expected_output_pos)
        self.assertEqual(pairs_finder(data_1, 10), expected_output_pos)

        # find pairs for negative number in range of -10 to 10
        data_2 = [x for x in range(-10, 11)]
        expected_output_neg = [(-10, 5), (-9, 4), (-8, 3), (-7, 2), (-6, 1), (-5, 0), (-4, -1), (-3, -2)]
        print(expected_output_neg)
        self.assertEqual(pairs_finder(data_2, -5), expected_output_neg)

if __name__ == "__main__":
    unittest.main()