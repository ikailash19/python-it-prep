# SQL Indexes

## Why do Indexes exist?

Without an index, PostgreSQL performs a Sequential Scan (Full Table Scan), checking rows one by one until it finds the required data.

Example:

```sql
SELECT *
FROM movies
WHERE movie_id = 8531912;
```

Without an index, PostgreSQL scans the table row by row.

Indexes improve data retrieval by allowing PostgreSQL to locate rows efficiently instead of scanning the entire table.

Book analogy:

Without Index:
- Read every page.

With Index:
- Find the topic in the index.
- Jump directly to the required page.

---

# Sequential Scan

Sequential Scan (Seq Scan) means PostgreSQL reads every row in the table.

Usually happens when:

- No index exists.
- Table is very small.
- Query returns most of the table.
- Optimizer decides Seq Scan is cheaper.

---

# Index Scan

Index Scan uses an index to quickly locate matching rows.

Useful when queries return only a small number of rows.

Example:

```sql
SELECT *
FROM movies
WHERE movie_id = 100;
```

---

# Why not create indexes on every column?

Indexes improve:

- SELECT

Indexes slow down:

- INSERT
- UPDATE
- DELETE

because PostgreSQL must maintain every index whenever data changes.

Indexes also consume additional storage.

Create indexes only on frequently searched, filtered, joined or sorted columns.

---

# Creating an Index

Syntax:

```sql
CREATE INDEX index_name
ON table_name(column_name);
```

Example:

```sql
CREATE INDEX idx_movies_title
ON movies(title);
```

Naming Convention:

```
idx_<table>_<column>
```

Example:

```
idx_movies_title
idx_movies_release_date
```

---

# Dropping an Index

Syntax:

```sql
DROP INDEX index_name;
```

Example:

```sql
DROP INDEX idx_movies_title;
```

---

# Primary Key Index

Primary Keys automatically create a Unique Index.

Example:

```sql
movie_id PRIMARY KEY
```

No need to manually create another index.

---

# Foreign Key Index

Foreign Keys are frequently used in:

- JOIN
- WHERE
- Filtering

Good candidates:

- language_id
- genre_id

---

# Unique Index

Unique Index:

- Improves search performance.
- Prevents duplicate values.

Example:

```sql
CREATE UNIQUE INDEX idx_users_email
ON users(email);
```

Useful for:

- email
- username
- phone_number

Do not use for:

- rating
- release_date
- movie_title

unless business rules require uniqueness.

---

# Composite Index

A Composite Index contains multiple columns.

Example:

```sql
CREATE INDEX idx_language_genre
ON movies(language_id, genre_id);
```

Useful when multiple columns are frequently queried together.

Example:

```sql
SELECT *
FROM movies
WHERE language_id = 1
AND genre_id = 3;
```

Instead of two separate indexes, a composite index can optimize this query.

---

# EXPLAIN

Purpose:

Shows PostgreSQL's execution plan.

Syntax:

```sql
EXPLAIN
SELECT *
FROM movies
WHERE title = 'Leo';
```

EXPLAIN helps understand how PostgreSQL plans to execute a query.

Common outputs:

```
Seq Scan
```

or

```
Index Scan
```

---

# Why PostgreSQL may ignore an Index

Having an index does not guarantee PostgreSQL will use it.

Possible reasons:

- Small table.
- Query returns a large percentage of rows.
- Sequential Scan has lower estimated cost.

The PostgreSQL Query Optimizer always chooses the cheapest execution plan.

---

# Choosing Columns for Indexes

Good candidates:

- Primary Keys
- Foreign Keys
- Frequently searched columns
- Frequently filtered columns
- Frequently sorted columns
- Frequently joined columns

Examples:

- movie_id
- title
- language_id
- genre_id
- release_date
- rating (if often filtered/sorted)

Avoid indexing:

- Large text columns (description)
- Rarely used columns

---

# API-driven Index Design

API:

GET /movies/{id}

Index:

movie_id

----------------------------------

API:

GET /movies?language=tamil

Index:

language_id

----------------------------------

API:

GET /movies?genre=action

Index:

genre_id

----------------------------------

API:

GET /movies?search=leo

Index:

title

----------------------------------

API:

GET /movies/latest

Index:

release_date

----------------------------------

API:

GET /movies/top-rated

Index:

rating

---

# Interview Tips

- Indexes improve read performance.
- Indexes slow down write operations.
- Primary Keys automatically create a Unique Index.
- Foreign Keys are good indexing candidates.
- Composite Indexes optimize multi-column queries.
- Use EXPLAIN to view PostgreSQL's execution plan.
- PostgreSQL may ignore an index if Sequential Scan is cheaper.
- Create indexes based on query patterns, not simply because a column exists.