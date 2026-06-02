# HTML & CSS Basics Cheat Sheet

## Purpose

Understand how web pages are structured and arranged.

HTML = Structure  
CSS = Appearance + Layout

Think:

```text
HTML = Skeleton
CSS = Skin + Clothing + Positioning
```

---

# Mental Model

```text
Web Page

<html>
 ├── Header
 ├── Navigation
 ├── Main Content
 ├── Sidebar
 └── Footer
```

HTML creates the blocks.

CSS decides:

- Size
- Color
- Position
- Alignment
- Spacing

---

# 1. div

## Concept

Generic container.

Used to group elements together.

## Example

```html
<div>
    Hello World
</div>
```

## Real Example

```html
<div class="card">
    <h2>Product Name</h2>
    <p>Description</p>
</div>
```

## Visual

```text
+----------------+
| Product Name   |
| Description    |
+----------------+
```

---

# 2. form

## Concept

Collect user input.

Used for:

- Login
- Registration
- Search
- Contact Forms

## Example

```html
<form>
    ...
</form>
```

## Visual

```text
+------------------+
| Username         |
| Password         |
| Submit           |
+------------------+
```

---

# 3. input

## Concept

Field where users enter data.

## Example

```html
<input type="text">
```

### Common Types

Text

```html
<input type="text">
```

Password

```html
<input type="password">
```

Email

```html
<input type="email">
```

Number

```html
<input type="number">
```

Date

```html
<input type="date">
```

---

# 4. button

## Concept

Triggers an action.

## Example

```html
<button>Submit</button>
```

## Visual

```text
[ Submit ]
```

---

# Login Form Example

```html
<form>

    <input
        type="text"
        placeholder="Username"
    >

    <input
        type="password"
        placeholder="Password"
    >

    <button>
        Login
    </button>

</form>
```

Result:

```text
+------------------+
| Username         |
+------------------+

+------------------+
| Password         |
+------------------+

[ Login ]
```

---

# CSS Layout

Before CSS:

```text
Everything stacks vertically.
```

```text
Item 1

Item 2

Item 3
```

CSS lets us control layout.

---

# 5. Flexbox

## Concept

Arrange items in one direction.

- Row
- Column

Perfect for:

- Navigation bars
- Buttons
- Cards
- Menus

---

## HTML

```html
<div class="container">

    <div>A</div>
    <div>B</div>
    <div>C</div>

</div>
```

---

## CSS

```css
.container {
    display: flex;
}
```

Result:

```text
A B C
```

---

## Column Layout

```css
.container {
    display: flex;
    flex-direction: column;
}
```

Result:

```text
A
B
C
```

---

## Centering

```css
.container {

    display: flex;

    justify-content: center;

    align-items: center;
}
```

Result:

```text
       A
   (centered)
```

---

# Common Flexbox Commands

## Space Between

```css
justify-content: space-between;
```

```text
A         B         C
```

---

## Space Around

```css
justify-content: space-around;
```

```text
  A      B      C
```

---

## Align Center

```css
align-items: center;
```

```text
   A
   B
   C
```

---

# 6. Grid

## Concept

Arrange items in rows and columns.

Perfect for:

- Dashboards
- Galleries
- Product pages

---

## HTML

```html
<div class="grid">

    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>4</div>

</div>
```

---

## CSS

```css
.grid {

    display: grid;

    grid-template-columns:
        1fr 1fr;
}
```

Result:

```text
1 2
3 4
```

---

## Three Columns

```css
.grid {

    display: grid;

    grid-template-columns:
        1fr 1fr 1fr;
}
```

Result:

```text
1 2 3
4 5 6
```

---

# Flexbox vs Grid

| Flexbox | Grid |
|----------|----------|
| One Direction | Two Directions |
| Row OR Column | Rows AND Columns |
| Menus | Dashboards |
| Navbar | Gallery |
| Buttons | Product Layout |

Think:

```text
Flexbox = Line

Grid = Table
```

---

# 7. Positioning

## Concept

Control where elements appear.

---

## Static (Default)

```css
position: static;
```

Browser decides placement.

---

## Relative

```css
position: relative;
left: 20px;
```

Moves relative to original location.

```text
Original → Shifted
```

---

## Absolute

```css
position: absolute;
top: 0;
right: 0;
```

Placed relative to parent.

Useful for:

- Badges
- Notifications
- Icons

---

## Fixed

```css
position: fixed;
bottom: 20px;
right: 20px;
```

Stays on screen while scrolling.

Example:

```text
Chat Button
Back To Top Button
```

---

## Sticky

```css
position: sticky;
top: 0;
```

Behaves normally until scrolling reaches it.

Then it sticks.

Example:

```text
Sticky Navbar
```

---

# Typical Page Structure

```html
<body>

    <header>
        Navbar
    </header>

    <main>

        <section>
            Hero
        </section>

        <section>
            Products
        </section>

    </main>

    <footer>
        Footer
    </footer>

</body>
```

Visual:

```text
+-------------------+
| Navbar            |
+-------------------+

| Hero Section      |

+-------------------+

| Products          |

+-------------------+

| Footer            |
+-------------------+
```

---

# Mini Project

```html
<div class="card">

    <h2>Laptop</h2>

    <p>₹50,000</p>

    <button>
        Buy Now
    </button>

</div>
```

```css
.card {

    width: 300px;

    padding: 20px;

    border: 1px solid black;
}
```

Result:

```text
+------------------+
| Laptop           |
| ₹50,000          |
| [ Buy Now ]      |
+------------------+
```

---

# 90% Concepts You'll Use

```html
<div></div>

<form></form>

<input>

<button>
```

```css
display: flex;

display: grid;

justify-content: center;

align-items: center;

position: relative;

position: absolute;

position: fixed;
```

---

# Core Memory

```text
HTML
 ↓
Creates Structure

CSS
 ↓
Controls Layout

Flexbox
 ↓
One Direction Layout

Grid
 ↓
Two Direction Layout

Position
 ↓
Manual Placement
```

Understand these concepts and you can read most modern web page structures.