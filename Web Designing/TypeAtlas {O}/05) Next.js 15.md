# Next.js 15 Cheat Sheet

## Purpose

Next.js is a full-stack React framework.

Think:

```text
React
  +
Routing
  +
Backend
  +
Rendering
  =
Next.js
```

React builds components.

Next.js builds complete applications.

---

# Mental Model

```text
Browser
    ↓
Next.js
    ↓
React Components
    ↓
Database / APIs
```

---

# App Router

## Concept

File-system based routing.

Folders become URLs.

---

## Example

```text
app/

├── page.tsx
├── about/
│   └── page.tsx
└── contact/
    └── page.tsx
```

Produces:

```text
/
/about
/contact
```

---

# Rule

```text
Folder
   ↓
Route

page.tsx
   ↓
Page Content
```

---

# Example

```text
app/

└── profiles/
    └── page.tsx
```

URL:

```text
/profiles
```

---

# Page

## Concept

A page shown at a route.

---

## Example

```tsx
export default function Page() {

    return (
        <h1>
            Profiles
        </h1>
    );

}
```

URL:

```text
/profiles
```

---

# Layouts

## Concept

Shared UI across pages.

Examples:

- Navbar
- Sidebar
- Footer

---

# Structure

```text
app/

├── layout.tsx
├── page.tsx
└── profiles/
    └── page.tsx
```

---

# Layout Example

```tsx
export default function Layout({

    children

}: {

    children: React.ReactNode

}) {

    return (

        <html>

            <body>

                <nav>
                    Navbar
                </nav>

                {children}

            </body>

        </html>

    );

}
```

---

# Result

```text
Navbar
   ↓

Profiles Page

OR

Theory Page

OR

Debate Page
```

Navbar appears everywhere.

---

# Dynamic Routes

## Concept

Variable URL segments.

Instead of:

```text
/profiles/gourav

/profiles/alice

/profiles/bob
```

Create one route:

```text
/profiles/[slug]
```

---

# Folder Structure

```text
app/

└── profiles/
    └── [slug]/
        └── page.tsx
```

---

# URL Examples

```text
/profiles/gourav

/profiles/alice

/profiles/john
```

---

# Access Parameter

```tsx
export default async function Page({

    params

}: {

    params: Promise<{

        slug: string

    }>

}) {

    const { slug } =
        await params;

    return (
        <h1>
            {slug}
        </h1>
    );

}
```

---

# TypeAtlas Examples

## Profiles

```text
/profiles/[slug]
```

Examples:

```text
/profiles/gourav

/profiles/alice
```

---

## Theory Systems

```text
/theory/[system]
```

Examples:

```text
/theory/mbti

/theory/socionics

/theory/enneagram
```

---

## Debates

```text
/debates/[id]
```

Examples:

```text
/debates/101

/debates/102
```

---

# Nested Routes

## Structure

```text
app/

└── theory/
    ├── mbti/
    │   └── page.tsx
    │
    └── socionics/
        └── page.tsx
```

URLs:

```text
/theory/mbti

/theory/socionics
```

---

# Server Components

## Concept

Default component type.

Runs on server.

---

# Example

```tsx
export default function Page() {

    return (
        <h1>
            Server Component
        </h1>
    );

}
```

---

# Benefits

```text
Faster

Smaller JS Bundle

Can Access Database Directly
```

---

# Server Component Mental Model

```text
Server
   ↓
Generate HTML
   ↓
Send To Browser
```

---

# Example Database Query

```tsx
export default async function Page() {

    const users =
        await getUsers();

    return (

        <div>

            {users.length}

        </div>

    );

}
```

---

# Client Components

## Concept

Runs inside browser.

Required for:

- useState
- useEffect
- Click handlers
- Forms

---

# Enable Client Component

Must be first line:

```tsx
"use client";
```

---

# Example

```tsx
"use client";

import {

    useState

} from "react";

export default function Counter() {

    const [

        count,

        setCount

    ] = useState(0);

    return (

        <button
            onClick={() =>
                setCount(
                    count + 1
                )
            }
        >

            {count}

        </button>

    );

}
```

---

# Rule

Need:

```text
useState

useEffect

onClick

onChange
```

Then:

```tsx
"use client";
```

---

# Server vs Client

| Server Component | Client Component |
|----------|----------|
| Default | Requires `"use client"` |
| Faster | Interactive |
| Database Access | Browser Events |
| Fetch Data | useState |
| Secure | useEffect |

---

# API Routes

## Concept

Backend endpoints inside Next.js.

---

# Structure

```text
app/

└── api/
    └── users/
        └── route.ts
```

---

# URL

```text
/api/users
```

---

# Example

```tsx
export async function GET() {

    return Response.json({

        message: "Hello"

    });

}
```

---

# Response

```json
{
    "message": "Hello"
}
```

---

# POST Example

```tsx
export async function POST(
    request: Request
) {

    const body =
        await request.json();

    return Response.json(
        body
    );

}
```

---

# Typical TypeAtlas Structure

```text
app/

├── layout.tsx
├── page.tsx
│
├── profiles/
│   ├── page.tsx
│   └── [slug]/
│       └── page.tsx
│
├── theory/
│   ├── page.tsx
│   └── [system]/
│       └── page.tsx
│
├── debates/
│   ├── page.tsx
│   └── [id]/
│       └── page.tsx
│
└── api/
    ├── profiles/
    │   └── route.ts
    │
    └── debates/
        └── route.ts
```

---

# Request Flow

```text
User Visits

/profiles/gourav
        ↓

Next.js Router
        ↓

profiles/[slug]/page.tsx
        ↓

Fetch Data
        ↓

Render Page
        ↓

Send HTML
```

---

# 90% of Next.js You'll Use

## Page

```tsx
export default function Page() {

    return <div />;
}
```

---

## Layout

```tsx
export default function Layout({

    children

}) {

    return children;
}
```

---

## Dynamic Route

```text
[slug]
```

---

## Client Component

```tsx
"use client";
```

---

## API Route

```tsx
export async function GET() {

}
```

---

## Server Component

```tsx
export default async function Page() {

}
```

---

# Core Memory

```text
Folder
 ↓
Route

page.tsx
 ↓
Page

layout.tsx
 ↓
Shared UI

[slug]
 ↓
Dynamic Route

Server Component
 ↓
Default

Client Component
 ↓
Interactive

api/
 ↓
Backend Endpoints
```

---

# Most Important Flow

```text
URL
 ↓
Route Folder
 ↓
page.tsx
 ↓
Fetch Data
 ↓
Render HTML
 ↓
Browser
```

If you understand **Pages + Layouts + Dynamic Routes + Server/Client Components**, you understand the majority of practical Next.js development.