# Importing Libraries
import pandas as pd
import os
from pathlib import Path
from datetime import datetime
from colorama import Fore as F, init

# Reset Colorama
init(autoreset=True)

# Time Display
def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Load Files
def load_file(path, **kwargs):
    # Get the extension
    extension = os.path.splitext(path)[1].lower()

    # If extension is csv read it
    if extension == ".csv":
        return pd.read_csv(path, **kwargs)

    # If extension is xlsx or xls read it
    elif extension in [".xlsx", ".xls"]:
        return pd.read_excel(path, **kwargs)

    # Else return unspported file type issue
    else:
        raise ValueError(f"[{get_time}] Unsupported file type: {extension}")

# Save Files
def save_file(df, filename, force_csv=False, **kwargs):
    # Get the orginial path
    data_directory = Path(__file__).resolve().parent.parent / "Data"
    data_directory.mkdir(parents=True, exist_ok=True)
    
    # If user want to force to be csv
    if force_csv:
        filename = Path(filename).stem + ".csv"
    
    # Output path
    output_path = data_directory / filename
    
    # Get the extension
    extension = output_path.suffix.lower()

    # If extension is csv save it
    if extension == ".csv":
        df.to_csv(output_path, index=False, **kwargs)

    # If extension is xlsx or xls save it
    elif extension in [".xlsx", ".xls"]:
        df.to_excel(output_path, index=False, **kwargs)
    
    # Else return unspported file type issue
    else:
        raise ValueError(f"[{get_time()}] Unsupported file type: {extension}")
    
    # Inform user that file have been save in this location
    print(F.GREEN + f"[{get_time()}] File saved to: {output_path}")