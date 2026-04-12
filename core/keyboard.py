# Exit Key Function
def exit_key(root, function):

    # Bind the 'Q' key
    root.bind('<q>', lambda e: function())
    root.bind('<Q>', lambda e: function())

# Log Toggle Function
def log_toggle(root, function):

    # Bind the '`' key
    root.bind('<grave>', lambda e: function()) 