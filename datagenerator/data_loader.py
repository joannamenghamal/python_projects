#! bin/usr/python3

import json
import csv

jsonfile = "L1.json"
csvfile_L1 = "L1.csv"
csvfile_Q1 = "Q1.csv"
csvfile_Q2 = "Q2_x2.csv"

# Function to load data JSON data
def load_json(jsonfile):
    with open(jsonfile, "r") as json_file:
        data = json.load(json_file)
    return data

# Print confirmation message
print("JSON data loaded successfully")

# Function to load data from CSV file
def load_csv(csvfile):
    with open(csvfile, "r") as csv_file:
        data = csv.DictReader(csv_file)
        data = [row for row in data]
    return data



# Print confirmation message
print("CSV data loaded successfully")

# Define functions to load data from JSON and CSV files
if __name__ == "__main__":
    # Load data from JSON file
    json_data = load_json(jsonfile)
    # Load data from CSV file
    csv_data = load_csv(csvfile_L1)
    csv_data = load_csv(csvfile_Q1)
    csv_data = load_csv(csvfile_Q2)
  
    