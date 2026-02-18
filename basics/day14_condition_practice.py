#Task 1 - Grade calculator
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"

#Task 2 - Nested condition
def access(age, has_id):
    if age >= 18:
        if has_id:
            return "Allowed"
        else:
            return "ID required"
    else:
        return "Too young"

#Task 3 - Ternary practice
def even_or_odd(x):
    return "Even" if x % 2 == 0 else "Odd"

print(grade(82)) #B
print(access(20, True)) #Allowed
print(even_or_odd(7)) #Odd