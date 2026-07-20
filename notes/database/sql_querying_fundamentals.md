# SQL Querying Fundamentals

## LIKE

Used for pattern matching.

### Wildcards

`%`
- Matches zero or more characters.

Examples:

```sql
SELECT *
FROM movies
WHERE title LIKE 'A%';
```

Starts with A.

```sql
SELECT *
FROM movies
WHERE title LIKE '%man%';
```

Contains "man".

`_`
- Matches exactly one character.

Example:

```sql
SELECT *
FROM movies
WHERE title LIKE 'A__';
```

Matches exactly three-character titles starting with A.

### ILIKE (PostgreSQL)

Case-insensitive version of LIKE.

```sql
SELECT *
FROM movies
WHERE title ILIKE '%avengers%';
```

---

## NULL

NULL represents an unknown or missing value.

Never compare NULL using `=`.

Incorrect:

```sql
WHERE release_date = NULL;
```

Correct:

```sql
WHERE release_date IS NULL;
```

```sql
WHERE release_date IS NOT NULL;
```

---

## ORDER BY

Sort query results.

Ascending:

```sql
ORDER BY rating ASC;
```

Descending:

```sql
ORDER BY rating DESC;
```

Multiple columns:

```sql
ORDER BY rating DESC,
         title ASC;
```

---

## LIMIT

Limits the number of rows returned.

```sql
SELECT *
FROM movies
ORDER BY rating DESC
LIMIT 10;
```

---

## OFFSET

Skips rows before returning results.

```sql
SELECT *
FROM movies
ORDER BY movie_id
LIMIT 10
OFFSET 20;
```

Pagination formula:

```
OFFSET = (Page - 1) × Page Size
```

---

## AS (Aliases)

Temporary column names.

```sql
SELECT
    title AS Movie_Name,
    rating AS IMDb_Rating
FROM movies;
```

Aliases do not rename the actual database columns.

---

## Key Learnings

- Filter as much as possible inside SQL.
- Always use ORDER BY with LIMIT/OFFSET.
- LIKE is commonly used for search features.
- Use IS NULL instead of = NULL.
- LIMIT improves performance by returning only required rows.
- OFFSET enables pagination.
- SQL aliases improve readability without modifying schema.