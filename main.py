import tkinter as tk
from UI.display import LazyDataCleaner

if __name__ == "__main__":    
    root = tk.Tk()
    app = LazyDataCleaner(root)
    root.configure(bg="light grey")
    root.mainloop()
