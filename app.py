from csv_file_data import CSVFileData
from air_data import AirData

class Main:
    def __init__(self):
        """
        Initializes the object
        """
        BRISTOL_FILE = "./data/air_quality_data.csv"
        try:
            air_data_obj = CSVFileData(BRISTOL_FILE)
        except FileNotFoundError:
            print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        except Exception:
            print(f"Input file is not a csv file.")

        
if __name__ == "__main__":
    main = Main()