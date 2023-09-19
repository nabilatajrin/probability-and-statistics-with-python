# Set the random seed to reproduce the results
np.random.seed(42)

# Simulate 20 trials of 10 coin flips 
draws = binom.rvs(p=0.35, size=20, n=10)
print(draws)
