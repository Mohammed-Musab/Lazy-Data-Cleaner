# Importing Libraries
import tkinter as tk

"""
DEV NOTE:

For version v0.4.2-prerelease

I am working on thoses list... and the update will be GUI focus:

Customizable optimization screen
Progress bar
Show estimate time              (Might be delayed if I have to)

"""

class LazyDataCleaner():
    def __init__(self, root):

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

        # Create all widgets
        self.create_widgets()

        # Main Screen
        self.main_screen()
    
    def create_widgets(self):

        # Defualt Values For Buttons & Labels Size
        button_width            = 40
        button_height           = 2
        button_settings_width   = 10
        button_settings_height  = 2
    
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
            text="v0.4.1-PRERELEASE",
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
            command=lambda: self.preset_selection(5, "Custom Settings Have Been Selected"),
            bd=0,
            highlightthickness=0,
            relief="flat"
        )
    
    def clear_frame(self):
        # Remove everything in screen
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

        # Restore background
        self.mainframe.configure(bg="light grey")

    def main_screen(self):

        # Clear The Screen
        self.clear_frame()

        # Display
        self.run_button.grid(row=1, sticky="ew")
        self.version_label.grid(row=2, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def preset_selection(self, value, text):
            
            # Set New Preset
            self.preset = value

            # Add The New Text
            self.settings_label_output.config(text=text)

            # Update The Screen
            self.root.update()

    def run(self):
        # Clear Frame
        self.clear_frame()
        # Remove returned button
        self.return_button.place_forget()

        # Inform User That Program Finished Running
        self.output_label.config(text="The Program Finish Sucessfully!",fg="green")

        # Main Function
        self.main_function(self.preset)

        # Display
        self.output_label.grid(row=1, sticky="ew")
        self.restart_button.grid(row=2, sticky="ew")
        self.exit_button.grid(row=3, sticky="ew")
        self.root.update()

    def rerun(self):
        # Clear Frame
        self.clear_frame()
        # Remove returned button
        self.return_button.place_forget()

        # Display
        self.clear_frame()
        self.output_label.grid(row=1, sticky="ew")
        self.restart_button.grid(row=2, sticky="ew")
        self.exit_button.grid(row=3, sticky="ew")
        self.settings_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.main_function(self.preset)

        # Update The Screen
        self.root.update()
    
    def exit_function(self):
        # Exit The Program
        self.root.destroy()
    
    def settings(self):
        # Clear Settings Button
        self.settings_button.place_forget()
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
        self.root.update()
    
    def returned(self):
        # Remove returned button
        self.return_button.place_forget()        

        # Show Main Screen
        self.main_screen()
    
    def main_function(self, preset):
        # Importing Libraries
        from core.processing import process_files_csv
        from colorama import Fore as F, init
        from datetime import datetime
        from pathlib import Path
        from core.presets import default, AI, bussinses, streaming, custom

        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")
        # Reset Colorama
        init(autoreset=True)

        # Processing files
        success_process_csv, message_process_csv = process_files_csv()

        # Getting Paths
        base_directory = Path(__file__).resolve().parent
        upload_directory = base_directory / "Upload"
        data_csv = list(upload_directory.glob("*.csv"))

        # If no errors
        if success_process_csv:

            # Preset Selected
            if preset == 1:
                default(data_csv)
            elif preset == 2:
                AI(data_csv)
            elif preset == 3:
                bussinses(data_csv)
            elif preset == 4:
                streaming(data_csv)
            elif preset == 5:
                custom(data_csv)
            else:
                print(F.RED + f"[{current_time}] Error In Presets Selection... Switching to Defualt")
                default(data_csv)

        else: 

            # Print Current Time & The Errror Message 
            print(F.RED + f"[{current_time}] {message_process_csv}")
