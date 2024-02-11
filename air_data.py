from csv_file_data import CSVFileData


class AirData(CSVFileData):
    """
    A subclass of CSVFileData for handling and extracting air quality
    data from a CSV file.
    """

    def __init__(self, file):
        """
        Initialise the AirData object.

        Invoke the constructor of the superclass (CSVFileData) and then
        extracts air quality data.
        """

        super().__init__(file)
        self._extract_information()

    def _extract_information(self):
        """Extract and parse various data from the inherited CSV file data.
        """

        self._extract_title()
        self._extract_location_names()
        self._extract_readings()

    def _extract_title(self):
        """Extract the title from the file"""

        self._title = self._file_data[0][0]

    def get_title(self):
        """Return the title of the air quality data."""

        return self._title

    def _extract_location_names(self):
        """Extract the two location names from the file"""

        self._location_names = self._file_data[6][2:4]

    def get_location_names(self):
        """Return the two location names of the air quality data"""

        return self._location_names

    def get_data(self):
        """Override the function from the parent class
        Extracts and Returns the data fr the air quality dat
        """
        
        # Creates deep copy of the file data
        data = [x[:] for x in self._file_data][9:]

        for i,row in enumerate(data):
            data[i][2] = self.cast_to_num(row[2])
            data[i][3] = self.cast_to_num(row[3])

        return data

    def _extract_readings(self):
        """Extract and parse the raw data readings from the file"""

        reading1 = []
        reading2 = []
        for row in self.get_data():
            reading1.append((row[2]))
            reading2.append((row[3]))

        self._readings = [reading1, reading2]

    def get_readings(self):
        return self._readings

    def parse_data(self, data_field):
        """Convert the given data field into float if it is not empty"""

        if data_field.isspace():
            return data_field

        return float(data_field)

    def get_timescale(self):
        """Returns the timestamps for the readings."""
        data = self.get_data()
        timescale = []

        for row in data:
            timescale.append(row[1])

        return timescale
    
    def cast_to_num(self,data_field):
        """Converts the given data field into float if it is not empty"""
        if data_field.isspace():
            return data_field
        
        return float(data_field)
