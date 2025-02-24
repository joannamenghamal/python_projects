#! usr/bin/python3

import data_loader
import random
import pandas as pd
import numpy as np
import time

# Loads the x values from L1.csv and Q1.csv into two Python arrays
L1_data = data_loader.load_csv("L1.csv")
Q1_data = data_loader.load_csv("Q1.csv")
x_values_L1 = [float(item["x"]) for item in L1_data]
x_values_Q1 = [float(item["x"]) for item in Q1_data]

# Performs element-wise multiplication between the x-valuse from both arrays and displays the sum of all products L1 and Q1 and time taken to complete the operation
start_time = time.time()
dot_product = sum([x * y for x, y in zip(x_values_L1, x_values_Q1)])
end_time = time.time()
print(f"Dot product of L1 and Q1: {dot_product}")
print(f"Time taken: {end_time - start_time} seconds")

# Loads the data into Numpy arrays and performs the dot product operation using Numpy and displays the result and time taken as vectors
np_array_L1 = np.dot(np.array(x_values_L1), np.array(x_values_Q1))
start_time = time.time()
np_array = np.dot(np.array(x_values_L1), np.array(x_values_Q1))
end_time = time.time()
print(f"Dot product of L1 and Q1 (Numpy): {np_array}")
print(f"Time taken: {end_time - start_time} seconds")

# Loads data from Q2.csv into both Python arrays and NumPy arrays then compute sqaure of the arrays (like matrix multiplicatiion A^2)
Q2_data = data_loader.load_csv("Q2_x2.csv")
x_values_Q2 = [float(item["x"]) for item in Q2_data]
np_array_Q2 = np.array(x_values_Q2)
square_Q2 = np.dot(np_array_Q2, np_array_Q2)
print(f"Square of Q2: {square_Q2}")
start_time = time.time()
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")


