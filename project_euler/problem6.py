# Sum Square Difference
# ------------------------------------------------------------------------------
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#
# Answer: 25164150

def sumsquare(l):
    """Returns the sum of each term of l squared"""
    new = []
    for i in range(len(l)):
        # square each term
        new.append(l[i] ** 2)
    return sum(new)


def squaresum(l):
    """Returns the sqaure of each term of l summed"""
    return sum(l) ** 2

nums = list(range(1,101))
print(squaresum(nums) - sumsquare(nums))
