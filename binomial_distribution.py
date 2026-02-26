# Binomial Distribution
import numpy as np
import matplotlib.pyplot as plt

# Parameters for Binomial distribution
n = 10       # number of trials
p = 0.5      # probability of success in each trial
size = 1000  # how many random samples to generate

# Generate random numbers from a Binomial distribution
data = np.random.binomial(n=n, p=p, size=size)

# Plot histogram
plt.hist(data, bins=range(n + 2), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("Number of successes")
plt.ylabel("Frequency")
plt.xticks(range(n + 1))
plt.show()