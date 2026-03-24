# Importing Librarie(s)
import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from datetime import datetime
from word2number import w2n
import numpy as np
from .read_and_write import load_file, save_file
import contextlib

# Reset Colorama
init(autoreset=True)

# Time Display
def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Convert word to number
def safe_w2n(value):
    return value
"""

Disabled, waiting for word2number dev update it

    # Check if value is not a string or is nan
    if not isinstance(value, str) or pd.isna(value):
        return value
    
    # Try to convert it
    try:
        return w2n.word_to_num(value)
    
    # If convertion failed return original value
    except:
        return value

"""

# Clean the nan
def clean(x):

    # Check if it definison of pandas empty
    if pd.isna(x): 
        # If yes yes return numpy empty
        return np.nan
    
    # Remove any space (before/after)
    s = str(x).strip()

    # If it contain any of those values return numpy empty
    if s.lower() in ['nan', 'none', '']:
        return np.nan
    
    # Return the lower text
    return s.lower()

# Format String
def format_string_values(x):

    # Replacing space with "_" if it a string
    if isinstance(x, str) and not pd.isna(x):
        return x.replace(" ", "_").replace("-", "_")

    # Return the lower text
    return x

# Merging Columns
def merging(df):

    # Column name directory
    new_column_names = {}

    # For each column name
    for column in df.columns:
        # Format the column Name
        cleaned_name = clean(column)
        cleaned_name = safe_w2n(cleaned_name)
        cleaned_name = format_string_values(cleaned_name)

        # Save the new column name
        new_column_names[column] = str(cleaned_name)

    # Rename columns
    df = df.rename(columns=new_column_names)

    # Lists
    columns = df.columns.tolist()
    normalized = {}
    to_remove = []

    # For each column in columns
    for column in columns:
        # Correct Format
        normal = column.lower().strip()

        # Check if the name is already there
        if normal in normalized:
            # Filter the normalized data to keep only the normal rows
            main_column = normalized[normal]

            # Inform user that column will be merged
            print(F.RED + f"[{get_time()}] Duplicate Detected: '{column}' looks like '{main_column}'")
            
            # User input loop
            while True:
                # User Input
                user_input = input(F.CYAN + f"[{get_time()}] Would you like to merge them? (Y/N): ").lower()

                # If user allow merging
                if user_input == "y":
                    # Check both right and left columns
                    left = df[main_column]
                    right = df[column]

                    # First replace missing data in the right with left columns
                    if isinstance(left, pd.DataFrame):
                        left = left.iloc[:, 0]

                    # Then replace missing data in the left with right columns 
                    if isinstance(right, pd.DataFrame):
                        right = right.iloc[:, 0]
                    
                    # Combine them and remove the left column
                    df[main_column] = left.combine_first(right)
                    to_remove.append(column)

                    # Inform user that process finished and end cycle
                    print(F.YELLOW + f"[{get_time()}] Merged '{column}' into '{main_column}'")
                    break

                # If user doesn't allow merging
                elif user_input == "n":
                    # Rename column
                    new_name = f"{column}_2"
                    df = df.rename(columns={column: new_name})

                    # Inform user that process finished and end cycle
                    print(F.YELLOW + f"[{get_time()}] Kept both. Renamed '{column}' to '{new_name}'")
                    break

                # If invaild input
                else:
                    print(F.RED + f"[{get_time()}] Invalid Input Try Again")
        
        # If the name not already there add it
        else:
            normalized[normal] = column

    # Delete the redundant columns
    df = df.drop(columns=to_remove)
    return df

# Function - Copying Files
def process_files(force_change_csv=False):
    
    # Notify user that process started
    print(F.GREEN + f"[{get_time()}] Processing started...")

    # Getting (Paths)
    base_directory = Path(__file__).resolve().parent.parent     ## Parent Folder Directory
    upload_directory = base_directory / "Upload"                ## Upload Folder
    data_directory = base_directory / "Data"                    ## Data Folder
    
    # Files list
    data = []
    data.extend(upload_directory.glob("*.csv"))                 ## Add csv files to list
    data.extend(upload_directory.glob("*.xlsx"))                ## Add xlsx files to list
    data.extend(upload_directory.glob("*.xls"))                 ## Add xls files to list

    # What happens if the system had found no file(s)
    if not data:

        # Inform user that system had found no file(s)!
        print(F.RED + f"[{get_time()}] Error: No file have been found!")

        # Retrun Error
        return False, f"[{get_time()}] Error: No file have been found!"

    # Procced if the system had found a file(s)
    else:
        
        # Inform user that system had found a file(s)!
        print(F.GREEN + f"[{get_time()}] File(s) have been found!")

        # Copied files list
        copied_files = []

        # Copying files to Data folder
        for i, file in enumerate(data, start=1):
            # Mute pandas error notification
            pd.set_option('future.no_silent_downcasting', True)
            
            # Check if (Data) folder exist, if not, create it
            data_directory.mkdir(exist_ok=True)
            
            # Read the CSV file
            df = load_file(file)
            df = df.map(clean)
            df = df.map(safe_w2n)
            df = df.map(format_string_values)
            df = merging(df)

            # Rename the file while keeping orginial name and save it to (Data) folder
            original_name = Path(file).stem
            extension = Path(file).suffix
            new_name = data_directory / f"{original_name}_cleaned{extension}"

            # Save the file
            if force_change_csv == True:
                save_file(df, new_name, True)
            else:
                save_file(df, new_name)

            # Inform user that system had processed a copy of the file
            print(F.GREEN + f"[{get_time()}] Processed a copy for file located in {new_name}")
            copied_files.append(new_name)


        # Return sucess message
        return True, f"[{get_time()}] Finished Copying Files"