# Smallest Multiple
# ------------------------------------------------------------------------------
# What is the smallest positive number that is evely divisible by all of the
# numbers from 1 to 20?
#
# Answer: 232792560

def smallest_multiple(l):
    """Returns the smallest number that is the multiple of all numbers in given
    l(list)"""
    divisible = False
    num = 1
    while divisible == False:
        # iterate through numbers until the multiple is fulfilled
        if isDivisible(num, l):
            return num
        num += 1


def isDivisible(n, l):
    """Returns bollean representing if n(int) is divisible by each of the
    numbers in l(list)"""
    for i in l:
        if n % i != 0:
            # not divisble
            return False
    # if it gets through the whole list, means it is divisble by the whole list
    return True


print(smallest_multiple(list(range(1,21))))
