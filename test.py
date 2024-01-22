import unittest
from csv_file_data import CSVFileData
from helper import *

BRISTOL_FILE_LOC = "./data/air_quality_data.csv"

class TestCSVFileDataClass(unittest.TestCase):
    """Test cases for CSVFileData class"""

    def test_csv_data_parsing(self):
        """Test CSV data parsing functionality"""
        expected_result = [['a','b','c','d'],
                            ['e','f','g','h']]
        csv_file = CSVFileData("./data/test_data.csv")
        actual_result = csv_file.get_data()
        self.assertEqual(actual_result, expected_result,
                         "Data is not parsed correctly")
        
    def test_incorrect_file_type(self):
        """Test raising of exception for incorrect file type"""
        with self.assertRaises(Exception):
            CSVFileData("Some_file.pdf")

    def test_file_not_existing(self):
        """Test raising of exception for file not existing"""
        with self.assertRaises(FileNotFoundError):
            CSVFileData("./data/does_not_exist.csv")

class TestAverageAQIFunction(unittest.TestCase):
    def test_average_aqi_no_empty_inputs(self):
        """Test function with no empty inputs"""
        expected_result = 9.5

        input_reading1 = [i for i in range(20)]
        input_reading2 = [2*i for i in range(20)]
        actual_result = calculate_average_aqi(input_reading1, input_reading2)
        self.assertEqual(actual_result, expected_result,
                        f"Average for test data should be {expected_result}")
        
    def test_average_aqi_all_empty_inputs(self):
        expected_result = 0

        input_readings = [['    ', '    '] for _ in range(20)]
        actual_result = calculate_average_aqi(input_readings[0], 
                                              input_readings[1])
        self.assertEqual(actual_result, expected_result,
            f"Average for empty inputs should be {expected_result}")
        
    def test_average_aqi_no_inputs(self):
        expected_result = 0
        input_readings = []
        actual_result = calculate_average_aqi(input_readings, input_readings)
        self.assertEqual(actual_result, expected_result,
                         f"Average for no inputs should be {expected_result}")

    def test_average_aqi_with_actual_data(self):
        expected_result = 27.80
        readings = bristol_data.get_readings()
        average = calculate_average_aqi(readings[0], readings[1])
        actual_result = round(average, 2)
        self.assertEqual(expected_result, actual_result,
                        f"Average for data should be {expected_result}")

    def test_average_aqi_one_column_empty(self):
        input_data = [i for i in range(20)]
        expected_result = 9.5
        actual_result = calculate_average_aqi(input_data, [])
        self.assertEqual(expected_result, actual_result,
                         "Result for average AQI should be 9.5")