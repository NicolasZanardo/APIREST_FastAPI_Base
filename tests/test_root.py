import unittest
from app import TestedClass


class TestStringMethods(unittest.TestCase):
    def test_read_root(self):
        tested = TestedClass()
        self.assertTrue(tested.true_method())

if __name__ == '__main__':
    unittest.main()