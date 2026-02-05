# Python Setup, Variables, Comments — Notes

## Python Installation & Nature

- Python is an interpreted language
- Code runs line by line (no compile step like Java/C++)
- Good for rapid development and scripting
- Widely used in:
  - Automation testing
  - Backend services
  - AI/ML
  - Data engineering

---

## PyCharm IDE

PyCharm is a professional Python IDE.

Features:
- Smart code completion
- Built-in debugger
- Virtual environment support
- Git integration
- Test runner support

Suitable for:
- Python development
- SDET automation
- Backend APIs
- AI/ML projects

We will use PyCharm as primary IDE (no need to switch).

---

## Comments in Python

Purpose:
Comments explain code for humans. Python ignores them.

### Single-line comment

```python
# This is a comment
```

### Multi-line comment / docstring

```python
"""
Multi-line explanation
Used also as docstrings in functions/classes
"""
```

Best Practice:
- Comment WHY logic exists
- Don’t comment obvious syntax

Bad:
```python
x = x + 1  # increment x
```

Good:
```python
# increment retry counter after failed API call
x = x + 1
```

---

## Variables in Python

Variables store values.

Python is dynamically typed:
- No type declaration required
- Type decided at runtime

Examples:

```python
x = 10
name = "Kailash"
is_valid = True
price = 10.5
```

---

## Variable Naming Rules

Allowed:
- letters
- numbers
- underscore `_`

Rules:
- cannot start with number
- case-sensitive
- no spaces
- avoid special characters

Examples:

```python
user_name = "abc"   # good (snake_case)
UserName = "abc"    # class style
a = 5               # allowed but not descriptive
```

Preferred in Python:
```
snake_case
```

---

## Dynamic Typing

Variable type can change:

```python
x = 10
x = "ten"
```

Python allows reassignment with different type.

---

## Multiple Assignment

Assign multiple values at once:

```python
a, b = 1, 2
```

Assign same value:

```python
a = b = c = 5
```

Unpacking:

```python
x, y, z = [1, 2, 3]
```

---

## Type Checking

Use `type()` to check data type:

```python
x = 10
print(type(x))
```

Output:

```
<class 'int'>
```

---

## SDET Relevance of Variables

Variables are heavily used in automation:

They store:
- test data
- expected values
- API payloads
- selectors
- configuration values
- environment data

Example:

```python
expected_status = 200
response_code = api_call()

assert response_code == expected_status
```

---

## Key Takeaway

Variables + comments are foundation blocks.

They directly support:
- readable automation scripts
- maintainable frameworks
- test data driven design
