# Importing Libraries
import pandas as pd
import numpy as np
from scipy import stats
from .read_and_write import load_file, save_file
from core.log import save_to_log

# Standardization
def standardization(data):

    # Loop through each file in the data list
    for file in data:

        # Read file
        df = load_file(file)
        save_to_log("g", "Loaded Dataset for Standardization.")

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns
        save_to_log("g", "Got Numerical Columns for Standardization.")

        # Standardization function for columns
        df[numerical_columns] = (df[numerical_columns] - df[numerical_columns].mean()) / df[numerical_columns].std()

        # Save file
        save_file(df, file)

        # Infrom user that standardization have finished
        save_to_log("g", f"Applied standardization for '{file}'.")

# Outlier
def outlier(data, threshold=3):

    # Loop through each file in the data list
    for file in data:

        # Read file
        df = load_file(file)
        save_to_log("g", "Loaded Dataset for Outlier Removal.")

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=[np.number]).columns
        save_to_log("g", "Got Numerical Columns for Outlier Removal.")

        # Calculate Z-score
        z_scores = np.abs(stats.zscore(df[numerical_columns]))
        save_to_log("g", "Calculated the Z-Score.")

        # Remove the outlier
        df_clean = df[(z_scores < threshold).all(axis=1)]

        # Save file
        save_file(df_clean, file)

        # Infrom user that outlier have been removed
        save_to_log("g", f"Removed outliers for '{file}'.")

# Duplicates
def duplicate(data):

    # Loop through each file in the data list
    for file in data:

        # Read file
        df = load_file(file)

        # Store the initial count of rows
        initial_count = len(df)
        df.drop_duplicates(inplace=True)
        save_to_log("g", "Counted the number of rows.")

        # Inform user that duplicates have been removed
        if len(df) < initial_count:
            save_to_log("y", f"Removed {initial_count - len(df)} exact duplicate rows.")

        # Smart duplicate merge using the row content instead of the row index
        if not df.empty:

            # Get the index labels and initialize a dictionary to track normalized rows and a list to track rows to remove
            indexs = df.index.tolist()
            normalized = {}
            to_remove = []
            save_to_log("g", "Got the row values.")

            # Loop through each index label to check for duplicates based on the content of the row
            for index_label in indexs:

                # Get the row corresponding to the index label
                row = df.loc[index_label]

                # Normalize the whole row with spaces as the separator
                normal = tuple(
                    str(value).strip().lower().replace("_", " ").replace("-", " ")
                    if pd.notna(value) else "<na>"
                    for value in row.tolist()
                )

                # Check if the normalized row already exists
                if normal in normalized:

                    # Merge the current row with the existing row in the DataFrame and mark the current row for removal
                    main_index = normalized[normal]
                    save_to_log("r", f"Duplicate Detected: row '{index_label}' looks like row '{main_index}'")
                    df.loc[main_index] = df.loc[main_index].combine_first(df.loc[index_label])
                    to_remove.append(index_label)
                    save_to_log("y", f"Merged row '{index_label}' into row '{main_index}'")

                # If the normalized row does not exist, add it to the dictionary
                else:
                    normalized[normal] = index_label

            # Remove the marked rows and inform user about the number of removed rows
            if to_remove:
                df.drop(index=to_remove, inplace=True)
                save_to_log("g", "Deleted the redundant rows.")

            # Reset the index
            df.reset_index(drop=True, inplace=True)
            save_to_log("g", "Reset the index after removing duplicates.")

        # Save file and Inform user that duplicates have been removed
        save_file(df, file)
        save_to_log("g", "Finished Removing Duplicates.")

# Fill in missing data with mean
def fill_mean(delete, na_threshold=30, data=[]):

    # Loop through each file in the data list
    for file in data:

        # Read file
        df = load_file(file)
        save_to_log("g", "Loaded Dataset for Applying the Mean.")

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns
        save_to_log("g", "Got the numerical columns.")

        # Loop through each numerical column to fill in missing data
        for column in numerical_columns:
            
            # Calculate missing percentage
            na_percentage = df[column].isna().mean() * 100
            save_to_log("g", f"Calculated the missing Data Percentage, which is around {na_percentage.round()}")

            # Check if there is no missing data
            if na_percentage == 0:
                save_to_log("y", f"No missing data for {column}")

            # If percentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            elif na_threshold >= na_percentage and delete:
                df = df.dropna(subset=[column])
                save_to_log("g", f"Dropped missing data for {column}.")

            # If percentage of missing data is greater than missing data threshold, fill in missing data
            elif na_threshold <= na_percentage:
                df[column] = df[column].fillna(df[column].mean())
                save_to_log("g", f"Missing data in column {column} filled with mean.")
        
        # Save File
        save_file(df, file)
        save_to_log("g", "Finished Applying Mean")

# Fill in missing data with median
def fill_median(delete, na_threshold=30, data=[]):

    # Loop through each file in the data list
    for file in data:

        # Read File
        df = load_file(file)
        
        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns

        # Loop through each numerical column to fill in missing data
        for column in numerical_columns:

            # Calculate missing precentage
            na_precentage = df[column].isna().mean() * 100

            # Check if there is no missing data
            if na_precentage == 0:
                save_to_log("y", f"No missing data for {column}")

            # If prcentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            elif na_threshold >= na_precentage and delete:
                df = df.dropna(subset=[column])
                save_to_log("g", f"Dropped missing data for {column}.")

            # If prcentage of missing data is greater than missing data threshold, fill in missing data
            elif na_threshold <= na_precentage:
                df[column] = df[column].fillna(df[column].median())
                save_to_log("g", f"Missing data in column {column} filled with median.")
        
        # Save File
        save_file(df, file)

# Fill in missing data with mode
def fill_mode(delete,  na_threshold=30, data=[]):

    # Loop through each file in the data list
    for file in data:

        # Read File
        df = load_file(file)

        # Get categorical columns
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns

        # Loop through each categorical column to fill in missing data
        for column in categorical_columns:

            # Calculate missing precentage
            na_precentage = df[column].isna().mean() * 100

            # Check if there is no missing data
            if na_precentage == 0:
                save_to_log("y", f"No missing data for {column}")

            # If prcentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            elif na_threshold >= na_precentage and delete:
                df = df.dropna(subset=[column])
                save_to_log("g", f"Dropped missing data for {column}.")

            # If prcentage of missing data is greater than missing data threshold, fill in missing data 
            elif na_threshold <= na_precentage:
                try:
                    df[column] = df[column].fillna(df[column].mode()[0])
                    save_to_log("g", f"Missing data in column {column} filled with mode.")
                except Exception as e:
                    save_to_log("r", f"Error occurred while filling missing data in column {column}: {e}")

        # Save file
        save_file(df, file)
