from csv_file_data import CSVFileData
from air_data import AirData
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

            self.render_window()

        except FileNotFoundError:
            print(f"The file at location '{BRISTOL_FILE}' cannot be found.")
        except Exception:
            print(f"Something went wrong.")

    def render_window(self):
        """Instantiates the main GUI window"""
        self.root = tk.Tk()
        self.root.title("Python GUI")
        self.root.geometry("700x400")

        self.display_as_table(self.header,
                            self.three_window_data, self.root)

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

if __name__ == "__main__":
    main = Main()