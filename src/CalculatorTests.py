import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.testData = CsvReader()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


    def test_instantiate_parser(self):
        self.assertIsInstance(self.testData, CsvReader)


    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


    def test_add_method_calculator(self):
        data_path = 'src/Addition.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()





if __name__ == '__main__':
    unittest.main()
