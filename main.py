import process
from time import sleep as s
from colorama import Fore as F, init

# Valiables

delete_data = False

# Welcome
print("Lazy Data Cleaner")
s(1)

# Run all commands in process.py
process.processing()

# Respone for deleting data
delete_respone = input(F.YELLOW +"Can the system delete columns/rows, recommended for large datasets (Y/N)?").lower()
if delete_respone == "y":
    delete_data = True
    print(F.GREEN +"System can now delete data")
elif delete_respone == "n":
    print(F.GREEN +"System won't delete data")
else:
    print(F.RED + "Error: Invaild Input...")
    s(0.5)
    print(F.RED + "System will countine to defualt, won't delete data")

s(1)
F.RESET

s(1)
print(F.GREEN + "Lazy Data Cleaner have finished all cleaning!")

F.RESET
