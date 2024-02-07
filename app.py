import tkinter as tk
from helper import *
from csv_file_data import CSVFileData
from air_data import AirData

class Main:
    def __init__(self):
        """
        Initialises the Main object.
        
        Creates a GUI.
        """
        BRISTOL_FILE = "./data/air_quality_data.csv"
        try:
            self.air_data_obj = AirData(BRISTOL_FILE)
        except FileNotFoundError:
            print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        except Exception:
            print(f"Input file is not a csv file.")

        self.start_application()

    def start_application(self):
        """Collects data needed to display in GUI and renders window"""
        NUM_OF_DP = 3 #Decimal Places

        self.title = self.air_data_obj.get_title()
        self.readings = self.air_data_obj.get_readings()
        self.avg_aqi_diff = calculate_average_aqi(self.readings[0],
                                                  self.readings[1])
        self.avg_aqi_diff = round(self.avg_aqi_diff, NUM_OF_DP)

        self.render_window()

    def render_window(self):
        """Instantiates the main GUI window"""
        self.root = tk.Tk()
        self.root.title("Python GUI")
        self.root.geometry("300x300")

        title_label = tk.Label(text = self.title,
                               font=('Helvetica bold', 20),
                               pady=20)
        title_label.pack()

        avg_diff_label = tk.Label(
            text=f"Mean AQI Difference: {self.avg_aqi_diff}",
            font=('Helvetica bold', 16),
            pady=8)
        avg_diff_label.pack()

        self.root.mainloop()

if __name__ == "__main__":
    main = Main()