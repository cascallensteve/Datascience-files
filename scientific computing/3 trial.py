import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have a DataFrame 'data' with a column 'Attack'
# Sample data for illustration purposes
data = pd.DataFrame({
    'Attack': [5, 15, 25, 35, 45, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
})

# Creating the histogram
plt.figure(figsize=(10, 6))  # setting the figure size
n, bins, patches = plt.hist(data['Attack'], bins=15, alpha=0.7, color='blue', edgecolor='black')

# Adding labels and title
plt.xlabel('Attack')                  # label = name of label
plt.ylabel('Frequency')               # label = name of label
plt.title('Attack Histogram')         # title = name of the plot

# Adding grid lines
plt.grid(axis='y', alpha=0.75)

# Calculating and plotting mean and median lines
mean = data['Attack'].mean()
median = data['Attack'].median()

plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dotted', linewidth=1, label=f'Median: {median:.2f}')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
