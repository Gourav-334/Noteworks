# Tailwind CSS Cheat Sheet

## Purpose

Tailwind CSS is a utility-first CSS framework.

Instead of writing:

```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

You write:

```html
<div class="flex justify-center items-center">
</div>
```

---

# Mental Model

Traditional CSS:

```text
Write CSS Class
       ↓
Apply Class
```

Tailwind:

```text
Apply Utility Classes Directly
```

---

# Example

Traditional CSS:

```html
<div class="card">
    Hello
</div>
```

```css
.card {
    padding: 20px;
    background: blue;
}
```

Tailwind:

```html
<div class="p-5 bg-blue-500">
    Hello
</div>
```

---

# Most Important Utilities

## Display

### Block

```html
<div class="block"></div>
```

---

### Inline

```html
<span class="inline"></span>
```

---

### Hidden

```html
<div class="hidden"></div>
```

---

# Flexbox

## Create Flex Layout

```html
<div class="flex">
</div>
```

Result:

```text
A B C
```

---

## Column Layout

```html
<div class="flex flex-col">
</div>
```

Result:

```text
A
B
C
```

---

## Center Horizontally

```html
<div class="flex justify-center">
</div>
```

---

## Center Vertically

```html
<div class="flex items-center">
</div>
```

---

## Center Both

```html
<div class="flex justify-center items-center">
</div>
```

---

## Space Between

```html
<div class="flex justify-between">
</div>
```

Result:

```text
A         B         C
```

---

## Practical Navbar

```html
<nav class="flex justify-between items-center p-4">

    <h1>TypeAtlas</h1>

    <button>
        Login
    </button>

</nav>
```

---

# Grid

## Two Columns

```html
<div class="grid grid-cols-2">
</div>
```

Result:

```text
1 2
3 4
```

---

## Three Columns

```html
<div class="grid grid-cols-3">
</div>
```

Result:

```text
1 2 3
4 5 6
```

---

## Gap

```html
<div class="grid grid-cols-3 gap-4">
</div>
```

Result:

```text
1    2    3

4    5    6
```

---

# Spacing

## Padding

### All Sides

```html
<div class="p-4">
</div>
```

---

### Horizontal

```html
<div class="px-4">
</div>
```

---

### Vertical

```html
<div class="py-4">
</div>
```

---

## Margin

### All Sides

```html
<div class="m-4">
</div>
```

---

### Top

```html
<div class="mt-4">
</div>
```

---

### Bottom

```html
<div class="mb-4">
</div>
```

---

### Left

```html
<div class="ml-4">
</div>
```

---

### Right

```html
<div class="mr-4">
</div>
```

---

# Common Spacing Scale

| Class | Size |
|---------|---------|
| p-1 | 4px |
| p-2 | 8px |
| p-4 | 16px |
| p-6 | 24px |
| p-8 | 32px |
| p-10 | 40px |

---

# Colors

## Background

```html
<div class="bg-blue-500">
</div>
```

---

## Text

```html
<p class="text-red-500">
</p>
```

---

## Border

```html
<div class="border border-gray-300">
</div>
```

---

# Common Colors

```html
bg-blue-500

bg-red-500

bg-green-500

bg-yellow-500

bg-gray-500

bg-black

bg-white
```

---

# Typography

## Text Sizes

```html
text-sm
text-base
text-lg
text-xl
text-2xl
text-4xl
```

---

## Font Weight

```html
font-light

font-normal

font-medium

font-bold
```

---

# Width & Height

## Width

```html
w-full
```

100%

---

```html
w-1/2
```

50%

---

```html
w-screen
```

Full screen width

---

## Height

```html
h-full
```

---

```html
h-screen
```

Full screen height

---

# Borders

## Basic Border

```html
<div class="border">
</div>
```

---

## Rounded Corners

```html
rounded
```

---

```html
rounded-lg
```

---

```html
rounded-xl
```

---

## Example

```html
<div
    class="
    border
    rounded-lg
    p-4
">
</div>
```

---

# Shadows

```html
shadow
```

---

```html
shadow-md
```

---

```html
shadow-lg
```

---

Example:

```html
<div
    class="
    shadow-lg
    rounded-lg
    p-4
">
</div>
```

---

# Responsive Layouts

## Concept

Different styles for different screen sizes.

---

# Breakpoints

| Prefix | Device |
|----------|----------|
| sm: | Small |
| md: | Tablet |
| lg: | Laptop |
| xl: | Desktop |

---

# Example

```html
<div
    class="
    grid
    grid-cols-1
    md:grid-cols-2
    lg:grid-cols-3
">
</div>
```

---

Result

Mobile:

```text
1
2
3
```

Tablet:

```text
1 2
3
```

Desktop:

```text
1 2 3
```

---

# Practical Card

```html
<div
    class="
    border
    rounded-lg
    shadow-md
    p-4
    bg-white
"
>

    <h2
        class="
        text-xl
        font-bold
        mb-2
    "
    >
        TypeAtlas
    </h2>

    <p
        class="
        text-gray-600
    "
    >
        Theory Database
    </p>

</div>
```

---

# Practical Centered Page

```html
<div
    class="
    flex
    justify-center
    items-center
    h-screen
"
>

    <h1>
        Welcome
    </h1>

</div>
```

---

# Practical Responsive Grid

```html
<div
    class="
    grid
    grid-cols-1
    md:grid-cols-2
    lg:grid-cols-3
    gap-6
"
>

    <div>Card 1</div>

    <div>Card 2</div>

    <div>Card 3</div>

</div>
```

---

# 90% of Tailwind You'll Use

## Layout

```html
flex

flex-col

grid

grid-cols-2

grid-cols-3
```

---

## Alignment

```html
justify-center

justify-between

items-center
```

---

## Spacing

```html
p-4

p-6

m-4

mt-4

mb-4

gap-4
```

---

## Colors

```html
bg-blue-500

bg-white

text-black

text-gray-600
```

---

## Sizing

```html
w-full

h-screen
```

---

## Styling

```html
border

rounded-lg

shadow-md
```

---

## Responsive

```html
sm:

md:

lg:

xl:
```

---

# Core Memory

```text
flex
 ↓
Row / Column Layout

grid
 ↓
Rows + Columns

p-4
 ↓
Padding

m-4
 ↓
Margin

bg-blue-500
 ↓
Background Color

text-xl
 ↓
Text Size

rounded-lg
 ↓
Rounded Corners

shadow-md
 ↓
Shadow

md:
 ↓
Tablet Style

lg:
 ↓
Desktop Style
```

---

# Most Important Tailwind Pattern

```html
<div
    class="
    flex
    justify-between
    items-center
    p-4
    bg-white
    rounded-lg
    shadow-md
"
>
</div>
```

If you master **flex**, **grid**, **spacing**, **responsive breakpoints**, and **common utility classes**, you can build the vast majority of practical UIs without writing custom CSS.