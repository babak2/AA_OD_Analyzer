"""
AA_OD_Analyzer Unit Tests

Author: Babak Mahdavi Ardestani
Email: babak.m.ardestani@gmail.com

Description:
This script contains unit tests for the AA_OD_Analyzer (Amino Acid, Optical Density Analyzer) script.
The unit tests ensure that the functions in the 'aa_od_analyzer.py' script are working as expected.

"""

import sys
import os

# Get the absolute path of the current script and its directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Get the project root directory by going one level up from the script directory
project_root = os.path.dirname(script_dir)

# Add the project root directory to sys.path
sys.path.append(project_root)

import unittest
import pandas as pd
import aa_od_analyzer


class Test_AA_OD_Analyzer(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.sample_data = {
            'index': ['A01', 'A02', 'A03', 'A04'],
            'optical_density': [0.8, 1.3, 1.3, 0.9],
            'amino_acid_sequence': ['GFTFSSYF', 'GFTFSNYA', 'GFTFSSYW', 'GFPFEMYD']
        }

        # Convert sample data to DataFrame
        self.sample_df = pd.DataFrame(self.sample_data)

    def test_read_input_csv(self):
        # Test if input CSV is read correctly

        # TODO the location of the input data should not be ideally hard-coded (change to pass it as an argument, ...)
        df = aa_od_analyzer.read_input_csv('../example_data/input_data.csv')

        #print(df.head())  # Print the first few rows of the DataFrame for debugging

        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_generate_histogram(self):
        # Test histogram generation
        aa_od_analyzer.generate_histogram(self.sample_df)

        # Add assertions to check if the histogram was generated correctly (e.g., check the saved file)

    def test_calculate_amino_acid_stats(self):
        # Test amino acid statistics calculation
        stats_df = aa_od_analyzer.calculate_amino_acid_stats(self.sample_df)
        self.assertIsNotNone(stats_df)
        self.assertIsInstance(stats_df, pd.DataFrame)

    def test_write_output_csv(self):
        # Test writing statistics to CSV
        stats_df = aa_od_analyzer.calculate_amino_acid_stats(self.sample_df)
        aa_od_analyzer.write_output_csv(stats_df)

        # Add assertions to check if the output CSV file was created and contains the expected data

if __name__ == '__main__':
    unittest.main()
