import numpy as np
import matplotlib.pyplot as plt

# Function to plot y(n) = (c1 + 1/2) * delta(n) + (2*c1 + 1) * y(n-1)
def compute_y_n(c1, n_max):
    y_values = np.zeros(n_max)
    for n in range(1, n_max):
        y_values[n] = (2 * c1 + 1) * y_values[n - 1] + (c1 + 1 / 2) * (1 if n == 0 else 0)
    return y_values

# Function to plot y(x) = (c1 + 1/2) * e^x - (1/2) * cos(x) + (1/2) * sin(x)
def compute_yx(c1, x_values):
    return (c1 + 1/2) * np.exp(x_values) - (1/2) * np.cos(x_values) + (1/2) * np.sin(x_values)

# Function to compute y_{n+1} = (y_n * (1 + h / 2) + (h / 2) * (cos(x_n) + cos(x_{n+1}))) / (1 - h / 2)
def compute_recursive_eq(h, y_0, n_max, x_values):
    y_values = np.zeros(n_max)
    y_values[0] = y_0  # Initial condition

    for n in range(1, n_max):
        x_n = x_values[n - 1]
        x_n1 = x_values[n]
        y_values[n] = (y_values[n - 1] * (1 + h / 2) + (h / 2) * (np.cos(x_n) + np.cos(x_n1))) / (1 - h / 2)
    
    return y_values

# Parameters
c1 = 1  # Example value for c1
h = 0.1  # Step size for recursive equation
y_0 = 1  # Initial value for y_0
n_max = 50  # Number of steps for the recursive computation
x_values = np.linspace(0, 10, n_max)  # x values for the equations

# Compute all values for plotting
y_n_values = compute_y_n(c1, n_max)
y_x_values = compute_yx(c1, x_values)
y_recursive_values = compute_recursive_eq(h, y_0, n_max, x_values)

# Plot all three equations in one figure
plt.figure(figsize=(10, 6))

# Plot y(n) for the first equation
plt.plot(np.arange(n_max), y_n_values, label=r'$y(n) = (c_1 + \frac{1}{2})\delta(n) + (2c_1 + 1) y(n-1)$', color='blue')

# Plot y(x) for the second equation
plt.plot(x_values, y_x_values, label=r'$y(x) = (c_1 + \frac{1}{2})e^x - \frac{1}{2}\cos(x) + \frac{1}{2}\sin(x)$', color='green')

# Plot y_{n+1} for the third equation
plt.plot(x_values, y_recursive_values, label=r'$y_{n+1} = \frac{y_n \left(1 + \frac{h}{2}\right) + \frac{h}{2} (\cos x_n + \cos x_{n+1})}{1 - \frac{h}{2}}$', color='red')

# Labels and title
plt.xlabel('n or x')
plt.ylabel('y')
plt.title('Combined Plot of y(n), y(x), and Recursive y_{n+1}')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

