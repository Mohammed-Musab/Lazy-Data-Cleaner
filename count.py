"""
This should count:

- Null done
- Columns done
- Countable values
- Uncountable values
"""

import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from time import sleep as s

init(autoreset=True)


def count(show, delete):

    delete = delete

    print(F.YELLOW + "Counting started...")
    s(1)

    # Path
    base_directory = Path(__file__).resolve().parent
    data_directory = base_directory / "Data"

    data_csv = list(data_directory.glob("*.csv"))

    # Check if there is files
    if not data_csv:

        print(F.RED + "Error: No CSV files have been found!")
        s(1)

    else:
        
        print(F.GREEN + "CSV files have been found!")
        s(1)

        for file in enumerate(data_csv, start=1):
            
            s(1)

            # Read current file
            df = pd.read_csv(file)
            print(F.YELLOW + f"counting valuables... for csv file located '{file}'")
            
            s(1)

            # Informations
            columns = df.columns
            print(df.shape)
            if show:
                print(F.YELLOW + "(Rows, Columns)")
                print(df.info())
            
            s(1)
 
            total_cells = df.size
            missing_cells = df.isnull().sum().sum()
            if missing_cells == 0:
                precentage_na = 0.00
            else:
                precentage_na = (missing_cells / total_cells) * 100

            if precentage_na < 15 and delete == False:
                delete_comfirm = input(F.YELLOW + f"It is recommended to delete missing data since it is {precentage_na:.2f}%.. can system delete(Y/N)?").lower()
                if delete_comfirm == "y":
                    delete = True
                elif delete_comfirm == "n":
                    pass
                else:
                    print(F.RED + "Error: Invaild Input... System will countinue in older answer!")
            
            if delete:
                df = df.dropna()
                print(F.GREEN + "System deleted missing files!")

            s(1)