# Importing Libraries
from .functions import fill_mean, fill_median, fill_mode, outlier, duplicates, standardization
from datetime import datetime
from colorama import Fore as F

# Get Current Time
current_time = datetime.now().strftime("%H:%M:%S")

# Default preset
def default(data_csv):

    fill_mean(True, 2, data_csv)
    fill_mode(True, 2, data_csv)
    outlier(data_csv)
    duplicates(data_csv)

# AI preset
def AI(data_csv):

    fill_median(True, 30, data_csv)
    fill_mode(True, 30, data_csv)
    outlier(data_csv)
    duplicates(data_csv)
    standardization(data_csv)

# Bussiness preset
def bussinses(data_csv):

    fill_mode(False, 5, data_csv)
    duplicates(data_csv)

# Streaming preset
def streaming(data_csv):

    fill_mode(True, 50, data_csv)
    outlier(data_csv)
    duplicates(data_csv)

# Custom preset
def custom(data_csv):

    print(F.RED + f"[{current_time}] NOT AVALIABLE YET!")
    print(F.RED + f"[{current_time}] Will come in v0.4.2-prerelease...")
    print(F.YELLOW + f"[{current_time}] Using defualt presets.")
    default(data_csv)
