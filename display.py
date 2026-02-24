# Importing Libraries
import tkinter as tk
from controll import controlling
from time import sleep as s

# Run on clicking run_button
def run():
    output_label.config(text="Running...")
    success, message = controlling()

    output_label.after(0, lambda: output_label.config(text=message, fg="green" if success else "red"))

# Displaying
def displaying(informations):
    output_label.config(text=f"{informations}", font=("Arial", 20, "bold"), fg="black")

# Create the main window
root = tk.Tk()

# Set window title
root.title("Lazy Data Cleaner - BETA")

# Set window size & non-resizable
root.geometry("1200x600")
root.resizable(False, False)

# Labels
#  Output label
output_label = tk.Label(root, text="OUTPUT", font=("Arial", 18, "bold"), fg="black")
output_label.grid()

# Buttons
#  Run button
run_button = tk.Button(root, text="RUN", font=("Arial", 40, "bold"), bg="blue", command=run)
run_button.grid()

# Main frame and main loop
mainframe = tk.Frame(root)
root.mainloop()