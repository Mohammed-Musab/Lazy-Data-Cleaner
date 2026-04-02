# Importing Libraries
import tkinter as tk
from tkinter import ttk
from colorama import Fore as F, init
from pathlib import Path

"""

Green     : #003609
Red       : #3d0000

"""

# Lazy Data Cleaner Class
class LazyDataCleaner():

    # Init Function
    def __init__(self, root):

        # Importing Libraries
        from datetime import datetime

        # Get current time
        self.current_time = datetime.now().strftime("%H:%M:%S")
        
        # Main Root
        self.root = root

        # Create the main window
        self.root.title("Lazy Data Cleaner - PRERELEASE")

        # Window size and properties
        self.root.geometry("920x500")
        self.root.resizable(False, False)
        self.root.configure(bg="light grey")

        # Main frame - center
        self.mainframe = tk.Frame(root)
        self.mainframe.place(relx=0.5, rely=0.5, anchor="center")

        # Preset (defualt)
        self.preset = 1

        # Defualts Values for Customize
        self.mean                       = 0
        self.median                     = 0
        self.mode                       = 0
        self.duplicates                 = 0
        self.outlier                    = 0
        self.standardizations           = 0
        self.force_csv                  = 0

        # Create all widgets
        self.create_widgets()

        # Main Screen
        self.main_screen()
    
    # Get Time Function
    def get_time(self):

        # Get the Current Time
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
    # Create Widgets
    def create_widgets(self):

        # Defualt Values For Buttons & Labels Size
        button_width            = 40
        button_height           = 2
        button_settings_width   = 10
        button_settings_height  = 2
        button_customize_width  = 30
        button_customize_height = 2
    
        # Label - Output
        self.output_label = tk.Label(
            self.mainframe,
            text="Process Finished!",
            font=("Arial", 15, "bold"),
            bg="#2c3e50",
            fg="white",
            wraplength=160,
            width=40,
            height=6,
            bd=0
        )

        # Label - Version
        self.version_label = tk.Label(
            self.mainframe,
            text="v0.4.4",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white",
            width=20,
            height=2,
            bd=0
        )

        # Button - Run
        self.run_button = tk.Button(
            self.mainframe,
            text=" RUN ",
            font=("Arial", 20, "bold"),
            bg="#2ecc71",
            fg="white",
            width=20,
            height=2,
            command=self.run,
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Button - Restart
        self.restart_button = tk.Button(
            self.mainframe,
            text="Restart the Program",
            font=("Arial", 15, "bold"),
            bg="#3498db",
            fg="white",
            width=button_width,
            height=button_height,
            command=self.rerun,
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Button - Exit
        self.exit_button = tk.Button(
            self.mainframe,
            text=" Leave the Program ",
            font=("Arial", 15, "bold"),
            bg="#e74c3c",
            fg="white",
            width=button_width,
            height=button_height,
            command=self.exit_function,
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Button - Settings
        self.settings_button = tk.Button(
            self.root,
            text="Settings",
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=self.settings
        )

        # Button - Return
        self.return_button = tk.Button(
            self.root,
            text="Return",
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=self.returned
        )

        # Settings - Label - Output
        self.settings_label_output = tk.Label(
            self.mainframe,
            text="Default Settings Have Been Selected",
            font=("Arial", 15, "bold"),
            bg="#2c3e50",
            fg="white",
            wraplength=160,
            width=40,
            height=6,
            bd=0
        )

        # Settings - Button - Defualt
        self.settings_button_defualt = tk.Button(
            self.mainframe,
            text=" Defualt ",
            font=("Arial", 15, "bold"),
            bg="#005a8f",
            fg="white",
            width=button_settings_width,
            height=button_settings_height,
            command=lambda: self.preset_selection(1, "Default Settings Have Been Selected"),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Settings - Button - AI
        self.settings_button_AI = tk.Button(
            self.mainframe,
            text="   AI    ",
            font=("Arial", 15, "bold"),
            bg="#005a8f",
            fg="white",
            width=button_settings_width,
            height=button_settings_height,
            command=lambda: self.preset_selection(2, "AI Settings Have Been Selected"),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Settings - Button - Business
        self.settings_button_business = tk.Button(
            self.mainframe,
            text="Business",
            font=("Arial", 15, "bold"),
            bg="#005a8f",
            fg="white",
            width=button_settings_width,
            height=button_settings_height,
            command=lambda: self.preset_selection(3, "Business Settings Have Been Selected"),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Settings - Button - Streaming
        self.settings_button_streaming = tk.Button(
            self.mainframe,
            text="Streaming",
            font=("Arial", 15, "bold"),
            bg="#005a8f",
            fg="white",
            width=button_settings_width,
            height=button_settings_height,
            command=lambda: self.preset_selection(4, "Streaming Settings Have Been Selected"),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Settings - Button - Custom
        self.settings_button_custom = tk.Button(
            self.mainframe,
            text="Customize",
            font=("Arial", 15, "bold"),
            bg="#005a8f",
            fg="white",
            width=button_settings_width,
            height=button_settings_height,
            command=self.customize,
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Mean
        self.customize_button_mean = tk.Button(
            self.mainframe,
            text="Fill in using the Mean",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(1),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Median
        self.customize_button_median = tk.Button(
            self.mainframe,
            text="Fill in using the Median",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(2),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Mode
        self.customize_button_mode = tk.Button(
            self.mainframe,
            text="Fill in using the Mode",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(3),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Duplicates
        self.customize_button_duplicates = tk.Button(
            self.mainframe,
            text="Remove Duplicates",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(4),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Outlier
        self.customize_button_outlier = tk.Button(
            self.mainframe,
            text="Remove Outlier",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(5),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Standardization
        self.customize_button_standardization = tk.Button(
            self.mainframe,
            text="Apply Standardization",
            font=("Arial", 15, "bold"),
            bg="#3d0000",
            fg="white",
            width=button_customize_width,
            height=button_customize_height,
            command=lambda: self.customizable_selection(6),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        # Customize - Button - Returned
        self.return_customize_button = tk.Button(
            self.root,
            text="Return",
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=self.returned_custom
        )
        
        # Force save as csv
        self.force_csv_button = tk.Button(
                    self.root,
                    text="Force csv save as files",
                    font=("Arial", 10, "bold"),
                    bg="#3d0000",
                    fg="white",
                    bd=0,
                    highlightthickness=0,
                    relief="flat",
                    command=lambda: self.customizable_selection(7)
        )

        # Upload File - Button
        from UI.upload_file import upload_file
        self.upload_file_button = tk.Button(
            self.root,
            text="Upload File",
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=upload_file
        )

    # Clear Frame
    def clear_frame(self):

        # Remove everything in screen
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

        # Remove placed buttons
        self.upload_file_button.place_forget()
        self.settings_button.place_forget()
        self.return_button.place_forget()
        self.return_customize_button.place_forget()
        self.force_csv_button.place_forget()

        # Restore background
        self.mainframe.configure(bg="light grey")

    # Main Screen
    def main_screen(self):

        # Clear The Screen
        self.clear_frame()

        # Display
        self.run_button.grid(row=1, sticky="ew")
        self.version_label.grid(row=2, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.upload_file_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

    # Preset Selection
    def preset_selection(self, value, text): 

        # Set New Preset
        self.preset = value

        # Add The New Text
        self.settings_label_output.config(text=text)

        # Update The Screen
        self.root.update()

    # Customizable Selection
    def customizable_selection(self, value_1):

        # Importing Libraries
        from colorama import Fore as F

        # Toggle Map
        toggle_map = {
        1: ("mean", self.customize_button_mean),
        2: ("median", self.customize_button_median),
        3: ("mode", self.customize_button_mode),
        4: ("duplicates", self.customize_button_duplicates),
        5: ("outlier", self.customize_button_outlier),
        6: ("standardizations", self.customize_button_standardization),
        7: ("force_csv", self.force_csv_button),
        }

        # Check if the value is in the toggle map
        if value_1 not in toggle_map:
            print(F.RED + f"[{self.get_time()}] Error: Invalid selection {value_1}")
            return

        # Get the attribute name and button from the toggle map
        attribute_name, button = toggle_map[value_1]

        # Get current value
        current_value = getattr(self, attribute_name)
    
        # Toggle the value
        if current_value in [0, 1]:

            # Toggle the value and update the button color
            new_value = 1 - current_value
            setattr(self, attribute_name, new_value)
            button.config(bg="#003609" if new_value == 1 else "#3d0000")
        
        # If the current value is not 0 or 1, print an error message
        else:
            print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")

        # Update The Screen
        self.root.update()

    # Run Function
    def run(self):

        # Clear Frame
        self.clear_frame()

        # Progress Bar
        self.progress_start()

    # Progress Bar
    def progress_start(self):

        # Importing Libraries
        import threading

        # Define Loading Frame
        self.clear_frame()
        self.loadingframe = tk.Frame(self.mainframe, bg="light grey")
        self.loadingframe.grid()

        # Progress Bar
        self.progress_var = tk.IntVar()
        self.progress = ttk.Progressbar(
            self.loadingframe,
            orient="horizontal",
            length=400,
            mode="determinate",
            maximum=100,
            variable=self.progress_var
        )

        # Loading Label
        self.loading_label = tk.Label(
        self.loadingframe,
        text="Processing...",
        font=("Arial", 20, "bold"),
        bg="light grey"
        )

        # Display 
        self.loading_label.grid(row=0, pady=20)
        self.progress.grid(row=1, pady=10)

        # Main Function
        thread = threading.Thread(target=self.main_function, args=(self.preset,), daemon=True)
        thread.start()

    # Rerun Function
    def rerun(self):   

        # Clear Frame
        self.clear_frame()

        # Progress Bar
        self.progress_start()
    
    # Exit Function
    def exit_function(self):

        # Exit The Program
        self.root.destroy()
    
    # Settings Function
    def settings(self):

        # Clear Frame
        self.clear_frame()

        # Display
        self.settings_label_output.grid(row=1, column=0, sticky="ew")
        self.settings_button_defualt.grid(row=2, column=0, sticky="ew")
        self.settings_button_AI.grid(row=3, column=0, sticky="ew")
        self.settings_button_business.grid(row=4, column=0, sticky="ew")
        self.settings_button_streaming.grid(row=5, column=0, sticky="ew")
        self.settings_button_custom.grid(row=6, column=0, sticky="ew")
        self.return_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.force_csv_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
        self.root.update()
    
    # Returned Functions
    def returned(self):  

        # Show Main Screen
        self.main_screen()

    # Returned Custom Function
    def returned_custom(self):

        # Show Settings Screen
        self.settings()

    # Customize Function
    def customize(self):

        # Set The Preset To Custom
        self.preset_selection(5, "Custom Settings Have Been Selected")
        
        # Clear Frame
        self.clear_frame()

        # Display
        self.customize_button_mean.grid(row=1, column=0, sticky="ew")
        self.customize_button_median.grid(row=2, column=0, sticky="ew")
        self.customize_button_mode.grid(row=3, column=0, sticky="ew")
        self.customize_button_duplicates.grid(row=4, column=0, sticky="ew")
        self.customize_button_outlier.grid(row=5, column=0, sticky="ew")
        self.customize_button_standardization.grid(row=6, column=0, sticky="ew")
        self.return_customize_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.root.update()

    # Main Function
    def main_function(self, preset):

        # Importing Libraries
        from core.processing import process_files
        from core.presets import default, AI, business, streaming
        from core.functions import fill_mean, fill_median, fill_mode, duplicate, outlier, standardization

        # Initialize step and current for progress tracking
        self.step    = 1
        self.current = 0

        # Preset Selected
        if preset in [1, 2, 3, 4]:
            self.step += 1

        # If Custom Preset Selected, Calculate The Number Of Selected Options
        elif preset == 5:
            self.step += sum([
                self.mean,
                self.median,
                self.mode,
                self.duplicates,
                self.outlier,
                self.standardizations
            ])

        # Step Done Function To Update Progress Bar
        def step_done():
                self.current += 1
                progress = int((self.current / self.step) * 100)
                self.update_progress(progress)

        # Reset Colorama
        init(autoreset=True)

        # Processing files
        success_process_csv, message_process_csv = process_files(bool(self.force_csv))
        step_done()

        # Getting Paths
        base_directory = Path(__file__).resolve().parents[1]        ## Parent Folder Directory
        upload_directory = base_directory / "Data"
        data = []
        data.extend(upload_directory.glob("*.csv"))                 ## Add csv files to list
        data.extend(upload_directory.glob("*.xlsx"))                ## Add xlsx files to list
        data.extend(upload_directory.glob("*.xls"))                 ## Add xls files to list

        # If no errors
        if success_process_csv:

            # Preset Functions Map
            preset_funcions = {
                1: default,
                2: AI,
                3: business,
                4: streaming
            }

            # If the preset is in the preset functions map, call the corresponding function and update progress
            if preset in preset_funcions:
                preset_funcions[preset](data)
                step_done()
            
            # If the preset is custom, call the selected functions and update progress for each function
            elif preset == 5:
                custom_functions = {
                    "mean": (self.mean, lambda: fill_mean(True, 5, data)),
                    "median": (self.median, lambda: fill_median(True, 5, data)),
                    "mode": (self.mode, lambda: fill_mode(True, 5, data)),
                    "duplicates": (self.duplicates, lambda: duplicate(data)),
                    "outlier": (self.outlier, lambda: outlier(data)),
                    "standardizations": (self.standardizations, lambda: standardization(data))
                    }

                # Loop through each selected option and call the corresponding function
                for option, function in custom_functions:
                    if option == 1:
                        function()
                        step_done()
                
            # If the preset value is invalid, print an error message and switch to default preset
            else:
                self.get_time()
                print(F.RED + f"[{self.get_time()}] Error In Presets Selection... Switching to Defualt")
                default(data)
                self.step = 1
                step_done()

        # If there is an error in processing files, print the error message
        else: 

            # Print Current Time & The Errror Message 
            self.get_time()
            print(F.RED + f"[{self.get_time()}] {message_process_csv}")
            self.step = 1
            step_done()

        # Display End Screen
        self.root.after(0, self.end_screen)

    # End Screen
    def end_screen(self):

        # Clear Frame
        self.clear_frame()

        # Display
        self.output_label.grid(row=1, sticky="ew")
        self.restart_button.grid(row=2, sticky="ew")
        self.exit_button.grid(row=3, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.output_label.config(text="The Program Finish Sucessfully!", fg="green")

        # Update The Screen
        self.root.update()

    # Update Progress
    def update_progress(self, value):

        # Update the progress bar value
        self.root.after(0, self.progress_var.set, value)