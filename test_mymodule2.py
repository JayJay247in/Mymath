import unittest
from mymodule2 import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_integers(self):
        self.assertEqual(add(2, 4), 6)

    def test_add_zero_integers(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_positive_floats(self):
        self.assertEqual(add(2.3, 3.6), 5.9)

    def test_add_strings(self):
        self.assertEqual(add('hello', 'world'), 'helloworld')

    def test_add_floats_with_precision(self):
          self.assertEqual(add(2.3000, 4.300), 6.6)

    def test_add_negative_integers(self):
        self.assertNotEqual(add(-2, -2), 0)

if __name__ == '__main__':
    unittest.main()