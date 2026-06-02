# React Cheat Sheet

## Purpose

React is a library for building user interfaces.

Think:

```text
HTML
+
JavaScript
+
Reusable Components
=
React
```

React allows pages to update automatically when data changes.

---

# Mental Model

Traditional HTML:

```text
Change Data
    ↓
Manually Update Page
```

React:

```text
Change Data
    ↓
React Updates Page
```

---

# Core Idea

Everything is a Component.

```text
Web Page

├── Navbar
├── Sidebar
├── Profile Card
├── Project Card
└── Footer
```

Each piece becomes a reusable component.

---

# 1. Components

## Concept

Reusable UI block.

Think:

```text
Function
   ↓
Returns UI
```

---

## Example

```jsx
function Welcome() {

    return (
        <h1>Hello</h1>
    );

}
```

Usage:

```jsx
<Welcome />
```

Result:

```html
<h1>Hello</h1>
```

---

# Real Example

```jsx
function UserCard() {

    return (

        <div>

            <h2>Gourav</h2>

            <p>Systems Programmer</p>

        </div>

    );

}
```

Usage:

```jsx
<UserCard />
```

---

# Component Mental Model

```text
Function
   ↓
UI
```

Like:

```text
printf()
returns text

UserCard()
returns HTML
```

---

# 2. Props

## Concept

Pass data into a component.

Think:

```text
Function Argument
      ↓
Props
```

---

## Example

```jsx
function Welcome(props) {

    return (
        <h1>
            Hello {props.name}
        </h1>
    );

}
```

Usage:

```jsx
<Welcome name="Gourav" />
```

Output:

```text
Hello Gourav
```

---

# Destructuring (Modern)

```jsx
function Welcome({ name }) {

    return (
        <h1>
            Hello {name}
        </h1>
    );

}
```

---

# Multiple Props

```jsx
function UserCard({

    name,

    role

}) {

    return (

        <div>

            <h2>{name}</h2>

            <p>{role}</p>

        </div>

    );

}
```

Usage:

```jsx
<UserCard

    name="Gourav"

    role="Systems Programmer"

/>
```

---

# Props Mental Model

```text
Parent
   ↓
Props
   ↓
Child
```

---

# 3. State

## Concept

Component's internal memory.

Stores values that can change.

Examples:

- Counter
- Search text
- Form data
- Theme

---

Without state:

```text
UI Never Changes
```

With state:

```text
Data Changes
      ↓
UI Updates
```

---

# 4. Hooks

## Concept

Special React functions.

Examples:

```jsx
useState()

useEffect()

useRef()

useMemo()
```

For beginners:

```text
Hooks
  ↓
Give Components Extra Powers
```

---

# 5. useState

## Concept

Store changing data.

---

## Syntax

```jsx
const [

    value,

    setValue

] = useState(initialValue);
```

---

## Example

```jsx
import { useState }
from "react";

function Counter() {

    const [

        count,

        setCount

    ] = useState(0);

    return (

        <div>

            <p>
                {count}
            </p>

            <button
                onClick={() =>
                    setCount(
                        count + 1
                    )
                }
            >
                Increment
            </button>

        </div>

    );

}
```

---

# Mental Model

```text
count
  ↓
Stored In State

setCount()
  ↓
Changes State

State Changes
  ↓
React Re-renders
```

---

# Example

Initial:

```text
0
```

Click:

```text
1
```

Click:

```text
2
```

Click:

```text
3
```

React updates automatically.

---

# useState With Text

```jsx
const [

    name,

    setName

] = useState("");
```

Update:

```jsx
setName("Gourav");
```

---

# Form Example

```jsx
function Form() {

    const [

        username,

        setUsername

    ] = useState("");

    return (

        <input

            value={username}

            onChange={
                (e) =>
                    setUsername(
                        e.target.value
                    )
            }

        />

    );

}
```

---

# 6. useEffect

## Concept

Run code when something happens.

Examples:

- Component loads
- State changes
- API call
- Timer

---

# Syntax

```jsx
useEffect(() => {

    // code

}, []);
```

---

# Run Once

```jsx
useEffect(() => {

    console.log(
        "Loaded"
    );

}, []);
```

Runs only when component first appears.

---

# Run When State Changes

```jsx
useEffect(() => {

    console.log(
        count
    );

}, [count]);
```

Every time count changes:

```text
count changed
```

---

# API Example

```jsx
useEffect(() => {

    fetch("/api/users")
        .then(res =>
            res.json()
        )
        .then(data =>
            console.log(
                data
            )
        );

}, []);
```

---

# useEffect Mental Model

```text
Event Happens
      ↓
Effect Runs
```

---

# Putting Everything Together

```jsx
import {

    useState,

    useEffect

} from "react";

function Counter() {

    const [

        count,

        setCount

    ] = useState(0);

    useEffect(() => {

        console.log(
            "Count changed"
        );

    }, [count]);

    return (

        <div>

            <p>
                {count}
            </p>

            <button
                onClick={() =>
                    setCount(
                        count + 1
                    )
                }
            >
                Increment
            </button>

        </div>

    );

}
```

---

# Data Flow

```text
Parent Component
       ↓
      Props
       ↓
Child Component
       ↓
      State
       ↓
UI Updates
```

---

# Typical TypeAtlas Example

```jsx
function ProjectCard({

    project

}) {

    return (

        <div>

            <h2>
                {project.name}
            </h2>

            <p>
                {project.description}
            </p>

        </div>

    );

}
```

Usage:

```jsx
<ProjectCard
    project={project}
/>
```

---

# 90% of React You'll Use

## Component

```jsx
function Component() {

    return <div />;
}
```

---

## Props

```jsx
function User({

    name

}) {

    return <p>{name}</p>;
}
```

---

## State

```jsx
const [

    value,

    setValue

] = useState("");
```

---

## Effect

```jsx
useEffect(() => {

}, []);
```

---

## Event

```jsx
onClick={() => {}}
```

---

# Core Memory

```text
Component
 ↓
Reusable UI

Props
 ↓
Data From Parent

State
 ↓
Internal Memory

Hook
 ↓
Special React Function

useState
 ↓
Store Changing Data

useEffect
 ↓
Run Side Effects

State Changes
 ↓
React Re-renders UI
```

---

# Most Important Flow

```text
User Clicks Button
        ↓
setState()
        ↓
State Changes
        ↓
React Re-renders
        ↓
UI Updates
```

If you understand Components + Props + useState, you understand the majority of beginner-to-intermediate React.