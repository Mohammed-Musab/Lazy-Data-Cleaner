# Importing Libraries
import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from datetime import datetime

# Get Current Time
current_time = datetime.now().strftime("%H:%M:%S")
# Reset Colorama
init(autoreset=True)

# Function - Copying Files
def process_files_csv():
    
    # Notify user that process started
    print(F.GREEN + f"[{current_time}] Processing started...")

    # Getting Paths
    base_directory = Path(__file__).resolve().parent.parent
    upload_directory = base_directory / "Upload"
    data_directory = base_directory / "Data"
    data_csv = list(upload_directory.glob("*.csv"))

    # What happens if the system had found no .csv file(s)
    if not data_csv:

        # Inform user that system had found no .csv file(s)!
        print(F.RED + f"[{current_time}] Error: No CSV files have been found!")

        # Retrun Error
        return False, "Error: No CSV files have been found!"

    # Procced if the system had found a .csv file(s)
    else:
        
        # Inform user that system had found a .csv file(s)!
        print(F.GREEN + f"[{current_time}] CSV files have been found!")

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
            print(F.GREEN + f"[{current_time}] Processed a copy for file located in {new_name}")
            copied_files.append(new_name)
        
        # Return Sucess message
        return True, "Finished Copying Files"
