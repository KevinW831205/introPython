import unittest

from practice.duplicate_count import duplicate_count


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = "abcde"
        actual = duplicate_count(input)
        self.assertEqual(0, actual)

    def test_2(self):
        input = "abcdea"
        actual = duplicate_count(input)
        self.assertEqual(1, actual)

    def test_3(self):
        input = "indivisibility"
        actual = duplicate_count(input)
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
