test = "test"

# Run this how file run
from time import sleep as s
from colorama import Fore as F, init
from process import processing
from count import count
# Valiables

delete_data = False # Defualt False
show = False        # Defualt False

invaild = F.RED + "Error: Invaild Input... System will countinue in Defualt!"

init(autoreset=True)

F.RESET

# Welcome
print("Lazy Data Cleaner")
s(1)

# Run all commands in process.py
processing()

# Respone for deleting data
delete_respone = input(F.YELLOW +"Can the system delete columns/rows, recommended for large datasets (Y/N)?").lower()

if delete_respone == "y":
    delete_data = True
    print(F.GREEN + "System can now delete data.")
elif delete_respone == "n":
    print(F.GREEN + "System won't delete data")
else:
    print(F.RED + invaild)
s(1)

# Show tables
show_table = input(F.YELLOW + "Do you want to see the tables? (Y/N)?").lower()
if show_table == "y":
    show = True
    print(F.GREEN + "System will show tables.")
elif show_table == "n":
    print(F.GREEN + "System will not show tables")
else:
    print(F.RED + invaild)
s(1)

# Run all commands in count.py
count(show, delete_data)
s(1)

# End
print(F.GREEN + "Lazy Data Cleaner have finished all cleaning!")
