# Task 1 - Build Prefix Array
arr = [2, 4, 1, 3, 6]

# assigns 0 in 5x indexes
# [0, 0, 0, 0, 0]
prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)
#[2, 6, 7, 10, 16]

###################################################
# Task 2 - Range Sum Query Using Prefix
def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L - 1]

print(range_sum(prefix, 1, 3))
print(range_sum(prefix, 2, 4))
# 8
# 10