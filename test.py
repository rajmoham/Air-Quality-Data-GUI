import unittest
from csv_file_data import CSVFileData

BRISTOL_FILE_LOC = "./data/air_quality_data.csv"

class TestCSVFileDataClass(unittest.TestCase):
    def test_csv_data_parsing(self):
        expected_result = [['a','b','c','d'],
                            ['e','f','g','h']]
        csv_file = CSVFileData("./data/test_data.csv")
        actual_result = csv_file.get_data()
        self.assertEqual(actual_result, expected_result,
                         "Data is not parsed correctly")
