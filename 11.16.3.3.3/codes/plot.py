import numpy as np
import matplotlib.pyplot as plt

# Read the outcomes from the file
with open("outcomes.so", "r") as file:
    outcomes = [int(line.strip()) for line in file]

# Calculate probabilities
total_outcomes = len(outcomes)
probabilities = {
    ">=1": sum(1 for x in outcomes if x >= 1) / total_outcomes,
    "=1": outcomes.count(1) / total_outcomes,
    "=2": outcomes.count(2) / total_outcomes,
    "=3": outcomes.count(3) / total_outcomes,
    "=4": outcomes.count(4) / total_outcomes,
    "=5": outcomes.count(5) / total_outcomes,
    "=6": outcomes.count(6) / total_outcomes,
}

# Prepare data for the stem plot
categories = list(probabilities.keys())
values = list(probabilities.values())

# Plotting
plt.figure(figsize=(8, 5))
plt.stem(categories, values, basefmt=" ")
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

