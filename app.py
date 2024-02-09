from csv_file_data import CSVFileData
from air_data import AirData
from matplotlib.figure import Figure
import tkinter as tk


class Main:
    def __init__(self):
        """
        Initialises the Main object.
        
        Creates a GUI.
        """
        BRISTOL_FILE = "./data/air_quality_data.csv"
        try:
            air_data_obj = AirData(BRISTOL_FILE)

            self.timescale = air_data_obj.get_timescale()
            self.readings = air_data_obj.get_readings()
            self.locations = air_data_obj.get_location_names()

            self.render_window()

        except FileNotFoundError:
            print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        except Exception:
            print(f"Input file is not a csv file.")

    def render_window(self):
        """Instantiates the main GUI window"""
        self.root = tk.Tk()
        self.root.title("Python GUI")
        self.root.geometry("300x300")

        self.plot_graph()

        self.root.mainloop()

    def plot_graph(self):
        """Plot air quality data on line grpah and embed into GUI"""

        # Setup the graph, stated in matplotlib documentation
        fig = Figure(figsize=(8, 6),
                     dpi=80)
        graph = fig.add_subplot(111)

        # Separate the data filtered along with timescale
        loc1_data = [self.timescale, self.readings[0]]
        loc2_data = [self.timescale, self.readings[1]]

        x1, y1 = self.filter_graph_data(loc1_data)
        x1, y1 = self.filter_graph_data(loc1_data)

    def filter_graph_data(self, reading_data):
        """Disregards the row if it contains an non-float value"""
        filtered_times = []
        filtered_readings = []
        for i, val in enumerate(reading_data[0]):
            if isinstance(reading_data[1][i], float):
                filtered_times.append(val)
                filtered_readings.append(reading_data[1][i])

        return [filtered_times, filtered_readings]


if __name__ == "__main__":
    main = Main()