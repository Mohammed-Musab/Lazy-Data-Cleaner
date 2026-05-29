# Importing Libraries
import pandas as pd
import os
from pathlib import Path
from datetime import datetime
from core.log import save_to_log

# Time Display
def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Load Files
def load_file(path, **kwargs):
    # Get the extension
    extension = os.path.splitext(path)[1].lower()
    save_to_log("g", "Getting the {.extension} of the file.")

    # If extension is csv read it
    if extension == ".csv":
        save_to_log("g", "Reading the {.csv} file.")
        return pd.read_csv(path, index_col=None, **kwargs)

    # If extension is xlsx or xls read it
    elif extension in [".xlsx", ".xls"]:
        save_to_log("g", "Reading the {.xlsx}/{.xls} file.")
        return pd.read_excel(path, index_col=None, **kwargs)

    # Else return unspported file type issue
    else:
        raise ValueError(f"[{get_time()}] Unsupported file type: {extension}")

# Save Files
def save_file(df, filename, force_csv=False, **kwargs):
    # Get the orginial path
    data_directory = Path(__file__).resolve().parents[1] / "Data"
    data_directory.mkdir(parents=True, exist_ok=True)
    save_to_log("g", "Getting the directory.")
    
    # If user want to force to be csv
    if force_csv:
        filename = Path(filename).stem + ".csv"
    
    # Output path
    output_path = data_directory / filename
    save_to_log("g", "Getting the output path.")
    
    # Get the extension
    extension = output_path.suffix.lower()
    save_to_log("g", "Getting the {.extension} of the file.")

    # If extension is csv save it
    if extension == ".csv":
        save_to_log("g", "Saving the file as {.csv} file.")
        df.to_csv(output_path, index=False, **kwargs)

    # If extension is xlsx or xls save it
    elif extension in [".xlsx", ".xls"]:
        save_to_log("g", "Saving the file as {.xlsx} file.")
        df.to_excel(output_path, index=False, **kwargs)
    
    # Else return unspported file type issue
    else:
        raise ValueError(f"[{get_time()}] Unsupported file type: {extension}")
    
    # Inform user that file have been save in this location
    save_to_log("g", f"File saved to: {output_path}")