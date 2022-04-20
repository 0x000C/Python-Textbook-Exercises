# Estimate the probability that a randomly chosen American is both male
# and weighs more than 197 pounds. Assume that 50% of the population is
# male, and that the weights of the male population are normally
# distributed with a mean of 210 pounds and a standard deviation of 30
# pounds. (Hint: think about using the empirical rule.)

import scipy.integrate
import numpy as np


def gaussian(x, mu, sigma):
    """assumes x, mu, sigma numbers
       returns the value of P(x) for a Gaussian
          with mean mu and sd sigma"""
    factor1 = (1.0 / (sigma * ((2 * np.pi)**0.5)))
    factor2 = np.e**-(((x - mu)**2) / (2 * sigma**2))
    return factor1 * factor2


male_and_over_197_odds = 0.5 * \
    scipy.integrate.quad(gaussian, 197, 1000, (210, 30))[0]

print(f'Odds of random being >197lbs and male = {male_and_over_197_odds}')
