# SLOT 1 - One-Pass Multiple Results
arr = [2, 5, 1, 8, 3]

total = 0
min_var = arr[0]
max_var = arr[0]

for x in arr:
    total += x
    if x < min_var:
        min_var = x
    if x > max_var:
        max_var = x

print("Sum:", total) # Sum: 19
print("Min:", min_var) # Min: 1
print("Max:", max_var) # Max: 8

########################################################################

# SLOT 2 - Index-based thinking

# Task 1 - Index of maximum element
arr = [4, 7, 1, 9, 3]

max_index = 0
for i in range(len(arr)):
    # 4 > 4 x
    # 7 > 4 ->
    # 1 > 7 x
    # 9 > 7 ->
    # 3 > 9 x
    if arr[i] > arr[max_index]:
        max_index = i

print("Max index:", max_index) # Max index: 3
print("Max value:", arr[max_index]) # Max value: 9

# Task 2 - First occurrence of a value (early exit)
arr = [5, 3, 7, 3, 9]
target = 3

index = -1 # If not found returns -1 else gets reassigned
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("First occurrence index:", index) # First occurrence index: 1

#############################################################################

# Slot 3 - Mini Problem

# Count how many elements are greater than all previous elements.

arr = [3, 4, 2, 7, 5, 8]

count = 1
max_so_far = arr[0]

for x in arr[1:]:
    # 4 > 3 ->
    # 2 > 4 x
    # 7 > 4 ->
    # 5 > 7 x
    # 8 > 7 ->
    if x > max_so_far:
        count += 1
        max_so_far = x

print("Count:", count) # Count: 4