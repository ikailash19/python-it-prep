#Task 1 - count numbers greater than threshold
def count_gt(arr, t):
    count = 0
    for x in arr:
        if x > t:
            count += 1
    return count

#Task 2 - build frequency dict
def freq_map(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

#Task 3 - operator + logic combo
def in_range(x, low, high):
    return x >= low and x <= high

print(count_gt([1, 5, 8, 2, 10], 5))
#2
print(freq_map([1, 2, 2, 3, 3, 3]))
#{1:1, 2:2, 3:3}
print(in_range(7, 5, 10))
#True