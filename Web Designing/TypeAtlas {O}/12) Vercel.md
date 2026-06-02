# Vercel Cheat Sheet

## Purpose

Vercel hosts and deploys your web application.

Think:

```text
Your Computer
      ↓

GitHub
      ↓

Vercel
      ↓

Live Website
```

Instead of:

```text
Run Project Locally
```

You get:

```text
https://your-app.vercel.app
```

accessible from anywhere.

---

# Mental Model

```text
Code Change
     ↓

Git Push
     ↓

GitHub
     ↓

Vercel
     ↓

Automatic Build
     ↓

Website Updated
```

---

# Why Vercel?

It is designed specifically for:

```text
Next.js

React

TypeScript

Tailwind
```

which makes it ideal for TypeAtlas.

---

# Deployment Pipeline

```text
VS Code
    ↓

Git Commit
    ↓

Git Push
    ↓

GitHub
    ↓

Vercel
    ↓

Build
    ↓

Deploy
    ↓

Live Website
```

---

# 1. Connect GitHub

## Concept

Allow Vercel to access your repository.

---

# Step 1

Push project to GitHub.

```bash
git add .

git commit -m "Initial commit"

git push
```

---

# Step 2

Login to Vercel.

Website:

```text
https://vercel.com
```

---

# Step 3

Click:

```text
Add New Project
```

---

# Step 4

Select GitHub repository.

Example:

```text
typeatlas
```

---

# Step 5

Click:

```text
Deploy
```

---

# Result

```text
https://typeatlas.vercel.app
```

---

# Mental Model

```text
GitHub Repo
      ↓

Connected

      ↓

Vercel Project
```

---

# 2. Automatic Deployments

## Concept

Every push automatically redeploys.

---

# Example

Change:

```tsx
<h1>Hello</h1>
```

to:

```tsx
<h1>Hello World</h1>
```

---

Push:

```bash
git add .

git commit -m "Updated title"

git push
```

---

Automatically:

```text
GitHub
    ↓

Vercel Detects Change
    ↓

Build Starts
    ↓

New Version Live
```

---

# No Manual Upload Needed

You never do:

```text
Upload Files

FTP

Copy Server Files
```

Everything happens automatically.

---

# Mental Model

```text
Push
 ↓

Deploy
```

---

# Deployment Status

When deploying:

```text
Building...
```

---

Success:

```text
Ready
```

---

Failure:

```text
Build Failed
```

---

# Common Build Failure

```text
TypeScript Error

Missing Environment Variable

Import Error
```

---

# 3. Environment Variables

## Concept

Store secrets safely.

Never commit secrets to GitHub.

---

# Bad

```typescript
const apiKey =
    "secret-key";
```

---

# Good

```typescript
const apiKey =
    process.env.GEMINI_API_KEY;
```

---

# Local Development

File:

```env
.env.local
```

```env
GEMINI_API_KEY=xxxx

SUPABASE_URL=xxxx

SUPABASE_KEY=xxxx
```

---

# Vercel Dashboard

Add:

```text
Settings
 ↓

Environment Variables
```

---

Example:

```text
GEMINI_API_KEY

SUPABASE_URL

SUPABASE_ANON_KEY
```

---

# Access In Code

```typescript
process.env.GEMINI_API_KEY
```

---

# Mental Model

```text
Environment Variable
      ↓
Secret Configuration
```

---

# Common Variables For TypeAtlas

```env
GEMINI_API_KEY=

SUPABASE_URL=

SUPABASE_ANON_KEY=

SUPABASE_SERVICE_ROLE_KEY=
```

---

# 4. Custom Domains

## Concept

Replace:

```text
typeatlas.vercel.app
```

with:

```text
typeatlas.com
```

---

# Step 1

Buy domain.

Examples:

```text
Namecheap

Cloudflare

GoDaddy
```

---

# Step 2

Open:

```text
Vercel

Settings

Domains
```

---

# Step 3

Add:

```text
typeatlas.com
```

---

# Step 4

Update DNS records.

---

# Result

```text
https://typeatlas.com
```

instead of:

```text
https://typeatlas.vercel.app
```

---

# Mental Model

```text
Custom Domain
      ↓

Points To

      ↓

Vercel Deployment
```

---

# Project Structure

```text
TypeAtlas

├── Next.js
├── Tailwind
├── Supabase
├── Gemini
└── Vercel
```

---

# Complete Deployment Flow

```text
Build Feature
       ↓

git add .
       ↓

git commit
       ↓

git push
       ↓

GitHub
       ↓

Vercel
       ↓

Build
       ↓

Deploy
       ↓

Website Live
```

---

# Typical First Deployment

## Create Project

```bash
npx create-next-app@latest
```

---

## Run Locally

```bash
npm run dev
```

---

## Push To GitHub

```bash
git add .

git commit -m "Initial"

git push
```

---

## Import Into Vercel

```text
Vercel
 ↓

Import Repository
 ↓

Deploy
```

---

# Vercel Dashboard

Common Sections:

```text
Overview

Deployments

Analytics

Storage

Domains

Settings
```

---

# Useful Commands

## Install Dependencies

```bash
npm install
```

---

## Start Development

```bash
npm run dev
```

---

## Production Build

```bash
npm run build
```

---

## Production Preview

```bash
npm run start
```

---

# Deployment Troubleshooting

## Build Works Locally But Not On Vercel

Check:

```text
Environment Variables

TypeScript Errors

Case-Sensitive File Names
```

---

## Missing API Key

Error:

```text
undefined
```

Usually means:

```text
Environment Variable Not Set
```

---

## Build Failure

Run:

```bash
npm run build
```

locally first.

---

# Typical TypeAtlas Environment Variables

```env
NEXT_PUBLIC_SUPABASE_URL=

NEXT_PUBLIC_SUPABASE_ANON_KEY=

SUPABASE_SERVICE_ROLE_KEY=

GEMINI_API_KEY=
```

---

# 90% of Vercel You'll Use

## Deploy

```text
Connect GitHub Repository
```

---

## Redeploy

```text
git push
```

---

## Secrets

```text
Environment Variables
```

---

## Domain

```text
Custom Domain
```

---

## Monitor

```text
Deployments Page
```

---

# Core Memory

```text
GitHub
 ↓
Source Code

Vercel
 ↓
Hosting

Push
 ↓
Automatic Deployment

Environment Variables
 ↓
Secrets

Custom Domain
 ↓
Professional URL
```

---

# Most Important Flow

```text
Code Change
      ↓

git push
      ↓

GitHub
      ↓

Vercel
      ↓

Build
      ↓

Deploy
      ↓

Website Live
```

For most Next.js projects, your entire deployment workflow eventually becomes:

```bash
git add .

git commit -m "feature"

git push
```

Everything after that is handled automatically by Vercel.