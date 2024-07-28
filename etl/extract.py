import os
import pandas as pd

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Args:
    - directory_path (str): Path of the directory to be created.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_and_save_csv(file_path, save_directory):
    """
    Load CSV file from `file_path` and save it to `save_directory`.

    Args:
    - file_path (str): Path to the CSV file to load.
    - save_directory (str): Directory to save the loaded DataFrame as a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_directory, file_name)
        data.to_csv(save_path, index=False)
        print(f"Data from {file_name} successfully loaded and saved to {save_path}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

def main():
    """
    Main function to execute the data loading and saving workflow.
    """
    # Define file paths and directories
    files_to_extract = ['creditcard.csv', 'creditcard_2023.csv']
    raw_data_directory = 'data/raw/'

    # Create the raw data directory if it doesn't exist
    create_directory(raw_data_directory)

    # Load and save each CSV file
    for file in files_to_extract:
        file_path = os.path.join(raw_data_directory, file)
        load_and_save_csv(file_path, raw_data_directory)

if __name__ == "__main__":
    main()
