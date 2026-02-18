# Python Conditional Statements & Formatting Output — Notes

## Output Formatting in Python

There are multiple ways to print variables in Python.

### 1. String Concatenation

```python
print("Name: " + name)
```

- Works only if both sides are strings
- Requires explicit type conversion if mixing types

---

### 2. Comma Separation

```python
print("Name:", name)
```

- Automatically adds space between arguments
- Safest and most commonly used method

---

### 3. Percent Formatting (Old Style)

```python
print("Name: %s" % name)
```

- `%s` → string placeholder
- Older style formatting
- Still seen in legacy code

---

### 4. format() Method

```python
print("Name: {}".format(name))
```

- Cleaner and more flexible than `%`
- Can control order:

```python
print("Name: {1} Age: {0}".format(age, name))
```

---

### 5. Escape Characters

Used for formatting output:

- `\n` → new line
- `\t` → tab space

Example:

```python
print("Hello\nWorld")
print("Name:\tKailash")
```

---

## Conditional Statements in Python

Used to control program flow based on conditions.

---

### if Statement

```python
if condition:
    statement
```

---

### if-else Statement

```python
if condition:
    statement
else:
    statement
```

---

### if-elif-else Ladder

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Used when multiple conditions must be checked.

---

### Nested if

```python
if condition1:
    if condition2:
        statement
```

Used for layered decision logic.

---

## Short-hand if

```python
if condition: print("True")
```

Single-line conditional.

---

## Ternary Operator (Short-hand if-else)

```python
result = "Adult" if age >= 18 else "Minor"
```

Useful for simple assignments.

---

## pass Keyword

Used when a block is syntactically required but no action is needed.

```python
if condition:
    pass
```

Common in:
- Placeholder logic
- Framework scaffolding
- Future implementation areas

---

## Important Note

Python does not support traditional `switch` statements.

(From Python 3.10+, `match-case` exists, but basic Python uses if-elif.)

---

## SDET Relevance

Conditionals are used heavily in:

- Assertion logic
- Response validation
- Data-driven test flows
- Error handling
- Environment configuration logic

Example:

```python
if response_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
```

---

## Key Takeaway

Conditional statements form the decision-making backbone of automation scripts and backend logic.

Clear conditional logic = maintainable test frameworks.
