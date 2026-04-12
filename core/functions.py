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

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns

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

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=[np.number]).columns
        
        # Calculate Z-score
        z_scores = np.abs(stats.zscore(df[numerical_columns]))

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
        df.drop_duplicates(drop=True, inplace=True)

        # Inform user that duplicates have been removed
        if len(df) < initial_count:
            save_to_log("y", f"Removed {initial_count - len(df)} exact duplicate rows.")

        # Get the index labels
        if not df.empty:

            # Get the index labels
            indexs = df.index.astype(str).tolist()
            normalized = {}
            to_remove = []

            # Loop through the index labels to find duplicates
            for index_label in indexs:

                # Correct Format
                normal = index_label.lower().strip().replace(" ", "_").replace("-", "_")

                # Check if the normalized index label already exist in the normalized dictionary, if exist, merge the two rows and mark the redundant row for deletion
                if normal in normalized:
                    
                    # Get the main index label
                    main_index = normalized[normal]

                    # Inform User That Column Will Be Merged
                    save_to_log("r", f"Duplicate Detected: '{index_label}' looks like '{main_index}'")
                    
                    # Merge the two rows and mark the redundant row for deletion
                    df.loc[main_index] = df.loc[main_index].combine_first(df.loc[index_label])
                    to_remove.append(index_label)

                    # Inform user that the two rows have been merged
                    save_to_log("y", f"Merged '{index_label}' into '{main_index}'")
                
                # If not exist, add the normalized index label to the normalized dictionary
                else:
                    normalized[normal] = index_label

            # Delete the redundant columns
            if to_remove:
                df.drop(index=to_remove, inplace=True)
            
            # Reset the index after merging and deleting duplicates
            df.reset_index(drop=True, inplace=True)

        # Save file and Inform user that duplicates have been removed
        save_file(df, file)
        save_to_log("g", "Finished Removing Duplicates")

# Fill in missing data with mean
def fill_mean(delete, na_threshold=30, data=[]):

    # Loop through each file in the data list
    for file in data:

        # Read file
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
                df[column] = df[column].fillna(df[column].mean())
                save_to_log("g", f"Missing data in column {column} filled with mean.")
        
        # Save File
        save_file(df, file)

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
                df[column] = df[column].fillna(df[column].mode()[0])
                save_to_log("g", f"Missing data in column {column} filled with mode.")

        # Save file
        save_file(df, file)