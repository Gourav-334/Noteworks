# Environment Variables Cheat Sheet

## Purpose

Environment Variables store configuration and secrets outside your code.

Examples:

```text
API Keys

Database URLs

Passwords

Tokens

Project Settings
```

---

# Problem

Without Environment Variables:

```typescript
const apiKey =
    "secret-key";
```

Problems:

```text
Visible In Source Code

Accidentally Uploaded To GitHub

Security Risk
```

---

# Solution

```typescript
const apiKey =
    process.env.GEMINI_API_KEY;
```

Secret stored elsewhere.

---

# Mental Model

```text
Code
 ↓

Reads Configuration
 ↓

Environment Variable
```

---

# Example

Instead of:

```typescript
const databaseUrl =
    "postgres://...";
```

Use:

```typescript
const databaseUrl =
    process.env.DATABASE_URL;
```

---

# Environment Variable File

## Local Development

File:

```text
.env.local
```

Example:

```env
DATABASE_URL=postgres://localhost

GEMINI_API_KEY=abc123

SUPABASE_URL=https://xyz.supabase.co
```

---

# Project Structure

```text
project/

├── app/
├── components/
├── public/
├── .env.local
└── package.json
```

---

# Important Rule

Never commit:

```text
.env.local
```

to GitHub.

---

# .gitignore

Usually contains:

```gitignore
.env.local

.env

.env.*
```

---

# Access Variables

## TypeScript

```typescript
const apiKey =
    process.env.GEMINI_API_KEY;
```

---

# Example

```typescript
const url =
    process.env.SUPABASE_URL;
```

---

# Flow

```text
.env.local
      ↓

process.env
      ↓

Application
```

---

# NEXT_PUBLIC_ Variables

## Concept

Variables visible to browser.

---

Normally:

```env
GEMINI_API_KEY=secret
```

Accessible only on server.

---

If you need browser access:

```env
NEXT_PUBLIC_API_URL=https://api.com
```

---

# Access

```typescript
process.env.NEXT_PUBLIC_API_URL
```

---

# Example

```env
NEXT_PUBLIC_SITE_NAME=TypeAtlas
```

Use:

```typescript
const siteName =
    process.env.NEXT_PUBLIC_SITE_NAME;
```

---

# Rule

## Private

```env
DATABASE_URL=

GEMINI_API_KEY=

SUPABASE_SERVICE_ROLE_KEY=
```

Server only.

---

## Public

```env
NEXT_PUBLIC_SITE_NAME=

NEXT_PUBLIC_SUPABASE_URL=

NEXT_PUBLIC_SUPABASE_ANON_KEY=
```

Visible to browser.

---

# Mental Model

```text
NEXT_PUBLIC_
      ↓

Safe To Expose
```

---

# Secret Keys

## Concept

Sensitive values.

Never expose them.

---

# Examples

```env
GEMINI_API_KEY=

DATABASE_URL=

JWT_SECRET=

SUPABASE_SERVICE_ROLE_KEY=
```

---

# Bad

```typescript
console.log(
    process.env.GEMINI_API_KEY
);
```

inside browser code.

---

# Good

Use only in:

```text
Server Components

API Routes

Backend Logic
```

---

# Secret Key Mental Model

```text
Secret
 ↓

Server Only
```

---

# Public vs Secret

| Variable | Public? |
|------------|------------|
| NEXT_PUBLIC_SITE_NAME | Yes |
| NEXT_PUBLIC_SUPABASE_URL | Yes |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | Yes |
| DATABASE_URL | No |
| GEMINI_API_KEY | No |
| JWT_SECRET | No |
| SUPABASE_SERVICE_ROLE_KEY | No |

---

# Next.js Example

## Server Component

```typescript
const apiKey =
    process.env.GEMINI_API_KEY;
```

Allowed.

---

## Client Component

```typescript
"use client";

const apiKey =
    process.env.GEMINI_API_KEY;
```

Not available.

---

Must use:

```typescript
process.env.NEXT_PUBLIC_...
```

---

# Common TypeAtlas Variables

## Public

```env
NEXT_PUBLIC_SITE_NAME=TypeAtlas

NEXT_PUBLIC_SUPABASE_URL=

NEXT_PUBLIC_SUPABASE_ANON_KEY=
```

---

## Private

```env
GEMINI_API_KEY=

SUPABASE_SERVICE_ROLE_KEY=

JWT_SECRET=
```

---

# Vercel Environment Variables

Local:

```env
.env.local
```

---

Production:

```text
Vercel Dashboard

Settings

Environment Variables
```

---

# Example

Development:

```env
GEMINI_API_KEY=local-key
```

Production:

```env
GEMINI_API_KEY=production-key
```

---

# Flow

```text
Local Development
      ↓

.env.local
```

```text
Production
      ↓

Vercel Environment Variables
```

---

# Common Mistakes

## Forgetting NEXT_PUBLIC_

```env
SITE_NAME=TypeAtlas
```

Browser:

```typescript
undefined
```

---

Correct:

```env
NEXT_PUBLIC_SITE_NAME=TypeAtlas
```

---

## Exposing Secrets

Bad:

```env
NEXT_PUBLIC_GEMINI_API_KEY=
```

Anyone can see it.

---

Correct:

```env
GEMINI_API_KEY=
```

Server only.

---

## Missing Variable

Code:

```typescript
process.env.GEMINI_API_KEY
```

Result:

```text
undefined
```

Usually means:

```text
Variable Not Set
```

---

# Typical TypeAtlas Setup

```env
# Public

NEXT_PUBLIC_SITE_NAME=TypeAtlas

NEXT_PUBLIC_SUPABASE_URL=

NEXT_PUBLIC_SUPABASE_ANON_KEY=

# Private

GEMINI_API_KEY=

SUPABASE_SERVICE_ROLE_KEY=

JWT_SECRET=
```

---

# 90% of Environment Variables You'll Use

## File

```text
.env.local
```

---

## Access

```typescript
process.env.KEY
```

---

## Public

```env
NEXT_PUBLIC_*
```

---

## Private

```env
SECRET_KEYS
```

---

## Production

```text
Vercel Environment Variables
```

---

# Core Memory

```text
Environment Variable
 ↓
Configuration

.env.local
 ↓
Local Development

process.env
 ↓
Access Value

NEXT_PUBLIC_
 ↓
Browser Accessible

Secret Key
 ↓
Server Only
```

---

# Most Important Rule

```text
NEXT_PUBLIC_
      ↓
Browser Can See It

No Prefix
      ↓
Server Only
```

Whenever handling API keys, database passwords, JWT secrets, or service-role keys:

```text
Never Use NEXT_PUBLIC_
```

Only use `NEXT_PUBLIC_` for values that are safe for every visitor to see.