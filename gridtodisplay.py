#Three lines to make our compiler able to draw:
import sys
import matplotlib
# matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])


plt.title("Movers transport system", loc='left')
plt.xlabel("Numbers of trials")
plt.ylabel("Days gone")

plt.plot(y1)
plt.plot(y2,color='g' ,ls='dotted')

plt.grid(axis='x', color='g',ls='dotted', linewidth='5.4')

plt.show()

#Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()