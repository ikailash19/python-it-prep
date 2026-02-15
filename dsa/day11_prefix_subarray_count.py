# Slot 1 - Prefix Pattern
arr = [1, 2, 1, 2, 1]
K = 3

prefix_sum = 0
count = 0
freq = {0:1}

for x in arr:
    # 1, 3, 4, 6, 7
    prefix_sum += x
    # -2, 0, 1, 3, 4
    needed = prefix_sum - K

    # -2 x, 0 ->, 1 ->, 3 ->, 4 ->
    if needed in freq:
        # count = 1
        # count = 2
        # count = 3
        # count = 4
        count += freq[needed]

    #{0:1}, {1:1}, {3:1}, {4:1}, {6:1}, {7:1}
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print("Subarray count:", count)
# Subarray count: 4
# Time complexity: O(n)