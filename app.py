from csv_file_data import CSVFileData
from air_data import AirData
import tkinter as tk
from helper import *

class Main:
    def __init__(self):
        """
        Initialises the Main object.
        
        Creates a GUI.
        """
        BRISTOL_FILE = "./data/air_quality_data.csv"
        # try:
        #     air_data_obj = AirData(BRISTOL_FILE)

        #     self.locations = air_data_obj.get_location_names()

        #     data = air_data_obj.get_data()
        #     data = separate_data(data)
        #     three_window_data1 = highest_three_point_sd(data[0])
        #     three_window_data2 = highest_three_point_sd(data[1])
            
        #     sd_data1 = population_sd(
        #         get_three_point_window_data(three_window_data1))
        #     sd_data2 = population_sd(
        #         get_three_point_window_data(three_window_data2))
            
        #     print("3")

        #     self.header = ['Date', 'Time']

        #     if sd_data1 > sd_data2:
        #         self.header.append(self.locations[0])
        #         self.three_window_data = three_window_data1
        #     else:
        #         self.header.append(self.locations[1])
        #         self.three_window_data = three_window_data2

        #     self.render_window()
        # except FileNotFoundError:
        #     print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        # except Exception:
        #     print(f"Something went wrong.")

        air_data_obj = AirData(BRISTOL_FILE)

        self.locations = air_data_obj.get_location_names()

        data = air_data_obj.get_data()
        print(data)
        data = separate_data(data)
        three_window_data1 = highest_three_point_sd(data[0])
        three_window_data2 = highest_three_point_sd(data[1])

        sd_data1 = population_sd(
            get_three_point_window_data(three_window_data1))
        sd_data2 = population_sd(
            get_three_point_window_data(three_window_data2))
        
        print("3")

        self.header = ['Date', 'Time']

        if sd_data1 > sd_data2:
            self.header.append(self.locations[0])
            self.three_window_data = three_window_data1
        else:
            self.header.append(self.locations[1])
            self.three_window_data = three_window_data2

        self.render_window()

    def render_window(self):
        """Instantiates the main GUI window"""
        self.root = tk.Tk()
        self.root.title("Python GUI")
        self.root.geometry("300x300")

        title_label = tk.Label(text = "Python GUI")
        title_label.pack()

        self.root.mainloop()

if __name__ == "__main__":
    main = Main()