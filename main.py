# Importing Libraries
import tkinter as tk
from UI.display import LazyDataCleaner
"Fun Fact: If I don't know what is happen, you won't and I don't.. send help!"
# Run
if __name__ == "__main__":    
    root = tk.Tk()
    app = LazyDataCleaner(root)
    root.mainloop()
