# Largest Palindrome Product
# ------------------------------------------------------------------------------
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

def largest_palindrome():
    """Returns the largest palindrome made from the product of two 3-digit
    numbers through brute force"""
    largest = 0
    for i in range(100, 999):
        for j in range(100, 999):
            # check if i * j is a palindrome
            if isPalindrome(str(i*j)) and (i*j) > largest:
                largest = i * j
    return largest


def isPalindrome(s):
    """Returns boolean representing if n(str) is a palindrome"""
    if s == s[::-1]:
        # if flipped string = original string, then s is a palindrome
        return True
    else:
        return False


print(largest_palindrome())
