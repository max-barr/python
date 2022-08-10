import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        # Create 2 new employee instances
        employee_1 = Employee('Max', 'Barr', 50000)
        employee_2 = Employee('Jon', 'Diggs', 75000)

        # Test employee email addresses match format
        self.assertEqual(employee_1.email, 'Max.Barr@email.com')
        self.assertEqual(employee_2.email, 'Jon.Diggs@email.com')

        # Change employee first names
        employee_1.first = 'James'
        employee_2.first = 'Stephon'

        # Test employee emails
        self.assertEqual(employee_1.email, 'James.Barr@email.com')
        self.assertEqual(employee_2.email, 'Stephon.Diggs@email.com')

    def test_fullname(self):
        

