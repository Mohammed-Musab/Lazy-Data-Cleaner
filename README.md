# Lazy Data Cleaner

A straightforward data cleaning tool designed to help you preprocess datasets with high accuracy and efficiency. It offers simple setup and execution, making data cleaning accessible even for beginners.

Right now the only datasets that it cleans are `.csv` files.

# REQUIREMENTS

64-bit Windows 10/11

- Python 3.13 or higher

- Colorama library

- pandas library

- numpy library

All are **mandatory** to run the program successfully.

# How to Run

Double-click `run.bat` to start the application. Before running, place your `CSV` file into the `Upload` folder and the results will come in the `Data` folder.
The script will process the uploaded file and display logs in the console window. Keep the console (`cmd`) open during operation.

Please note that the program **doesn't** remove or delete files in `Upload` folder.

# Customizing Settings

Configurable parameters are being worked on but for now there are 5 presets:

- Default   (fill in the mean, fill in the mode, remove outlier, and remove duplicates)
- AI        (fill in the median, fill in the mode, remove outlier, remove duplicates and apply standardization)
- Business  (fill in the mode and remove duplicates)
- Streaming (fill in the mode, remove outlier, and remove duplicates)
- Custom    (redirected to the default preset for now)

Please note that a custom settings menu will come in version `v0.4.2-PRERELEASE` 

# Additional Notes

The program is in active development; features and workflows may evolve.

The project is intended for **personal use**; modifications or redistribution are prohibited without permission.

# Credits

Thanks to the following members for helping develop the project:

- @Atesthecoder; for designing interface (**GUI**).

- @Qoyyuum; for testing the code and giving feedback.

# License

This project is licensed under a **Personal Use Only License**. Redistribution, modification, or commercial use is not permitted without explicit permission.
