# Common Table Expressions (CTEs)

## What is a CTE?

CTE stands for Common Table Expression.

A CTE is a temporary named result set created using the WITH clause that exists only for the duration of a single SQL statement.

It helps simplify complex SQL queries by breaking them into smaller, logical steps.

---

## Syntax

```sql
WITH cte_name AS
(
    SELECT ...
)
SELECT *
FROM cte_name;
```

---

## Why do we use CTEs?

- Improve readability
- Improve maintainability
- Simplify complex nested queries
- Organize SQL into logical steps
- Reuse intermediate results within the same SQL statement

---

## Why is a CTE temporary?

A CTE exists only during the execution of a single SQL statement.

Once the SQL statement finishes execution, PostgreSQL automatically removes the CTE from memory.

If the same result is required across multiple queries, use a View instead.

---

## Single SQL Statement

Example:

```sql
WITH average_rating AS
(
    SELECT AVG(rating) AS avg_rating
    FROM movies
)
SELECT *
FROM movies
WHERE rating >
(
    SELECT avg_rating
    FROM average_rating
);
```

Although there are two SELECT statements inside the query, the entire block is considered one SQL statement because the WITH clause is part of the final SELECT statement.

---

## Multiple CTEs

Multiple CTEs can be created within the same SQL statement.

Each CTE can:

- Be independent
- Use a previous CTE
- Be used by the final query

Example:

```sql
WITH movie_count AS
(
    SELECT COUNT(*) AS total_movies
    FROM movies
),

average_rating AS
(
    SELECT AVG(rating) AS avg_rating
    FROM movies
),

active_movies AS
(
    SELECT COUNT(*) AS active_movies
    FROM movies
    WHERE is_active = TRUE
)

SELECT
    total_movies,
    avg_rating,
    active_movies
FROM movie_count,
     average_rating,
     active_movies;
```

---

## Chained CTEs

CTEs can depend on previous CTEs.

Example Flow:

movies
↓

average_rating
↓

high_rated_movies
↓

sorted_movies
↓

Final SELECT

This is similar to calling helper functions or using intermediate variables in programming.

---

## Recursive CTE

A Recursive CTE is a CTE that references itself repeatedly until a stopping condition is met.

Used for hierarchical or tree-structured data.

Common use cases:

- Employee hierarchy
- Manager hierarchy
- Folder structure
- Category tree
- Family tree
- Bill of Materials

---

## CTE vs View

| Feature | CTE | View |
|---------|-----|------|
| Lifetime | Single SQL Statement | Permanent until dropped |
| Stores | Temporary Result Set | SQL Query Definition |
| Reusable | No | Yes |
| Storage Required | Temporary Memory | Metadata Only |

---

## Advantages

- Cleaner SQL
- Better readability
- Better maintainability
- Easier debugging
- Reduces deeply nested subqueries
- Supports modular query design

---

## Limitations

- Exists only for one SQL statement
- Cannot be reused across multiple queries
- Not a replacement for Views

---

# Interview Questions

1. What is a CTE?
2. Why do we use CTEs?
3. Difference between a CTE and a View.
4. Why does a CTE exist only for one SQL statement?
5. Can one CTE reference another CTE?
6. Can multiple CTEs exist in one query?
7. When would you choose a CTE over a View?
8. What is a Recursive CTE?
9. Give real-world use cases of Recursive CTEs.
10. Explain how CTEs improve software engineering.