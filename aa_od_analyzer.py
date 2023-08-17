"""
AA_OD_Analyzer (Amino Acid, Optical Density Analyzer)

Author: Babak Mahdavi Ardestani
Email: babak.m.ardestani@gmail.com

Description:
This script is used for analyzing optical density data associated with amino acid sequences. 
It reads input data from a CSV file, generates a histogram of optical densities, calculates 
statistics for each unique amino acid sequence, and writes the statistics to a CSV file. 
The script provides options for enabling logging to keep track of its operations.

Dependencies:
- Python 3.x
- pandas
- matplotlib

Usage:
python3 aa_od_analyzer.py [--log]

Optional Arguments:
--log       Enable logging to display detailed information during execution.
"""


import pandas as pd
import matplotlib.pyplot as plt
import logging
import argparse

# Configure argument parser
parser = argparse.ArgumentParser(description='Script with logging options')
parser.add_argument('--log', action='store_true', help='Enable logging')

args = parser.parse_args()

# Configure logging if --log argument is provided
if args.log:
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname)s] %(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[
                            logging.StreamHandler(),  # Log to console
                            logging.FileHandler('logfile.log')  # Log to file
                        ])
else:
    logging.basicConfig(level=logging.CRITICAL)  # Disables logging

def read_input_csv(file_path):
    """
    Read input CSV file and parse the data into a Pandas DataFrame.

    :param file_path: Path to the input CSV file.
    :return: DataFrame containing the parsed data.
    """
    try:
        logging.info(f"Reading input CSV file: {file_path}")
        # Read the CSV file and parse the data into a Pandas DataFrame
        df = pd.read_csv(file_path)
        logging.debug(f"Data loaded from the CSV file:\n{df.head()}")
        return df
    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        logging.error(f"File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        logging.error(f"Unable to parse file '{file_path}'. Please check the file format.")
        return None

    print(df.head())  # Print the first few rows of the DataFrame for debugging

def generate_histogram(df):
    """
    Generate a histogram plot of optical densities.

    :param df: DataFrame containing the data.
    """
    try:
        logging.info("Generating histogram...")
        # Create a histogram plot of optical densities
        plt.hist(df['optical_density'], bins=10)  # You can adjust the number of bins as needed
        plt.xlabel('Optical Density')
        plt.ylabel('Frequency')
        plt.title('Histogram of Optical Densities')
        plt.savefig('output_histogram.png')
        plt.close()
        logging.info("Histogram saved as 'output_histogram.png'")
    except KeyError:
        logging.error("'optical_density' column not found in the input data.")

def calculate_amino_acid_stats(df):
    """
    Calculate statistics for amino acid sequences.

    :param df: DataFrame containing the data.
    :return: DataFrame with calculated statistics.
    """
    try:
        logging.info("Calculating amino acid statistics...")
        # Group the data by amino acid sequences and calculate statistics
        grouped_df = df.groupby('amino_acid_sequence')
        stats_df = grouped_df['optical_density'].agg(['mean', 'max', 'min']).round(1)
        stats_df.reset_index(inplace=True)  # Reset the index to get 'amino_acid_sequence' as a column
        stats_df.columns = ['amino_acid_sequence', 'mean_optical_density', 'max_optical_density', 'min_optical_density']
        logging.debug(f"Statistics DataFrame:\n{stats_df}")
        return stats_df
    except KeyError:
        logging.error("'amino_acid_sequence' column not found in the input data.")
        return None

def write_output_csv(stats_df):
    """
    Write calculated statistics to a CSV file.

    :param stats_df: DataFrame with calculated statistics.
    """
    if stats_df is not None:
        logging.info("Writing statistics to CSV...")
        # Write the statistics DataFrame to a CSV file with the desired column order and names
        stats_df.to_csv('output_data_stats.csv', index=False)
        logging.info("Statistics written to 'output_data_stats.csv'")
    else:
        logging.warning("Unable to write output due to missing data.")


if __name__ == "__main__":

    # TODO the location of the input data should not be ideally hard-coded (change to pass it as an argument, ...)
    input_file_path = './example_data/input_data.csv'
    
    # Input parsing
    input_df = read_input_csv(input_file_path)
    if input_df is None:
        exit(1)  # Exit the script if there was an error reading the input data.

    # Data analysis
    generate_histogram(input_df)
    stats_df = calculate_amino_acid_stats(input_df)
    if stats_df is None:
        exit(1)  # Exit the script if there was an error calculating statistics.

    # Output generation
    write_output_csv(stats_df)
