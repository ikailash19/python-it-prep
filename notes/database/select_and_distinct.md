# PostgreSQL - SELECT & DISTINCT

## SELECT

`SELECT` is used to retrieve data from one or more tables.

### Retrieve all columns

```sql
SELECT *
FROM movies;
```

### Retrieve specific columns

```sql
SELECT
    movie_id,
    title,
    rating
FROM movies;
```

## Why avoid SELECT * in production?

Instead of retrieving every column, only retrieve the data required by the API.

Benefits:

- Reduces unnecessary data transfer
- Uses less memory
- Improves readability
- Makes queries easier to maintain
- Scales better as tables grow

---

# DISTINCT

`DISTINCT` removes duplicate values from the selected columns.

Example:

```sql
SELECT DISTINCT
    language_id
FROM movies;
```

---

# Source of Truth

Every piece of data should have one authoritative owner.

Examples:

- movie_languages → Languages
- movie_genres → Genres
- movies → Movie information

Applications should query the source of truth whenever possible.

---

# Lookup Table

A lookup table stores predefined reference data that other tables access using foreign keys.

Examples:

- movie_languages
- movie_genres
- user_roles
- booking_status
- payment_status

Benefits:

- Eliminates duplicate data
- Ensures consistency
- Enforces referential integrity
- Simplifies future changes

Use lookup tables when the list of values may evolve over time.