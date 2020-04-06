import unittest
from adding import add

class MyTestCase(unittest.TestCase):
    def test_add(self):
        testcase = (1,2)
        expected = 3;
        self.assertEqual(add(testcase[0],testcase[1]), expected)


if __name__ == '__main__':
    unittest.main()
