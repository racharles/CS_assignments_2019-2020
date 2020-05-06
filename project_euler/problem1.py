# Multiples of 3 and 5
# ------------------------------------------------------------------------------
# Find the sum of all the multiples of 3 or 5 below 1000
#


def multiples_up_to(n,end):
    """Returns list of all the multiples of n that are less than end"""
    multiples = []
    i = 1
    # calculate multiple of n by iterating until the end number
    while n*i < end:
        multiples.append(n * i)
        i += 1
    return multiples
  
  answer = sum(multiples_up_to(3,1000), multiples_up_to(5,1000))
