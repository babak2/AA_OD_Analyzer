# AA_OD_Analyzer

AA_OD_Analyzer (Amino Acid, Optical Density Analyzer) is a Python program for analyzing optical density (OD) data and amino acid sequences. It calculates statistics on the OD values and performs analysis on amino acid sequences to generate valuable insights for biological research.

The AA_OD_Analyzer program takes an input CSV file containing optical density and amino acid sequence data. It performs the following tasks:

- Reads the input CSV file and parses the data into a Pandas DataFrame.
- Generates a histogram of optical density values and saves it as 'output_histogram.png'.
- Calculates statistics on amino acid sequences, including mean, maximum, and minimum optical density values.
- Writes the amino acid sequence statistics to a CSV file named 'output_data_stats.csv'.

This tool is designed to be flexible, allowing users to enable or disable logging based on their preferences.


## Installation

Clone the repository to your local machine:

`git clone https://github.com/babak2/AA_OD_Analyzer.git  `

or if you have the program as a ZIP file, simply extract the zip file to a directory of your choice.

Change your working directory to AA_OD_Analyzer:

`cd AA_OD_Analyzer`


## Program Requirements

You need Python 3 installed 

Moreover, install the required dependencies using pip:

`pip install pandas matplotlib argparse`


## Input File Format

The input file should have the following format:

Input Data Format:

The input data should be provided in a CSV file with the following columns:
- optical_density: The optical density values for each amino acid sequence.
- amino_acid_sequence: The amino acid sequences being analyzed.


### Input Data Format

The input data should be provided in a CSV file with the following columns:

| index | optical_density | amino_acid_sequence |
|-------|-----------------|--------------------|
| A01   | 0.8             | GFTFSSYF           |
| A02   | 1.3             | GFTFSNYA           |
| A03   | 1.3             | GFTFSSYW           |
| A04   | 0.9             | GFPFEMYD           |
| ...   | ...             | ...                |


An example is located in the `example_data` directory.

## Output Format

Output Files:
- output_histogram.png: A histogram plot of optical densities.
- output_data_stats.csv: A CSV file containing statistics for each amino acid sequence.

An example is located in the `example_data` directory.


## Usage

To use AA_OD_Analyzer, run the aa_od_analyzer.py.py script with the following command:

`python3 aa_od_analyzer.py [--log]`

Example usage:

`python3 aa_od_analyzer.py`

## Command Line Arguments

AA_OD_Analyzer supports the following command-line arguments

`--log`     
: Enables logging, displaying information messages to the console and writing them to the 'logfile.log' file.

Example usage:

`python3 aa_od_analyzer.py --log`

## Unit Tests

Unit tests ensure the correctness and reliability of the AA_OD_Analyzer program. To run the unit tests, you need to be in the `tests` directory (currently the location of the input file is hard-coded which needs to change later, to pass as an argument, for example): 

`cd tests`

and then use the test_aa_od_analyzer.py script:

`python3 test_aa_od_analyzer.py`

The unit tests cover various scenarios, including file reading, data analysis, and output generation.


## Security Considerations

AA_OD_Analyzer is designed with security in mind, especially when handling sensitive data. It uses Python's standard logging library to log important events, warnings, and errors. By default, logging is disabled, but users can enable it using the --log command-line argument.

When working with sensitive data, make sure to follow best practices for data handling, storage, and access control. Avoid sharing sensitive data through insecure channels and implement appropriate security measures to protect against unauthorized access.


## License

AA_OD_Analyzer is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE for more information.


## Author 

Babak Mahdavi Aresetani

babak.m.ardestani@gmail.com
