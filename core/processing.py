# Importing Libraries
import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from datetime import datetime
from word2number import w2n
import numpy as np

# Get Current Time
current_time = datetime.now().strftime("%H:%M:%S")
# Reset Colorama
init(autoreset=True)

def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Function - Copying Files
def process_files_csv():
    
    # Notify user that process started
    print(F.GREEN + f"[{get_time()}] Processing started...")

    # Getting Paths
    base_directory = Path(__file__).resolve().parent.parent
    upload_directory = base_directory / "Upload"
    data_directory = base_directory / "Data"
    data_csv = list(upload_directory.glob("*.csv"))

    # What happens if the system had found no .csv file(s)
    if not data_csv:

        # Inform user that system had found no .csv file(s)!
        print(F.RED + f"[{get_time()}] Error: No CSV files have been found!")

        # Retrun Error
        return False, "Error: No CSV files have been found!"

    # Procced if the system had found a .csv file(s)
    else:
        
        # Inform user that system had found a .csv file(s)!
        print(F.GREEN + f"[{get_time()}] CSV files have been found!")

        copied_files = []

        # Copying files to Data folder
        for i, file in enumerate(data_csv, start=1):

            pd.set_option('future.no_silent_downcasting', True)
            # Check if Data folder exist, if not, create it
            data_directory.mkdir(exist_ok=True)
            
            # Read the CSV file
            df = pd.read_csv(file)
            df = df.map(clean)
            df = df.map(safe_w2n)
            df = df.map(format_string_values)
            df = merging(df)

            # Rename the file and save it to Data folder
            new_name = data_directory / f"data_{i}.csv"
            df.to_csv(new_name, index=False)

            # Inform user that system had processed a copy of the file
            print(F.GREEN + f"[{get_time()}] Processed a copy for file located in {new_name}")
            copied_files.append(new_name)
        
        # Return Sucess message
        return True, "Finished Copying Files"

def merging(df):

    new_column_names = {}

    for column in df.columns:
        cleaned_name = clean(column)
        cleaned_name = safe_w2n(cleaned_name)
        cleaned_name = format_string_values(cleaned_name)
        new_column_names[column] = str(cleaned_name)

    df = df.rename(columns=new_column_names)

    columns = df.columns.tolist()
    normalized = {}
    to_remove = []

    for column in columns:
        # Correct Format
        normal = column.lower().strip()

        if normal in normalized:
            main_column = normalized[normal]

            # Inform User That Column Will Be Merged
            print(F.RED + f"[{get_time()}] Duplicate Detected: '{column}' looks like '{main_column}'")
            
            while True:
                user_input = input(F.CYAN + f"[{get_time()}] Would you like to merge them? (Y/N): ").lower()

                if user_input == "y":
                    left = df[main_column]
                    right = df[column]
                    if isinstance(left, pd.DataFrame):
                        left = left.iloc[:, 0]
                    if isinstance(right, pd.DataFrame):
                        right = right.iloc[:, 0]
                    df[main_column] = left.combine_first(right)
                    to_remove.append(column)
                    print(F.YELLOW + f"[{get_time()}] Merged '{column}' into '{main_column}'")
                    break
                elif user_input == "n":
                    new_name = f"{column}_2"
                    df = df.rename(columns={column: new_name})
                    print(F.YELLOW + f"[{get_time()}] Kept both. Renamed '{column}' to '{new_name}'")
                    break
                else:
                    print(F.RED + f"[{get_time()}] Invalid Input Try Again")
        else:
            normalized[normal] = column

    # Delete the redundant columns
    df = df.drop(columns=to_remove)
    return df

def safe_w2n(value):
    if not isinstance(value, str) or pd.isna(value):
        return value
    try:
        return w2n.word_to_num(value)
    except:
        return value

def clean(x):
    if pd.isna(x): 
        return np.nan
    s = str(x).strip()
    if s.lower() in ['nan', 'none', '']:
        return np.nan
    return s.lower()

def format_string_values(x):
    if isinstance(x, str) and not pd.isna(x):
        return x.replace(" ", "_")
    return x
