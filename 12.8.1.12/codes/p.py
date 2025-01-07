import numpy as np
import matplotlib.pyplot as plt

# Define the circle function
def circle_function(x):
    return np.sqrt(4 - x**2)

# Define the range for x (first quadrant, x = 0 to x = 2)
x = np.linspace(0, 2, 1000)
y = circle_function(x)

# Plot the intersected area
plt.figure(figsize=(8, 8))
plt.fill_between(x, 0, y, color="skyblue", alpha=0.5, label="Intersected Area")

# Plot the boundary lines and the circle curve
plt.plot(x, y, color="blue", label="Circle: $x^2 + y^2 = 4$")
plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis
plt.axvline(2, color="red", linestyle="--", label="x = 2")  # Line x=2

# Add labels and legend
plt.title("Intersected Area Bounded by the Circle and Lines", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()

# Show the plot
plt.show()

