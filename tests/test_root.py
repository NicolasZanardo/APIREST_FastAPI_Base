import unittest
from app.app_root import *


class TestStringMethods(unittest.TestCase):
    def test_read_root(self):
        self.assertEqual(read_root(), { "Hello" : "World" })
        
    def test_read_item(self):
        self.assertEqual(read_item(12), { "item_id": 12, "q": None })

    def test_true_is_true(self):
        tester = TestedClass()
        self.assertFalse(tester.true_method())

if __name__ == '__main__':
    unittest.main()