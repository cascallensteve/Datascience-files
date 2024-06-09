import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame 'data' with columns 'Attack' and 'Defense'
# Sample data for illustration purposes
data = pd.DataFrame({
    'Attack': [5, 15, 25, 35, 45, 55],
    'Defense': [3, 10, 20, 30, 40, 50]
})

# Creating the scatter plot
data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')

# Adding labels and title
plt.xlabel('Attack')               # label = name of label
plt.ylabel('Defense')              # label = name of label
plt.title('Attack Defense Scatter Plot')  # title = name of the plot

# Displaying the plot
plt.show()
