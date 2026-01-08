# This part of code main function is to read all files in Upload folder

import pandas as pd
from pathlib import Path
from time import sleep as s
from colorama import Fore as F, init

init(autoreset=True)

print(F.GREEN + "Processing started!")
F.RESET

def processing():
    
    base_directory = Path(__file__).resolve().parent
    upload_directory = base_directory / "Upload"
    data_directory = base_directory / "Data"

    data_csv = list(upload_directory.glob("*.csv"))

    # Check if there is files
    
    if not data_csv:

        print(F.RED + "Error: No CSV files have been found!")
        s(0.5)

    else:
        
        print(F.GREEN + "CSV files have been found!")
        F.RESET
        s(0.5)

        for i, file in enumerate(data_csv, start=1):

            df = pd.read_csv(file)
            new_name = data_directory / f"data_{i}.csv"
            df.to_csv(new_name, index=False)
            print(f"Processed a copy for file located in {new_name}")
            s(0.1)
