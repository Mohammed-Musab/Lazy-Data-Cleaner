import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Supported files", "*.txt *.csv *.xlsx"),
            ("Text files", "*.txt"),
            ("CSV files", "*.csv"),
            ("Excel files", "*.xlsx")
        ]
    )

    if not file_path:
        return  # user cancelled

    # Make sure Upload folder exists
    upload_folder = "Upload"
    os.makedirs(upload_folder, exist_ok=True)

    # Copy file
    try:
        destination = os.path.join(upload_folder, os.path.basename(file_path))
        shutil.copy(file_path, destination)
        messagebox.showinfo("Success", f"File uploaded to:\n{destination}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("File Uploader")

btn = tk.Button(root, text="Upload File", command=upload_file)
btn.pack(pady=20)

root.mainloop()