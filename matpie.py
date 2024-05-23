import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.title("Population distribution of kenya" ,loc="right")

mylabels=["apple","dates","pineapple","avacado"]

plt.pie(y,labels=mylabels,startangle=90)

plt.show()
