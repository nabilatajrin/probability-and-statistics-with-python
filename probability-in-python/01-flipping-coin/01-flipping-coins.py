# Import the bernoulli object from scipy.stats
from scipy.stats import bernoulli

# Set the random seed to reproduce the results
np.random.seed(42)

# Simulate one coin flip with 35% chance of getting heads
coin_flip = bernoulli.rvs(p=0.35, size=1)
print(coin_flip)

# Simulate ten coin flips and get the number of heads
ten_coin_flips = bernoulli.rvs(p=0.5, size=5)
coin_flips_sum = sum(ten_coin_flips)
print(coin_flips_sum)
