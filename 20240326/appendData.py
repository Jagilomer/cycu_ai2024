import pandas as pd
import os

# Get the list of all file names in the specified directory
file_names = os.listdir('20240326/downloaded_files')

# Create an empty list to store the DataFrames
dfs = []

# Loop over each file name
for file_name in file_names:
    # Check if the file name ends with .csv
    if file_name.endswith('.csv'):
        # Read the CSV file and append the resulting DataFrame to the list
        dfs.append(pd.read_csv(f'20240326/downloaded_files/{file_name}', header=None))

# Concatenate all the DataFrames in the list
df = pd.concat(dfs, ignore_index=True)

# Write the resulting DataFrame to a new CSV file
df.to_csv('20240326/merged.csv', index=False)