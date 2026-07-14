# PostgreSQL - Table Constraints and Referential Integrity

## GENERATED ALWAYS AS IDENTITY
- Auto-generates integer IDs.
- Modern replacement for SERIAL.

## NOT NULL
- Prevents NULL values.

## DEFAULT
- Assigns a value when none is provided.
- Example:
  - seat_type = 'chair'
  - is_booked = FALSE

## UNIQUE Constraint
- Prevents duplicate values.

Example:
UNIQUE(movie_id, seat_name)

Meaning:
- A1 can exist in Movie 1
- A1 can exist in Movie 2
- A1 cannot exist twice in Movie 1

## Foreign Key
- Ensures referenced parent row exists.

Example:
movie_id REFERENCES movies(movie_id)

## Referential Integrity
The database prevents:
- Invalid movie_id values
- Deleting parent rows while child rows exist (default RESTRICT behavior)

## Constraint Errors Learned
- Duplicate UNIQUE constraint violation
- Foreign key violation
- Delete restricted by foreign key