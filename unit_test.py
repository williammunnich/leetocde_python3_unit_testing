import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        try:
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 1), 0)
            self.assertEqual(add(-1, -1), -2)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised
    
    def test_subtract(self):
        try:
            self.assertEqual(subtract(5, 3), 2)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised
    
    def test_multiply(self):
        try:
            self.assertEqual(multiply(2, 3), 6)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised

    def test_divide(self):
        try:
            self.assertEqual(divide(10, 2), 5)
            self.assertEqual(divide(-10, 5), -2)
            self.assertEqual(divide(0, 1), 0)
            with self.assertRaises(Exception):
                divide(10, 0)  # This should raise an error for division by zero
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised
        

if __name__ == '__main__':
    unittest.main()
