# Libraries
from time import sleep as s
from colorama import Fore as F, init
from process import processing
from count import count
from data_cleaing import clean
from pathlib import Path

# Valiables
delete_data = False                                                                 # Defualt False
show = False                                                                        # Defualt False
invaild = F.RED + "Error: Invaild Input... System will countinue in Defualt!"       # Error message
init(autoreset=True)                                                                # Reset color

# Welcome
print("Lazy Data Cleaner")
s(0.25)

# File path
base_directory = Path(__file__).resolve().parent
data_directory = base_directory / "Data"
data_csv = list(data_directory.glob("*.csv"))

# Run all commands in process.py
processing()

# Check if there is files before start cleaning data
files_exist = processing()

if not files_exist:
    
    # Exit if there is no files to clean
    print(F.RED + "No files to clean. Exiting.")
    s(0.5)

else:
    
    # Run all commands in count.py
    count(data_csv)
    s(1)

# End
print(F.GREEN + "Lazy Data Cleaner have finished all cleaning!")
