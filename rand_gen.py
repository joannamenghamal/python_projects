#! bin/usr/python3

import random

# Declare a one-dimensional array to store a 10 floating-point numbers

float_array = [0.0] * 10

# Populate the array with random floating-point numbers
for i in range(10):
    float_array[i] = random.uniform(-10.0, +10.0)

    print(float_array[i])