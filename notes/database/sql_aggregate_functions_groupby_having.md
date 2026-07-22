# SQL Aggregate Functions, GROUP BY and HAVING

## Aggregate Functions

Aggregate functions perform calculations across multiple rows and return a single value.

### COUNT()

Counts rows.

```sql
SELECT COUNT(*)
FROM movies;
```

Count active movies.

```sql
SELECT COUNT(*)
FROM movies
WHERE is_active = TRUE;
```

### COUNT(*) vs COUNT(column)

`COUNT(*)`

- Counts all rows.

`COUNT(column)`

- Counts only non-NULL values.

Example:

```sql
SELECT COUNT(release_date)
FROM movies;
```

Counts only movies that have a release date.

---

## SUM()

Adds numeric values.

```sql
SELECT SUM(duration_minutes)
FROM movies;
```

Example:

```sql
SELECT SUM(duration_minutes)
FROM movies
WHERE is_active = TRUE;
```

Real-world use cases

- Total booking amount
- Total revenue
- Total duration
- Total seats booked

---

## AVG()

Returns the average value.

```sql
SELECT AVG(rating)
FROM movies;
```

Example:

```sql
SELECT AVG(duration_minutes)
FROM movies
WHERE is_active = TRUE;
```

Important

`AVG()` ignores NULL values.

---

## MIN()

Returns the smallest value.

```sql
SELECT MIN(duration_minutes)
FROM movies;
```

Examples

- Shortest movie
- Earliest release date
- Lowest rating

---

## MAX()

Returns the largest value.

```sql
SELECT MAX(rating)
FROM movies;
```

Examples

- Highest rating
- Longest movie
- Latest release date

---

## Multiple Aggregate Functions

Multiple aggregate functions can be executed in one query.

```sql
SELECT
    COUNT(*) AS total_movies,
    AVG(rating) AS average_rating,
    MAX(rating) AS highest_rating,
    MIN(rating) AS lowest_rating
FROM movies;
```

This is preferred over making multiple database calls.

---

# GROUP BY

GROUP BY divides rows into groups.

Aggregate functions are then calculated separately for each group.

Example

```sql
SELECT
    language_id,
    COUNT(*) AS movie_count
FROM movies
GROUP BY language_id;
```

Average rating per language

```sql
SELECT
    language_id,
    AVG(rating) AS average_rating
FROM movies
GROUP BY language_id;
```

Highest rating per language

```sql
SELECT
    language_id,
    MAX(rating) AS highest_rating
FROM movies
GROUP BY language_id;
```

---

## GROUP BY Rule

Every non-aggregated column in SELECT must also appear in GROUP BY.

Correct

```sql
SELECT
    language_id,
    COUNT(*)
FROM movies
GROUP BY language_id;
```

Incorrect

```sql
SELECT
    title,
    COUNT(*)
FROM movies
GROUP BY language_id;
```

Reason

One language contains many movie titles.

PostgreSQL does not know which title should be returned for that group.

---

## GROUP BY with ORDER BY

```sql
SELECT
    language_id,
    COUNT(*) AS movie_count
FROM movies
GROUP BY language_id
ORDER BY movie_count DESC;
```

---

# HAVING

HAVING filters groups after aggregation.

Example

```sql
SELECT
    language_id,
    COUNT(*) AS movie_count
FROM movies
GROUP BY language_id
HAVING COUNT(*) > 10;
```

Average rating filter

```sql
SELECT
    language_id,
    AVG(rating) AS average_rating
FROM movies
GROUP BY language_id
HAVING AVG(rating) >= 8;
```

---

# WHERE vs HAVING

WHERE

- Filters individual rows.
- Executes before GROUP BY.

Example

```sql
SELECT *
FROM movies
WHERE is_active = TRUE;
```

HAVING

- Filters grouped results.
- Executes after GROUP BY and aggregate functions.

Example

```sql
SELECT
    language_id,
    COUNT(*)
FROM movies
GROUP BY language_id
HAVING COUNT(*) > 5;
```

Both together

```sql
SELECT
    language_id,
    AVG(rating) AS average_rating
FROM movies
WHERE is_active = TRUE
GROUP BY language_id
HAVING AVG(rating) >= 8.5;
```

---

# SQL Execution Order

SQL is written in this order

```
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

But PostgreSQL executes approximately in this order

```
FROM
↓
WHERE
↓
GROUP BY
↓
Aggregate Functions
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT
```

Understanding this execution order explains why aggregate functions cannot be used inside WHERE.

---

# Interview Tips

Use `COUNT(*)` when counting rows.

Use `COUNT(column)` only when NULL values should be ignored.

Filter rows with `WHERE`.

Filter aggregated results with `HAVING`.

Use aliases for readability.

Prefer a single query with multiple aggregate functions over multiple database calls whenever the aggregates operate on the same filtered dataset.

---

# Key Learnings

- Aggregate functions summarize data.
- GROUP BY creates groups before aggregation.
- HAVING filters groups after aggregation.
- WHERE filters rows before aggregation.
- SQL execution order is important for writing correct queries.
- Aggregate functions are heavily used in dashboards, reports, analytics, and backend APIs.