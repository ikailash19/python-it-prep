# Day 17 - Rebuild Core Patterns (Recovery Session)
# Task 1 - Reverse Number:
def reverse_number(n):
    reversed_number = 0
    while n > 0:
        last_digit= n % 10
        reversed_number = reversed_number * 10 + last_digit
        n //= 10

    return reversed_number
print(reverse_number(1234))

################################################
# Task 2 - Two Pointer Reverse Array
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse_array([1, 2, 3, 4, 5]))

################################################
# Task 3 - Sliding Window (Optimized Version Only)
def max_windows_sum(arr, k):
    window_sum = sum(arr[0:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_windows_sum(arr, k))