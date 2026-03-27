# Importing Libraries
import tkinter as tk
from tkinter import ttk

"""

Green     : #003609
Red       : #3d0000

"""

class LazyDataCleaner():
    def __init__(self, root):
        # Importing Libraries
        from datetime import datetime

        # Get current time
        self.current_time = datetime.now().strftime("%H:%M:%S")
        # Main Root
        self.root = root

        # Create the main window
        self.root.title("Lazy Data Cleaner - PRERELEASE")

        # Window size
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
    
    def get_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
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
            text="v0.4.3-PRERELEASE",
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
        # Settings - Button - Bussinses
        self.settings_button_bussinses = tk.Button(
            self.mainframe,
            text="Bussinses",
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

    def main_screen(self):
        # Clear The Screen
        self.clear_frame()

        # Display
        self.run_button.grid(row=1, sticky="ew")
        self.version_label.grid(row=2, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.upload_file_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

    def preset_selection(self, value, text): 
        # Set New Preset
        self.preset = value

        # Add The New Text
        self.settings_label_output.config(text=text)

        # Update The Screen
        self.root.update()

    def customizable_selection(self, value_1):
        from colorama import Fore as F
        # Change Values
        if value_1 == 1:
            if self.mean == 0:
                self.mean = 1
                self.customize_button_mean.config(bg="#003609")
            elif self.mean == 1:
                self.mean = 0
                self.customize_button_mean.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 2:
            if self.median == 0:
                self.median = 1
                self.customize_button_median.config(bg="#003609")
            elif self.median == 1:
                self.median = 0
                self.customize_button_median.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 3:
            if self.mode == 0:
                self.mode = 1
                self.customize_button_mode.config(bg="#003609")
            elif self.mode == 1:
                self.mode = 0
                self.customize_button_mode.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 4:
            if self.duplicates == 0:
                self.duplicates = 1
                self.customize_button_duplicates.config(bg="#003609")
            elif self.duplicates == 1:
                self.duplicates = 0
                self.customize_button_duplicates.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 5:
            if self.outlier == 0:
                self.outlier = 1
                self.customize_button_outlier.config(bg="#003609")
            elif self.outlier == 1:
                self.outlier = 0
                self.customize_button_outlier.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 6:
            if self.standardizations == 0:
                self.standardizations = 1
                self.customize_button_standardization.config(bg="#003609")
            elif self.standardizations == 1:
                self.standardizations = 0
                self.customize_button_standardization.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")
        elif value_1 == 7:
            if self.force_csv == 0:
                self.force_csv = 1
                self.force_csv_button.config(bg="#003609")
            elif self.force_csv == 1:
                self.force_csv = 0
                self.force_csv_button.config(bg="#3d0000")
            else:
                print(F.RED + f"[{self.get_time()}] Error In Selection Changing To False")

        # Update The Screen
        self.root.update()

    def run(self):
        # Clear Frame
        self.clear_frame()

        # Progress Bar
        self.progress_start()

    def progress_start(self):
        # Importing Libraries
        import threading

        # Define Loading Frame
        self.clear_frame()
        self.loadingframe = tk.Frame(self.mainframe, bg="light grey")
        self.loadingframe.grid()

        # Define Progress Bar
        self.progress_var = tk.IntVar()
        self.progress = ttk.Progressbar(
            self.loadingframe,
            orient="horizontal",
            length=400,
            mode="determinate",
            maximum=100,
            variable=self.progress_var
        )
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

    def rerun(self):        
        # Clear Frame
        self.clear_frame()

        # Progress Bar
        self.progress_start()
    
    def exit_function(self):
        # Exit The Program
        self.root.destroy()
    
    def settings(self):
        # Clear Frame
        self.clear_frame()

        # Display
        self.settings_label_output.grid(row=1, column=0, sticky="ew")
        self.settings_button_defualt.grid(row=2, column=0, sticky="ew")
        self.settings_button_AI.grid(row=3, column=0, sticky="ew")
        self.settings_button_bussinses.grid(row=4, column=0, sticky="ew")
        self.settings_button_streaming.grid(row=5, column=0, sticky="ew")
        self.settings_button_custom.grid(row=6, column=0, sticky="ew")
        self.return_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.force_csv_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
        self.root.update()
    
    def returned(self):      
        # Show Main Screen
        self.main_screen()

    def returned_custom(self):
        # Show Settings Screen
        self.settings()

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

    def main_function(self, preset):
        # Importing Libraries
        from core.processing import process_files
        from colorama import Fore as F, init
        from pathlib import Path
        from core.presets import default, AI, bussinses, streaming
        from core.functions import fill_mean, fill_median, fill_mode, duplicate, outlier, standardization

        self.step    = 2
        self.current = 0

        if preset == 1:
            self.step += 1
        elif preset == 2:
            self.step += 1
        elif preset == 3:
            self.step += 1
        elif preset == 4:
            self.step += 1
        elif preset == 5:
            if self.mean == 1:
                self.step += 1
            if self.median == 1:
                self.step += 1
            if self.mode == 1:
                self.step += 1
            if self.duplicates == 1:
                self.step += 1
            if self.outlier == 1:
                self.step += 1
            if self.standardizations == 1:
                self.step += 1

        def step_done():
                self.current += 1
                progress = int((self.current / self.step) * 100)
                self.update_progress(progress)

        # Reset Colorama
        init(autoreset=True)

        # Processing files
        if self.force_csv == 0:
            success_process_csv, message_process_csv = process_files()
        if self.force_csv == 1:
            success_process_csv, message_process_csv = process_files(True)
        step_done()

        # Getting Paths
        base_directory = Path(__file__).resolve().parent.parent
        upload_directory = base_directory / "Data"
        data = []
        data.extend(upload_directory.glob("*.csv"))                 ## Add csv files to list
        data.extend(upload_directory.glob("*.xlsx"))                ## Add xlsx files to list
        data.extend(upload_directory.glob("*.xls"))                 ## Add xls files to list

        # If no errors
        if success_process_csv:

            # Preset Selected
            if preset == 1:
                default(data)
                step_done()
            elif preset == 2:
                AI(data)
                step_done()
            elif preset == 3:
                bussinses(data)
                step_done()
            elif preset == 4:
                streaming(data)
                step_done()
            elif preset == 5:
                if self.mean == 1:
                    fill_mean(True, 5, data)
                    step_done()
                if self.median == 1:
                    fill_median(True, 5, data)
                    step_done()
                if self.mode == 1:
                    fill_mode(True, 5, data)
                    step_done()
                if self.duplicates == 1:
                    duplicate(data)
                    step_done()
                if self.outlier == 1:
                    outlier(data)
                    step_done()
                if self.standardizations == 1:
                    standardization(data)
                    step_done()
                
            else:
                self.get_time()
                print(F.RED + f"[{self.get_time()}] Error In Presets Selection... Switching to Defualt")
                default(data)
                self.step = 1
                step_done()

        else: 
            # Print Current Time & The Errror Message 
            self.get_time()
            print(F.RED + f"[{self.get_time()}] {message_process_csv}")
            self.step = 1
            step_done()

        # Display End Screen
        self.root.after(0, self.end_screen)

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

    def update_progress(self, value):
        self.root.after(0, self.progress_var.set, value)