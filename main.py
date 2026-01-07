# Run this how file run

import process
from time import sleep as s
from colorama import Fore as F, init


# Run all commands in process.py
s(0.5)
print("Lazy Data Cleaner")
s(1)
print("Processing files located in Upload folder in 5 seconds...")
s(5)
process.processing()
s(1)
print(F.GREEN + "Lazy Data Cleaner have finished all cleaning!")
print("")
F.RESET