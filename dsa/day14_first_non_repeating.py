#Slot 1 - HashMap Pattern Level - 2
#First Non-Repeating Element
arr = [4, 5, 1, 2, 1, 4, 5]

freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
#freq = {4:2, 5:2, 1:2, 2:1}

answer = None
for x in arr:
    if freq[x] == 1:
        answer = x
        break

print("First non-repeating element:", answer)
#First non-repeating element: 2
#Time complexity: O(n)

##################################################
#Slot 2 - Character Frequency in String
s = "automation"

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
#freq = {"a":2, "u":1, "t":2, "o":2, "m":1, "i":1, "n":1}

for char in s:
    if freq[char] == 1:
        print("First unique char:", char)
        break

#First unique char: u
#Time complexity: O(n)