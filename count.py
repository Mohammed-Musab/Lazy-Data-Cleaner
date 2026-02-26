# Import Libraries
import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from time import sleep as s

# Defualt Values, note that those values will be edittied by check list
defualt_threshold   = 12.50         # Defualt value for missing data percentage to decide whether to delete or not
show_infomations    = False         # Defualt value for displaying information
fill_mean           = True          # Defualt value for filling in missing data with mean
fill_medium         = False         # Defualt value for filling in missing data with medium
fill_skip           = False         # Defualt value for skipping filling in missing data
delete_data         = False         # Defualt value for deleting data
# Fill in mode for categorical data will be mode of the column unless fill_skip is True

# Reset colorama settings after each print
init(autoreset=True)

def counting_valuables(data_csv):

    # Notify user that counting process have started
    print(F.YELLOW + "Counting valuables started...")
    s(0.05)

    for file in data_csv:

        s(0.01)
        
        # Read current file
        df = pd.read_csv(file)
        columns = df.columns
        print(F.YELLOW + f"Counting valuables... for csv file located '{file}'")

        s(0.01)

        # Numerical and categorical columns
        numerical_column = df.select_dtypes(include=['number']).columns
        categorical_column = df.select_dtypes(include=['object', 'category']).columns

        if show_infomations:

            # Display Dataset shape
            print(df.shape)
            print(F.YELLOW + "(Rows, Columns)")
            s(0.2)

            # Display Dataset info
            print("")
            print(df.info())
            print("")
            s(0.2)

        if fill_mean and len(numerical_column) > 0:

            # Fill in missing data with mean
            df.fillna(df.mean(numeric_only=True), inplace=True)
            print(F.GREEN + "Missing data filled with mean.")
        
        elif fill_medium and len(numerical_column) > 0:

            # Fill in missing data with medium
            df.fillna(df.median(numeric_only=True), inplace=True)
            print(F.GREEN + "Missing data filled with medium.")
        
        elif fill_skip:

            # Skip filling in missing data
            print(F.GREEN + "Missing data will not be filled.")
        
        elif not fill_skip and len(categorical_column) > 0:
            
            for column in categorical_column:
                
                # Get value counts for the column
                mode_value = df[column].mode()
                
                # Check if mode value is not empty, if no fill in with mode value for this column
                if not mode_value.empty:
                    
                    # Fill in missing data with mode
                    df[column].fillna(mode_value[0], inplace=True)
                    print(F.GREEN + f"Missing data in column '{column}' filled with mode.")
                
                # Check if mode value is empty, if empty skip filling in missing data for this column
                else:
                    print(F.YELLOW + f"Column '{column}' has no mode value, skipping filling missing data for this column.")

        else:

            print(F.RED + "SYSTEM ERROR: Invalid filling method.")
            
            return False, "SYSTEM ERROR: Invalid filling method."
