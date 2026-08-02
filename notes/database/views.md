# Views

## What is a View?

A View is a virtual table based on the result of a SQL query.

A View stores only the SQL query definition, not the actual data.

Whenever a View is queried, PostgreSQL executes the underlying query and returns the latest data.

---

## Why do we use Views?

- Reduce code duplication
- Improve maintainability
- Simplify complex SQL queries
- Improve readability
- Hide sensitive columns
- Single Source of Truth (SSOT)

---

## Create a View

```sql
CREATE VIEW movie_details AS
SELECT
    movie_id,
    title
FROM movies;
```

Query a View:

```sql
SELECT * FROM movie_details;
```

---

## Virtual Table

A View behaves like a table but does not physically store data.

It stores only the SQL query definition.

Physical Table

- Stores data
- Occupies storage

View

- Stores SQL query definition
- Does not store data
- Behaves like a table

---

## Data Changes vs Schema Changes

### Data Changes

Examples

- INSERT
- UPDATE
- DELETE

Automatically reflected in the View because the View executes the underlying query every time.

### Schema Changes

Examples

- Rename column
- Drop column
- Modify table structure

Not automatically reflected.

The View must be recreated or updated.

---

## Updatable Views

Simple Views created from a single table are generally updatable.

Example

```sql
CREATE VIEW movie_basic AS
SELECT
    movie_id,
    title,
    language_id
FROM movies;
```

Generally supports

- INSERT
- UPDATE
- DELETE

Reason:

PostgreSQL clearly knows which table should be modified.

---

## Non-Updatable Views

Views created using

- JOIN
- GROUP BY
- HAVING
- DISTINCT
- Aggregate Functions
- UNION

are generally not updatable.

Reason:

PostgreSQL cannot determine which underlying table should be modified.

---

## Materialized View

A Materialized View stores the result of a query physically.

Unlike a normal View, it stores data.

Example

```sql
CREATE MATERIALIZED VIEW movie_statistics AS
SELECT ...
```

Refresh using

```sql
REFRESH MATERIALIZED VIEW movie_statistics;
```

---

## View vs Materialized View

| Feature | View | Materialized View |
|---------|------|-------------------|
| Stores Query Definition | Yes | Yes |
| Stores Data | No | Yes |
| Latest Data | Always | Only after Refresh |
| Query Speed | Slower | Faster |
| Storage Required | No | Yes |

---

# Advantages

- Code reuse
- Easier maintenance
- Better readability
- Additional security
- Single Source of Truth

---

# Limitations

- Complex Views are generally not updatable.
- Normal Views execute the query every time.
- Materialized Views require refresh to get latest data.

---

# Interview Questions

1. What is a View?
2. Why is a View called a Virtual Table?
3. Difference between View and Table.
4. Difference between View and Materialized View.
5. Can Views be updated?
6. What makes a View non-updatable?
7. What are the advantages of Views?
8. Explain Data Changes vs Schema Changes.
9. What is a Materialized View?
10. When would you use a Materialized View?