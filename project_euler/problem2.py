# Even Fibonacci Numbers
# ------------------------------------------------------------------------------
# Find the sum of all the even-valued terms in Fibonacci sequence which do not
# exceed 4 million
#
# Answer: 4613732

def fibonacci_up_to(n):
    """Returns list of fibonacci numbers up to n"""
    fib_list = []
    i = 0
    while fib(i) < n:
        fib_list.append(fib(i))
        i += 1
    return fib_list


def fib(n):
    """Returns the nth fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # find the next fib. number based on def of fibonacci sequence
        return fib(n-1) + fib(n-2)


def even_check(list):
    """Returns a list with only even numbers"""
    even_list = []
    for i in range(len(list)):
        # check if term is odd
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list

answer = sum(even_check(fibonacci_up_to(4000000)))
print(answer)
