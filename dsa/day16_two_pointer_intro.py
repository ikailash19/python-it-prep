# Task 1 - Reverse array using two pointers
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    #1, 5 = 5, 1 Swapping
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
# [5, 4, 3, 2, 1]
###################################################
# Task 2 - Check if array is palindrome using two pointers
def is_palindrome_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_array([1, 2, 3, 2, 1]))
# True
print(is_palindrome_array([1, 2, 3, 4, 5]))
# False
###################################################
# Task 3 - Two Sum in Sorted Array (Two Pointer Version)
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return (left, right)
        elif current < target:
            # Since sorted array & we already have largest
            # element in the right but still not enough
            # So moving away from smallest element
            left += 1
        else:
            # Same logic as above but moving prior to largest element
            right -= 1
    return None

print(two_sum_sorted([1, 2, 3, 4, 6], 6))
#(1, 3)