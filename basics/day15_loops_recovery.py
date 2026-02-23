#Task 1 - print numbers 1 to 20
for i in range(1, 21):
    print(i)
#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

#Task 2 - sum of numbers divisible by 3
total = 0
for i in range(1, 51):
    if i % 3 == 0:
        total += i

print("Sum:", total)
# Sum: 408

# Task 3 - simple while loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1
#Count: 1, Count:2 ... Count: 5

# Task 4 - break usage
for i in range(1, 11):
    if i == 6:
        break
    print(i)
# 1, 2, 3, 4, 5

# Task 5 - continue usage
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd:", i)
# Odd: 1, Odd: 3... Odd: 9