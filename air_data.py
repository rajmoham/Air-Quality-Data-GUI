from csv_file_data import CSVFileData


class AirData(CSVFileData):
    """A subclass of CSVFileData for handling and extracting air quality
    data from a CSV file.
    """

    def __init__(self, file):
        """Initialise the AirData object."""

        super().__init__(file)

    def get_title(self):
        """Return the title of the air quality data."""

        return self._file_data[0][0]

    def get_location_names(self):
        """Return the two location names of the air quality data"""

        return self._file_data[6][2:4]

    def get_data(self):
        """Extract and Return the data for the air quality data
        (Overrides the function from the parent class)
        """

        # Create deep copy of the file data
        data = [x[:] for x in self._file_data][9:]

        for i, row in enumerate(data):
            data[i][2] = self.cast_to_num(row[2])
            data[i][3] = self.cast_to_num(row[3])

        return data

    def get_readings(self):
        """Return readings from file data in separating columns."""
        reading1 = []
        reading2 = []
        for row in self.get_data():
            reading1.append((row[2]))
            reading2.append((row[3]))

        return reading1, reading2

    def get_timescale(self):
        """Return the timestamps for the readings."""
        data = self.get_data()
        timescale = []

        for row in data:
            timescale.append(row[1])

        return timescale

    def parse_data(self, data_field):
        """Convert the given data field into float if it is not empty."""

        if data_field.isspace():
            return data_field

        return float(data_field)

    def cast_to_num(self, data_field):
        """Convert the given data field into float if it is not empty."""
        if data_field.isspace():
            return data_field

        return float(data_field)
