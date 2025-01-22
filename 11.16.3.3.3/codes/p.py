import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./c1.so')

# Create an array to hold PMF values (7 elements for outcomes 1, 2, 3, 4, 5, 6, >= 1)
pmf = (ctypes.c_double * 7)()

# Call the C function to calculate PMF
lib.get_probabilities(pmf)

# Convert the PMF to a Python list
pmf_values = [pmf[i] for i in range(7)]

# Plotting the PMF
x = [1, 2, 3, 4, 5, 6, 7]  # Numeric values for the x-axis
labels = ['1', '2', '3', '4', '5', '6', '>=1']  # Custom labels for the x-axis

plt.stem(x, pmf_values)
plt.xlabel('Outcome')
plt.ylabel('Probability')

# Customize the x-axis labels to show '>=1'
plt.xticks(x, labels)

plt.show()

