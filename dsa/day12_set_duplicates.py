#Task 1 - Detect duplicate in Array
arr = [3, 1, 4, 2, 5, 1]

seen = []
has_dup = False

for x in arr:
    if x in seen:
        has_dup = True
        break
    seen.append(x)

print("Has duplicate:", has_dup)
#Has duplicate: True
#Time complexity: O(n)

######################################################
#Task 2 - Print First Duplicate value
arr = [7, 2, 4, 9, 2, 5]

seen = set()
dup_value = None

for x in arr:
    if x in seen:
        dup_value = x
        break
    seen.add(x)

print("First Duplicate:", dup_value)
#First Duplicate: 2
#Time complexity: O(n)
######################################################
#Task 3 - Two-Sum base version (Set Pattern)
arr = [2, 7, 11, 15]
target = 9

seen = set()
found = False

for x in arr:
    needed = target - x
    if needed in seen:
        found = True
        print("Pair found:", needed, x)
        break
    seen.add(x)

print("Exists:", found)
#Pair found: 2 7
#Exists: True