class CSVFileData:
    """
    A class for extracting and parsing data from a CSV file.

    Attributes:
        _file_data (list): contains the parsed data from the CSV file.

    Methods:
        _parse_row(row): parses a given string into a list
        get_data(): returns the file data
    """

    def __init__(self, file):
        """Reads file path, parses data and stores in object"""

        self._file_data = []

        if self.file_type(file) != "csv":
            raise Exception("File type is not csv")

        reader = open(file, 'r')
        for row in reader:
            parsed_data = self._parse_row(row)
            self._file_data.append(parsed_data)
        reader.close()

    def file_type(self, file_name):
        """Returns the file type of a given file"""

        file_split = file_name.split(".")
        return file_split[-1]  # Gets the extension after the last period

    def _parse_row(self, row):
        """Parses a single row from a string to a list format"""

        row_without_endline = row[:-1]
        split_row = row_without_endline.split(',')
        return split_row

    def get_data(self):
        """Get the file data that has been parsed"""

        return self._file_data
