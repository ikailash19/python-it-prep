score = 59

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Fail")

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Too young")

values = [0, 1, "", "text", [], [1,2], None]

for v in values:
    if v:
        print(v, "-> Truthy")
    else:
        print(v, "-> Falsy")