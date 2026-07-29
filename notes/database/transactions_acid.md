# Transactions & ACID

## What is a Transaction?

A transaction is a group of one or more SQL operations that are executed as a single unit of work.

A transaction ensures that either:
- All operations succeed.
- All operations fail and are rolled back.

### Example

Movie Ticket Booking:

1. Create Booking
2. Reserve Seat
3. Process Payment

If payment fails, the entire transaction should be rolled back.

---

## Transaction Commands

### BEGIN

Starts a new transaction.

```sql
BEGIN;
```

---

### COMMIT

Permanently saves all changes made during the transaction.

```sql
COMMIT;
```

---

### ROLLBACK

Cancels all changes made during the current transaction.

```sql
ROLLBACK;
```

---

# ACID Properties

ACID is a set of four properties that ensure reliable and consistent database transactions.

- Atomicity
- Consistency
- Isolation
- Durability

---

## 1. Atomicity

### Definition

Atomicity ensures that all operations inside a transaction either complete successfully or none of them are applied.

### Example

Bank Transfer

1. Debit ₹500 from Account A
2. Credit ₹500 to Account B

If the second operation fails, the first operation is also rolled back.

### Key Points

- All or Nothing
- No Partial Transactions
- Failed transactions are rolled back

---

## 2. Consistency

### Definition

Consistency ensures that the database always remains in a valid state before and after a transaction.

### Example

Movie Ticket Booking

Available Seats = 10

Booking 2 tickets

Available Seats = 8

The database remains valid.

Incorrect Example:

Available Seats = -1

This violates business rules and breaks consistency.

### Key Points

- Preserves business rules
- Preserves constraints
- Database always remains valid

---

## 3. Isolation

### Definition

Isolation ensures that concurrent transactions do not interfere with each other.

Each transaction behaves as if it is running alone.

### Example

There is only one seat left.

Two users attempt to book it simultaneously.

Without Isolation:

- Both users may successfully book the same seat.

With Isolation:

- Only one booking succeeds.

### Key Points

- Prevents transaction interference
- Supports concurrent users safely
- Prevents concurrency problems

---

## Concurrency Problems

### Dirty Read

### Definition

Occurs when one transaction reads data that has been modified by another transaction but has not yet been committed.

If the other transaction rolls back, the first transaction has read invalid data.

### Example

Transaction A

```text
BEGIN

Balance = ₹10,000

Update Balance = ₹5,000

(Not Committed)
```

Transaction B reads:

```text
₹5,000
```

Transaction A:

```text
ROLLBACK
```

Actual Balance:

```text
₹10,000
```

Transaction B read uncommitted data.

---

### Non-Repeatable Read

### Definition

Occurs when the same transaction reads the same row multiple times and gets different values because another transaction modified and committed the row.

### Example

Transaction A

```text
Read Balance

₹10,000
```

Transaction B

```text
Update Balance

₹8,000

COMMIT
```

Transaction A

```text
Read Balance

₹8,000
```

Same row.

Different value.

---

### Phantom Read

### Definition

Occurs when the same transaction executes the same query twice and gets a different set of rows because another transaction inserted, deleted or updated rows matching the query.

### Example

Transaction A

```sql
SELECT *
FROM bookings
WHERE movie_id = 1;
```

Result:

```text
3 Rows
```

Transaction B

```text
INSERT New Booking

COMMIT
```

Transaction A

```sql
SELECT *
FROM bookings
WHERE movie_id = 1;
```

Result:

```text
4 Rows
```

Same query.

Different number of rows.

---

## Isolation Levels

Isolation Levels determine how much protection PostgreSQL provides against concurrent transaction problems.

Higher Isolation

- More Safety
- Less Concurrency
- Potentially Lower Throughput

Lower Isolation

- Less Safety
- Higher Concurrency
- Better Throughput

---

### Read Uncommitted

Weakest isolation level.

- Dirty Read ✅ Possible
- Non-Repeatable Read ✅ Possible
- Phantom Read ✅ Possible

> PostgreSQL treats Read Uncommitted the same as Read Committed because MVCC does not allow Dirty Reads.

---

### Read Committed (PostgreSQL Default)

Only committed data can be read.

- Dirty Read ❌ Prevented
- Non-Repeatable Read ✅ Possible
- Phantom Read ✅ Possible

---

### Repeatable Read

Ensures the same row always returns the same value during a transaction.

- Dirty Read ❌ Prevented
- Non-Repeatable Read ❌ Prevented
- Phantom Read ⚠ Mostly Prevented in PostgreSQL

---

### Serializable

Highest isolation level.

Transactions behave as if they are executed one after another.

- Dirty Read ❌ Prevented
- Non-Repeatable Read ❌ Prevented
- Phantom Read ❌ Prevented

---

## 4. Durability

### Definition

Once a transaction is committed, its changes are permanently stored and survive crashes, power failures and server restarts.

### Example

Movie Ticket Booking

Booking Confirmed

Immediately after confirmation,

Server crashes.

After restart,

Booking still exists.

---

## Write-Ahead Logging (WAL)

### Definition

Write-Ahead Logging (WAL) is PostgreSQL's mechanism that records changes in a log before updating the actual database files.

During crash recovery PostgreSQL uses WAL to restore committed transactions.

### Flow

```text
BEGIN
   │
Execute SQL
   │
Write to WAL
   │
COMMIT
   │
Update Database Files
```

### Key Points

- Ensures Durability
- Enables Crash Recovery
- Prevents Data Loss

---

# Interview Tips

## ACID

| Property | Purpose |
|----------|---------|
| Atomicity | All operations succeed or rollback together |
| Consistency | Database always remains valid |
| Isolation | Concurrent transactions do not interfere |
| Durability | Committed data survives crashes |

---

## Concurrency Problems

| Problem | Description |
|----------|-------------|
| Dirty Read | Read uncommitted data |
| Non-Repeatable Read | Same row returns different values |
| Phantom Read | Same query returns different rows |

---

## PostgreSQL Default Isolation Level

```text
Read Committed
```

Prevents:

- Dirty Read

Still Allows:

- Non-Repeatable Read
- Phantom Read

---

# Important Interview Questions

1. What is a transaction?
2. Difference between COMMIT and ROLLBACK.
3. Explain ACID properties with examples.
4. What is Atomicity?
5. What is Consistency?
6. What is Isolation?
7. What is Durability?
8. Explain Dirty Read.
9. Explain Non-Repeatable Read.
10. Explain Phantom Read.
11. Difference between Dirty Read and Non-Repeatable Read.
12. Difference between Non-Repeatable Read and Phantom Read.
13. What are Isolation Levels?
14. What is PostgreSQL's default isolation level?
15. What is WAL?
16. How does PostgreSQL recover after a crash?