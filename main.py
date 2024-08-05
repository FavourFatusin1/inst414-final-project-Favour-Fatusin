import logging
from etl.extract import extract_table
from etl.transform import transform
from etl.load import *
from analysis.model import model
from vis.visualization import scatterplot, d1, d2, boxplot

# Configure logging
logging.basicConfig(filename='data/outputs/pipeline.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    """
    try:
        logging.info("Starting the data pipeline workflow.")

        # Step 1: Extract data
        file_path1 = 'data/statistic1.csv'
        file_path2 = 'data/statistic2.csv'
        url1 = 'https://www.fool.com/the-ascent/research/identity-theft-credit-card-fraud-statistics/'
        url2 = 'https://www.bankrate.com/credit-cards/news/credit-card-fraud-statistics/#fraud'
        
        logging.info("Extracting data from URLs.")
        df1 = extract_table(url1, file_path1)
        df2 = extract_table(url2, file_path2)

        # Step 2: Transform data
        logging.info("Transforming data.")
        transform(df1, df2)

        # Step 3: Load data
        processed_file_path1 = 'data/outputs/transformed_statistic1.csv'
        processed_file_path2 = 'data/outputs/transformed_statistic2.csv'
        logging.info("Loading transformed data.")
        load(processed_file_path1, processed_file_path2)

        # Step 4: Build and train model
        logging.info("Building and training model.")
        model(processed_file_path1, processed_file_path2)

        # Step 5: Create visualizations
        logging.info("Creating visualizations.")
        scatterplot(processed_file_path1)
        d1(processed_file_path1)
        d2(processed_file_path2)
        boxplot(processed_file_path2)
        
        logging.info("Workflow executed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
