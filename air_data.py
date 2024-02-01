from csv_file_data import CSVFileData
class AirData(CSVFileData):
    """
    A subclass of CSVFileData for handling and extracting air quality
    data from a CSV file.
    """

    def __init__(self, file):
        """
        Initializes the AirData object.
        """
        super().__init__(file)