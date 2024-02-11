import tkinter as tk
from helper import *
from csv_file_data import CSVFileData
from air_data import AirData
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from helper import *


class Main:
    def __init__(self):
        """
        Initialises the Main object.
        
        Creates a GUI.
        """
        BRISTOL_FILE = "./data/air_quality_data.csv"
        try:
            air_data_obj = AirData(BRISTOL_FILE)

            self.locations = air_data_obj.get_location_names()
            self.timescale = self.air_data_obj.get_timescale()
            self.readings = self.air_data_obj.get_readings()

            data = air_data_obj.get_data()
            data = separate_data(data)
            three_window_data1 = highest_three_point_sd(data[0])
            three_window_data2 = highest_three_point_sd(data[1])

            sd_data1 = population_sd(
                get_three_point_window_data(three_window_data1))
            sd_data2 = population_sd(
                get_three_point_window_data(three_window_data2))

            self.header = ['Date', 'Time']

            if sd_data1 > sd_data2:
                self.header.append(self.locations[0])
                self.three_window_data = three_window_data1
            else:
                self.header.append(self.locations[1])
                self.three_window_data = three_window_data2

        except FileNotFoundError:
            print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        except Exception:
            print(f"Something went wrong.")

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
        self.root.geometry("8000x600")

        self.display_as_table(self.header,
                            self.three_window_data, self.root)
    
        title_label = tk.Label(text = self.title,
                               font=('Helvetica bold', 20),
                               pady=20)
        title_label.pack()
        
        self.plot_graph()

        avg_diff_label = tk.Label(
            text=f"Mean AQI Difference: {self.avg_aqi_diff}",
            font=('Helvetica bold', 16),
            pady=8)
        avg_diff_label.pack()

        self.root.mainloop()

    def display_as_table(self, headers, entries, window):
        """Displays data in a table format using Treeview (tkinker)"""

        if entries is None:
            return

        # Constants used for table styling
        COL_WIDTH = 175
        ANCHOR_POS = 'center'
        ROW_HEIGHT = 25

        # Styling for table
        table = ttk.Treeview(window, columns=headers, show='headings')
        table.heading(headers[0], text=headers[0])
        table.heading(headers[1], text=headers[1])
        table.heading(headers[2], text=headers[2])
        table.column(headers[0], width=COL_WIDTH, anchor=ANCHOR_POS)
        table.column(headers[1], width=COL_WIDTH, anchor=ANCHOR_POS)
        table.column(headers[2], width=COL_WIDTH, anchor=ANCHOR_POS)
        ttk.Style().configure('Treeview', rowheight=ROW_HEIGHT)
        ttk.Style().configure('Treeview.Heading', font=('Helvetica bold', 14))
        
        table['height'] = len(entries)

        for row in entries:
            table.insert('', index='end', values=row)
        table.pack()

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
        x2, y2 = self.filter_graph_data(loc2_data)

        graph.plot(x2, y2, label=self.locations[1])
        graph.plot(x1, y1, label=self.locations[0])

        # Adjust visual configs for graph
        graph.set_xticks([x1[i] for i in range(0, len(x1), 
                                               round(len(x1) / 8))])
        graph.legend(loc="upper center")
        graph.set_ylabel("Air Quality (ppb)")
        graph.set_xlabel("Time")

        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()
        canvas.get_tk_widget().pack()

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