# SQL JOINs

## Why JOINs?

Normalization stores related data in separate tables to avoid duplication.

Example:

movies
- movie_id
- title
- language_id
- genre_id

movie_languages
- language_id
- language

movie_genre
- genre_id
- genre

JOIN combines related data from multiple tables using a common column.

---

# INNER JOIN

Returns only matching records from both tables.

Example:

```sql
SELECT
    m.title,
    ml.language
FROM movies m
INNER JOIN movie_languages ml
ON m.language_id = ml.language_id;
```

Use Case:
- Show movies with their language.
- Show bookings with users.
- Show orders with customers.

---

# Multiple INNER JOINs

A query can join multiple tables.

Example:

```sql
SELECT
    m.title,
    ml.language,
    mg.genre
FROM movies m
INNER JOIN movie_languages ml
ON m.language_id = ml.language_id
INNER JOIN movie_genre mg
ON m.genre_id = mg.genre_id;
```

Each INNER JOIN joins one table.

---

# Table Aliases

Aliases improve readability.

Example:

```sql
movies            -> m
movie_languages   -> ml
movie_genre       -> mg
```

Instead of

```sql
movies.title
```

use

```sql
m.title
```

Production code almost always uses aliases.

---

# LEFT JOIN

Returns:

- All rows from LEFT table
- Matching rows from RIGHT table

If no matching row exists, RIGHT table columns become NULL.

Example:

```sql
SELECT
    ml.language,
    m.title
FROM movie_languages ml
LEFT JOIN movies m
ON ml.language_id = m.language_id;
```

Use LEFT JOIN when the business requirement says:

- Show all languages
- Show all genres
- Show all users
- Show all categories

The table that must never disappear should be placed on the LEFT.

---

# RIGHT JOIN

Returns:

- All rows from RIGHT table
- Matching rows from LEFT table

Example:

```sql
FROM movies
RIGHT JOIN movie_languages
```

RIGHT JOIN is functionally equivalent to LEFT JOIN by swapping table positions.

Most production code prefers LEFT JOIN because it is easier to read.

---

# FULL OUTER JOIN

Returns:

- All rows from LEFT table
- All rows from RIGHT table

Matching rows are combined.

Non-matching rows contain NULL for missing columns.

Example:

```sql
SELECT
    ml.language,
    m.title
FROM movie_languages ml
FULL OUTER JOIN movies m
ON ml.language_id = m.language_id;
```

Use Case:
Reports, data reconciliation, migration validation.

---

# Choosing the Correct JOIN

Requirement:
Show only matching records

JOIN:
INNER JOIN

------------------------------------

Requirement:
Show all movies

LEFT:
movies

JOIN:
LEFT JOIN

------------------------------------

Requirement:
Show all languages

LEFT:
movie_languages

JOIN:
LEFT JOIN

------------------------------------

Requirement:
Show all genres

LEFT:
movie_genre

JOIN:
LEFT JOIN

------------------------------------

Requirement:
Show everything

JOIN:
FULL OUTER JOIN

---

# JOIN + WHERE

WHERE filters rows after JOIN.

Example:

```sql
SELECT
    m.title,
    ml.language
FROM movies m
INNER JOIN movie_languages ml
ON m.language_id = ml.language_id
WHERE m.is_active = TRUE;
```

---

# JOIN + GROUP BY

Example:

```sql
SELECT
    ml.language,
    COUNT(m.movie_id)
FROM movie_languages ml
LEFT JOIN movies m
ON ml.language_id = m.language_id
GROUP BY ml.language;
```

---

# JOIN + HAVING

Example:

```sql
SELECT
    ml.language
FROM movie_languages ml
LEFT JOIN movies m
ON ml.language_id = m.language_id
GROUP BY ml.language
HAVING COUNT(m.movie_id) >= 2;
```

---

# COUNT(*) vs COUNT(column)

COUNT(*)

Counts every row.

COUNT(column)

Counts only NON-NULL values.

With LEFT JOIN:

Use

```sql
COUNT(m.movie_id)
```

instead of

```sql
COUNT(*)
```

to correctly count related rows.

---

# Interview Tips

- JOIN combines related tables.
- INNER JOIN returns matching records only.
- LEFT JOIN preserves LEFT table.
- RIGHT JOIN preserves RIGHT table.
- FULL OUTER JOIN preserves both tables.
- Decide JOIN type based on the business requirement.
- Use aliases in production code.
- Use COUNT(column) instead of COUNT(*) when counting related records after LEFT JOIN.