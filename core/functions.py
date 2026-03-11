# Importing Libraries
import pandas as pd
from datetime import datetime
from colorama import init, Fore as F
import numpy as np
from scipy import stats

# Get Current Time
current_time = datetime.now().strftime("%H:%M:%S")
# Reset Colorama
init(autoreset=True)

# Standardization
def standardization(data_csv):
    for file in data_csv:

        # Read file
        df = pd.read_csv(file)

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns

        # Standardization function for columns
        df[numerical_columns] = (df[numerical_columns] - df[numerical_columns].mean()) / df[numerical_columns].std()

        # Save file
        df.to_csv(file, index=False)

        # Infrom user that standardization have finished
        print(F.GREEN + f"[{current_time}] Standardization Done for '{file}'.")

# Outlier
def outlier(data_csv):
    for file in data_csv:

        # Read file
        df = pd.read_csv(file)

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=[np.number]).columns
        
        # Calculate Z-score
        z_scores = np.abs(stats.zscore(df[numerical_columns]))
        threshold = 3

        # Remove the outlier
        df_clean = df[(z_scores < threshold).all(axis=1)]

        # Save file
        df_clean.to_csv(file)

        # Infrom user that outlier have been removed
        print(F.GREEN + f"[{current_time}] Removed outliers for '{file}'.")

# Duplicates
def duplicates(data_csv):
    for file in data_csv:

        # Read file
        df = pd.read_csv(file)

        # Remove duplicates
        df_clean = df.drop_duplicates()

        # Save file
        df_clean.to_csv(file)

        # Infrom user that duplicates rows have been removed
        print(F.GREEN + f"[{current_time}] Removed duplicate rows for '{file}'.")

# Fill in missing data with mean
def fill_mean(delete, na_threshold, data_csv):
    for file in data_csv:

        # Read file
        df = pd.read_csv(file)

        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns

        for column in numerical_columns:
            
            # Calculate missing precentage
            na_precentage = df[column].isna().mean() * 100

            # If prcentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            if na_threshold >= na_precentage and delete:
                df = df.dropna(subset=[column])
                print(F.GREEN + f"[{current_time}] Dropped missing data.")

            # If prcentage of missing data is greater than missing data threshold, fill in missing data
            elif na_threshold <= na_precentage:
                df[column] = df[column].fillna(df[column].mean())
                print(F.GREEN + f"[{current_time}] Missing data in column '{column}' filled with mean.")
        
        # Save File
        df.to_csv(file)

# Fill in missing data with median
def fill_median(delete, na_threshold, data_csv):
    for file in data_csv:

        # Read File
        df = pd.read_csv(file)
        
        # Get numerical columns
        numerical_columns = df.select_dtypes(include=['number']).columns

        for column in numerical_columns:

            # Calculate missing precentage
            na_precentage = df[column].isna().mean() * 100

            # If prcentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            if na_threshold >= na_precentage and delete:
                df = df.dropna(subset=[column])
                print(F.GREEN + f"[{current_time}] Dropped missing data.")

            # If prcentage of missing data is greater than missing data threshold, fill in missing data
            elif na_threshold <= na_precentage:
                df[column] = df[column].fillna(df[column].median())
                print(F.GREEN + f"[{current_time}] Missing data in column '{column}' filled with median.")
        
        # Save File
        df.to_csv(file)

# Fill in missing data with mode
def fill_mode(delete, na_threshold, data_csv):
    for file in data_csv:

        # Read File
        df = pd.read_csv(file)

        # Get categorical columns
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns

        for column in categorical_columns:

            # Calculate missing precentage
            na_precentage = df[column].isna().mean() * 100

            # If prcentage of missing data is less than missing data threshold and user allowed deleting data, drop missing rows
            if na_threshold >= na_precentage and delete:
                df = df.dropna(subset=[column])
                print(F.GREEN + f"[{current_time}] Dropped missing data.")

            # If prcentage of missing data is greater than missing data threshold, fill in missing data 
            elif na_threshold <= na_precentage:
                df[column] = df[column].fillna(df[column].mode()[0])
                print(F.GREEN + f"[{current_time}] Missing data in column '{column}' filled with mode.")

        # Save file
        df.to_csv(file)
