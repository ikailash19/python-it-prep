#Slot 1 - Dict Pattern - Two Sum with Indices
arr = [2, 7, 11, 15]
target = 9

pos = {}

#i is index, x is item
for i, x in enumerate(arr):
    # 7, 2, -2, -6
    needed = target - x
    # 7 x, 2->
    if needed in pos:
        print("Indices:", pos[needed], i)
        break

    #{2:0},
    pos[x] = i

#Indices: 0, 1

##########################################################
#Slot 2 - Return All Pairs
##########################################################
arr = [1, 3, 2, 2, 4]
target = 4

pos = {}
pairs = []

for i, x in enumerate(arr):
    needed = target - x
    #3 x, 1->, 2 x, 2->, 0 x
    if needed in pos:
        #[(0, 1), (2, 3)]
        pairs.append((pos[needed], i))
    #{1:0}, {3:1}, {2:3}, {4: 4}
    pos[x] = i

print("Pairs:", pairs)
#Pairs: [(0, 1), (2, 3)]