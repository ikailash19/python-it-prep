a = True
b = False

print(type(a)) # <class 'bool'>
print(10 > 5) # True
print(10 == "10") # False

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

x = 10

print(x > 5 and x < 20) # True
print(x < 5 or x == 10) # True
print(not(x == 10)) # False