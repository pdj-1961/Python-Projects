import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
plt.plot(x, y)
plt.title("Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
