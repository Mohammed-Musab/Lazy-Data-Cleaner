# Importing Librarie(s)
import pandas as pd
from pathlib import Path
from word2number import w2n
import numpy as np
from .read_and_write import load_file, save_file
import contextlib, os
from core.log import save_to_log
from datetime import datetime

# Get Current Time
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
        save_to_log("y", f"Warning: Too many unique values, {len(unique_values)}.\nSkipping word to number conversion.")
        return series
    
    # Cache for converted values
    cache = {}

    # Loop through each unique value and try to convert it to a number
    for value in unique_values:
 
        # Try to convert the value to a number
        try:
            # Convert the value to a number
            with open(os.devnull, 'w') as f, \
                contextlib.redirect_stdout(f), \
                contextlib.redirect_stderr(f):
                cache[value] = w2n.word_to_num(value)
        
        # If conversion fails, keep the original value
        except:
            cache[value] = value

    # Map the original series to the converted values
    return series.map(lambda x: cache.get(x, x))

# Clean the nan
def clean(x):

    # If it is already nan return it
    if pd.isna(x): 
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

    # Normalize column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r'[\s\-]+', '_', regex=True)
        .str.replace(r'_+', '_', regex=True)
        .str.strip('_')
    )

    # Group columns by their normalized names
    grouped = {}

    # Loop through each column and group them by their normalized names
    for index, column in enumerate(df.columns):
        grouped.setdefault(column, []).append(index)

    # Create a new DataFrame to hold the merged columns
    new_df = pd.DataFrame()

    # Loop through each group of columns and merge them
    for column, columnss in grouped.items():

        # If there is only one column with this name, just copy it to the new DataFrame
        if len(columnss) == 1:
            new_df[column] = df.iloc[:, columnss[0]]
        
        # If there are multiple columns with this name, merge them and add the merged column to the new DataFrame
        else:

            # Start with the first column as the base for merging
            merged = df.iloc[:, columnss[0]]

            # Loop through the remaining columns and merge them with the base column
            for index in columnss[1:]:
                merged = merged.combine_first(df.iloc[:, index])

            # Add the merged column to the new DataFrame and inform user about the merging process
            new_df[column] = merged
            save_to_log("y", f"Merged {columnss} into '{column}'")

    # Return the new DataFrame with merged columns
    return new_df

# Function - Copying Files
def process_files(force_change_csv=False):
    
    # Notify user that process started
    save_to_log("g", "Processing started...")

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
        save_to_log("r", "Error: No file have been found!")

        # Retrun Error
        return False, f"[{get_time()}] Error: No file have been found!"

    # Procced if the system had found a file(s)
    else:
        
        # Inform user that system had found a file(s)!
        save_to_log("g", "File(s) have been found!")

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
            
            # Normalize column names
            for column in df.columns:
                if df[column].dtype == object and not is_numeric_like(df[column]):
                    df[column] = (
                        df[column]
                        .astype(str)
                        .str.strip()
                        .str.lower()
                        .str.replace(r'[^\w]+', '_', regex=True)
                        .str.replace(r'_+', '_', regex=True)
                        .str.strip('_')
                    )
            
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
            save_to_log("g", f"Processed a copy for file located in {new_name}")
            copied_files.append(new_name)


        # Return sucess message
        return True, f"[{get_time()}] Finished Copying Files"