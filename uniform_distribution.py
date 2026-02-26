
import numpy as np
import matplotlib.pyplot as plt

# Default: low=0.0, high=1.0
default = np.random.uniform(size=5)
print("Default (0 to 1), size=5:", default)

# Custom bounds
low, high = 10, 20
samples = np.random.uniform(low=low, high=high, size=1000)
print(f"\nUniform between {low} and {high}, size=1000")
print("First 5:", samples[:5])

# size as shape: 2D array
matrix = np.random.uniform(low=0, high=1, size=(3, 4))
print("\nShape (3, 4):\n", matrix)

# Histogram
plt.hist(samples, bins=30, density=True, alpha=0.7, color="steelblue", edgecolor="black")
plt.title(f"Uniform Distribution (low={low}, high={high})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
