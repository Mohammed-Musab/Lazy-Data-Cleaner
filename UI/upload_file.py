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
    base_directory = Path(__file__).resolve().parent[1]

    # Create Upload folder inside project
    upload_folder = base_directory / "Upload"
    upload_folder.mkdir(exist_ok=True)
    file_path = Path(file_path).resolve(strict=True)

    # Copy file
    try:
        destination = upload_folder / file_path.name
        shutil.copy(file_path, destination)
        messagebox.showinfo("Success", f"File uploaded to:\n{destination}")
    
    #
    except Exception as e:
        messagebox.showerror("Error", str(e))