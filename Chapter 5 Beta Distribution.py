from scipy.stats import beta

# 1. Flip coin 10 times and get 4H 6T.
# What is probability the coin lands on heads more than 60% of the time?
n = 10
heads = 4
tails = 6
p = 0.6
# CDF integrates the beta distribution from 0 to p.
prob = 1 - beta.cdf(p, heads, tails)
print(f'1. Probability the coin lands on heads more than 60%: {round(prob, 3)}')

# 2. Now 9H 11T. What is probability coin is fair within 5%?


def fair_coin(h, t, question_num):
    prob45 = beta.cdf(0.45, h, t)
    prob55 = beta.cdf(0.55, h, t)
    print(f'{question_num}. Probability the coin is fair within 5%: {round(prob55 - prob45, 3)}')


fair_coin(9, 11, 2)

# 3. 109H, 111T. Now what?
fair_coin(109, 111, 3)