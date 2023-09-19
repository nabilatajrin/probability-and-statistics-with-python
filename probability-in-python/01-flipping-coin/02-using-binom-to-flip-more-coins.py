# Import the bernoulli object from scipy.stats
from scipy.stats import bernoulli

# Simulate 20 trials of 10 coin flips 
draws = binom.rvs(p=0.35, size=20, n=10)
print(draws)
