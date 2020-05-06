# Even Fibonacci Numbers
# ------------------------------------------------------------------------------
# Find the sum of all the even-valued terms in Fibonacci sequence which do not
# exceed 4 million
#
# Answer:

def fibonacci_up_to(n):
    """Returns list of fibonacci numbers up to n"""
    if n<2:
        # base case
        return [1,1]
    else:
        list = fibonacci_up_to(n-1)
        if list[-1] < n:
            # add the next fibonacci number to the list, sum of last two nums
            list.append(list[-1] + list[-2])
        return list

def even_check(list):
    """Returns a list with only even numbers"""
    even_list = []
    for i in range(len(list)):
        # check if term is odd
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list

answer = even_check(fibonacci_up_to(1000))
print(answer)
