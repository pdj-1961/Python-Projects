from pathlib import PureWindowsPath
import pandas as pd

# This script reads a CSV file containing historical data for Apple Inc. (AAPL) stock
# and prints the first few rows of the DataFrame.

# Define the path to the CSV file using PureWindowsPath
AAPL_path = PureWindowsPath('c:/', 'Users', 'PdJ-1', 'Documents', 'GitHub', 'Python-Projects', 'HistoricalDataAAPL.csv')

# Read the CSV file into a DataFrame
APPL = pd.read_csv(AAPL_path)

# Display the first few rows of the DataFrame
print(APPL.head())
