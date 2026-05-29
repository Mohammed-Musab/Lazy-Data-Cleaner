# Importing Libraries
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from time import sleep as s
from tkinter import scrolledtext
from core.log import save_to_log
from config.config import config_save, config_load

# Waiting Time For Progress Bar
waiting_time = 0.2

# Version Name
version = "v0.4.7"

# Lazy Data Cleaner Class
class LazyDataCleaner():

    # Get Current Settings
    def get_current_settings(self):
        return {
            "preset": self.preset,
            "mean": self.mean,
            "median": self.median,
            "mode": self.mode,
            "duplicates": self.duplicates,
            "outlier": self.outlier,
            "standardizations": self.standardizations,
            "force_csv": self.force_csv,
            "missing_threshold": self.missing_threshold,
            "outlier_threshold": self.outlier_threshold,
            "theme": self.current_theme,
        }

    # Apply Settings
    def apply_settings(self, settings):

        # Update settings with loaded values, using current values as defaults
        self.preset = settings.get("preset", self.preset)
        self.mean = settings.get("mean", self.mean)
        self.median = settings.get("median", self.median)
        self.mode = settings.get("mode", self.mode)
        self.duplicates = settings.get("duplicates", self.duplicates)
        self.outlier = settings.get("outlier", self.outlier)
        self.standardizations = settings.get("standardizations", self.standardizations)
        self.force_csv = settings.get("force_csv", self.force_csv)
        self.missing_threshold = settings.get("missing_threshold", self.missing_threshold)
        self.outlier_threshold = settings.get("outlier_threshold", self.outlier_threshold)

        # Apply Theme
        theme = settings.get("theme", self.current_theme)
        if self.current_theme != theme:
            self.current_theme = theme
            self.theme_button.config(text="Dark" if theme == "light" else "Light")
            self.apply_theme()

        # Update Sliders
        self.threshold_slider.set(self.missing_threshold)
        self.outlier_threshold_var.set(int(self.outlier_threshold))
        
        # Update Toggle Buttons
        toggle_pairs = [
            (self.mean,               self.customize_button_mean),
            (self.median,             self.customize_button_median),
            (self.mode,              self.customize_button_mode),
            (self.duplicates,         self.customize_button_duplicates),
            (self.outlier,            self.customize_button_outlier),
            (self.standardizations,    self.customize_button_standardization),
            (self.force_csv,          self.force_csv_button),
        ]

        # Update Toggle Buttons Colors
        for value, button in toggle_pairs:
            button.config(bg=self.theme("green") if value else self.theme("red"))

        # Update Preset Text
        preset_texts = {
            1: "Default Settings Have Been Selected",
            2: "AI Settings Have Been Selected",
            3: "Business Settings Have Been Selected",
            4: "Streaming Settings Have Been Selected",
            5: "Custom Settings Have Been Selected",
        }
        self.settings_label_output.config(text=preset_texts.get(self.preset, ""))
        self.root.update()

    # Save Current Settings
    def save_current_settings(self):
        settings = self.get_current_settings()
        config_save(settings)

    # Load Saved Settings
    def load_saved_settings(self):
        settings = config_load()
        if settings:
            self.apply_settings(settings)

    # Init Function
    def __init__(self, root):

        # Initialize log viewer state
        self.last_log_size = 0

        # Importing Libraries
        from datetime import datetime

        # Log Refresh
        save_to_log("g", "Running log...")

        # Get current time
        self.current_time = datetime.now().strftime("%H:%M:%S")
        
        # Main Root
        self.root = root

        # Current Theme
        self.current_theme = "light"

        # Create the main window
        self.root.title(f"Lazy Data Cleaner")

        # Window size and properties
        self.root.geometry("920x500")
        self.root.resizable(False, False)
        self.root.configure(bg=self.theme("bg"))

        # Main frame - center
        self.mainframe = tk.Frame(root)
        self.mainframe.place(relx=0.5, rely=0.5, anchor="center")

        # Remove the old keyboard_input call and set up Tkinter bindings
        self.setup_bindings()

        # Log viewer state
        self.log_viewer_window = None
        self.log_update_job = None

        # Preset (default)
        self.preset = 1

        # Default Values for Customize
        self.mean                       = 0
        self.median                     = 0
        self.mode                       = 0
        self.duplicates                 = 0
        self.outlier                    = 0
        self.standardizations           = 0
        self.force_csv                  = 0

        # Threshold Values
        self.missing_threshold = 2.5
        self.outlier_threshold = 3

        self.theme_button = tk.Button(
            self.root,
            text="Dark" if self.current_theme == "light" else "Light",
            font=("Arial", 10, "bold"),
            bg=self.theme("gray"),
            fg=self.theme("text"),
            bd=0,
            command=self.toggle_theme
        )
        self.theme_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        # Create all widgets
        self.create_widgets()

        # Load saved settings
        self.load_saved_settings()

        # Main Screen
        self.main_screen()

    # Theme function 
    def theme(self, color):
        
        # Define color codes for light
        if self.current_theme == "light":

            colors = {
                "red"           : "#E74C3C",
                "green"         : "#2ECC71",
                "blue"          : "#005A8F",
                "gray"          : "#34495E",
                "darker gray"   : "#2C3E50",
                "white"         : "#F9FAFB",
                "bg"            : "light grey",
                "text"          : "#FFFFFF"
            }

        # Define color codes for dark
        else:
            
            colors = {
                "red"           : "#EF4444",
                "green"         : "#22C55E",
                "blue"          : "#3B82F6",
                "gray"          : "#475569",
                "darker gray"   : "#1E293B",
                "white"         : "#FFFFFF",
                "bg"            : "#0F172A",
                "text"          : "#DDDDDD"
            }   
        
        if color in colors:
            return colors.get(color)
        
        else:
            # Log the invalid color request and return a default color (magenta) to indicate an error
            save_to_log("r", f"Invalid color '{color}' requested in theme function.")
            return "#FF00FF"  # Return magenta for invalid color requests
        

    # Apply Theme
    def apply_theme(self):
        
        # Update background colors
        self.root.configure(bg=self.theme("bg"))
        self.mainframe.configure(bg=self.theme("bg"))

        # List of widgets to update with their corresponding background and foreground color keys
        widgets = [
            (self.theme_button, "gray", "text"),
            (self.output_label, "gray", "text"),
            (self.version_label, "gray", "text"),
            (self.run_button, "green", "text"),
            (self.restart_button, "blue", "text"),
            (self.exit_button, "red", "text"),
            (self.settings_button, "gray", "text"),
            (self.return_button, "gray", "text"),
            (self.settings_label_output, "gray", "text"),
            (self.settings_button_default, "blue", "text"),
            (self.settings_button_AI, "blue", "text"),
            (self.settings_button_business, "blue", "text"),
            (self.settings_button_streaming, "blue", "text"),
            (self.settings_button_custom, "blue", "text"),
            (self.customize_button_mean, "red", "text"),
            (self.customize_button_median, "red", "text"),
            (self.customize_button_mode, "red", "text"),
            (self.customize_button_duplicates, "red", "text"),
            (self.customize_button_outlier, "red", "text"),
            (self.customize_button_standardization, "red", "text"),
            (self.return_customize_button, "gray", "text"),
            (self.force_csv_button, "red", "text"),
            (self.upload_file_button, "gray", "text"),
        ]

        # Update each widget's colors if it exists
        for widget, bg_key, fg_key in widgets:
            if widget and widget.winfo_exists():
                widget.configure(bg=self.theme(bg_key), fg=self.theme(fg_key))

        # Update sliders
        for slider in [self.threshold_slider, self.outlier_threshold_slider]:
            if slider and slider.winfo_exists():
                slider.configure(
                    bg=self.theme("darker gray"),
                    fg=self.theme("text"),
                    troughcolor=self.theme("darker gray")
                )

        # Update loading label if it exists
        if hasattr(self, 'loading_label') and self.loading_label.winfo_exists():
            self.loading_label.configure(bg=self.theme("bg"), fg=self.theme("text"))
        if hasattr(self, 'loadingframe') and self.loadingframe.winfo_exists():
            self.loadingframe.configure(bg=self.theme("bg"))
        if hasattr(self, 'text_frame') and self.text_frame.winfo_exists():
            self.text_frame.configure(bg=self.theme("bg"))
        if hasattr(self, 'log_viewer_window') and self.log_viewer_window and self.log_viewer_window.winfo_exists():
            self.log_viewer_window.configure(bg=self.theme("bg"))
        if hasattr(self, 'log_text') and self.log_text.winfo_exists():
            self.log_text.configure(
                bg=self.theme("darker gray"),
                fg=self.theme("text"),
                insertbackground=self.theme("text"),
            )

        self.root.update()

    # Toggle Theme
    def toggle_theme(self):
        
        # Toggle the theme between light and dark
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.theme_button.config(text="Dark" if self.current_theme == "light" else "Light")
        
        # Apply the new theme to all widgets
        self.apply_theme()
    
    # Create Widgets
    def create_widgets(self):

        # Default Values For Buttons & Labels Size
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
            wraplength=160,
            width=40,
            height=6,
            bd=0
        )

        # Label - Version
        self.version_label = tk.Label(
            self.mainframe,
            text=version,
            font=("Arial", 20, "bold"),
            bg=self.theme("gray"),
            fg=self.theme("text"),
            width=20,
            height=2,
            bd=0
        )

        # Button - Run
        self.run_button = tk.Button(
            self.mainframe,
            text=" RUN ",
            font=("Arial", 20, "bold"),
            bg=self.theme("green"),
            fg=self.theme("text"),
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
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg=self.theme("red"),
            fg=self.theme("text"),
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
            wraplength=160,
            width=40,
            height=6,
            bd=0
        )

        # Settings - Button - Default
        self.settings_button_default = tk.Button(
            self.mainframe,
            text=" Default ",
            font=("Arial", 15, "bold"),
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg=self.theme("blue"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg= self.theme("red"),
            fg=self.theme("text"),
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
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
            bg=self.theme("red"),
            fg=self.theme("text"),
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
            bg=self.theme("gray"),
            fg=self.theme("text"),
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=upload_file
        )

        # Slider - Preset Selection - Threshold
        self.threshold_slider = tk.Scale(
            self.mainframe,
            from_=0,
            to=100,
            orient="horizontal",
            resolution=0.1,
            label="Missing Threshold (%)",
            length=300,
            bg=self.theme("darker gray"),
            fg=self.theme("text"),
            troughcolor=self.theme("darker gray"),
            activebackground=self.theme("blue"),
            highlightthickness=0,
            bd=0
        )

        # Bar - Preset Selection - Outlier Threshold
        self.outlier_threshold_var = tk.IntVar()
        self.outlier_threshold_slider = tk.Scale(
            self.mainframe,
            from_=1,
            to=10,
            orient="horizontal",
            resolution=1,
            label="Outlier Threshold",
            length=300,
            variable=self.outlier_threshold_var,
            digits=0,
            bg=self.theme("darker gray"),
            fg=self.theme("text"),
            troughcolor=self.theme("darker gray"),
            activebackground=self.theme("blue"),
            highlightthickness=0,
            bd=0
        )
        
        self.threshold_slider.set(self.missing_threshold)
        self.outlier_threshold_var.set(self.outlier_threshold)

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
        self.mainframe.configure(bg=self.theme("bg"))

        # Check colors
        self.apply_theme()

    # Main Screen
    def main_screen(self):

        # Clear The Screen
        self.clear_frame()

        # Display
        self.run_button.grid(row=1, sticky="ew")
        self.version_label.grid(row=2, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.upload_file_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
        self.apply_theme()

    # Preset Selection
    def preset_selection(self, value, text): 

        # Set New Preset
        self.preset = value

        # Add The New Text
        self.settings_label_output.config(text=text)

        # Save current settings
        self.save_current_settings()

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
            save_to_log("r", f"Error: Invalid selection {value_1}")
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
            button.config(bg=self.theme("green") if new_value == 1 else self.theme("red"))
        
        # If the value is not 0 or 1, log an error message
        else:
            save_to_log("r", f"Error: Invalid selection {value_1}")

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
        self.loadingframe = tk.Frame(self.mainframe, bg=self.theme("bg"))
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
            bg=self.theme("bg"),
            fg=self.theme("text")
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

        # Save Current Settings
        self.save_current_settings()

        # Exit The Program
        self.root.destroy()
    
    # Settings Function
    def settings(self):

        # Clear Frame
        self.clear_frame()

        # Display
        self.settings_label_output.grid(row=1, column=0, sticky="ew")
        self.settings_button_default.grid(row=2, column=0, sticky="ew")
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
        self.threshold_slider.grid(row=1, column=0, sticky="ew")
        self.outlier_threshold_slider.grid(row=2, column=0, sticky="ew", pady=10)
        self.customize_button_mean.grid(row=3, column=0, sticky="ew")
        self.customize_button_median.grid(row=4, column=0, sticky="ew")
        self.customize_button_mode.grid(row=5, column=0, sticky="ew")
        self.customize_button_duplicates.grid(row=6, column=0, sticky="ew")
        self.customize_button_outlier.grid(row=7, column=0, sticky="ew")
        self.customize_button_standardization.grid(row=8, column=0, sticky="ew")
        self.return_customize_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        self.root.update()

    # Main Function
    def main_function(self, preset):

        # Importing Libraries
        from core.processing import process_files
        from core.presets import default, AI, business, streaming
        from core.functions import fill_mean, fill_median, fill_mode, duplicate, outlier, standardization

        # Get Threshold Values
        self.missing_threshold = self.threshold_slider.get()
        self.outlier_threshold = self.outlier_threshold_var.get()

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
        def step_done(information=""):
                self.current += 1
                self.loading_label.config(text=f"{information}... ({self.current}/{self.step})")
                progress = int((self.current / self.step) * 100)
                self.update_progress(progress)
                self.root.update()
                s(waiting_time)

        # Processing files
        success_process_csv, message_process_csv = process_files(bool(self.force_csv))
        step_done("File Formatting")

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

            preset_labels = {
                1: "Default Cleaning Preset",
                2: "AI Cleaning Preset",
                3: "Business Cleaning Preset",
                4: "Streaming Cleaning Preset"
            }


            # If the preset is in the preset functions map, call the corresponding function and update progress
            if preset in preset_funcions:
                for preset_label in preset_labels:
                    if preset == preset_label:
                        step_done(preset_labels[preset_label])
                preset_funcions[preset](data)
                
            
            # If the preset is custom, call the selected functions and update progress for each function
            elif preset == 5:
                custom_functions = {
                    "mean": (self.mean, lambda: fill_mean(True, self.missing_threshold, data)),
                    "median": (self.median, lambda: fill_median(True, self.missing_threshold, data)),
                    "mode": (self.mode, lambda: fill_mode(True, self.missing_threshold, data)),
                    "duplicates": (self.duplicates, lambda: duplicate(data)),
                    "outlier": (self.outlier, lambda: outlier(data, self.outlier_threshold)),
                    "standardizations": (self.standardizations, lambda: standardization(data))
                    }

                # Loop through each selected option and call the corresponding function
                for key, (is_selected, func) in custom_functions.items():
                    if is_selected:
                        func()
                        step_done("Custom Preset, " + key)
                
            # If the preset is not recognized, log an error message and switch to default preset
            else:
                save_to_log("r", f"Error In Presets Selection... Switching to Default")
                default(data)
                self.step = 1
                step_done("Default Cleaning Preset... Due To An Error In Preset Selection")

        # If there was an error in processing files, log the error message and switch to default preset
        else: 
            save_to_log("r", f"{message_process_csv}")
            self.step = 1
            step_done("Default Cleaning Preset... Due To An Error In Preset Selection")

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
        self.output_label.config(text="The Program Finish Sucessfully!", fg=self.theme("text"))

        # Update The Screen
        self.root.update()

    # Update Progress
    def update_progress(self, value):

        # Update the progress bar value
        self.root.after(0, self.progress_var.set, value)

    # Setup Bindings Keys
    def setup_bindings(self):

        # Importing Libraries
        from core.keyboard import exit_key, log_toggle

        # Bind Exit Key
        exit_key(self.root, self.exit_function)

        # Bind Log Toggle Key
        log_toggle(self.root, self.toggle_log_window)
    
    # Toggle Log Window
    def toggle_log_window(self):

        # If the log viewer window exists and is open, close it
        if self.log_viewer_window and self.log_viewer_window.winfo_exists():
            self.close_log_viewer()
        
        # Otherwise, open the log viewer window
        else:
            self.open_log_viewer()
    
    # Open Log Viewer
    def open_log_viewer(self):

        # Create a new Toplevel window for the log viewer
        self.log_viewer_window = tk.Toplevel(self.root)
        self.log_viewer_window.title("Log Viewer")
        self.log_viewer_window.geometry("700x400")
        self.log_viewer_window.protocol("WM_DELETE_WINDOW", self.close_log_viewer)

        # Text widget with scrollbar
        self.text_frame = tk.Frame(self.log_viewer_window)
        self.text_frame.pack(fill=tk.BOTH, expand=True)

        # Create a scrolled text widget for displaying logs
        self.log_text = scrolledtext.ScrolledText(
            self.text_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            state=tk.DISABLED
        )

        # Pack the text widget to fill the window
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.apply_theme()

        # Load initial content
        self.refresh_log_viewer()

        # Schedule periodic updates (every 1000 ms)
        self.schedule_log_update()
    
    # Close Log Viewer
    def close_log_viewer(self):

        # Cancel any scheduled log updates
        if self.log_update_job:
            self.root.after_cancel(self.log_update_job)
            self.log_update_job = None

        # Destroy the log viewer window if it exists
        if self.log_viewer_window and self.log_viewer_window.winfo_exists():
            self.log_viewer_window.destroy()
            self.log_viewer_window = None
    
    # Schedule Log Update
    def schedule_log_update(self):

        # If the log viewer window exists and is open, update the logs every second
        if self.log_viewer_window and self.log_viewer_window.winfo_exists():
            self.refresh_log_viewer()
            self.log_update_job = self.root.after(1000, self.schedule_log_update)

    # Refresh Log Viewer  
    def refresh_log_viewer(self):

        # Importing Libraries
        from core.log import log_filename

        # Read the log file content
        try:
                            
            # Try to create the log file if it doesn't exist
            with open(log_filename, "r", encoding="utf-8") as f:
                content = f.read()
        
        # If error reading the log file, log the error and set content to an error message
        except Exception as e:
            save_to_log("r", "Error reading log file:")
            content = ""


        # Check if the scrollbar is at the bottom before updating the log content
        bottom_visible = self.log_text.yview()[1] > 0.9

        # Get the new content since the last update
        new_content = content[self.last_log_size:]

        # If there is new content, update the log viewer       
        if new_content:

            # Enable the text widget to update the content
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, new_content)

            # Scroll to the bottom if the user was already at the bottom
            if bottom_visible:
                self.log_text.see(tk.END)

            # Disable the text widget to prevent user edits
            self.log_text.config(state=tk.DISABLED)

            # Update last size
            self.last_log_size = len(content)