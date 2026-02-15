# Task 1 - Count Subarrays with Sum = K (Brute First)
arr = [1, 2, 3, 2, 1]
K = 5

count = 0
# i = 0 to 4
for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        if total == K:
            count += 1
        elif total > K:
            break
            #Small optimization to avoid unwanted passing
            #Only if array elements >= 0
print("Count:", count)
# Count: 2
# Time complexity O(n²)

################################################################
# Task - Optimized Version
arr = [1, 2, 3, 2, 1]
K = 5

prefix_sum = 0
count = 0

freq = {0 : 1}

for x in arr:
    # 1, 3, 6, 8, 9
    prefix_sum += x
    # 1 - 5, 3 - 5, 6 - 5, 8 - 5, 9 - 5
    # -4, -2, 1, 3, 4
    needed = prefix_sum - K

    # -4 x, -2 x, 1 ->,
    if needed in freq:
        # count = 1
        #
        count += freq[needed]

    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print("Count optimized:", count)
# Count optimized: 2
# Time complexity: O(n)
