# Importing Libraries
from processing import processing
from count import counting_valuables
from colorama import Fore as F, init
from time import sleep as s
from pathlib import Path

# Reset colorama settings after each print
init(autoreset=True)

# Controll function
def controlling():

    # Get the data from processing function
    data_csv = processing()

    # Process the files and make copies of them in Data folder
    if data_csv:

        # Notify user that processing have finished
        print(F.GREEN + "Processing have finished!")

        s(0.05)
    
        # Start counting valuables
        counting_valuables(data_csv)
        return True, "Process have finished successfully!"

    else:

        # Notify user that processing have failed
        print(F.RED + "Processing have failed!")

        s(0.05)

        # Return FileNotFoundError if the system had found no .csv file(s)
        return False, "File not found!"