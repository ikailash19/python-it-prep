# PostgreSQL Functions — Pending Notes

# 1. PostgreSQL Functions

A PostgreSQL function is reusable database-side logic that can:

- accept parameters
- perform SQL/procedural operations
- return a result

Basic structure:

```sql
CREATE FUNCTION function_name(parameter_name data_type)
RETURNS return_data_type
LANGUAGE SQL
AS $$
    SELECT ...;
$$;
```

A function can be called from SQL:

```sql
SELECT get_rating(8);
```

---

# 2. Scalar Functions

A **scalar function returns one value**.

Examples:

- one movie rating
- one movie title
- one calculated price
- one tax amount

Example:

```sql
CREATE FUNCTION get_rating(p_movie_id INT)
RETURNS NUMERIC
LANGUAGE SQL
AS $$
    SELECT rating
    FROM movies
    WHERE movie_id = p_movie_id;
$$;
```

Call:

```sql
SELECT get_rating(8);
```

Mental model:

> **Scalar = one value.**

## Scalar expression

A **scalar expression** is an expression that produces a single value.

Examples:

```sql
price * 0.90
```

```sql
rating + 1
```

```sql
get_rating(8)
```

---

# 3. Set-Returning Functions

A set-returning function can return **multiple rows** instead of one scalar value.

Example:

```sql
CREATE FUNCTION get_movies_by_rating(p_min_rating INT)
RETURNS TABLE(
    title TEXT,
    rating INT
)
LANGUAGE SQL
AS $$
    SELECT title, rating
    FROM movies
    WHERE rating >= p_min_rating;
$$;
```

Call:

```sql
SELECT *
FROM get_movies_by_rating(6);
```

Mental model:

```text
Scalar function
    ↓
one value

Set-returning function
    ↓
multiple rows / result set
```

---

# 4. `RETURNS TABLE`

`RETURNS TABLE` allows a function to define the columns of its returned result.

Example:

```sql
CREATE FUNCTION get_movie_details(p_movie_id INT)
RETURNS TABLE(
    movie_title TEXT,
    movie_rating INT,
    movie_duration INT
)
LANGUAGE SQL
AS $$
    SELECT
        title,
        rating,
        duration_minutes
    FROM movies
    WHERE movie_id = p_movie_id;
$$;
```

Call:

```sql
SELECT *
FROM get_movie_details(11);
```

The returned columns are:

```text
movie_title
movie_rating
movie_duration
```

This is useful when a function needs to return multiple attributes belonging to a record.

---

# 5. Functions Returning Multiple Rows

A function can return multiple records based on a condition.

Example:

```sql
CREATE FUNCTION get_movies_by_rating(p_min_rating INT)
RETURNS TABLE(
    title TEXT,
    rating INT
)
LANGUAGE SQL
AS $$
    SELECT title, rating
    FROM movies
    WHERE rating >= p_min_rating;
$$;
```

Call:

```sql
SELECT *
FROM get_movies_by_rating(6);
```

The result is a **set of rows**, not a single scalar value.

---

# 6. Functions and DML

PostgreSQL functions can perform database operations such as:

- `INSERT`
- `UPDATE`
- `DELETE`

They are not limited to `SELECT`.

The function's return type should match what the function is designed to return.

A useful design question is:

> Is this operation naturally a reusable calculation/query that should return a result?

If yes, a function can be a good fit.

---

# 7. Database vs Application-Side Calculation

Consider:

```text
discount_amount = (discount_percentage / 100) * price
final_price = price - discount_amount
```

The calculation can belong in either the application or database depending on the requirement.

### Application server can be appropriate when:

- the calculation is primarily application business logic
- the rules change frequently
- the calculation needs application state/services
- the result is mainly consumed by the application

### Database function can be appropriate when:

- the required data is already in PostgreSQL
- the same rule must be reused consistently
- multiple applications need the same database-side rule
- keeping the calculation near the data is beneficial

There is no universal rule that every calculation belongs in the database or application.

Consider **ownership, reuse, consistency, data locality, and maintainability**.

---

# 8. Function Parameter Naming

Prefer parameter names that clearly distinguish them from table columns.

Example:

```sql
CREATE FUNCTION get_rating(p_movie_id INT)
```

Then:

```sql
WHERE movie_id = p_movie_id
```

Using a prefix such as `p_` makes it obvious that `p_movie_id` is a function parameter.

---

# 9. Function vs Procedure — Initial Mental Model

We started distinguishing these concepts:

### Function

A function is designed around **returning a result**.

Example:

```sql
SELECT get_rating(8);
```

### Procedure

A procedure is designed around **performing an operation/workflow** and is invoked with:

```sql
CALL procedure_name(...);
```

Useful initial mental model:

```text
Function
    → calculate/query
    → return result


Procedure
    → perform operation/workflow
    → result is not the primary purpose
```

This is a practical rule of thumb, not an absolute limitation of PostgreSQL.

---

# 10. Key Takeaways

1. **Scalar function** → returns one value.
2. **Set-returning function** → returns multiple rows.
3. `RETURNS TABLE` → defines the columns of the returned result set.
4. A function can execute SQL and perform DML such as `INSERT`, `UPDATE`, and `DELETE`.
5. `SELECT function_name(...)` is commonly used when a function returns a value.
6. Use clear parameter names such as `p_movie_id`.
7. Database-side vs application-side calculations should be decided using ownership, reuse, consistency, data locality, and maintainability.
8. Function vs procedure is primarily about the intended interaction: **returning a result vs performing an operation/workflow**.

---
