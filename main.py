# Importing Libraries
import tkinter as tk
from UI.display import LazyDataCleaner

# Run
if __name__ == "__main__":    
    root = tk.Tk()
    app = LazyDataCleaner(root)
    root.mainloop()

"""
By: Solo Developer
Project: Lazy Data Cleaner
This project is designed to provide a user-friendly interface for cleaning and preprocessing data.
Main goal is to provide high accuracy dataset cleaning for beginners and non-technical users,
but also includes advanced features for experienced data scientists.
"""