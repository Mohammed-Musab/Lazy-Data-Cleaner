"""
Creater note:

if someone who works on developing pandas library

it not 'mediam', it is 'medium'

and i won't write it unless it is absolutly needed

note to self:
df.method({col: value}, inplace=True)
to make code work with 3.0 pandas

"""

# Import Libraries
import pandas as pd
from colorama import Fore as F, init
from time import sleep as s
from pathlib import Path

# Reset colorama settings after each print
init(autoreset=True)

def counting_valuables():

    # Getting libraries
    base_directory = Path(__file__).resolve().parent
    data_directory = base_directory / "Data"
    data_csv = list(data_directory.glob("*.csv"))

    # Defualt Values, note that those values will be edittied by check list in future update
    defualt_threshold   = 02.50         # Defualt value for missing data percentage to decide whether to delete or not
    show_infomations    = True          # Defualt value for displaying information
    delete_data         = False         # Defualt value for deleting data
    fill_mode           = True          # Defualt value for filling in categorical columns missing data with mode
    safe_guard_fill     = False         # Don't Change unless testing

    # Please don't have more than one set to True
    fill_mean           = True          # Defualt value for filling in numerical columns missing data with mean
    fill_medium         = False         # Defualt value for filling in numerical columns missing data with medium
    fill_skip           = False         # Defualt value for skipping filling in missing data

    # Fill in mode for categorical data will be mode of the column unless fill_skip is True

    # Safe Guard
    fill_in = 0

    # Check if more than 1 fill in options is true
    if fill_mean:
        fill_in += 1
    if fill_medium:
        fill_in += 1
    if fill_skip:
        fill_in += 1

    # Check if something happened
    nothing = True


    # Notify user that counting process have started
    print(F.YELLOW + "Counting valuables started...")
    s(0.05)

    for file in data_csv:

        s(0.01)
        
        # Read current file
        df = pd.read_csv(file)
        print(F.YELLOW + f"Counting valuables... for csv file located '{file}'")

        s(0.01)

        # Numerical and Categorical columns
        numerical_column = df.select_dtypes(include=['number']).columns
        categorical_column = df.select_dtypes(include=['object', 'category']).columns

        # Show information about the datasets
        if show_infomations:

            # Display Dataset shape
            print("")
            print(df.shape)
            print(F.YELLOW + "(Rows, Columns)")

            s(0.1)
            print("")
            
            # Display Dataset info
            print(df.info())
            print("")
            s(0.1)

        # What happens if user have more than 1 set to True
        if fill_in > 1:
            print(F.RED + "WARNING SYSTEM HAS ALL FILL IN OPTIONS INEABLED OR NONE ENABLED")
            s(0.01)
            print(F.RED + "SYSTEM CHANGING SETTINGS TO MAKE IT SKIP")
            s(0.01)
            safe_guard_fill = True

        # What happens if user have all set to False
        elif fill_in == 0:
            print(F.RED + "WARNING SYSTEM HAS ALL FILL IN OPTIONS INEABLED OR NONE ENABLED")
            s(0.01)
            print(F.RED + "SYSTEM CHANGING SETTINGS TO MAKE IT SKIP")
            s(0.01)
            safe_guard_fill = True

        # Set all to False execpt fill_skip if safe guard active
        if safe_guard_fill:
            fill_mean   = False
            fill_medium = False
            fill_skip   = True

        # Fill in missing data with mean
        if fill_mean and len(numerical_column) > 0:

            # Loop for handling each column
            for column in numerical_column:

                # Calculate missing percentage
                mean_value = df[column].isna().mean() * 100

                # Delete column if mode value is more than defualt threadhold
                if mean_value > defualt_threshold and delete_data:
                    df.drop(columns=[column], inplace=True)
                    print(F.GREEN + f"Column '{column}' has been deleted because it has more than {defualt_threshold}% missing data.")

                # Check if mean value is not empty, if no fill in with mean value for this column
                elif not numerical_column.empty:

                    # Filling in missing data with mean
                    df[column] = df[column].fillna(df[column].mean())
                    print(F.GREEN + f"Missing data in column '{column}' filled with mean.")
                
                # Check if mode value is empty, if empty skip filling in missing data for this column
                else:
                    print(F.YELLOW + f"Column '{column}' has no mean value, skipping filling missing data for this column.")

            nothing = False

        # Fill in missing data with medium
        if fill_medium and len(numerical_column) > 0:
            
            # Loop for handling each column
            for column in numerical_column:

                # Calculate missing percentage
                medium_value = df[column].isna().mean() * 100
                
                # Delete column if mode value is more than defualt threadhold
                if medium_value <= defualt_threshold and delete_data:
                    df.drop(columns=[column], inplace=True)
                    print(F.GREEN + f"Column '{column}' has been deleted because it has more than {defualt_threshold}% missing data.")

                # Check if medium value is not empty, if no fill in with medium value for this column
                elif not numerical_column.empty:

                    # Filling in missing data with medium
                    df[column] = df[column].fillna(df[column].median())
                    print(F.GREEN + f"Missing data in column '{column}' filled with medium.")
                
                # Check if mode value is empty, if empty skip filling in missing data for this column
                else:
                    print(F.YELLOW + f"Column '{column}' has no medium value, skipping filling missing data for this column.")

            nothing = False
            
        # Don't fill in data if fill_skip is True
        if fill_skip:

            # Skip filling in missing data
            print(F.GREEN + "Missing data will not be filled.")
            nothing = False
        
        # Fill in mode
        if fill_mode and len(categorical_column) > 0:
            
            for column in categorical_column:
                
                # Get value counts for the column
                mode_value_na = df[column].isna().mean() * 100
                mode_value = df[column].mode()

                # Delete column if mode value is more than defualt threadhold
                if mode_value_na <= defualt_threshold and delete_data:
                    df.drop(columns=[column], inplace=True)
                    print(F.GREEN + f"Column '{column}' has been deleted because it has more than {defualt_threshold}% missing data.")

                # Check if mode value is not empty and less than defualt threadhold, if no fill in with mode value for this column
                elif not delete_data:
                    
                    # Fill in missing data with mode
                    df[column] = df[column].fillna(mode_value[0])
                    print(F.GREEN + f"Missing data in column '{column}' filled with mode.")
                
                # Check if mode value is empty, if empty skip filling in missing data for this column
                else:
                    print(F.YELLOW + f"Column '{column}' has no mode value, skipping filling missing data for this column.")
            
            nothing = False

        if nothing:

            print(F.RED + "SYSTEM ERROR: Invalid filling method.")
            
            return False, "SYSTEM ERROR: Invalid filling method."
            break

