# Supabase Cheat Sheet

## Purpose

Supabase is a Backend-as-a-Service (BaaS).

It provides:

```text
PostgreSQL
+
Authentication
+
File Storage
+
API
+
Security
=
Supabase
```

Instead of building your own backend server, Supabase provides most backend features out of the box.

---

# Mental Model

Traditional Backend

```text
Frontend
    ↓

Backend Server
    ↓

Database
```

Supabase

```text
Frontend
    ↓

Supabase
 ├── Auth
 ├── Database
 ├── Storage
 └── Security
```

---

# What You'll Use

```text
Authentication
Database
Storage
RLS
Policies
```

---

# 1. Authentication

## Concept

User login system.

Handles:

```text
Register

Login

Logout

Password Reset

User Sessions
```

---

# Sign Up

```typescript
const {

    data,

    error

} = await supabase.auth.signUp({

    email:
        "user@email.com",

    password:
        "password123"

});
```

---

# Sign In

```typescript
const {

    data,

    error

} = await supabase.auth.signInWithPassword({

    email:
        "user@email.com",

    password:
        "password123"

});
```

---

# Sign Out

```typescript
await supabase.auth.signOut();
```

---

# Get Current User

```typescript
const {

    data

} = await supabase.auth.getUser();
```

---

# Mental Model

```text
Register
    ↓

auth.users

    ↓

User Session

    ↓

Logged In
```

---

# Typical TypeAtlas Example

```text
User Registers
      ↓

Supabase Auth
      ↓

User Receives ID
      ↓

Create Profile
```

---

# 2. Database

## Concept

Managed PostgreSQL database.

Exactly like PostgreSQL.

---

# Table Example

```sql
CREATE TABLE profiles (

    id UUID PRIMARY KEY,

    slug TEXT,

    bio TEXT

);
```

---

# Insert Data

```typescript
await supabase

    .from("profiles")

    .insert({

        slug: "gourav",

        bio: "Systems Programmer"

    });
```

---

# Read Data

```typescript
const {

    data

} = await supabase

    .from("profiles")

    .select("*");
```

---

# Filter

```typescript
const {

    data

} = await supabase

    .from("profiles")

    .select("*")

    .eq(
        "slug",
        "gourav"
    );
```

---

# Update

```typescript
await supabase

    .from("profiles")

    .update({

        bio: "Database Engineer"

    })

    .eq(
        "id",
        userId
    );
```

---

# Delete

```typescript
await supabase

    .from("profiles")

    .delete()

    .eq(
        "id",
        userId
    );
```

---

# Mental Model

```text
Supabase Database
       ↓

PostgreSQL

       ↓

Tables

       ↓

Rows
```

---

# 3. Storage

## Concept

Store files.

Examples:

```text
Profile Pictures

Avatars

Documents

Images

Videos
```

---

# Upload File

```typescript
await supabase.storage

    .from("avatars")

    .upload(

        "avatar.png",

        file

    );
```

---

# Folder Structure

```text
Storage

└── avatars
    ├── avatar1.png
    ├── avatar2.png
    └── avatar3.png
```

---

# Get Public URL

```typescript
const {

    data

} = supabase.storage

    .from("avatars")

    .getPublicUrl(
        "avatar.png"
    );
```

---

# Delete File

```typescript
await supabase.storage

    .from("avatars")

    .remove([

        "avatar.png"

    ]);
```

---

# Mental Model

```text
Bucket
 ↓
Folder

File
 ↓
Stored Asset
```

---

# Storage Terminology

```text
Bucket
 ↓
Container

avatars

documents

images
```

---

# 4. Row Level Security (RLS)

## Concept

Database-level permissions.

Controls:

```text
Who Can Read

Who Can Insert

Who Can Update

Who Can Delete
```

---

# Problem

Without RLS

```text
User A

Can Read

User B Data
```

Dangerous.

---

# With RLS

```text
User A

Can Access

Only User A Data
```

---

# Enable RLS

```sql
ALTER TABLE profiles

ENABLE ROW LEVEL SECURITY;
```

---

# Mental Model

```text
Database Firewall
```

---

# Example

Table:

```text
profiles

id
user_id
bio
```

---

Users:

```text
User A

User B
```

Without RLS:

```text
A sees B

B sees A
```

---

With RLS:

```text
A sees A

B sees B
```

---

# 5. Policies

## Concept

Rules used by RLS.

Policies define exactly what users may do.

---

# Read Own Profile

```sql
CREATE POLICY

"Users can read own profile"

ON profiles

FOR SELECT

USING (

    auth.uid()

    =

    user_id

);
```

---

# Update Own Profile

```sql
CREATE POLICY

"Users can update own profile"

ON profiles

FOR UPDATE

USING (

    auth.uid()

    =

    user_id

);
```

---

# Mental Model

```text
RLS
 ↓
Security System

Policies
 ↓
Rules
```

---

# Visual

```text
User

 ↓

Policy Check

 ↓

Allowed?

 ├── Yes → Continue
 └── No  → Reject
```

---

# Typical TypeAtlas Tables

## Profiles

```sql
profiles

id
slug
bio
user_id
```

---

## Debates

```sql
debates

id
title
content
author_id
```

---

## Comments

```sql
comments

id
content
author_id
debate_id
```

---

# Typical Security Rules

## Profiles

```text
Anyone
 ↓
Read

Owner
 ↓
Update
```

---

## Debates

```text
Anyone
 ↓
Read

Logged User
 ↓
Create

Author
 ↓
Edit
```

---

## Comments

```text
Anyone
 ↓
Read

Author
 ↓
Delete
```

---

# Typical TypeAtlas Flow

```text
User Registers
        ↓

Supabase Auth
        ↓

Create Profile
        ↓

Profile Stored
        ↓

User Uploads Avatar
        ↓

Storage Bucket
        ↓

Avatar URL Saved
```

---

# Example Project Structure

```text
Supabase

├── Auth
│   └── Users
│
├── Database
│   ├── Profiles
│   ├── Debates
│   └── Comments
│
├── Storage
│   └── Avatars
│
└── Security
    ├── RLS
    └── Policies
```

---

# Common Queries

## Get Current User

```typescript
await supabase.auth.getUser();
```

---

## Read Profiles

```typescript
await supabase

    .from("profiles")

    .select("*");
```

---

## Create Profile

```typescript
await supabase

    .from("profiles")

    .insert(...);
```

---

## Upload Avatar

```typescript
await supabase.storage

    .from("avatars")

    .upload(...);
```

---

# 90% of Supabase You'll Use

## Authentication

```typescript
signUp()

signInWithPassword()

signOut()

getUser()
```

---

## Database

```typescript
select()

insert()

update()

delete()
```

---

## Storage

```typescript
upload()

remove()

getPublicUrl()
```

---

## Security

```sql
ENABLE ROW LEVEL SECURITY
```

---

## Policies

```sql
CREATE POLICY
```

---

# Core Memory

```text
Authentication
 ↓
Users

Database
 ↓
PostgreSQL

Storage
 ↓
Files

RLS
 ↓
Security Layer

Policy
 ↓
Permission Rule

auth.uid()
 ↓
Current User ID
```

---

# Most Important Flow

```text
User Logs In
        ↓

Supabase Auth
        ↓

User ID Available
        ↓

Database Query
        ↓

RLS Checks Policy
        ↓

Allowed?
        ↓

Return Data
```

If you understand **Authentication + Database + Storage + RLS**, you understand the majority of practical Supabase development used in modern Next.js applications.