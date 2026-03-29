# Importing Libraries
from tkinter import filedialog, messagebox
import shutil
import os
from pathlib import Path

# Upload File
def upload_file():
    # 
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Supported files", "*.txt *.csv *.xlsx"),
            ("Text files", "*.txt"),
            ("CSV files", "*.csv"),
            ("Excel files", "*.xlsx")
        ]
    )

    # If user cancels
    if not file_path:
        return

    # Get absolute path of current script directory
    base_directory = Path(__file__).resolve().parent.parent

    # Create Upload folder inside project
    upload_folder = base_directory / "Upload"
    os.makedirs(upload_folder, exist_ok=True)

    # Copy file
    try:
        destination = os.path.join(upload_folder, os.path.basename(file_path))
        shutil.copy(file_path, destination)
        messagebox.showinfo("Success", f"File uploaded to:\n{destination}")
    
    #
    except Exception as e:
        messagebox.showerror("Error", str(e))