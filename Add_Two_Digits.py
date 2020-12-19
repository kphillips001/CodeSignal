# You are given a two-digit integer n. Return the sum of its digits.

# Example

# For n = 29, the output should be
# addTwoDigits(n) = 11
def addTwoDigits(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    return sum
