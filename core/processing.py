# Importing Librarie(s)
import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from datetime import datetime
from word2number import w2n
import numpy as np
from .read_and_write import load_file, save_file
import contextlib, os

# Reset Colorama
init(autoreset=True)

# Time Display
def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Identify numerical like columns
def is_numeric_like(series, sample_size=100):
    # Get a sample of the series
    series = series.dropna().astype(str).head(sample_size)

    # If more than 50% of values are digits or can be converted to a number
    count_numeric = sum([v.replace('.', '', 1).isdigit() or v.replace('-', '', 1).isdigit() for v in series])
    return count_numeric / max(len(series), 1) > 0.5

# Convert word to number
def safe_w2n(series, cap=1000):

    # Get the unquie values
    unique_values = series.dropna().unique()

    # Check if the number of unique values >= cap
    if len(unique_values) >= cap:
        print(F.YELLOW + f"[{get_time()}] Warning: Too many unique values, {len(unique_values)}.\nSkipping word to number conversion.")
        return series
    
    cache = {}

    for value in unique_values:
 
        try:
            # Convert the value to a number
                with open(os.devnull, 'w') as f, \
                     contextlib.redirect_stdout(f), \
                     contextlib.redirect_stderr(f):

                    cache[value] = w2n.word_to_num(value)
        except:
            # If conversion fails, keep the original value
            cache[value] = value

    return series.map(lambda x: cache.get(x, x))

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
    
    # Return
    return s

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
    normalized = {}  
    to_merge = []  

    # For each column name
    for column in df.columns:
        normal = column.lower().replace(" ", "_").replace("-", "_")
        if normal in normalized:
            to_merge.append((normalized[normal], column))
        else:
            normalized[normal] = column

    for target, source in to_merge:
        left = df[target]
        right = df[source]

        if isinstance(left, pd.DataFrame):
            left = left.iloc[:, 0]
        if isinstance(right, pd.DataFrame):
            right = right.iloc[:, 0]

        df[target] = left.where(left.notna(), right)
        df = df.drop(columns=[source])
        print(F.YELLOW + f"[{get_time()}] Merged '{source}' into '{target}'")

    return df

# Function - Copying Files
def process_files(force_change_csv=False):
    
    # Notify user that process started
    print(F.GREEN + f"[{get_time()}] Processing started...")

    # Getting (Paths)
    base_directory = Path(__file__).resolve().parents[1]         ## Parent Folder Directory
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
            
            # Clean the data
            for column in df.columns:
                if df[column].dtype == object:
                    df[column] = df[column].apply(clean)
            
            # Convert numeric columns
            for column in df.columns:
                if df[column].dtype != object:
                    df[column] = pd.to_numeric(df[column], errors='coerce')

            # Convert word to numbers
            for column in df.columns:
                if df[column].dtype == object and is_numeric_like(df[column]):
                    df[column] = safe_w2n(df[column])

            # Format string values
            for column in df.columns:
                if df[column].dtype == object and not is_numeric_like(df[column]):
                    df[column] = df[column].apply(format_string_values)
                    df[column] = df[column].str.replace(r'[\s\-]+', '_', regex=True)
            
            # Merging columns
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