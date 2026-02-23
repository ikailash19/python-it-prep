# Python Loops — Notes

## What is a Loop?

- A loop is a group of statements that repeat multiple times.
- Used to automate repetitive tasks.
- Two main loop types in Python:
  - `for` loop
  - `while` loop

---

## for Loop

Used when the number of iterations is known.

Common usage:

```python
for i in range(5):
    print(i)
```

---

### range() Function

Generates a sequence of numbers.

Syntax:

```python
range(start, stop, step)
```

- `start` → starting value (optional, default = 0)
- `stop` → stopping value (required)
- `step` → increment/decrement (optional, default = 1)

Examples:

```python
range(5)          # 0,1,2,3,4
range(1, 6)       # 1,2,3,4,5
range(1, 10, 2)   # 1,3,5,7,9
range(10, 0, -1)  # 10,9,8,...,1
```

---

## while Loop

Used when the number of iterations is not fixed.

Syntax:

```python
while condition:
    statement
```

Example:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

Important:
- Must update condition variable inside loop
- Otherwise infinite loop occurs

---

## Loop Control Keywords

### break

- Terminates the loop immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### continue

- Skips current iteration
- Moves to next iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

---

## Loop Variable Scope

- In Python, loop variables are accessible outside the loop.

Example:

```python
for i in range(3):
    pass

print(i)  # Accessible
```

---

## Increment / Decrement in Python

- Python does NOT support `i++` or `i--`
- Must use:

```python
i += 1
i -= 1
```

---

## match-case (Switch Alternative)

Python does not support traditional switch-case.

From Python 3.10+, `match-case` is available:

```python
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Default")
```

- `case _` acts as default
- No `break` required

---

## Loop Usage in Automation (SDET Relevance)

Loops are used for:

- Iterating through test data
- Processing API responses
- Running repeated validations
- Data-driven testing
- Retrying failed steps

Example:

```python
for user in users_list:
    response = login(user)
    assert response.status_code == 200
```

---

## Key Takeaway

Loops allow repetition of logic efficiently.

Understanding loops + conditions is critical for:
- DSA
- Automation frameworks
- Backend logic
- Interview problem solving