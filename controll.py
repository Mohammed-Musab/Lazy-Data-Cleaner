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
    file_found = processing()

    # Getting path
    base_directory = Path(__file__).resolve().parent
    data_directory = base_directory / "Data"
    data_csv = list(data_directory.glob("*.csv"))

    # Process the files and make copies of them in Data folder
    if file_found:

        # Notify user that processing have finished
        print(F.GREEN + "Processing have finished!")

        s(0.05)

        result = counting_valuables()

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
