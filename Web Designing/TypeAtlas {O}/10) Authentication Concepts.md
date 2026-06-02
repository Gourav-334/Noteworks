# Authentication Concepts Cheat Sheet

## Purpose

Authentication answers:

```text
Who is this user?
```

Authorization answers:

```text
What is this user allowed to do?
```

Example:

```text
Authentication
 ↓
Is this Gourav?

Authorization
 ↓
Can Gourav edit this profile?
```

---

# Mental Model

```text
Register
    ↓

Login
    ↓

Receive Token
    ↓

Access Protected Pages
```

---

# Authentication Flow

```text
User
 ↓

Login Form
 ↓

Server
 ↓

Verify Password
 ↓

Create Session / JWT
 ↓

User Logged In
```

---

# 1. Registration

## Concept

Create a new account.

---

## Example

User enters:

```text
Email:
gourav@email.com

Password:
password123
```

---

Application stores:

```text
Email

Hashed Password
```

Not:

```text
Plain Password
```

---

# Registration Flow

```text
User
 ↓

Register Form
 ↓

Server
 ↓

Hash Password
 ↓

Database
```

---

# Example Table

```text
users

+----+-------------------+
| id | email             |
+----+-------------------+
| 1  | gourav@email.com  |
+----+-------------------+
```

Password stored separately:

```text
$2a$12$98ajdka...
```

Not:

```text
password123
```

---

# Why Hash Passwords?

Bad:

```text
password123
```

Database leak:

```text
Everyone sees password
```

---

Good:

```text
$2a$12$98ajdka...
```

Impossible to directly read.

---

# Mental Model

```text
Password
 ↓

Hash Function
 ↓

Stored Hash
```

---

# 2. Login

## Concept

Verify identity.

---

User enters:

```text
Email

Password
```

---

Server:

```text
Find User
 ↓

Compare Password Hash
 ↓

Match?
```

---

Result:

```text
Yes
 ↓
Login Success

No
 ↓
Reject
```

---

# Login Flow

```text
User
 ↓

Login Form
 ↓

Server
 ↓

Check Credentials
 ↓

Create Session/JWT
 ↓

Logged In
```

---

# 3. Sessions

## Concept

Server remembers who you are.

---

Without Session

```text
Request 1
 ↓
Who Are You?

Request 2
 ↓
Who Are You?

Request 3
 ↓
Who Are You?
```

---

With Session

```text
Login
 ↓

Session Created
 ↓

Session ID Stored
 ↓

Server Remembers User
```

---

# Example

Server creates:

```text
Session ID

abc123xyz
```

---

Browser stores:

```text
Cookie

abc123xyz
```

---

Future Requests

```text
Cookie
 ↓

Server
 ↓

Session Found
 ↓

User Identified
```

---

# Visual

```text
Browser

Cookie:
abc123

      ↓

Server

Session:
abc123 → Gourav
```

---

# Mental Model

```text
Session
 ↓
Server Memory
```

---

# Session Advantages

```text
Easy

Secure

Server Controlled
```

---

# Session Disadvantages

```text
Server Must Store Sessions
```

---

# 4. JWT (JSON Web Token)

## Concept

Store identity inside a token.

Instead of server remembering.

---

# Example

Server creates:

```text
JWT Token
```

Looks like:

```text
eyJhbGciOiJIUzI1...
```

---

Browser stores token.

Future requests:

```text
Authorization:

Bearer TOKEN
```

---

Server verifies token.

---

# JWT Flow

```text
Login
 ↓

JWT Created
 ↓

Browser Stores JWT
 ↓

Future Requests
 ↓

JWT Sent
 ↓

Verified
```

---

# Visual

```text
Browser

JWT
 ↓

Request
 ↓

Server
 ↓

Verify JWT
```

---

# Session vs JWT

| Sessions | JWT |
|-----------|-----------|
| Stored On Server | Stored On Client |
| Cookie | Token |
| Easy To Revoke | Harder To Revoke |
| Traditional | API Friendly |

---

# JWT Structure

```text
Header

Payload

Signature
```

---

Example Payload

```json
{
  "userId": 1,
  "role": "admin"
}
```

---

# Mental Model

```text
JWT
 ↓
Digital Identity Card
```

---

# 5. OAuth

## Concept

Login using another provider.

Examples:

```text
Google

GitHub

Discord

Facebook
```

---

Instead of:

```text
Create Password
```

User clicks:

```text
Login With Google
```

---

# OAuth Flow

```text
User
 ↓

Login With Google
 ↓

Google Login Page
 ↓

Approve
 ↓

Google Returns Identity
 ↓

Logged In
```

---

# Visual

```text
User

 ↓

Your Website

 ↓

Google

 ↓

Verified

 ↓

Your Website
```

---

# Example

```text
Click:

Continue With Google
```

---

User already signed into Google.

```text
No Password Needed
```

---

# Why OAuth?

Advantages:

```text
No Password Storage

Faster Registration

Trusted Identity Provider
```

---

# Common OAuth Providers

```text
Google

GitHub

Discord

Microsoft

Apple
```

---

# Supabase OAuth Example

```typescript
await supabase.auth.signInWithOAuth({

    provider: "google"

});
```

---

# Complete Authentication Flow

## Email Login

```text
Register
 ↓

Database
 ↓

Login
 ↓

Session/JWT
 ↓

Authenticated
```

---

## OAuth Login

```text
Google Login
 ↓

Google Verification
 ↓

Session/JWT
 ↓

Authenticated
```

---

# Authentication vs Authorization

## Authentication

```text
Who Are You?
```

Example:

```text
Gourav
```

---

## Authorization

```text
What Can You Do?
```

Example:

```text
Can Edit Own Profile

Cannot Edit Others
```

---

# TypeAtlas Example

## Anonymous Visitor

```text
Read Profiles

Read Debates
```

---

## Logged User

```text
Create Debate

Comment

Upload Avatar
```

---

## Author

```text
Edit Own Debate

Delete Own Debate
```

---

# Real Next.js + Supabase Flow

```text
User Login
      ↓

Supabase Auth
      ↓

JWT Issued
      ↓

Cookie Stored
      ↓

User Visits Profile
      ↓

JWT Verified
      ↓

Profile Returned
```

---

# 90% of Authentication You'll Use

## Registration

```text
Create Account
```

---

## Login

```text
Verify User
```

---

## Session

```text
Server Remembers User
```

---

## JWT

```text
Token Identifies User
```

---

## OAuth

```text
Login With Google
```

---

# Core Memory

```text
Registration
 ↓
Create Account

Login
 ↓
Verify Identity

Session
 ↓
Server Remembers User

JWT
 ↓
Client Stores Identity

OAuth
 ↓
Third-Party Login

Authentication
 ↓
Who Are You?

Authorization
 ↓
What Can You Do?
```

---

# Most Important Flow

```text
User Logs In
        ↓

Credentials Verified
        ↓

Session/JWT Created
        ↓

Browser Stores Identity
        ↓

Future Requests
        ↓

User Recognized
```

If you understand **Login + Sessions + JWT + OAuth**, you understand the foundation used by most modern authentication systems, including Next.js, Supabase, Google Login, GitHub Login, and enterprise web applications.