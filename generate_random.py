# generate random numbers
import numpy as np

arr = np.random.randint(0, 10, 5)

print(arr)

# generate random numbers from a normal distribution

arr = np.random.randn(5)

print(arr)

# generate random numbers from a uniform distribution   
arr = np.random.uniform(0, 1, 5)

print(arr)

# generate random numbers from a binomial distribution
arr = np.random.binomial(10, 0.5, 5)

print(arr)

# generate random numbers from a poisson distribution
arr = np.random.poisson(5, 5)           

print(arr)

# generate random numbers from a exponential distribution
arr = np.random.exponential(1, 5)

print(arr)

# generate random numbers from a chi-square distribution
arr = np.random.chisquare(2, 5)

print(arr)