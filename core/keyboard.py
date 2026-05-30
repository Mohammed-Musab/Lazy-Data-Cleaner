from .log import save_to_log

# Exit Key Function
def exit_key(root, function):

    # Bind the 'Q' key
    root.bind('<q>', lambda e: function())
    root.bind('<Q>', lambda e: function())
    save_to_log("g", "User Have Pressed the Quit Key To Exit Program.")

# Log Toggle Function
def log_toggle(root, function):

    # Bind the '`' key
    root.bind('<grave>', lambda e: function()) 
    save_to_log("g", "User Have Pressed the Log Key To Open/Close the Logs.")