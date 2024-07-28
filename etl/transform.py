import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data from {file_path} successfully loaded")
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def clean_and_transform_data(data):
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
    # Plot distributions
    for col in data.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    # Plot correlations
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def save_processed_data(data, file_path):
    data.to_csv(file_path, index=False)
    print(f"Processed data saved to {file_path}")

def main():
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
