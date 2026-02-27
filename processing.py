# Importing Libraries
import pandas as pd
from pathlib import Path
from time import sleep as s
from colorama import Fore as F, init

# Reset colorama settings after each print
init(autoreset=True)

# Processing function
def processing():
    
    # Notify user that processing have started
    print(F.YELLOW + "Processing started...")

    # Getting libraries
    base_directory = Path(__file__).resolve().parent
    upload_directory = base_directory / "Upload"
    data_directory = base_directory / "Data"
    data_csv = list(upload_directory.glob("*.csv"))

    # What happens if the system had found no .csv file(s)
    if not data_csv:

        # Inform user that system had found no .csv file(s)!
        print(F.RED + "Error: No CSV files have been found!")
        s(0.5)

        return False

    # Procced if the system had found a .csv file(s)
    else:
        
        # Inform user that system had found a .csv file(s)!
        print(F.GREEN + "CSV files have been found!")
        s(0.5)

        copied_files = []

        # Copying files to Data folder
        for i, file in enumerate(data_csv, start=1):
            
            # Check if Data folder exist, if not, create it
            data_directory.mkdir(exist_ok=True)
            
            # Read the CSV file
            df = pd.read_csv(file)
            
            # Rename the file and save it to Data folder
            new_name = data_directory / f"data_{i}.csv"
            df.to_csv(new_name, index=False)

            # Inform user that system had processed a copy of the file
            print(F.GREEN + f"Processed a copy for file located in {new_name}")
            copied_files.append(new_name)

            s(0.01)
        
        return True
