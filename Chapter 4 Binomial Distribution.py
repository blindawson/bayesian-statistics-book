from scipy.stats import binom

# 1. What are the parameters of the binomial distribution for the probability
# of rolling either a 1 or a 20 on a 20-sided die, if we roll the die 12 times?
n = 12
p = 2 / 20
r_values = list(range(n + 1))
mean, var = binom.stats(n, p)
dist = [binom.pmf(r, n, p) for r in r_values]
print(dist)

# 2. How many ways can you pull one ace in 5 pulls?
# 5 (AOOOO, OAOOO, OOAOO, OOOAO, OOOOA)

# 3. What is the probability of pulling 5 aces in 10 pulls?
n = 10
p = 4 / 52
k = 5
prob = binom.pmf(k, n, p)
print(f"3. In 10 pulls, draw 5 aces: {prob}")

# 4. If you have 1/5 probability of getting a job offer
# and interview with 7 companies, what are the chances you get 2 offers?
n = 7
p = 1 / 5
k = 2
prob = 1 - binom.cdf(k - 1, n, p)
# CDF gives you the chance of getting k hits or fewer in n tries given p.
print(f"4. In 7 interviews, get 2 offers: {prob}")

# 5. 25 interviews. When tired 1/10 chance of getting offer. Are you twice as likely to get 2 offers?
n = 25
p = 1 / 10
k = 2
prob_tired = 1 - binom.cdf(k - 1, n, p)
print(f"5. In 25 tired interviews, get 2 offers: {prob_tired}")
print(f"prob_tired / prob = {prob_tired/prob}")
