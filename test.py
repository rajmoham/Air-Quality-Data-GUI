import unittest
from csv_file_data import CSVFileData
from air_data import AirData
from helper import calculate_average_aqi, average, \
    calculate_difference, population_sd, highest_three_point_sd, \
    get_three_point_window_data, separate_data


class TestCSVFileDataClass(unittest.TestCase):
    """Test cases for CSVFileData class"""

    def test_csv_data_parsing(self):
        """Test CSV data parsing functionality"""
        expected_result = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
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
        input_reading2 = [2 * i for i in range(20)]
        actual_result = calculate_average_aqi(input_reading1, input_reading2)
        self.assertEqual(actual_result, expected_result,
                         f"Average for test data should be {expected_result}")

    def test_average_aqi_all_empty_inputs(self):
        """Test function where inputs are contentless strings"""
        expected_result = 0

        input_readings = [['    ', '    '] for _ in range(20)]
        actual_result = calculate_average_aqi(input_readings[0],
                                              input_readings[1])
        self.assertEqual(
            actual_result, expected_result,
            f"Average for empty inputs should be {expected_result}")

    def test_average_aqi_no_inputs(self):
        """Test function with an empty list"""
        expected_result = 0
        input_readings = []
        actual_result = calculate_average_aqi(input_readings, input_readings)
        self.assertEqual(actual_result, expected_result,
                         f"Average for no inputs should be {expected_result}")

    def test_average_aqi_one_column_empty(self):
        """Test function with only one column of 2D list filled"""
        input_data = [i for i in range(20)]
        expected_result = 9.5
        actual_result = calculate_average_aqi(input_data, [])
        self.assertEqual(expected_result, actual_result,
                         "Result for average AQI should be 9.5")


class TestAverageFunction(unittest.TestCase):

    def test_avg_with_no_data(self):
        """Test average function with no data"""
        input_data = []
        expected_result = 0
        actual_result = average(input_data)
        self.assertEqual(actual_result, expected_result,
                         "Average for no data should be 0")

    def test_avg_with_sample_data(self):
        """Test average function with set of data"""
        input_data = [1.3, 2.4, 19.4, 29.3, 20.9, 16.6, 25.5, 23.7]
        expected_result = 17.3875
        actual_result = average(input_data)
        self.assertEqual(
            actual_result, expected_result,
            f"Average for {input_data} should be {expected_result}")


class TestCalculateDifference(unittest.TestCase):

    def test_difference_wrong_order(self):
        """Test function with parameters passed in wrong order"""
        expected_result = 5.0

        actual_result = calculate_difference(15.0, 10.0)
        self.assertEqual(actual_result, expected_result,
                         "Difference for wrong order should be 5.0")

    def test_difference_correct_order(self):
        """Test function with parameters passed in correct order"""
        expected_result = 5.0

        actual_result = calculate_difference(10.0, 15.0)
        self.assertEqual(actual_result, expected_result,
                         "Difference for correct order should be 5.0")

    def test_difference_same_number(self):
        """Test function with the same value"""
        expected_result = 0.0

        actual_result = calculate_difference(15.0, 15.0)
        self.assertEqual(actual_result, expected_result,
                         "Difference for same numbers should be 0.0")


class TestStandardDeviation(unittest.TestCase):

    def test_sd_no_deviated_dataset(self):
        """Test SD function with no all items in list being the same"""
        input_data = [1 for i in range(5)]
        expected_result = 0
        actual_result = population_sd(input_data)
        self.assertEqual(actual_result, expected_result,
                         "Result should be 0 for no deviation")

    def test_sd_no_input_data(self):
        """Test SD function with empty list"""
        input_data = []
        expected_result = 0
        actual_result = population_sd(input_data)
        self.assertEqual(actual_result, expected_result,
                         "Result should be 0 for no inputs")

    def test_sd_dataset_length_one(self):
        """Test SD function with 1 item in the list"""
        input_data = [1]
        expected_result = 0
        actual_result = population_sd(input_data)
        self.assertEqual(actual_result, expected_result,
                         "Result should be 0 for a list of length 1")

    def test_sd_with_sample_data(self):
        """Test SD function with a sample of the data"""
        input_data = [
            18.1, 12.7, 9.9, 18.3, 13, 16.2, 17.6, 16.7, 13.9, 17.5, 25.4, 15.9
        ]
        expected_result = 3.698
        actual_result = round(population_sd(input_data), 3)
        self.assertEqual(
            actual_result, expected_result,
            f"Result should be {expected_result} for the data: \
                            {input_data}")


class TestAirDataClass(unittest.TestCase):
    BRISTOL_FILE_LOC = "./data/air_quality_data.csv"
    bristol_data = AirData(BRISTOL_FILE_LOC)

    def test_interitance(self):
        """Tests for inheritance between CSVFileData and AirData"""
        self.assertIsInstance(self.bristol_data, CSVFileData,
                              "Inheritance is not implemented")

    def test_air_data_title(self):
        """Tests for correct title output from data file"""
        expected_result = 'Mobile Pie NOx data'

        actual_result = self.bristol_data.get_title()
        self.assertEqual(actual_result, expected_result,
                         "Title not extracted correctly")

    def test_air_data_locations(self):
        """Tests for correct locations output from data file"""
        expected_result = ['NO2 Brislington', 'NO2 Rupert Street']

        actual_result = self.bristol_data.get_location_names()
        self.assertEqual(actual_result, expected_result,
                         "Locations not extracted correctly")

    def test_overriden_function_from_inheritance(self):
        """Tests for inheritance between parent and child class"""
        parent_class_function = CSVFileData.get_data
        child_class_function = AirData.get_data
        self.assertIsNot(parent_class_function, child_class_function,
                         "Overriding functions not done correctly")


class TestSeparateDataFunction(unittest.TestCase):

    def test_function_with_sample_data(self):
        """Tests function with a set of sample data"""
        input_data = [
            ['0', '0', 1.0, 2.0],
            ['0', '1', 3.0, 4.0],
            ['0', '2', 5.0, 6.0],
            ['1', '0', 7.0, 8.0],
            ['1', '1', 9.0, 10.0],
            ['1', '2', 11.0, 12.0],
        ]
        expected_results = ([['0', '0', 1.0], ['0', '1', 3.0], ['0', '2', 5.0],
                             ['1', '0', 7.0], ['1', '1', 9.0],
                             ['1', '2', 11.0]], [['0', '0', 2.0],
                                                 ['0', '1', 4.0],
                                                 ['0', '2', 6.0],
                                                 ['1', '0', 8.0],
                                                 ['1', '1', 10.0],
                                                 ['1', '2', 12.0]])
        actual_results = separate_data(input_data)
        self.assertEqual(expected_results, actual_results)

    def test_function_with_invalid_data(self):
        """Tests the function where no readings are valid"""
        input_data = [
            ['0', '0', '   ', '   '],
            ['0', '1', '   ', '   '],
            ['0', '2', '   ', '   '],
        ]
        expected_results = ([], [])
        actual_results = separate_data(input_data)
        self.assertEqual(expected_results, actual_results)


class TestThreePointWindowFunction(unittest.TestCase):

    def test_data_with_sample_data(self):
        input_data = [[3 * x + 2 * y for x in range(3)] for y in range(10)]
        actual_results = get_three_point_window_data(input_data, 3)
        expected_results = [12, 14, 16]
        self.assertEqual(actual_results, expected_results)


class TestHighestThreePointSDFunction(unittest.TestCase):
    BRISTOL_FILE_LOC = "./data/air_quality_data.csv"
    bristol_data = AirData(BRISTOL_FILE_LOC)

    def test_function_with_sample_data(self):
        input_data = [['0', '0', 1.2], ['0', '1', 3.4], ['1', '0', 34.5],
                      ['1', '1', 2.3]]
        actual_results = highest_three_point_sd(input_data)
        expected_results = [['0', '0', 1.2], ['0', '1', 3.4], ['1', '0', 34.5]]
        self.assertEqual(actual_results, expected_results)

    def test_function_with_not_enough_data(self):
        input_data = []
        actual_results = highest_three_point_sd(input_data)
        expected_results = None
        self.assertEqual(actual_results, expected_results)
