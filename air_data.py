from csv_file_data import CSVFileData
class AirData(CSVFileData):
    """
    A subclass of CSVFileData for handling and extracting air quality
    data from a CSV file.
    """

    def __init__(self, file):
        """
        Initializes the AirData object.

        Invokes the constructor of the superclass (CSVFileData) and then
        extracts air quality data.
        """
        super().__init__(file)
        self._extract_data()

    def _extract_data(self):
        """
        Extracts and parses various data from the inherited CSV file data.
        """
        self._extract_title()
        self._extract_location_names()
        self._extract_data()
        self._extract_readings()

    def _extract_title(self):
        """Extracts the title from the file"""
        self._title = self._file_data[0][0]

    def get_title(self):
        """Returns the title of the air quality data."""
        return self._title
    
    def _extract_location_names(self):
        """Extracts the two location names from the file"""
        self._location_names = self._file_data[6][2:4]
    
    def get_location_names(self):
        """Returns the two location names of the air quality data"""
        return self._location_names
    
    def get_data(self):
        """
        Overrides the function from the parent class
        Extracts and Returns the data fr the air quality dat
        """
        return self._file_data[9:]
