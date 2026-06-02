# PostgreSQL Cheat Sheet

## Purpose

PostgreSQL is a relational database.

It stores application data permanently.

Examples:

- Users
- Profiles
- Posts
- Debates
- Comments
- Theory Articles

---

# Mental Model

Think of a database as a collection of spreadsheets.

```text
Database

├── Users
├── Profiles
├── Debates
└── Comments
```

Each spreadsheet is called a:

```text
Table
```

---

# Database Structure

```text
Database
    ↓
Table
    ↓
Rows
    ↓
Columns
```

Example:

```text
Users Table

+----+---------+------+
| id | name    | age  |
+----+---------+------+
| 1  | Gourav  | 21   |
| 2  | Alice   | 25   |
+----+---------+------+
```

---

# 1. Tables

## Concept

A table stores one type of data.

Examples:

```text
users

profiles

debates

comments
```

---

## Create Table

```sql
CREATE TABLE users (

    id INTEGER,

    name TEXT,

    age INTEGER

);
```

---

## Result

```text
users

+----+------+------+
| id | name | age  |
+----+------+------+
```

---

# Mental Model

```text
Table
 ↓
Spreadsheet
```

---

# 2. Rows

## Concept

A single record.

---

Example Table

```text
users

+----+---------+------+
| id | name    | age  |
+----+---------+------+
| 1  | Gourav  | 21   |
+----+---------+------+
```

This is one row:

```text
1 | Gourav | 21
```

---

## Insert Row

```sql
INSERT INTO users (

    id,
    name,
    age

)

VALUES (

    1,
    'Gourav',
    21

);
```

---

## View Data

```sql
SELECT *
FROM users;
```

---

# Mental Model

```text
Row
 ↓
Single Record
```

---

# 3. Primary Keys

## Concept

Unique identifier for each row.

No duplicates allowed.

---

## Example

```text
users

+----+---------+
| id | name    |
+----+---------+
| 1  | Gourav  |
| 2  | Alice   |
+----+---------+
```

---

## Create Table

```sql
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name TEXT

);
```

---

## Why?

Without primary key:

```text
Gourav
Gourav
Gourav
```

Which one is which?

---

With primary key:

```text
1 Gourav

2 Gourav

3 Gourav
```

Every row is unique.

---

# Mental Model

```text
Primary Key
 ↓
Unique ID
```

---

# 4. Foreign Keys

## Concept

Connect tables together.

---

Example:

```text
Users

1 Gourav

2 Alice
```

---

Profiles:

```text
101 INTP User=1

102 ENTP User=2
```

---

Relationship:

```text
Profile
    ↓
Belongs To
    ↓
User
```

---

## Create Tables

Users:

```sql
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name TEXT

);
```

Profiles:

```sql
CREATE TABLE profiles (

    id SERIAL PRIMARY KEY,

    type TEXT,

    user_id INTEGER

        REFERENCES users(id)

);
```

---

## Result

```text
profiles.user_id

        ↓

users.id
```

---

# Mental Model

```text
Foreign Key
 ↓
Link Between Tables
```

---

# Example

```text
users

+----+---------+
| id | name    |
+----+---------+
| 1  | Gourav  |
+----+---------+

profiles

+-----+------+---------+
| id  | type | user_id |
+-----+------+---------+
| 101 | INTP | 1       |
+-----+------+---------+
```

---

# 5. Joins

## Concept

Combine data from multiple tables.

---

Without Join

Users:

```text
1 Gourav
```

Profiles:

```text
INTP user_id=1
```

Need:

```text
Gourav → INTP
```

---

# INNER JOIN

```sql
SELECT

    users.name,

    profiles.type

FROM users

JOIN profiles

ON users.id =
   profiles.user_id;
```

---

## Result

```text
+---------+------+
| name    | type |
+---------+------+
| Gourav  | INTP |
+---------+------+
```

---

# Visual

```text
users.id
    ↓
profiles.user_id

Combined
    ↓

name + type
```

---

# Real TypeAtlas Example

```text
Users
 ↓
Profiles
 ↓
Debates
 ↓
Comments
```

Join all related data together.

---

# 6. Indexes

## Concept

Speed up searches.

---

Without Index

```text
Search

1
2
3
4
5
6
7
8
9
...
100000
```

Database checks every row.

Slow.

---

With Index

```text
Database

      ↓

Index

      ↓

Jump Directly
```

Fast.

---

# Create Index

```sql
CREATE INDEX

idx_user_name

ON users(name);
```

---

# Example

Query:

```sql
SELECT *

FROM users

WHERE name = 'Gourav';
```

---

Without index:

```text
Scan Entire Table
```

---

With index:

```text
Jump To Record
```

---

# Mental Model

```text
Index
 ↓
Book Index

Find Page Fast
```

---

# Basic CRUD

## Create

```sql
INSERT INTO users (

    name

)

VALUES (

    'Gourav'

);
```

---

## Read

```sql
SELECT *

FROM users;
```

---

## Update

```sql
UPDATE users

SET name = 'Mallicknight'

WHERE id = 1;
```

---

## Delete

```sql
DELETE FROM users

WHERE id = 1;
```

---

# Typical TypeAtlas Schema

## Users

```sql
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    username TEXT

);
```

---

## Profiles

```sql
CREATE TABLE profiles (

    id SERIAL PRIMARY KEY,

    slug TEXT,

    user_id INTEGER

    REFERENCES users(id)

);
```

---

## Debates

```sql
CREATE TABLE debates (

    id SERIAL PRIMARY KEY,

    title TEXT,

    author_id INTEGER

    REFERENCES users(id)

);
```

---

## Comments

```sql
CREATE TABLE comments (

    id SERIAL PRIMARY KEY,

    content TEXT,

    debate_id INTEGER

    REFERENCES debates(id)

);
```

---

# Relationship Diagram

```text
Users
  |
  | user_id
  ↓
Profiles

Users
  |
  | author_id
  ↓
Debates
  |
  | debate_id
  ↓
Comments
```

---

# Common Queries

## Get All Users

```sql
SELECT *

FROM users;
```

---

## Get One User

```sql
SELECT *

FROM users

WHERE id = 1;
```

---

## Get Profile By Slug

```sql
SELECT *

FROM profiles

WHERE slug = 'gourav';
```

---

## Get Debate By ID

```sql
SELECT *

FROM debates

WHERE id = 10;
```

---

# 90% of PostgreSQL You'll Use

## Create Table

```sql
CREATE TABLE
```

---

## Insert

```sql
INSERT INTO
```

---

## Select

```sql
SELECT
```

---

## Update

```sql
UPDATE
```

---

## Delete

```sql
DELETE
```

---

## Join

```sql
JOIN
```

---

## Index

```sql
CREATE INDEX
```

---

# Core Memory

```text
Database
 ↓
Tables

Table
 ↓
Rows

Row
 ↓
Record

Primary Key
 ↓
Unique ID

Foreign Key
 ↓
Table Link

Join
 ↓
Combine Tables

Index
 ↓
Fast Search
```

---

# Most Important Flow

```text
User Requests Profile
          ↓

Next.js Route
          ↓

SQL Query
          ↓

Profiles Table
          ↓

Return Row
          ↓

Render Page
```

If you understand **Tables + Rows + Primary Keys + Foreign Keys + Joins**, you already understand the foundation of relational databases and most application data models.