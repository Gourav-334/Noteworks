# TCS IPA SQL Cheat Sheet

> Focus: SQL fundamentals, CRUD operations, filtering, joins, aggregate functions, constraints, and common MCQs.

---

# 1. What is SQL?

- SQL = Structured Query Language

#### Used to:

- Store data
- Retrieve data
- Update data
- Delete data

Works with Relational Databases.

#### Examples:

- MySQL
- PostgreSQL
- Oracle
- SQL Server

---

# 2. Database Terms

Database
↓
Table
↓
Row (Record)
↓
Column (Field)

---

# 3. Data Types

```
INT
FLOAT
DOUBLE
DECIMAL
CHAR
VARCHAR
DATE
TIME
DATETIME
BOOLEAN
```

---

# 4. Create Table

```sql
CREATE TABLE Student (
    id INT,
    name VARCHAR(50),
    age INT
);
```

---

# 5. Insert Data

```sql
INSERT INTO Student
VALUES
(1,'John',20);
```

---

# 6. Select Data

```sql
SELECT * FROM Student;
```

#### Specific columns:

```sql
SELECT name, age
FROM Student;
```

---

# 7. WHERE Clause

```sql
SELECT *
FROM Student
WHERE age > 18;
```

Operators

```
=
!=
<
>
<=
>=
```

---

# 8. Logical Operators

```
AND
OR
NOT
```

Example

```sql
WHERE age > 18
AND city='Delhi'
```

---

# 9. ORDER BY

Ascending

```sql
ORDER BY age ASC;
```

Descending

```sql
ORDER BY age DESC;
```

---

# 10. DISTINCT

Remove duplicates

```sql
SELECT DISTINCT city
FROM Student;
```

---

# 11. LIMIT

```sql
SELECT *
FROM Student
LIMIT 5;
```

---

# 12. Aggregate Functions

```
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Example

```sql
SELECT AVG(salary)
FROM Employee;
```

---

# 13. GROUP BY

Groups rows having the same value.

```sql
SELECT department,
COUNT(*)
FROM Employee
GROUP BY department;
```

---

# 14. HAVING

Filter groups.

```sql
SELECT department,
COUNT(*)
FROM Employee
GROUP BY department
HAVING COUNT(*) > 5;
```

---

# 15. UPDATE

```sql
UPDATE Student
SET age = 21
WHERE id = 1;
```

---

# 16. DELETE

```sql
DELETE FROM Student
WHERE id = 1;
```

---

# 17. TRUNCATE

Deletes all rows.

```sql
TRUNCATE TABLE Student;
```

Table remains.

---

# 18. DROP

Deletes entire table.

```sql
DROP TABLE Student;
```

---

# 19. ALTER

Add column

```sql
ALTER TABLE Student
ADD email VARCHAR(50);
```

---

# 20. Primary Key

- Unique
- NOT NULL
- One per table

```sql
PRIMARY KEY(id)
```

---

# 21. Foreign Key

Links two tables.

```sql
FOREIGN KEY(dept_id)
REFERENCES Department(id)
```

---

# 22. Constraints

```
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
CHECK
DEFAULT
```

---

# 23. NULL

Check

```sql
IS NULL
```

Not null

```sql
IS NOT NULL
```

---

# 24. LIKE

```
%
Any number of characters

_
Exactly one character
```

#### Examples:

Starts with A

```sql
LIKE 'A%'
```

Ends with A

```sql
LIKE '%A'
```

Contains A

```sql
LIKE '%A%'
```

---

# 25. IN

```sql
WHERE city
IN ('Delhi','Mumbai')
```

---

# 26. BETWEEN

```sql
WHERE salary
BETWEEN 30000
AND 50000
```

---

# 27. JOIN

#### INNER JOIN:

- Only matching rows.

```sql
SELECT *
FROM A
INNER JOIN B
ON A.id=B.id;
```

- LEFT JOIN = All left rows
- RIGHT JOIN = All right rows
- FULL OUTER JOIN = All rows

---

# 28. UNION

- Combines results.
- Removes duplicates.

```sql
SELECT ...

UNION

SELECT ...
```

- UNION ALL = Keeps duplicates

---

# 29. Common Clauses Order

```
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

---

# 30. Common MCQ Topics

✓ SELECT
✓ WHERE
✓ ORDER BY
✓ GROUP BY
✓ HAVING
✓ Aggregate functions
✓ LIKE
✓ IN
✓ BETWEEN
✓ DISTINCT
✓ JOIN
✓ PRIMARY KEY
✓ FOREIGN KEY
✓ Constraints
✓ NULL
✓ UPDATE
✓ DELETE
✓ DROP
✓ ALTER

---

# Common Functions

Length

```sql
LENGTH(name)
```

Uppercase

```sql
UPPER(name)
```

Lowercase

```sql
LOWER(name)
```

Round

```sql
ROUND(price)
```

Current Date

```sql
CURRENT_DATE
```

---

# Frequently Asked MCQs

**Which command retrieves data?**

```sql
SELECT
```

---

**Which clause filters rows?**

```sql
WHERE
```

---

**Which clause sorts rows?**

```sql
ORDER BY
```

---

**Which function counts rows?**

```sql
COUNT()
```

---

**Difference between WHERE and HAVING?**

- `WHERE` filters rows **before** grouping.
- `HAVING` filters groups **after** grouping.

---

**Difference between DELETE, TRUNCATE and DROP?**

| DELETE | TRUNCATE | DROP |
|---------|----------|------|
| Removes selected rows | Removes all rows | Deletes entire table |
| Can use WHERE | No WHERE | Removes table structure |
| Can rollback (DB-dependent) | Usually faster | Table no longer exists |

---

**Difference between CHAR and VARCHAR?**

| CHAR | VARCHAR |
|------|----------|
| Fixed length | Variable length |
| Faster for fixed-size values | Saves storage |

---

**Difference between PRIMARY KEY and UNIQUE?**

| PRIMARY KEY | UNIQUE |
|-------------|--------|
| Only one per table | Multiple allowed |
| Cannot contain NULL | NULL allowed (DB-dependent) |
| Always unique | Unique values |

---

**Difference between UNION and UNION ALL?**

| UNION | UNION ALL |
|--------|-----------|
| Removes duplicates | Keeps duplicates |

---

# Last-Minute Revision

✓ `SELECT` → Retrieve data
✓ `INSERT` → Add rows
✓ `UPDATE` → Modify rows
✓ `DELETE` → Delete rows
✓ `WHERE` → Filter rows
✓ `ORDER BY` → Sort
✓ `GROUP BY` → Group rows
✓ `HAVING` → Filter groups
✓ `COUNT()` → Count rows
✓ `AVG()` → Average
✓ `SUM()` → Sum
✓ `MIN()` → Minimum
✓ `MAX()` → Maximum
✓ `LIKE` → Pattern matching
✓ `%` → Any number of characters
✓ `_` → Exactly one character
✓ `PRIMARY KEY` → Unique + NOT NULL
✓ `FOREIGN KEY` → References another table
✓ `INNER JOIN` → Matching rows only
✓ `LEFT JOIN` → All left rows
✓ `RIGHT JOIN` → All right rows
✓ `UNION` → Removes duplicates
✓ `UNION ALL` → Keeps duplicates
✓ `TRUNCATE` → Deletes all rows, keeps table
✓ `DROP` → Deletes the entire table
