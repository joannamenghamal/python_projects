#! bin/usr/python3

import csv
import json
import random


# Declare a two-dimensional array to store 100,000,000 pairs of floating-point numbers (y, x)
float_array = [[0.0, 0.0]] * 100000
data_L1 = []

# Randomly generates x values in the range of [-1000.0, +1000.0] and
# computes the corresponding y values using the formula y = 2.0 + 0.5x
for i in range(100000):
    float_array[i][1] = random.uniform(-1000.0, +1000.0)
    float_array[i][0] = 2.0 + 0.5 * float_array[i][1]

# Converts the two-dimensional array to a list of dictionaries
# with the keys and pair as values
for i in range(100000):
    data_L1.append({"y": float_array[i][0], "x": float_array[i][1]})

# Writes/Saves the data to a JSON file
with open("L1.json", "w") as json_file:
    json.dump(data_L1, json_file)

# Populates the array with the generated pairs and display the first
# middle, and last pairs (records)


# Writes/Saves the data to a CSV file
with open("L1.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["y", "x"])
    writer.writeheader()
    writer.writerows(data_L1)

# Declare a two-dimensional array to store 100,000,000 real value pairs 
# (y, x) within range [-1000.0, +1000.0] and y-values are computed 
# using equation y = 2.0 + 0.5x -3x^2
data_L2 = []
float_array_2 = [[0.0, 0.0]] * 100000

# Randomly generates x values in the range of [-1000.0, +1000.0]
# and computes the corresponding y values using the formula y = 2.0 + 0.5x - 3x^2
for i in range(100000):
    float_array_2[i][1] = random.uniform(-1000.0, +1000.0)
    float_array_2[i][0] = 2.0 + 0.5 * float_array_2[i][1] - 3 * float_array_2[i][1] ** 2

# Converts the two-dimensional array to a list of dictionaries
for i in range(100000):
    data_L2.append({"y": float_array_2[i][0], "x": float_array_2[i][1], "x^2": float_array_2[i][1] ** 2})

# Create a separate list for Q1.csv with only "y" and "x" keys
data_L2_q1 = [{"y": item["y"], "x": item["x"]} for item in data_L2]

# Writes/Saves data into two CSV files (Q1.csv and Q2_x2.csv)
with open("Q1.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["y", "x"])
    writer.writeheader()
    writer.writerows(data_L2_q1)

with open("Q2_x2.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["y", "x", "x^2"])
    writer.writeheader()
    writer.writerows(data_L2)





