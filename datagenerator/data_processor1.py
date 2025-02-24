#! usr/bin/python3

import data_loader
import random
import pandas as pd
import numpy as np


# Load data from Q1.csv and Q2_x2.csv
data_Q1 = data_loader.load_csv("Q1.csv")
data_Q2 = data_loader.load_csv("Q2_x2.csv")

# Check for missing 'y' values and print the items
for i, item in enumerate(data_Q1):
    if "y" not in item:
        print(f"Item at index {i} is missing 'y':", item)


# Calculate Mean and Standard Deviation for Q1.csv
y_values = [float(item["y"]) for item in data_Q1 if "y" in item] 
x_values = [float(item["x"]) for item in data_Q1]
mean_y = sum(y_values) / len(y_values)
mean_x = sum(x_values) / len(x_values)
std_y = (sum([(y - mean_y) ** 2 for y in y_values]) / len(y_values)) ** 0.5
std_x = (sum([(x - mean_x) ** 2 for x in x_values]) / len(x_values)) ** 0.5
print(f"Mean of 'y': {mean_y}")
print(f"Standard Deviation of 'y': {std_y}")
print(f"Mean of 'x': {mean_x}")
print(f"Standard Deviation of 'x': {std_x}")



# Identify and print values greater than two standard deviations
# or less than two standard deviations from the mean to show outliers
outliers_y = [item for item in data_Q1 if abs(float(item["y"]) - mean_y) > 2 * std_y]
outliers_x = [item for item in data_Q1 if abs(float(item["x"]) - mean_x) > 2 * std_x]

# Removes outliers and normalizes the data so values fall within range
# [-1, 1] and the mean is adjusted to 0


normalized_data = []
for item in data_Q1:
    # values need to fall within [-1, 1] and the mean adjusted to 0
    if item not in outliers_y and item not in outliers_x:
        normalized_data.append({"y": (float(item["y"]) - mean_y) / std_y, "x": (float(item["x"]) - mean_x) / std_x})

normalized_data = []
normalized_x =[]
normalized_y = []
for item in data_Q1:
    try:
        x_val = float(item.get("x", 0))  # Default to 0 if key is missing
        y_val = float(item.get("y", 0))

        if std_x == 0 or std_y == 0:
            raise ValueError("Standard deviation cannot be zero")

        normalized_data.append({
            "x": (x_val - mean_x) / std_x,
            "y": (y_val - mean_y) / std_y
        })
        #Emsure that the values are within the range [-1, 1]
        normalized_x = max(min(normalized_x, 1), -1)
        normalized_y = max(min(normalized_y, 1), -1)

        normalized_data.append({
            "x": normalized_x,
            "y": normalized_y
        })
    except (ValueError, TypeError) as e:
        print(f"Skipping item due to error: {e}")


# Display 10 randomly selected values from the array to ensure all
# values are within the range [-1, 1]
random_data = random.sample(normalized_data, 10)
for item in random_data:
    print(item)

# Convert the list of dictionaries to a 2-dimensional list
normalized_data_2d = [[item["y"], item["x"]] for item in normalized_data]

# Loads the normalized data into Panda's DataFrame and NumPy's array
# and display 10 randomly selected values from each Pandas DataFrame
# and NumPy array
df = pd.DataFrame(normalized_data_2d, columns=["y", "x"])
np_array = np.array(normalized_data_2d)
random_df = df.sample(10)
random_np_array = np_array[np.random.choice(np_array.shape[0], 10, replace=False)]

#Splits the data stored in NumPy arrays into 𝑥𝑥 and 𝑦𝑦 values, saving them into two separate
#arrays: “X_data” and “Y_data”.
X_data = np_array[:, 1] # Extracts all x values
Y_data = np_array[:, 0] # Extracts all y values


print(random_df)


