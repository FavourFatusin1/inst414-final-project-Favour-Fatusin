import os
import pandas as pd

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_and_save_csv(file_path, save_directory):
    try:
        data = pd.read_csv(file_path)
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_directory, file_name)
        data.to_csv(save_path, index=False)
        print(f"Data from {file_name} successfully loaded and saved to {save_path}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

def main():
    # Define file paths
    files_to_extract = ['creditcard.csv', 'creditcard_2023.csv']
    raw_data_directory = 'data/raw/'

    # Create the raw data directory if it doesn't exist
    create_directory(raw_data_directory)

    # Load and save each CSV file
    for file in files_to_extract:
        load_and_save_csv(file, raw_data_directory)

if __name__ == "__main__":
    main()
