# -*- coding: utf-8 -*-
"""SPC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h5iD4_De96Kvs6N3O5qH57QpW0Tfb4qV
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
    # Generating n random data points
    return np.random.normal(loc=10, scale=2, size=n)

def calculate_control_limits(data, sigma=3):
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)

    # Control limits
    ucl = mean + sigma * std_dev
    lcl = mean - sigma * std_dev

    return ucl, lcl

def plot_spc(data, ucl, lcl):
    # Plot the control chart
    plt.figure(figsize=(10, 6))
    plt.plot(data, 'bo-', label='Data')
    plt.axhline(ucl, color='r', linestyle='--', label='UCL')
    plt.axhline(lcl, color='r', linestyle='--', label='LCL')
    plt.axhline(np.mean(data), color='g', linestyle='-', label='Mean')
    plt.xlabel('Sample Number')
    plt.ylabel('Value')
    plt.title('SPC Chart')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Number of data points
    n = 20

    # Generate random data
    data = generate_data(n)

    # Control limits calculation (3 sigma limits)
    ucl, lcl = calculate_control_limits(data, sigma=3)

    # Plot the SPC chart
    plot_spc(data, ucl, lcl)

if __name__ == "__main__":
    main()