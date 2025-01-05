import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
points_lib = ctypes.CDLL('./points.so')

# Define the Point structure (ensure it matches the C structure)
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

# Define the get_points function from the shared object
points_lib.get_points.argtypes = [ctypes.POINTER(ctypes.c_int)]
points_lib.get_points.restype = ctypes.POINTER(Point)

def get_points():
    size = ctypes.c_int(0)  # Variable to hold the size of the points array
    points = points_lib.get_points(ctypes.byref(size))
    
    # Ensure the returned points array is not NULL
    if not points:
        raise Exception("Failed to retrieve points from shared object.")
    
    point_list = []

    # Extract points from the returned pointer
    for i in range(size.value):
        point_list.append((points[i].x, points[i].y))
    
    return point_list

# Define the function y = 2 * tan(x/2) - x
def f(x):
    return 2 * np.tan(x / 2) - x

# Generate an array of x values from -10 to 10 (or any desired range)
x = np.linspace(-15, 15, 1500)

# Compute the corresponding y values using the function f(x)
y = f(x)

# Retrieve the points from the shared object
points = get_points()

# Unzip the list of points into x and y coordinates
x_vals, y_vals = zip(*points)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the first graph (from points.so) in blue
plt.scatter(x_vals, y_vals, color='blue', s=1, label=r'Sim')

# Plot the second graph (y = 2 * tan(x/2) - x) in red
plt.plot(x, y, color='red', label=r'Theory', linewidth=2)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')

# Set limits for the y-axis to make the graph clearer
plt.ylim(-20, 20)

# Add a grid
plt.grid(True)

# Display the legend
plt.legend()

# Show the plot
plt.show()

