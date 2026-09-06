# PostgreSQL Procedures

## 1. Procedure vs Function

A **procedure** is primarily used to perform an action or operation.

```sql
CALL update_movie_rating(8, 1);
```

A **function** is primarily used to return a value and can be used inside SQL expressions.

```sql
SELECT get_movie_rating(1);
```

### Mental Model

```text
Function  → Give me something
Procedure → Do something
```

> Procedures can also return values through `OUT` / `INOUT` parameters.

---

## 2. Creating a Procedure

```sql
CREATE OR REPLACE PROCEDURE update_movie_rating(
    p_rating INT,
    p_movie_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE movies
    SET rating = p_rating
    WHERE movie_id = p_movie_id;
END;
$$;
```

Execute using:

```sql
CALL update_movie_rating(8, 1);
```

---

## 3. Procedure Parameters

### IN

Input only.

```sql
IN p_movie_id INT
```

### OUT

Output only.

The caller does not provide the initial value.

```sql
OUT p_result INT
```

### INOUT

Input + output.

The caller provides an initial value, and the procedure can modify it.

```sql
INOUT p_amount INT
```

### Mental Model

```text
IN     → Input
OUT    → Output
INOUT  → Input + modified output
```

---

# Exception Handling

## 4. UPDATE and FOUND

An `UPDATE` affecting zero rows does **not** automatically raise an exception.

Example:

```sql
UPDATE movies
SET rating = 8
WHERE movie_id = 9999;
```

If the movie does not exist:

```text
0 rows affected
No exception
```

Use `FOUND` to detect this:

```sql
IF NOT FOUND THEN
    RAISE EXCEPTION 'Movie ID % does not exist', p_movie_id;
END IF;
```

### FOUND

- `FOUND = TRUE` → previous operation affected at least one row
- `FOUND = FALSE` → previous operation affected no rows

### Important Flow

```text
UPDATE
   ↓
0 rows affected
   ↓
No automatic exception
   ↓
Check FOUND
   ↓
IF NOT FOUND
   ↓
RAISE EXCEPTION
```

---

## 5. EXCEPTION

`EXCEPTION` is used to catch errors inside a PL/pgSQL block.

```sql
BEGIN
    -- Risky operation

EXCEPTION
    WHEN unique_violation THEN
        -- Handle duplicate error
END;
```

### Specific Exception Handling

Prefer a specific exception handler when the expected error is known:

```sql
WHEN unique_violation THEN
```

Instead of blindly catching everything:

```sql
WHEN OTHERS THEN
```

`WHEN OTHERS` is a catch-all fallback.

### Mental Model

```text
Known error
    ↓
Specific handler
    ↓
Handle it precisely
```

---

# RAISE

## 6. RAISE NOTICE

Displays an informational message.

```sql
RAISE NOTICE 'Movie updated successfully';
```

It does not represent an actual database error.

---

## 7. RAISE WARNING

Displays a warning.

```sql
RAISE WARNING 'Movie rating is unusually high';
```

A warning normally does not abort the operation.

---

## 8. RAISE EXCEPTION

Creates an actual error.

```sql
RAISE EXCEPTION 'Movie ID % does not exist', p_movie_id;
```

This is useful when a business condition should deliberately be treated as an error.

Example:

```sql
UPDATE movies
SET rating = p_rating
WHERE movie_id = p_movie_id;

IF NOT FOUND THEN
    RAISE EXCEPTION 'Movie ID % does not exist', p_movie_id;
END IF;
```

---

## 9. Bare RAISE

Inside an exception handler:

```sql
RAISE;
```

re-raises the **original exception**.

### Difference

```text
RAISE EXCEPTION 'Custom error'
→ Creates a new/custom error

RAISE;
→ Re-raises the original error
```

### Practical Pattern

```sql
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Duplicate detected';
        RAISE;
```

The error can be logged/informed and then allowed to reach the application.

> **Handle ≠ Hide**

---

# SQLSTATE and SQLERRM

## 10. SQLSTATE

`SQLSTATE` is a standardized, machine-readable error code.

Examples:

```text
23505 → unique_violation
23514 → check constraint violation
P0001 → custom RAISE EXCEPTION
```

Use `SQLSTATE` when reliable programmatic error identification is required.

---

## 11. SQLERRM

`SQLERRM` provides the human-readable error message.

Example:

```text
duplicate key value violates unique constraint "movies_pkey"
```

### Mental Model

```text
SQLSTATE → What type of error?

SQLERRM   → What does the error say?
```

### SQLSTATE vs SQLERRM

`SQLSTATE` is generally more reliable for program logic because it is standardized.

The human-readable `SQLERRM` text can vary.

```text
SQLSTATE → For machines / program logic
SQLERRM   → For humans / readable messages
```

---

# GET STACKED DIAGNOSTICS

## 12. Getting Detailed Error Information

`GET STACKED DIAGNOSTICS` is used inside an exception handler to retrieve detailed information about the exception.

```sql
GET STACKED DIAGNOSTICS
    v_state = RETURNED_SQLSTATE,
    v_message = MESSAGE_TEXT,
    v_detail = PG_EXCEPTION_DETAIL;
```

### Common Diagnostic Items

| Diagnostic Item | Information |
|---|---|
| `RETURNED_SQLSTATE` | SQLSTATE error code |
| `MESSAGE_TEXT` | Human-readable error message |
| `PG_EXCEPTION_DETAIL` | Additional error detail |
| `PG_EXCEPTION_HINT` | PostgreSQL's hint |
| `TABLE_NAME` | Related table |
| `CONSTRAINT_NAME` | Related constraint |

### Example

```sql
DECLARE
    v_state TEXT;
    v_message TEXT;
    v_constraint TEXT;
```

```sql
GET STACKED DIAGNOSTICS
    v_state = RETURNED_SQLSTATE,
    v_message = MESSAGE_TEXT,
    v_constraint = CONSTRAINT_NAME;
```

### Important Syntax

Multiple diagnostic assignments are separated by **commas**:

```sql
GET STACKED DIAGNOSTICS
    v_state = RETURNED_SQLSTATE,
    v_message = MESSAGE_TEXT;
```

Not:

```sql
GET STACKED DIAGNOSTICS
    v_state = RETURNED_SQLSTATE;
    v_message = MESSAGE_TEXT;
```

---

# 13. Practical Exception Handling Pattern

A procedure can combine `FOUND`, `RAISE EXCEPTION`, exception handling, diagnostics, and re-raising.

```sql
CREATE OR REPLACE PROCEDURE update_movie_rating(
    p_rating INT,
    p_movie_id INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_state TEXT;
    v_message TEXT;
BEGIN

    UPDATE movies
    SET rating = p_rating
    WHERE movie_id = p_movie_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Movie ID % does not exist', p_movie_id;
    END IF;

EXCEPTION
    WHEN OTHERS THEN

        GET STACKED DIAGNOSTICS
            v_state = RETURNED_SQLSTATE,
            v_message = MESSAGE_TEXT;

        RAISE NOTICE 'Error [%]: %', v_state, v_message;

        RAISE;
END;
$$;
```

### Flow

```text
UPDATE
  ↓
FOUND?
  ↓
No
  ↓
RAISE EXCEPTION
  ↓
EXCEPTION handler
  ↓
GET STACKED DIAGNOSTICS
  ↓
Log / inspect error
  ↓
RAISE;
  ↓
Original error reaches application
```

---

# Transaction Control

## 14. COMMIT and ROLLBACK in Procedures

Procedures can use transaction control under PostgreSQL's rules.

Functions cannot freely use transaction control.

```text
Function  → Cannot freely COMMIT / ROLLBACK

Procedure → Can use COMMIT / ROLLBACK with restrictions
```

---

## 15. Multiple COMMITs

Example:

```sql
UPDATE movies
SET rating = 8
WHERE movie_id = 1;

COMMIT;

UPDATE movies
SET rating = 9
WHERE movie_id = 2;

COMMIT;
```

Each `COMMIT` makes the preceding work permanent.

If the second operation fails:

```text
First UPDATE
    ↓
COMMIT
    ↓
Permanent
    ↓
Second UPDATE
    ↓
Fails
```

The first committed operation cannot be rolled back by a later failure.

---

## 16. Procedure Transaction Rule

Transaction control inside a procedure has restrictions.

A procedure containing transaction control should be invoked directly:

```sql
CALL process_movie();
```

Rather than being called from inside an explicit transaction:

```sql
BEGIN;

CALL process_movie();

COMMIT;
```

The important interview-level distinction is:

```text
Direct CALL
→ Procedure can control transactions under PostgreSQL's rules

Explicit surrounding transaction
→ Transaction control inside the procedure is restricted
```

---

# Function vs Procedure — Interview View

| Feature | Function | Procedure |
|---|---|---|
| Primary purpose | Return a value | Perform an operation |
| Invocation | `SELECT` / SQL expression | `CALL` |
| `IN` parameters | Yes | Yes |
| `OUT` parameters | Yes | Yes |
| `INOUT` parameters | Yes | Yes |
| Transaction control | Cannot freely control transactions | Can use transaction control with restrictions |
| Typical use | Calculation / retrieval | Business operation / action |

---

# Quick Interview Summary

```text
Procedure
→ Performs an operation
→ Invoked using CALL
→ Supports IN / OUT / INOUT
→ Can use transaction control under restrictions

FOUND
→ Tells whether the previous DML operation affected rows

RAISE NOTICE
→ Informational message

RAISE WARNING
→ Warning message

RAISE EXCEPTION
→ Deliberately creates an error

EXCEPTION
→ Catches errors

SQLSTATE
→ Standardized error code

SQLERRM
→ Human-readable error message

GET STACKED DIAGNOSTICS
→ Retrieves detailed exception information

RAISE;
→ Re-raises the original exception

COMMIT
→ Makes transaction changes permanent

ROLLBACK
→ Discards uncommitted changes
```

# Key Takeaways

1. `UPDATE` affecting zero rows is **not automatically an exception**.
2. Use `FOUND` to detect zero-row updates.
3. Use `RAISE EXCEPTION` when you want to deliberately create an error.
4. Prefer specific exception handlers when the expected error is known.
5. `SQLSTATE` is more reliable than `SQLERRM` for programmatic error handling.
6. `GET STACKED DIAGNOSTICS` provides detailed exception information.
7. `RAISE;` re-throws the original exception.
8. `RAISE EXCEPTION` creates a new/custom error.
9. Procedures can perform transaction control under PostgreSQL's restrictions.
10. Each `COMMIT` makes preceding changes permanent.
```