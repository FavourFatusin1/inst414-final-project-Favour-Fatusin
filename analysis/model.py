import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Define file paths
transformed_file_path1 = 'data/outputs/transformed_statistic1.csv'
transformed_file_path2 = 'data/outputs/transformed_statistic2.csv'

# Load the transformed data into DataFrames
df1 = pd.read_csv(transformed_file_path1)
df2 = pd.read_csv(transformed_file_path2)

# Merge dataframes on 'Year'
merged_df = pd.merge(df1, df2, on='year', how='outer')

# Drop rows with missing values in columns used for regression
merged_df = merged_df.dropna(subset=['amount_(in_billions)', 'identity_theft_reports'])

# Convert 'Amount (In billions)' to numeric if not already
merged_df['amount_(in_billions)'] = pd.to_numeric(merged_df['amount_(in_billions)'], errors='coerce')

# Basic Descriptive Analysis
print("\nDescriptive Analysis:")
print(merged_df.describe())

# Prepare data for regression
X = merged_df[['amount_(in_billions)']]
y = merged_df['identity_theft_reports']

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nLinear Regression Model Evaluation:")
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Save analysis results
analysis_dir = 'data/outputs/analysis_results'
if not os.path.exists(analysis_dir):
    os.makedirs(analysis_dir)

# Save merged data
merged_file_path = os.path.join(analysis_dir, 'merged_statistic_data.csv')
merged_df.to_csv(merged_file_path, index=False)

# Plotting results
plt.figure(figsize=(12, 6))
sns.lineplot(data=merged_df, x='year', y='identity_theft_reports', label='Identity Theft Reports')
sns.lineplot(data=merged_df, x='year', y='amount_(in_billions)', label='Amount (In billions)', color='red')
plt.title('Identity Theft Reports vs. Amount (In billions)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.savefig(os.path.join(analysis_dir, 'analysis_plot.png'))
plt.show()
plt.close()

print(f"\nAnalysis plot saved to '{os.path.join(analysis_dir, 'analysis_plot.png')}'")
(SEPERATE INTO EVALUATE SCRIPT AND MODEL SCIRPT)
