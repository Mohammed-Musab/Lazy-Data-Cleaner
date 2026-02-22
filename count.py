"""
This should count in next update: (I had to update alot of things so we getting new update!)

- Countable values
- Uncountable values
"""

import pandas as pd
from pathlib import Path
from colorama import Fore as F, init
from time import sleep as s

# Change this value to change the threshold for missing data percentage to decide whether to delete or not
missing_data_threshold = 15.00

init(autoreset=True)
invaild = F.RED + "Error: Invaild Input... System will countinue in Defualt!"

# Defualt values for cleaning data
delete_ultra_defualt = False        # Defualt value for deleting data
fill_ultra_defualt = "skip"         # Defualt value for filling in missing data, options are "mean", "medium" and "skip"
skipping = False                    # Defualt value for skipping questions about cleaning data

def count(data_csv):

    show = False
    delete = False

    # Notify user that counting process have started
    print(F.YELLOW + "Counting started...")
    s(0.5)

    # Process user input for showing tables
    show_info = input(F.YELLOW + "Do you want to see informations about dataset? (Y/N)?").lower()
    if show_info == "y":
        show = True
        print(F.GREEN + "System will show informations about the dataset.")
    elif show_info == "n":
        print(F.GREEN + "System will not show informations about the dataset.")
    else:
        print(F.RED + invaild)
    s(0.5)


    # Setting defualt value for cleaning data
    defualt_all = input(F.YELLOW + "Do you want to use make defualt value for all questions? (Y/N)?").lower()
    if defualt_all == "y":

        skipping = True

        delete_ultra = input(F.YELLOW + f"Do you want to delete missing data if the percentage of missing data is less than {missing_data_threshold}%? (Y/N)?").lower()
        if delete_ultra == "y":
            delete_ultra = True
        elif delete_ultra == "n":
            delete_ultra = False
        else:
            delete_ultra = False
            print(F.RED + invaild)
        
        fill_ultra = input(F.YELLOW + "Do you want to fill in the missing data with mean (A), medium (B), or skip (C)?").lower()
        if fill_ultra == "a":
            fill_ultra = "mean"
        elif fill_ultra == "b":
            fill_ultra = "medium"
        elif fill_ultra == "c":
            fill_ultra = "skip"
        else:
            fill_ultra = fill_ultra_defualt
            print(F.RED + invaild)

    elif defualt_all == "n":
        pass
    else:
        print(F.RED + invaild)


    for file in data_csv:
        
        s(0.25)
        
        # Read current file
        df = pd.read_csv(file)
        columns = df.columns
        print(F.YELLOW + f"counting valuables... for csv file located '{file}'")
        
        s(0.5)

        # Informations
        if show:
            
            # Dataset shape
            print(df.shape)
            print(F.YELLOW + "(Rows, Columns)")
            s(0.2)

            # Dataset info
            print("")
            print(df.info())
            print("")
            s(0.2)

            # Basic summery statistics
            print(df.describe(include='all'))
            s(0.2)

        for col in columns:

            delete = False


            if skipping == True:
                
                # Calculating missing data percentage
                precentage_na = df[col].isna().mean() * 100


                # You can figure it out by yourself, good luck!
                if delete_ultra_defualt == True and precentage_na < missing_data_threshold:
                    df[col] = df[col].dropna()
                    print(F.GREEN + f"System deleted missing files in column '{col}'!")
                elif fill_ultra_defualt == "mean":
                    df[col] = df[col].fillna(df[col].mean())
                    print(F.GREEN + f"System filled missing data in column '{col}' with mean value!")
                elif fill_ultra_defualt == "medium":
                    df[col] = df[col].fillna(df[col].median())
                    print(F.GREEN + f"System filled missing data in column '{col}' with medium value!")
                elif fill_ultra_defualt == "skip":
                    print(F.GREEN + f"System will not fill missing data in column '{col}'!")
                else:
                    print(F.RED + "SYSTEM ERROR")
                s(0.05)

            elif skipping == False:
                s(0.1)

                # Calculating missing data percentage
                precentage_na = df[col].isna().mean() * 100
                
                # Display missing data percentage
                if precentage_na > 0:
                    print(F.YELLOW + f"Missing data percentage for column '{col}': {precentage_na:.2f}%") 
                
                # Show user that there is no missing data
                else:
                    print(F.GREEN + f"No missing data for column '{col}'!")
                s(0.25)

                # Droping missing data if either user allowed or the percentage of missing data is less than threadhold
                if precentage_na < missing_data_threshold and precentage_na > 0:
                    
                    delete_comfirm = input(F.YELLOW + f"It is recommended to delete missing data since it is {precentage_na:.2f}%.. can system delete(Y/N)?").lower()
                    if delete_comfirm == "y":
                        delete = True
                    elif delete_comfirm == "n":
                        delete = False
                    else:
                        delete = False
                        print(F.RED + invaild)
                
                elif precentage_na >= 15:
                    
                    # Show user that system will not delete missing data since the percentage is more than threadhold
                    print(F.YELLOW + f"System will not delete missing data since it is {precentage_na:.2f}% which is more than {missing_data_threshold:.2f}%")
                    s(0.5)

                    # Ask user if they want to fill in the missing data with mean, medium or nothing
                    fill_in = input (F.YELLOW + "Do you want to fill in the missing data with mean (A), medium (B), nothing (C)? (A/B/N)?").lower()

                    # Fill in the missing data with mean value after double checking with user
                    if fill_in == "a":
                        fill_mean = input(F.YELLOW + "Do you want to countine? (Y/N)?").lower()
                        if fill_mean == "y":
                            df[col] = df[col].fillna(df[col].mean())
                            print(F.GREEN + "System filled missing data with mean value!")
                        elif fill_mean == "n":
                            print(F.GREEN + "System will not fill missing data with mean value!")
                        else:
                            print(F.RED + invaild)

                    # Fill in the missing data with medium value after double checking with user
                    elif fill_in == "b":
                        fill_medium = input(F.YELLOW + "Do you want to countine? (Y/N)?").lower()
                        if fill_medium == "y":
                            df[col] = df[col].fillna(df[col].median())
                            print(F.GREEN + "System filled missing data with medium value!")
                        elif fill_medium == "n":
                            print(F.GREEN + "System will not fill missing data with medium value!")
                        else:
                            print(F.RED + invaild)

                    # Skip filling in the missing data
                    elif fill_in == "c":
                        print(F.GREEN + "System will not fill missing data!")
                    
                    # Invalid input
                    else:
                        print(F.RED + invaild)

                    s(0.25)

                # Check if there is no missing data before deleting
                if delete and precentage_na == 0:
                    print(F.GREEN + "No missing data!")

                # Delete missing data if either user allowed and the percentage of missing data is less than threadhold
                elif delete:
                    df[col] = df[col].dropna()
                    print(F.GREEN + "System deleted missing files!")

                s(0.25)

        # Save the cleaned data to the same file
        df.to_csv(file, index=False)

        s(0.1)
