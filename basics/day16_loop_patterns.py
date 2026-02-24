# Task 1  - Count digits in a number
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    # 12345 > 0->
    # 1234 ->
    # 123 ->
    # 12 ->
    # 1 ->
    # 0 x
    while n>0:
        count += 1
        n //= 10
        # n = 1234
        # n = 123
        # n = 12
        # n = 1
        # n = 0
    return count

print(count_digits(12345))
# 5
##################################################
# Task 2 - Reverse a number
def reverse_number(n):
    rev = 0
    while n>0:
        # digit = 4, 3, 2, 1
        digit = n % 10
        # rev = 0 + 4, 40 + 3, 430 + 2, 432 + 1
        rev = rev * 10 + digit
        # n = 123, 12, 1, 0
        n //= 10
    return rev

print(reverse_number(1234))
# 4321
#################################################
# Task 3 - Check palindrome number
def is_palindrome(n):
    return n == reverse_number(n)

print(is_palindrome(121))
# True
print(is_palindrome(123))
# False