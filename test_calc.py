import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_devide(self):
        self.assertEqual(calc.devide(10, 5), 2)
        self.assertEqual(calc.devide(-1, 1), -1)
        self.assertEqual(calc.devide(-1, -1), 1)
        
        with self.assertRaises(ValueError):
            calc.devide(10, 0)
        
if __name__ == '__main__':
    unittest.main()