import unittest
from loader.reader import CSVReader
# from model.entity import Header

file_path = '/Users/olivier/PycharmProjects/opdracht-2/raw/employees.csv'


class TestCSVReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv_reader = CSVReader(file_path)

    def test_csv_name(self):
        csv = self.csv_reader
        self.assertEqual(csv.get_name(), 'employees')
        csv.set_name('Foo#Bar')
        self.assertEqual(csv.get_name(), 'foo_bar')

    def test_camel_to_snake_case(self):
        csv = self.csv_reader
        self.assertEqual(csv.camel_to_snake('CamelCase'), 'camel_case')
        self.assertNotEqual(csv.camel_to_snake('CamelCase'), 'CamelCase')

    def test_get_header_names(self):
        csv = self.csv_reader
        self.assertEqual(csv.get_header_names(), ['employee_id', 'manager_id', 'first_name', 'last_name', 'full_name',
 'job_title', 'organization_level', 'marital_status', 'gender', 'territory', 'country', 'group'])
        self.assertIsInstance(csv.get_header_names(), list)  # Ensure the returned value is a list
        self.assertNotEqual(csv.get_header_names(), [])  # Ensure the returned list is not empty
        self.assertNotEqual(csv.get_header_names(), ['test', 'test'])  # Ensure it's not equal to a specific dummy value
