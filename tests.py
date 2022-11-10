import unittest
import random

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
        self.assertEqual(pairs_finder(data_1, 10), expected_output_pos)

        # find pairs for negative number in range of -10 to 10
        data_2 = [x for x in range(-10, 11)]
        expected_output_neg = [(-10, 5), (-9, 4), (-8, 3), (-7, 2), (-6, 1), (-5, 0), (-4, -1), (-3, -2)]
        self.assertEqual(pairs_finder(data_2, -5), expected_output_neg)

        # find pairs for positive target number in positive list
        data_3 = [x for x in range(0, 100)]
        self.assertEqual(pairs_finder(data_3.copy(),11), [(0, 11), (1, 10), (2, 9), (3, 8), (4, 7), (5, 6)])
        self.assertEqual(pairs_finder(data_3.copy(), 40), [(0+x,40-x) for x in range(0,20)])
        self.assertEqual(pairs_finder(data_3.copy(), -10), [])

        # find pairs for negative  target number in negative list
        data_4 = [x for x in range(-100, 0)]
        self.assertEqual(pairs_finder(data_4, -10), [(-10+x, -x) for x in range(1,5)])
        self.assertEqual(pairs_finder(data_4, -199), [(-100, -99)])
        self.assertEqual(pairs_finder(data_4, -3), [(-2,-1)])

    def test_not_found_large_random_list(self):
        data = [random.randint(0,100000) for _ in range(10000)]
        data.sort()
        data_unique = list(set(data))
        self.assertEqual(pairs_finder(data_unique, -2000000), [])
        self.assertEqual(pairs_finder(data_unique, 2000000), [])


    def test_not_found_cases(self):
        five_interval = [x for x in range(-200,201,5)]
        self.assertEqual(pairs_finder(five_interval, 18), [])

        pairs = [x for x in range(-100, 101, 2)]
        self.assertEqual(pairs_finder(pairs, 11), [])
        self.assertEqual(pairs_finder(pairs, 15), [])

        odds = [x for x in range(-201, 202, 2)]
        self.assertEqual(pairs_finder(odds, 101), [])

        five_h = [x for x in range(-500, 500)]
        self.assertEqual(pairs_finder(five_h,1000), [])
        self.assertEqual(pairs_finder(five_h,-1000), [])

        single = [1]
        self.assertEqual(pairs_finder(single, 2), [])

        double = [1,3]
        self.assertEqual(pairs_finder(double, 3), [])

if __name__ == "__main__":
    unittest.main()