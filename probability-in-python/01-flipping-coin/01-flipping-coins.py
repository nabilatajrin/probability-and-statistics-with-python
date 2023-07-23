# Import the bernoulli object from scipy.stats
from scipy.stats import bernoulli

# Set the random seed to reproduce the results
np.random.seed(42)

# Simulate one coin flip with 35% chance of getting heads
coin_flip = bernoulli.rvs(p=0.35, size=1)
print(coin_flip)
