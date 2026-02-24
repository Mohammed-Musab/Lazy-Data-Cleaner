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

        if show_infomations:
            # Display Dataset shape
            print(df.shape)
            print(F.YELLOW + "(Rows, Columns)")
            s(0.2)

            # return

            # Display Dataset info
            print("")
            print(df.info())
            print("")
            s(0.2)
