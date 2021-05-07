# https://matplotlib.org/, Matploblib: Visualization with Python
import matplotlib.pyplot as plt
# https://numpy.org/, Numerical Computing Tools
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot