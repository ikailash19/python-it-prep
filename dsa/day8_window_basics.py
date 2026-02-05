#Slot 1 - DSA - Window Sum Pattern (Sliding Window Foundation)
#Task - Fixed window sum (size = 3)
arr = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0

# 0 to 4
for i in range(len(arr) - k + 1):
    window_sum = 0
    # 0, 0 + 3
    # 1, 1 + 3
    # 2, 2 + 3
    # 3, 3 + 3
    for j in range(i, i + k):
        # 2, 1, 5 -> window_sum = 8
        # 1, 5, 1 -> window_sum = 7
        # 5, 1, 3 -> window_sum = 9
        # 1, 3, 2 -> windows_sum = 6
        window_sum += arr[j]

    if window_sum > max_sum:
        max_sum = window_sum

print("Max window sum:", max_sum)
# Max window sum: 9
# Time Complexity: O(nk)
##################################################
# Slot 2 - DSA - Window Optimization (Real Sliding Window)
###################################################
#Task - Fixed window sum (size = 3)
arr = [2, 1, 5, 1, 3, 2]
k = 3

# window_sum = 8 Initial value
window_sum = sum(arr[:k])
# max_sum = 8
max_sum = window_sum
#
max_window = arr[:k]

# 3, 6
for i in range(k, len(arr)):
    # 8 + 1 -> 9
    # 7 + 3 -> 10
    # 9 + 2 -> 11
    window_sum += arr[i]
    # 9 - 2 -> 7
    # 10 - 1 -> 9
    # 11 - 5 -> 6
    window_sum -= arr[i - k]

    # 7 > 8 x
    # 9 > 8 ->
    # 6 > 9 x
    if window_sum > max_sum:
        # max_sum = 9
        max_sum = window_sum
        max_window = arr[(i - k + 1) : i + 1]

print("Max window sum:", max_sum)
print(max_window)
# Max window sum: 9
# Time Complexity: O(n)