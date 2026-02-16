# Python Datatypes, Operators, Concatenation — Notes

## Datatypes Overview

- Python provides built-in datatypes to store different kinds of values
- Datatypes are broadly divided into:
  - Basic (primitive) types
  - Derived (data structure) types

---

## Basic (Primitive) Datatypes — Single Value

- `int` → whole numbers → `10`
- `float` → decimal numbers → `3.14`
- `bool` → `True` / `False`
- `str` → text → `"hello"` or `'hello'`

Important:
- Python has **no separate char datatype**
- A single character like `'a'` is still a string

---

## Derived (Data Structure) Datatypes — Multiple Values

- Used to store collections of values
- Includes:
  - list
  - tuple
  - set
  - dict
  - range

Used heavily in:
- DSA problems
- automation frameworks
- data processing

---

## type() Function

Purpose:
- Used to check datatype of a value

Example:

```python
x = 10
print(type(x))
```

Output:

```
<class 'int'>
```

Useful for debugging and validation.

---

## del Keyword

Purpose:
- Deletes a variable reference

Example:

```python
x = 10
del x
```

- Accessing the variable after deletion raises an error
- Rarely used in regular scripts

---

## Operators — Definition

- An operator is a symbol that performs an operation on operands

Example:

```python
a + b
```

- `+` → operator  
- `a`, `b` → operands

---

## Arithmetic Operators

Used for mathematical operations.

- `+` → addition
- `-` → subtraction
- `*` → multiplication
- `/` → division (always returns float)
- `//` → floor division
- `%` → remainder (modulus)
- `**` → power

Examples:

```python
10 / 3
10 // 3
10 % 3
2 ** 5
```

---

## Comparison (Relational) Operators

- Used to compare values
- Always return boolean (`True` or `False`)

Operators:

```
>  <  >=  <=  ==  !=
```

Examples:

```python
5 > 3
5 == 5
5 != 2
```

Used heavily in:
- if / elif conditions
- loops
- assertions
- validations

---

## Logical Operators

Operate on boolean expressions.

- `and`
- `or`
- `not`

Examples:

```python
True and False
True or False
not True
```

Notes:
- Mainly used with boolean expressions
- Python also evaluates truthy/falsy values

---

## Concatenation — Joining Values

Concatenation means joining values.

### String + String → Concatenation

```python
"a" + "b"
```

Result:

```
"ab"
```

---

### Number + Number → Arithmetic Addition

```python
2 + 3
```

Result:

```
5
```

---

## Boolean Arithmetic Behavior

Python treats booleans as numbers:

- `True = 1`
- `False = 0`

Example:

```python
True + True
```

Result:

```
2
```

---

## Invalid Type Combinations — TypeError

These combinations are not allowed:

```python
"10" + 5
True + "abc"
```

Must convert explicitly:

```python
"10" + str(5)
```

---

## Java vs Python Concatenation Difference

Java:

```java
"num=" + 5
```

Python:

```python
"num=" + 5   # TypeError
```

- Python requires explicit conversion

---

## input() Function

Purpose:
- Used to take runtime user input

Example:

```python
name = input("Enter name: ")
```

Important rule:

- `input()` always returns string

Convert when needed:

```python
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```

---

## SDET Relevance

These concepts are used frequently in automation:

- datatype validation
- numeric comparisons
- assertion checks
- string concatenation for locators
- runtime data input
- API response validation

Example:

```python
expected_status = 200
assert response_code == expected_status
```

---

## Key Takeaway

Datatypes and operators are foundational for:

- automation scripting
- backend logic
- API validation
- test assertions
- framework design
