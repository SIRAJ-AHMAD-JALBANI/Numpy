# normal distribution 
import numpy as np
import matplotlib.pyplot as plt

# mean and standard deviation
mu = 0       # center of the distribution
sigma = 1    # spread (standard deviation)

# generate 1000 random numbers from a normal distribution
data = np.random.normal(mu, sigma, 1000)

# plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
plt.title("Normal Distribution (mu=0, sigma=1)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()