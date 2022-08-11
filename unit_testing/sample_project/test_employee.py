import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    # Setup method will run its code before every single test
    def setUp(self):
        # Create 2 new employee instances before tests
        self.employee_1 = Employee('Max', 'Barr', 50000)
        self.employee_2 = Employee('Jon', 'Diggs', 75000)

    # Teardown method will run its code after every single test
    def tearDown(self):
        pass

    def test_email(self):
        # Test employee email addresses match format
        self.assertEqual(self.employee_1.email, 'Max.Barr@email.com')
        self.assertEqual(self.employee_2.email, 'Jon.Diggs@email.com')

        # Change employee first names
        self.employee_1.first = 'James'
        self.employee_2.first = 'Stephon'

        # Test employee emails
        self.assertEqual(self.employee_1.email, 'James.Barr@email.com')
        self.assertEqual(self.employee_2.email, 'Stephon.Diggs@email.com')

    def test_fullname(self):
        # Test employee full names match format
        self.assertEqual(self.employee_1.fullname, 'Max Barr')
        self.assertEqual(self.employee_2.fullname, 'Jon Diggs')

        # Change employee first names
        self.employee_1.first = 'James'
        self.employee_2.first = 'Stephon'

        # Test employee full names
        self.assertEqual(self.employee_1.fullname, 'James Barr')
        self.assertEqual(self.employee_2.fullname, 'Stephon Diggs')

    def test_apply_raise(self):
        # Test apply raise method
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()

        self.assertEqual(self.employee_1.pay, 52500)
        self.assertEqual(self.employee_2.pay, 78750)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.employee_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Barr/May')
            self.assertEqual(schedule, 'Success')

            # Testing Bad Response with employee 2
            mocked_get.return_value.ok = False

            schedule = self.employee_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Diggs/June')
            self.assertEqual(schedule, 'Bad Response')

# Entry point into the command line
if __name__ == "__main__":
    unittest.main()

