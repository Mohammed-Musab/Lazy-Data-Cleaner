"""
This should count in next update:

- Countable values
- Uncountable values
"""

import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from time import sleep as s


init(autoreset=True)
invaild = F.RED + "Error: Invaild Input... System will countinue in Defualt!"


def count(data_csv):

    show = False
    delete = False

    # Notify user that counting process have started
    print(F.YELLOW + "Counting started...")
    s(0.5)

    # Process user input for showing tables
    show_table = input(F.YELLOW + "Do you want to see the tables? (Y/N)?").lower()
    if show_table == "y":
        show = True
        print(F.GREEN + "System will show tables.")
    elif show_table == "n":
        print(F.GREEN + "System will not show tables")
    else:
        print(F.RED + invaild)
    s(0.5)


    for file in data_csv:
        
        s(0.25)
        
        # Read current file
        df = pd.read_csv(file)
        print(F.YELLOW + f"counting valuables... for csv file located '{file}'")
        
        s(0.5)

        # Informations
        columns = df.columns
        print(df.shape)
        if show:
            print(F.YELLOW + "(Rows, Columns)")
            print("")
            print(df.info())
            print("")
        
        s(0.5)

        # Calculating missing data percentage
        total_cells = df.size
        missing_cells = df.isnull().sum().sum()
        if missing_cells == 0:
            precentage_na = 0.00
        else:
            precentage_na = (missing_cells / total_cells) * 100
        
        # Display missing data percentage
        if precentage_na > 0:
            print(F.YELLOW + f"Missing data percentage per column: {precentage_na:.2f}%") 
        
        # Show user that there is no missing data
        else:
            print(F.GREEN + "No missing data!")
        
        s(0.25)

        # Droping missing data if either user allowed or the percentage of missing data is less than 15%
        if precentage_na < 15 and precentage_na > 0:
            
            delete_comfirm = input(F.YELLOW + f"It is recommended to delete missing data since it is {precentage_na:.2f}%.. can system delete(Y/N)?").lower()
            if delete_comfirm == "y":
                delete = True
            elif delete_comfirm == "n":
                delete = False
            else:
                delete = False
                print(F.RED + invaild)
        
        elif precentage_na >= 15:
            
            # Show user that system will not delete missing data since the percentage is more than 15%
            print(F.YELLOW + f"System will not delete missing data since it is {precentage_na:.2f}% which is more than 15%")
            s(0.5)

            # Ask user if they want to fill in the missing data with mean, medium or nothing
            fill_in = input (F.YELLOW + "Do you want to fill in the missing data with mean (A), medium (B), nothing (N)? (A/B/N)?").lower()

            # Fill in the missing data with mean value after double checking with user
            if fill_in == "a":
                fill_mean = input(F.YELLOW + "Do you want to countine? (Y/N)?").lower()
                if fill_mean == "y":
                    df = df.fillna(df.mean())
                    print(F.GREEN + "System filled missing data with mean value!")
                elif fill_mean == "n":
                    print(F.GREEN + "System will not fill missing data with mean value!")
                else:
                    print(F.RED + invaild)

            # Fill in the missing data with medium value after double checking with user
            elif fill_in == "b":
                fill_medium = input(F.YELLOW + "Do you want to countine? (Y/N)?").lower()
                if fill_medium == "y":
                    df = df.fillna(df.median())
                    print(F.GREEN + "System filled missing data with medium value!")
                elif fill_medium == "n":
                    print(F.GREEN + "System will not fill missing data with medium value!")
                else:
                    print(F.RED + invaild)

            # Skip filling in the missing data
            elif fill_in == "n":
                print(F.GREEN + "System will not fill missing data!")
            
            # Invalid input
            else:
                print(F.RED + invaild)

            s(0.25)

        # Check if there is no missing data before deleting
        if delete and precentage_na == 0:
            print(F.GREEN + "No missing data!")

        # Delete missing data if either user allowed and the percentage of missing data is less than 15%
        elif delete:
            df = df.dropna()
            print(F.GREEN + "System deleted missing files!")

        s(0.25)

        # Save the cleaned data to the same file
        df.to_csv(file, index=False)

        s(0.1)
