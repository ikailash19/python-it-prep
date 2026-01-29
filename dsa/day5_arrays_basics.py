# SLOT 1
#####################################################################
# Task 1 - Index-based traversal
arr = [10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(i, arr[i])

# 0 10
# 1 20
# 2 30
# 3 40
# 4 50

# Task 2 - Value-based traversal
for value in arr:
    print(value)

# 10
# 20
# 30
# 40
# 50

# Task 3 - Reverse traversal
for i in range(len(arr) -1, -1, -1): #(5 - 1(Initial Index 4 so 50, -1(Marks before which point to iterate so 0, -1(traversal value)
    print(arr[i])

# 50
# 40
# 30
# 20
# 10

#####################################################################
# SLOT 2
#####################################################################

# Task 1 - Sum of array
arr = [3, 5, 7, 9]

total = 0
for x in arr:
    total += x
    # total = 0 + 3
    # total = 3 + 5
    # total = 8 + 7
    # total = 15 + 9 = 24


print("Sum:", total)

# Sum: 24

# Task 2 - Maximum element
arr = [12, 5, 22, 7, 18]

max_val = arr[0]
for x in arr:
    # 12 > 12
    # 5 > 12
    # 22 > 22 ->
    # 7 > 22
    # 18 > 22
    if x > max_val:
        max_val = x
        # max_val = 22

print("Max:", max_val)

# Max: 22

# Task 3 - Minimum element
arr = [12, 5, 22, 7, 18]

min_val = arr[0]
for x in arr:
    # 12 < 12
    # 5 < 12 ->
    # 22 < 5
    # 7 < 5
    # 18 < 5
    if x < min_val:
        min_val = x
        # min_val = 5

print("Min:", min_val)

# Min: 5

#####################################################################
# SLOT 3
#####################################################################

# Task 1 - Count elements matching condition
arr = [1, 2, 3, 4, 5, 6]

even_count = 0
for x in arr:
    # 1 % 2 = 1 x
    # 3 % 2 = 1 x
    # 5 % 2 = 1 x
    if x % 2 == 0:
        # 2 % 2 = 0
        # 4 % 2 = 0
        # 6 % 2 = 0
        even_count += 1

print("Even count:", even_count)

# Even count: 3

# Task 2 - Count elements greater than a value
arr = [10, 5, 20, 8, 15]
threshold = 10

count = 0
for x in arr:
    if x > threshold:
        # 20 > 10 ->
        # 15 > 10 ->
        count += 1

print("Count >", threshold, ":", count)

# Count > 10 : 2

# Task 3 - Count occurrences of specific value
arr = [1, 2, 2, 3, 2, 4]
target = 2

count = 0
for x in arr:
    if x == target:
        count += 1

print("Occurrences of", target, ":", count)

# Occurrences of 2 : 3

#####################################################################
