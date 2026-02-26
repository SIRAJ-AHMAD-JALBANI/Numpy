from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate samples
binomial = random.binomial(n=1000, p=0.01, size=1000)
poisson = random.poisson(lam=10, size=1000)

sns.kdeplot(binomial, fill=True, label="binomial")
sns.kdeplot(poisson, fill=True, label="poisson")
plt.legend()
plt.show()