import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame 'data' with columns 'Speed' and 'Defense'
# Sample data for illustration purposes
data = pd.DataFrame({
    'Speed': [5, 15, 25, 35, 45, 55],
    'Defense': [3, 10, 20, 30, 40, 50]
})

# Creating the line plot
data['Speed'].plot(kind='line', color='g', label='Speed', linewidth=1, alpha=0.5, grid=True, linestyle=':')
data['Defense'].plot(color='r', label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')

# Adding legend, labels, and displaying the plot
plt.legend(loc='upper right')  # legend = puts label into plot
plt.xlabel('x axis')           # label = name of label
plt.ylabel('y axis')           # label = name of label
plt.show()
