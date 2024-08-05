import pandas as pd
import os

# Define file paths
file_path1 = 'data/statistic1.csv'
file_path2 = 'data/statistic2.csv'

# Load the data into DataFrames
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Print basic info to verify successful loading
print("Data from statistic1.csv:")
print(df1.info())
print(df1.head())

print("\nData from statistic2.csv:")
print(df2.info())
print(df2.head())

# Ensure the 'processed' directory exists
os.makedirs('data/processed', exist_ok=True)

# Save loaded data to new CSV files in the 'processed' directory
df1.to_csv('data/processed/loaded_statistic1.csv', index=False)
df2.to_csv('data/processed/loaded_statistic2.csv', index=False)

print("\nData successfully loaded and saved to 'data/processed/loaded_statistic1.csv' and 'data/processed/loaded_statistic2.csv'")
