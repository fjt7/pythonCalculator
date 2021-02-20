import unittest
from Calculator import Calculator
import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_addition_method(self):
        self.assertEqual(self.calculator.add(5, 5), 10)

    def test_results_subtraction_method(self):
        self.assertEqual(self.calculator.subtract(12, 4), 8)

    def test_results_multiplication_method(self):
        self.assertEqual(self.calculator.multiply(8, 8), 64)

    def test_results_division_method(self):
        self.assertEqual(self.calculator.divide(72, 8), 9)

    def test_results_square_method(self):
        self.assertEqual(self.calculator.squaring(5), 25)
    
    def test_results_squareroot_method(self):
        self.assertEqual(self.calculator.squarerooting(169), 13)

    def test_subtraction(self):
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
