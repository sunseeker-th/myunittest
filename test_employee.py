""" Test employee """
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Test employee class """

    def test_email(self):
        """ test email """
        emp_1 = Employee('Jame', 'Doe', 50000)
        emp_2 = Employee('Smith', 'Tan', 60000)

        self.assertEqual(emp_1.email, 'Jame.Doe@email.com')
        self.assertEqual(emp_2.email, 'Smith.Tan@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Doe@email.com')
        self.assertEqual(emp_2.email, 'Jane.Tan@email.com')

if __name__ == '__main__':
    unittest.main()