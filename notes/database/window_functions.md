# PostgreSQL - Window Functions

## What are Window Functions?

Window Functions perform calculations across a window of rows while preserving the individual rows in the result set.

Unlike `GROUP BY`, Window Functions do not aggregate away the individual records.

---

## OVER()

The `OVER()` clause defines the window on which the Window Function operates.

Example:

```sql
ROW_NUMBER() OVER (ORDER BY rating DESC)
```

---

## ROW_NUMBER()

Assigns a unique sequential number to every row.

```sql
SELECT
    title,
    ROW_NUMBER() OVER
    (
        ORDER BY rating DESC
    ) AS row_num
FROM movies;
```

---

## RANK()

Assigns the same rank to tied rows and skips the next rank.

Example:

```
10 -> 1
9  -> 2
9  -> 2
8  -> 4
```

---

## DENSE_RANK()

Assigns the same rank to tied rows but does not skip ranks.

Example:

```
10 -> 1
9  -> 2
9  -> 2
8  -> 3
```

---

## PARTITION BY

Divides rows into independent groups while preserving all rows.

Each Window Function is calculated separately within each partition.

Example:

```sql
AVG(rating) OVER
(
    PARTITION BY language_id
)
```

---

## Running Total

```sql
SUM(rating) OVER
(
    ORDER BY rating
    ROWS BETWEEN UNBOUNDED PRECEDING
    AND CURRENT ROW
)
```

Calculates a cumulative total.

---

## AVG() OVER()

Calculates averages while preserving all rows.

Example:

```sql
AVG(rating) OVER
(
    PARTITION BY language_id
)
```

---

## LAG()

Returns the value from the previous row within the current window.

Example:

```sql
LAG(title) OVER
(
    ORDER BY release_date
)
```

---

## LEAD()

Returns the value from the next row within the current window.

Example:

```sql
LEAD(title) OVER
(
    ORDER BY release_date
)
```

---

## FIRST_VALUE()

Returns the value from the first row of the current window.

Example:

```sql
FIRST_VALUE(title) OVER
(
    ORDER BY rating DESC
)
```

Can also be used with ascending order to obtain the minimum value.

---

## LAST_VALUE()

Returns the value from the last row of the current window frame.

By default, it considers rows only up to the current row, so it often behaves differently than expected.

To consider the entire partition:

```sql
LAST_VALUE(title) OVER
(
    ORDER BY rating DESC
    ROWS BETWEEN UNBOUNDED PRECEDING
    AND UNBOUNDED FOLLOWING
)
```

---

## GROUP BY vs PARTITION BY

### GROUP BY

- Aggregates rows
- Individual rows are lost

### PARTITION BY

- Divides rows into groups
- Preserves every row
- Window Functions are calculated independently for each partition

---

## Top N per Group Pattern

```sql
WITH ranked_movies AS
(
    SELECT
        title,
        language_id,
        ROW_NUMBER() OVER
        (
            PARTITION BY language_id
            ORDER BY rating DESC
        ) AS row_num
    FROM movies
)

SELECT *
FROM ranked_movies
WHERE row_num <= 3;
```

This is the standard SQL approach for retrieving the Top N records within each group.

---

## Key Takeaways

- Window Functions preserve individual rows.
- `OVER()` defines the window.
- `PARTITION BY` creates independent windows.
- `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` are used for ranking.
- `SUM() OVER()` is commonly used for running totals.
- `LAG()` returns the previous row.
- `LEAD()` returns the next row.
- `FIRST_VALUE()` returns the first value in the window.
- `LAST_VALUE()` returns the last value in the current window frame.