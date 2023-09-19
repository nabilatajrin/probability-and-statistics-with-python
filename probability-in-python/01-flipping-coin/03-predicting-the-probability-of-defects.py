# Probability of getting exactly 1 defective component
prob_one_defect = binom.pmf(k=1, n=50, p=0.02)
print(prob_one_defect)

# Probability of not getting any defective components
prob_no_defects = binom.pmf(k=0, n=50, p=0.02)
print(prob_no_defects)

# Probability of getting 2 or less defective components
prob_two_or_less_defects = binom.cdf(k=2, n=50, p=0.02)
print(prob_two_or_less_defects)
