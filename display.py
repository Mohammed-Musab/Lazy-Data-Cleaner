# Importing Libraries
import tkinter as tk
from controll import controlling

# Run on clicking run_button
def run():
    
    # Inform user that the system is running
    output_label.config(text="Running...",fg="black")

    # Display either error or success message after controlling function have finished
    success, message = controlling()

    # Display either error or success message after controlling function have finished
    output_label.after(0, lambda: output_label.config(text=message, fg="green" if success else "red"))

    # Grid the beta label and infer button
    beta_label.grid()
    infer_button.grid()
    
# Displaying
def displaying(informations):
    output_label.config(text=f"{informations}", font=("Arial", 20, "bold"), fg="black")

# Continue function
def proceed():
    
    # Remove unneeded labels and buttons
    beta_label,infer_button.destroy()

    # Display either error or success message after controlling function have finished
    success, message = controlling()

    # Display either error or success message after controlling function have finished
    output_label.after(0, lambda: output_label.config(text=message, fg="green" if success else "red"))
    
    # Grid the restart button
    restart_button.grid()
    
# Create the main window
root = tk.Tk()

# Set window title
root.title("Lazy Data Cleaner - BETA")

# Set window size & non-resizable
root.geometry("460x250")
root.resizable(False, False)

# Labels
#  Output label
output_label = tk.Label(root, text="OUTPUT", font=("Arial", 18, "bold"), fg="black")
output_label.grid()
#  Beta informing label
beta_label = tk.Label(root,text=(f"This is a beta program it will be update"),font=("Arial", 18, "bold"), fg="green",)


# Buttons
#  Proceed button:
infer_button = tk.Button(root,text=f"if you want continue click me!!!",bg="black",command=proceed,fg="green")
#  Restart button
restart_button = tk.Button(text="re-start system",command=proceed)

#  Run button
run_button = tk.Button(root, text="RUN", font=("Arial", 40, "bold"), bg="blue", command=run)
run_button.grid()

# Main frame and main loop
mainframe = tk.Frame(root)
root.mainloop()
