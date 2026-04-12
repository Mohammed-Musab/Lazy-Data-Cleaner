# Importing Libraries
from tkinter import filedialog, messagebox
import shutil
from pathlib import Path

# Upload File
def upload_file():
    # Open a file dialog to select a file
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
    base_directory = Path(__file__).resolve().parents[1]

    # Create Upload folder inside project
    upload_folder = base_directory / "Upload"
    upload_folder.mkdir(exist_ok=True)

    # Try to copy the selected file to the Upload folder and inform user about the result
    try:

        # Copy the selected file to the Upload folder
        file_path = Path(file_path).resolve(strict=True)
        destination = upload_folder / file_path.name
        shutil.copy(file_path, destination)
        messagebox.showinfo("Success", f"File uploaded to:\n{destination}")
    
    # Handle exceptions
    except Exception as e:
        messagebox.showerror("Error", str(e))