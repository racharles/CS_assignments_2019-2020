# Largest Prime Factor
# ------------------------------------------------------------------------------
# What is the largest prime factor of the number 600851475143?
#
# Answer: 6857

import math

def largest_prime_factor(n):
    """Returns the largest prime factor of n"""
    factors = []
    while n % 2 == 0:
        # while loop needed in case of duplicate factors
        # if divisible by 2, then 2 is a prime factor
        factors.append(2)
        n = n/2
    else:
        # loop through all the odd(step=2) possibilities from 3 to sqrt(n),
        # divides the number into prime numbers, since prime = undivisible
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                # while loop needed in case of duplicate factors
                factors.append(i)
                n = n/i
    if n > 2:
        # only if n is a prime number not covered ex. n = 7
        factors.append(n)
    return factors


print(max(largest_prime_factor(600851475143)))
