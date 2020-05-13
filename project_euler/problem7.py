# 10001st Prime
# ------------------------------------------------------------------------------
# What is the 10001st prime number?
#
# Answer: 104743

import math

def findPrime(n):
    """Returns the nth prime number"""
    primes = []
    num = 2
    while len(primes) < n:
        # find the next prime number
        while isPrime(num) != True:
            # if its not prime, go to the next prime
            num += 1
        primes.append(num)
        num += 1
    return primes[-1]


def isPrime(n):
    """Returns boolean representing if n is a prime number"""
    for i in range(2, n // 2):
        if n % i == 0:
            # if its divisible, it is not a prime number
            return False
    return True


print(findPrime(10001))
