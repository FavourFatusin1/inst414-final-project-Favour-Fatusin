import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from io import StringIO

# Directory to save the raw data
output_dir = 'data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_table(url, file_name, table_index=0):
    # Send a GET request to the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.text
    else:
        raise Exception(f"Failed to retrieve the page from {url}. Status code: {response.status_code}")

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all tables
    tables = soup.find_all('table')

    # Ensure we have the right number of tables
    if len(tables) <= table_index:
        raise Exception(f"Table index {table_index} is out of range for the page {url}.")

    # Convert the chosen table to a DataFrame
    table_html = str(tables[table_index])
    df = pd.read_html(StringIO(table_html))[0]

    # Define the file path
    file_path = os.path.join(output_dir, file_name)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    print(f"Data successfully extracted and saved to {file_path}")

# Define sources with their specific table indices
sources = [
    {
        'url': 'https://www.fool.com/the-ascent/research/identity-theft-credit-card-fraud-statistics/',
        'file_name': 'statistic1.csv',
        'table_index': 0  # Adjust this index if the table you need is not the first one
    },
    {
        'url': 'https://www.bankrate.com/credit-cards/news/credit-card-fraud-statistics/#fraud',
        'file_name': 'statistic2.csv',
        'table_index': 0  # Adjust this index if the table you need is not the first one
    }
]

# Extract and save tables
for source in sources:
    extract_table(source['url'], source['file_name'], source['table_index'])
