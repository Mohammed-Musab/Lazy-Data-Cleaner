# ABOUT LAZY DATA CLEANING

**Lazy Data Cleaner** is a lightweight dataset cleaning tool designed to preprocess data quickly and efficiently. It focuses on simplicity, making essential data cleaning accessible even for beginners.

**Currently,** the program supports the following file formats:

- `.csv`
- `.xlsx`
- `.xls`

(More file formats support might be added on request)

# REQUIREMENTS

## System Requirements

- **Operating System:** Windows

- **Python:** 3.13 or higher

## Python Dependencies

See `requirements.txt` for the full list of required libraries.

## Installation

Install dependencies using:

`py -m pip install -r requirements.txt`

# HOW TO RUN

1. Place your dataset file inside the **`Upload`** folder

*(Alternatively, use the `Upload File` button in the application)*

2. Double-click **`run.bat`** to start the application

3. The program will automatically process your dataset

4. The cleaned dataset will be saved in the **`Data`** folder.

To open log window press **`` ` ``** and it will open another window that refreshes every second.

# ABOUT FILE PROCESSING

The program **never modifies or deletes** files located in the **`Upload`** folder.

Instead:

- Files are **copied**

- Cleaning operations are performed on the **copied version**

- Results are saved inside the **`Data`** folder

This ensures your original data always remains unchanged.

# FORCE CSV

Added option to force save all output files as `.csv` format, **regardless** of input format.

# APPLICATION SCREENS

## Starting Screen

![](Images/Main.png)

## Settings Screen

![](Images/Settings.png)

## Progress Bar Screen

![](Images/Progress.png)

## Customize Screen

![](Images/Customize.png)

## End Screen

![](Images/End.png)

## Log Screen

![](Images/Log.png)

**All Screens are accessible within the application.**

# CLEANING PRESETS

At the moment, the program provides **five cleaning presets**:

## Default   
  
- Remove **duplicates**.

## AI

- Fill missing values with **median**.

- Fill missing values with **mode**.

- Remove **outliers**.

- Remove **duplicates**.

- Apply **standardization**.

## Business

- Fill missing values with **mode**.

- Remove **duplicates**.

## Streaming 
 
- Fill missing values with **mode**.

-  Remove **outliers**.
  
-  Remove **duplicates**.

## Custom

Allows users to manually select cleaning operations through a configuration menu.

# CUSTOM THRESHOLDS

When using the **Custom** preset, you can configure:

- **Missing Threshold (%)** - Columns with missing (**`%`**) above this value will be filled (or dropped if delete mode is enabled)

- **Outlier Threshold (Z-score)** - Values with Z-score above this threshold are removed (*default: 3*)

# LOGGING

All processing output is automatically saved to the `Logs` folder as `YYYY-MM-DD-log-N.txt` (`year-month-day-log-number`).

These logs help with debugging and tracking what changes were made to your data. 

# DEVELOPMENT STATUS

The project is currently under **active development.**

Features, presets, and workflows may change in future releases.

# CREDITS

Special thanks to:

- **@Atesthecoder** - for designing the **initial GUI interface**.

- **@Qoyyuum** - for testing the code and giving feedback throughout the journey.

# LICENSE

This project is licensed under the **MIT License**.

## You are free to:

- Use the software for personal and commercial purposes

- Modify the source code

- Distribute the project

## Under the condition that:

- The original copyright and license notice are included

For full details, see the `LICENSE` file.