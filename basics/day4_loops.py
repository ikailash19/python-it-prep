for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(1, 6):
    print(i)

# 1
# 2
# 3
# 4
# 5

for i in range(0, 10, 2):
    print(i)

# 0
# 2
# 4
# 6
# 8

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

# 1, odd
# 2, even
# 3, odd
# 4, even
# 5, odd
# 6, even
# 7, odd
# 8, even
# 9, odd
# 10, even

numbers = [10, 20, 30, 40]

total = 0
for n in numbers:
    total += n
    # total = 0 + 10
    # total = 10 + 20
    # total = 30 + 30
    # total = 60 + 40 = 100

print("Sum:", total)

#Sum: 100