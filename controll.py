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
    
        # Capture the return value from counting_valuables
        result = counting_valuables(data_csv)

        # If the result is None, it means counting have completed successfully without any issues
        if result is None:
            return True, "Counting completed."
        
        # If the result is not None, it means counting have completed but with some issues (like no .csv file found)
        return result
        
    else:

        # Notify user that processing have failed
        print(F.RED + "Processing have failed! (check the cmd for more details)")

        s(0.05)

        # Return FileNotFoundError if the system had found no .csv file(s)
        return False, "File not found!"
