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

def load_analyzed_data(file_path):
    """
    Load analyzed data from a CSV file.

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

def plot_confusion_matrix(conf_matrix, title):
    """
    Plot a confusion matrix.

    Args:
    - conf_matrix (pd.DataFrame): Confusion matrix DataFrame.
    - title (str): Title for the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.show()

def plot_class_distribution(data, title):
    """
    Plot class distribution.

    Args:
    - data (pd.DataFrame): DataFrame containing 'Actual' and 'Predicted' columns.
    - title (str): Title for the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Actual')
    plt.title(title)
    plt.show()

def main():
    """
    Main function to execute the visualization workflow.
    """
    # Define file paths
    analyzed_data_directory = '../data/analyzed/'
    files_to_visualize = ['creditcard.csv', 'creditcard_2023.csv']

    # Create the visualization directory if it doesn't exist
    visualization_directory = '../visualizations/'
    create_directory(visualization_directory)

    # Visualize each file
    for file in files_to_visualize:
        file_path = os.path.join(analyzed_data_directory, file)
        data = load_analyzed_data(file_path)

        if data is not None:
            # Plot class distribution
            plot_class_distribution(data, f"Class Distribution - {file}")

            # Plot confusion matrix
            conf_matrix = pd.crosstab(data['Actual'], data['Predicted'], rownames=['Actual'], colnames=['Predicted'])
            plot_confusion_matrix(conf_matrix, f"Confusion Matrix - {file}")

if __name__ == "__main__":
    main()
