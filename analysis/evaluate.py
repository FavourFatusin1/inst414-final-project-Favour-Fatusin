import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Args:
    - directory_path (str): Path of the directory to be created.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_processed_data(file_path):
    """
    Load processed data from a CSV file.

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

def split_data(data, target_column):
    """
    Split data into features (X) and target (y).

    Args:
    - data (pd.DataFrame): DataFrame containing the dataset.
    - target_column (str): Name of the target column.

    Returns:
    - tuple: X_train, X_test, y_train, y_test
    """
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def scale_data(X_train, X_test):
    """
    Standardize features by removing the mean and scaling to unit variance.

    Args:
    - X_train (pd.DataFrame): Training data features.
    - X_test (pd.DataFrame): Test data features.

    Returns:
    - tuple: X_train_scaled, X_test_scaled
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

def train_random_forest(X_train, y_train):
    """
    Train a Random Forest classifier.

    Args:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data target labels.

    Returns:
    - RandomForestClassifier: Trained Random Forest model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on test data.

    Args:
    - model (RandomForestClassifier): Trained classifier model.
    - X_test (pd.DataFrame): Test data features.
    - y_test (pd.Series): Test data target labels.

    Returns:
    - tuple: y_test, y_pred
    """
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Accuracy Score:")
    print(accuracy_score(y_test, y_pred))

    return y_test, y_pred

def plot_confusion_matrix(y_test, y_pred):
    """
    Plot a confusion matrix.

    Args:
    - y_test (pd.Series): Actual target labels.
    - y_pred (pd.Series): Predicted target labels.
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

def save_analysis_results(data, file_path):
    """
    Save analyzed data to a CSV file.

    Args:
    - data (pd.DataFrame): DataFrame containing analyzed results.
    - file_path (str): Path to save the CSV file.
    """
    data.to_csv(file_path, index=False)
    print(f"Analyzed data saved to {file_path}")

def main():
    """
    Main function to execute the project workflow.
    """
    # Define file paths and directories
    processed_data_directory = 'data/processed/'
    analyzed_data_directory = 'data/analyzed/'
    files_to_analyze = ['creditcard.csv', 'creditcard_2023.csv']
    target_column = 'class'  # Assuming 'class' is the target column indicating fraud

    # Create the analyzed data directory if it doesn't exist
    create_directory(analyzed_data_directory)

    # Analyze each file
    for file in files_to_analyze:
        file_path = os.path.join(processed_data_directory, file)
        data = load_processed_data(file_path)

        if data is not None:
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = split_data(data, target_column)

            # Scale the data
            X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

            # Train a Random Forest model
            model = train_random_forest(X_train_scaled, y_train)

            # Evaluate the model
            y_test, y_pred = evaluate_model(model, X_test_scaled, y_test)

            # Plot confusion matrix
            plot_confusion_matrix(y_test, y_pred)

            # Save analyzed data and results
            save_path = os.path.join(analyzed_data_directory, file)
            analyzed_data = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
            save_analysis_results(analyzed_data, save_path)

if __name__ == "__main__":
    main()
