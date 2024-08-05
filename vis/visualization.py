import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file paths
transformed_file_path1 = 'data/outputs/transformed_statistic1.csv'
transformed_file_path2 = 'data/outputs/transformed_statistic2.csv'

# Load the transformed data into DataFrames
df1 = pd.read_csv(transformed_file_path1)
df2 = pd.read_csv(transformed_file_path2)

# Ensure the 'outputs' directory for plots exists
os.makedirs('data/outputs/plots', exist_ok=True)

def d1(data):
        # Distribution 1
    plt.figure(figsize=(10, 6))
    sns.histplot(df1['identity_theft_reports'], kde=True)
    plt.title('Distribution of Identity Theft Reports in Statistic1')
    plt.xlabel('Identity Theft Reports')
    plt.ylabel('Frequency')
    plt.savefig('data/outputs/df1_distribution.png')
    plt.show()  # Display the plot
    plt.close()

#boxplot
def boxplot(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='year', y='identity_theft_reports', data=df1)
    plt.title('Boxplot of Identity Theft Reports by Year in Statistic1')
    plt.xlabel('Year')
    plt.ylabel('Identity Theft Reports')
    plt.savefig('data/outputs/df1_boxplot.png')
    plt.show()  # Display the plot
    plt.close()

# Distribution 2
def d2(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(df2['amount_(in_billions)'], kde=True)
    plt.title('Distribution of Amount (in Billions) in Statistic2')
    plt.xlabel('Amount (in Billions)')
    plt.ylabel('Frequency')
    plt.savefig('data/outputs/df2_distribution.png')
    plt.show()  # Display the plot
    plt.close()

#scatterplot
def scatterplot(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='year', y='amount_(in_billions)', data=df2)
    plt.title('Scatter Plot of Amount (in Billions) vs. Year in Statistic2')
    plt.xlabel('Year')
    plt.ylabel('Amount (in Billions)')
    plt.savefig('data/outputs/df2_scatter.png')
    plt.show()  # Display the plot
    plt.close()

print("\nVisualizations successfully created and saved in 'data/outputs/plots'")
