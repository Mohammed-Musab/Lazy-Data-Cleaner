# Import Libraries
from datetime import datetime
import os

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

global log_filename

# Get the log filename
log_filename = get_log_filename()

# Save to Log Function
def save_to_log(color="", message=""):

    color = color.lower()
    current_message = ""

    # Print the message with the corresponding color based on the indicator - will be replaced in future
    if color == "g":
        current_message = (f"[{get_time()}] Success: {message}")
    elif color == "y":
        current_message = (f"[{get_time()}] Warning: {message}")
    elif color == "r":
        current_message = (f"[{get_time()}] Error: {message}")
    else:
        current_message = (f"[{get_time()}] Info: {message}")

    # Save the message to a log file with the current time as the name
    with open(f"{log_filename}", "a") as log_file:
        log_file.write(current_message + "\n")