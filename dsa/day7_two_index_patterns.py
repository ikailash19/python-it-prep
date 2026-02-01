# SLOT 1 - Pair Traversal (Same Loop, Two Indices)

# Task - 1 - Adjacent pair comparison
arr = [5, 2, 8, 3, 7]

for i in range(len(arr) - 1):
    print(arr[i], arr[i + 1])

# 5 2
# 2 8
# 8 3
# 3 7

# Task 2 - Count increasing adjacent pairs
arr = [1, 3, 2, 5, 4, 6]

count = 0
for i in range(len(arr) - 1):
    if arr[i+1] > arr[i]:
        count += 1

print("Increasing adjacent pairs:", count)

# Increasing adjacent pairs: 3

##########################################################
# SLOT 2 - Difference Pattern (Running state + Pairs
##########################################################

# Task - Maximum difference between adjacent elements
arr = [10, 3, 18, 7, 20]

# To set initial value, caution: Array must have atleast 2 elements
max_diff = abs(arr[0] - arr[1])

for i in range(len(arr) - 1):
    diff = abs(arr[i] - arr[i + 1])
    if diff > max_diff:
        max_diff = diff

print("Max adjacent diff:", max_diff)

# Max adjacent diff: 15

###########################################################
# SLOT 3 - Mini Problem (Strict Order Check
###########################################################

# Problem - Check if array is strictly increasing

arr = [1, 2, 3, 4]

is_increasing = True

for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
        is_increasing = False
        break

print("Strictly increasing:", is_increasing)

# Strictly increasing: True