# Import Libraries
from colorama import Fore as F, init
from datetime import datetime
import os

# Reset Colorama
init(autoreset=True)

# Time Functions
def get_time():
    return datetime.now().strftime("%H:%M:%S")
def get_date():
    return datetime.now().strftime("%d-%m-%Y")

# Current Time for Log File Name
current_time = get_date()

# Get Log Filename (to avoid overwriting existing logs)
def get_log_filename():
    
    # Ensure the logs directory exists
    os.makedirs("Logs", exist_ok=True)

    # Get the current date and initialize a counter
    date = get_date()
    n = 1

    while True:
        
        # Construct the filename using the date and counter
        filename = f"Logs/{date}-log-{n}.txt"

        # If the filename does not exist, return it; otherwise, increment the counter and try again
        if not os.path.exists(filename):
            return filename
        
        n += 1

# Get the log filename
log_filename = get_log_filename()

# Save to Log Function
def save_to_log(color="", message=""):

    color = color.lower()

    # Print the message with the corresponding color based on the indicator - will be replaced in future
    if color == "g" or color == "green":
        print(F.GREEN + f"[{get_time()}] {message}")
    elif color == "y" or color == "yellow":
        print(F.YELLOW + f"[{get_time()}] {message}")
    elif color == "r" or color == "red":
        print(F.RED + f"[{get_time()}] {message}")
    else:
        print(f"[{get_time()}] {message}")

    # Save the message to a log file with the current time as the name
    with open(f"{log_filename}", "a") as log_file:
        log_file.write(f"[{get_time()}] {message}\n")