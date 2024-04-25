import unittest
from app.app_root import *


class TestStringMethods(unittest.TestCase):
    def test_read_root(self):
        tested = TestedClass()
        self.assertTrue(tested.true_method())

if __name__ == '__main__':
    unittest.main()