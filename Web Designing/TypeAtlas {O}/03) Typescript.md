# TypeScript Cheat Sheet

## Purpose

TypeScript = JavaScript + Type Safety

It helps catch bugs before the program runs.

Think:

```text
JavaScript
    +
Type Checking
    =
TypeScript
```

---

# Mental Model

```text
Value
  +
Type
```

Example:

```typescript
let age: number = 21;
```

```text
21      → Value
number  → Type
```

TypeScript verifies that values match their types.

---

# Why TypeScript?

JavaScript:

```javascript
let age = 21;

age = "hello";
```

Allowed.

TypeScript:

```typescript
let age: number = 21;

age = "hello";
```

Error.

```text
Type 'string'
is not assignable
to type 'number'
```

---

# 1. Types

## Concept

Describe what kind of value a variable can store.

---

## Number

```typescript
let age: number = 21;
```

---

## String

```typescript
let name: string = "Gourav";
```

---

## Boolean

```typescript
let isAdmin: boolean = false;
```

---

## Type Inference

TypeScript can often guess.

```typescript
let score = 100;
```

Equivalent to:

```typescript
let score: number = 100;
```

---

# Common Types

```typescript
number
string
boolean
null
undefined
```

---

# 2. Arrays

## Concept

Store multiple values of the same type.

---

## Number Array

```typescript
let scores: number[] = [10, 20, 30];
```

---

## String Array

```typescript
let names: string[] = [
    "Alice",
    "Bob"
];
```

---

## Alternative Syntax

```typescript
let scores: Array<number> = [
    10,
    20,
    30
];
```

---

## Access Elements

```typescript
let names = ["Alice", "Bob"];

console.log(names[0]);
```

Output:

```text
Alice
```

---

# 3. Objects

## Concept

Group related data.

---

## Example

```typescript
let user = {

    name: "Gourav",

    age: 21

};
```

---

## Typed Object

```typescript
let user: {

    name: string;

    age: number;

} = {

    name: "Gourav",

    age: 21

};
```

---

## Access Fields

```typescript
console.log(user.name);
```

Output:

```text
Gourav
```

---

# 4. Interfaces

## Concept

Reusable object blueprint.

Instead of writing object types repeatedly.

---

## Without Interface

```typescript
let user: {

    name: string;

    age: number;

};
```

---

## With Interface

```typescript
interface User {

    name: string;

    age: number;

}
```

---

## Usage

```typescript
let user: User = {

    name: "Gourav",

    age: 21

};
```

---

## Multiple Objects

```typescript
let admin: User = {

    name: "Alice",

    age: 25

};
```

---

# Interface Mental Model

```text
Interface
     ↓
Blueprint
     ↓
Object
```

Like:

```text
Class Diagram
      ↓
Instance
```

---

# 5. Functions

## Concept

Reusable block of logic.

---

## Basic Function

```typescript
function greet(): void {

    console.log("Hello");

}
```

---

## Function With Parameter

```typescript
function greet(
    name: string
): void {

    console.log(name);

}
```

---

## Function Returning Value

```typescript
function add(
    a: number,
    b: number
): number {

    return a + b;

}
```

---

## Call Function

```typescript
let result = add(2, 3);
```

Output:

```text
5
```

---

# Arrow Functions

Modern style.

```typescript
const add = (
    a: number,
    b: number
): number => {

    return a + b;

};
```

---

# 6. Async / Await

## Concept

Handle slow operations.

Examples:

- Database queries
- API calls
- File loading

---

## Problem

Normal code:

```typescript
let data = fetchData();
```

Data may not be ready yet.

---

## Async Function

```typescript
async function getUser() {

}
```

---

## Await

```typescript
async function getUser() {

    const user =
        await fetchUser();

    console.log(user);

}
```

---

## Mental Model

```text
Start Request
      ↓
Wait
      ↓
Continue
```

instead of:

```text
Start Request
      ↓
Freeze Program
```

---

# Example

```typescript
async function getData() {

    const response =
        await fetch(
            "/api/users"
        );

    const users =
        await response.json();

    console.log(users);

}
```

---

# 7. Generics

## Concept

Create reusable types.

---

## Problem

This only works for numbers.

```typescript
function identity(
    value: number
): number {

    return value;

}
```

---

## Generic Version

```typescript
function identity<T>(
    value: T
): T {

    return value;

}
```

---

## Usage

```typescript
identity<number>(10);

identity<string>("hello");
```

---

## Generic Array

```typescript
let items: Array<string> = [
    "A",
    "B"
];
```

Equivalent:

```typescript
let items: string[] = [
    "A",
    "B"
];
```

---

# Generic Mental Model

```text
T
↓
Placeholder Type

number
string
User
Product
Anything
```

---

# Real Example

```typescript
interface User {

    id: number;

    name: string;

}

function printUser(
    user: User
): void {

    console.log(
        user.name
    );

}
```

Usage:

```typescript
printUser({

    id: 1,

    name: "Gourav"

});
```

---

# Typical API Response

```typescript
interface User {

    id: number;

    name: string;

}

async function getUsers()
: Promise<User[]> {

    const response =
        await fetch(
            "/api/users"
        );

    return response.json();

}
```

---

# TypeAtlas-Relevant Concepts

You'll constantly see:

```typescript
interface User {}

interface Project {}

interface Skill {}

type UserId = number;

async function getUsers() {}

const users: User[] = [];

const project: Project = {};

await fetch(...);
```

---

# 90% of TypeScript You'll Use

## Variables

```typescript
let age: number = 21;

let name: string = "Gourav";

let active: boolean = true;
```

---

## Arrays

```typescript
let users: User[] = [];
```

---

## Interfaces

```typescript
interface User {

    id: number;

    name: string;

}
```

---

## Functions

```typescript
function add(
    a: number,
    b: number
): number {

    return a + b;

}
```

---

## Async

```typescript
const data =
    await fetch(url);
```

---

## Generics

```typescript
function identity<T>(
    value: T
): T {

    return value;

}
```

---

# Core Memory

```text
Type
 ↓
Defines Allowed Data

Interface
 ↓
Blueprint For Objects

Array
 ↓
List Of Values

Function
 ↓
Reusable Logic

Async/Await
 ↓
Handle Slow Operations

Generic
 ↓
Reusable Types
```

If you understand Interfaces + Functions + Async/Await, you already understand the majority of TypeScript used in modern React, Next.js, and backend applications.