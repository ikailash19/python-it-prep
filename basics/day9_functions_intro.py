def greet(name):
    print("Hello", name)

greet("Kailash")
# Hello Kailash

def add(a, b):
    return a+b

result = add(3, 4)
print("Sum:", result)
# Sum: 7

###################################################
# Task 1 - Function with loop
def sum_list(arr):
    total = 0
    for num in arr:
        total += num
    return total

print("Sum of the list:", sum_list([1, 2, 3, 4]))
# Sum of the list: 10

####################################################
# Task 2 - Max element function
def max_in_list(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print("Max element in the list:", max_in_list([1, 2, 3, 4]))
# Max element in the list: 4

####################################################
# Task 3 - Count even numbers
def count_even(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

print("Even numbers in the list:", count_even([1, 2, 3, 4]))
# Even numbers in the list: 2

#####################################################
# Task 4 - Function calling another function
def average(arr):
    total = sum_list(arr)
    return total / len(arr)

print("Average of the list:", average([1, 2, 3, 4]))
# Average of the list: 2.5