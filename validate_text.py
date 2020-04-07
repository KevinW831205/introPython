import unittest
from validate import validate_length


class MyTestCase(unittest.TestCase):

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_length, "user",-1)


if __name__ == '__main__':
    unittest.main()
