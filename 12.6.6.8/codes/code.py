import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
max_lib = ctypes.CDLL('./max.so')

# Call the `get_last_point` function
max_lib.get_last_point.restype = ctypes.c_double
last_point = max_lib.get_last_point()

# Parameters for the function f(x)
ab = 20

# Define f(x)
def f(x):
    return ab * np.sin(x) * (1 - np.cos(x))

# Generate x values for the plot
x_vals = np.linspace(0, 2 * np.pi, 500)
y_vals = f(x_vals)

# Plot the function and the last point
plt.plot(x_vals, y_vals, label=r'$f(x) = ab \sin{x} (1 - \cos{x})$')
plt.scatter([last_point], [f(last_point)], color='red', label=f'Max Point: x={last_point:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

