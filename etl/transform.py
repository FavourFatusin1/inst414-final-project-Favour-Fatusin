import pandas as pd
import os

# Define file paths
file_path1 = 'data/processed/loaded_statistic1.csv'
file_path2 = 'data/processed/loaded_statistic2.csv'

# Load the data into DataFrames
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Example of data cleaning and wrangling
# Handle missing values (example: fill with mean or median, or drop)
df1.fillna(method='ffill', inplace=True)  # Forward fill for missing values
df2.fillna(method='ffill', inplace=True)

# Remove duplicates
df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)

# Normalize column names (example: lowercase and replace spaces with underscores)
df1.columns = [col.lower().replace(' ', '_') for col in df1.columns]
df2.columns = [col.lower().replace(' ', '_') for col in df2.columns]

# Handle inconsistent IDs (example: generate a new unique ID column if necessary)
df1['unique_id'] = df1.index
df2['unique_id'] = df2.index

# Merge datasets (if applicable)
# Example: merge on a common column (replace 'common_column' with actual column name)
# merged_df = pd.merge(df1, df2, on='common_column')

# Ensure the 'outputs' directory exists
os.makedirs('data/outputs', exist_ok=True)

# Save transformed data to new CSV files in the 'outputs' directory
transformed_file_path1 = 'data/outputs/transformed_statistic1.csv'
transformed_file_path2 = 'data/outputs/transformed_statistic2.csv'

df1.to_csv(transformed_file_path1, index=False)
df2.to_csv(transformed_file_path2, index=False)

print(f"\nData successfully transformed and saved to '{transformed_file_path1}' and '{transformed_file_path2}'")

# Perform exploratory data analysis (EDA)
print("\nExploratory Data Analysis:")
print("\nStatistic1 Data:")
print(df1.describe())
print(df1.info())

print("\nStatistic2 Data:")
print(df2.describe())
print(df2.info())
