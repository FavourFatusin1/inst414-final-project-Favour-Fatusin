import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Args:
    - directory_path (str): Path of the directory to be created.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_csv(file_path):
    """
    Load CSV file into a pandas DataFrame.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame or None: Loaded DataFrame if successful, None if an error occurs.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data from {file_path} successfully loaded")
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def clean_and_transform_data(data):
    """
    Perform cleaning and transformation on the data.

    Args:
    - data (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: Cleaned and transformed DataFrame.
    """
    # Handle missing values
    data = data.dropna()

    # Handle duplicates
    data = data.drop_duplicates()

    # Ensure consistent attribute naming
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

    # Convert categorical variables to numerical if necessary
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = data[col].astype('category').cat.codes

    # Normalize data if necessary
    numerical_cols = data.select_dtypes(include=['number']).columns
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()

    return data

def exploratory_data_analysis(data):
    """
    Perform exploratory data analysis (EDA) on the data.

    Args:
    - data (pd.DataFrame): Input DataFrame for EDA.
    """
    # Plot distributions of numerical columns
    for col in data.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    # Plot correlation matrix
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def save_processed_data(data, file_path):
    """
    Save processed data to a CSV file.

    Args:
    - data (pd.DataFrame): Processed DataFrame.
    - file_path (str): Path to save the CSV file.
    """
    data.to_csv(file_path, index=False)
    print(f"Processed data saved to {file_path}")

def main():
    """
    Main function to execute data preprocessing and EDA workflow.
    """
    # Define file paths
    raw_data_directory = 'data/raw/'
    processed_data_directory = 'data/processed/'
    files_to_process = ['creditcard.csv', 'creditcard_2023.csv']

    # Create the processed data directory if it doesn't exist
    create_directory(processed_data_directory)

    # Process each file
    for file in files_to_process:
        file_path = os.path.join(raw_data_directory, file)
        data = load_csv(file_path)
        
        if data is not None:
            # Clean and transform data
            cleaned_data = clean_and_transform_data(data)
            
            # Perform exploratory data analysis
            exploratory_data_analysis(cleaned_data)
            
            # Save processed data
            save_path = os.path.join(processed_data_directory, file)
            save_processed_data(cleaned_data, save_path)

if __name__ == "__main__":
    main()
