from csv_file_data import CSVFileData
from air_data import AirData
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

        title_label = tk.Label(text = "Python GUI")
        title_label.pack()

        self.root.mainloop()

if __name__ == "__main__":
    main = Main()