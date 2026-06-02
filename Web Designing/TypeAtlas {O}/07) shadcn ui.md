# shadcn/ui Cheat Sheet

## Purpose

shadcn/ui provides ready-made React components built with:

```text
React
+
Tailwind CSS
+
Radix UI
=
shadcn/ui
```

Instead of building buttons, dialogs, tables, and forms from scratch, you import them and customize them.

---

# Mental Model

Without shadcn/ui:

```text
Build Button
Build Modal
Build Form
Build Table
Build Menu
```

With shadcn/ui:

```text
Import Component
      ↓
Customize
      ↓
Done
```

---

# Installation

Initialize shadcn:

```bash
npx shadcn@latest init
```

Add a component:

```bash
npx shadcn@latest add button
```

Example:

```bash
npx shadcn@latest add card
```

```bash
npx shadcn@latest add dialog
```

---

# Project Structure

```text
components/

└── ui/
    ├── button.tsx
    ├── card.tsx
    ├── dialog.tsx
    ├── table.tsx
    └── dropdown-menu.tsx
```

---

# 1. Button

## Purpose

Clickable action.

Examples:

- Save
- Delete
- Login
- Submit

---

## Import

```tsx
import {

    Button

} from "@/components/ui/button";
```

---

## Example

```tsx
<Button>

    Save

</Button>
```

---

## Variants

### Default

```tsx
<Button>

    Save

</Button>
```

---

### Destructive

```tsx
<Button
    variant="destructive"
>

    Delete

</Button>
```

---

### Outline

```tsx
<Button
    variant="outline"
>

    Cancel

</Button>
```

---

### Secondary

```tsx
<Button
    variant="secondary"
>

    Back

</Button>
```

---

# Mental Model

```text
Button
 ↓
Action Trigger
```

---

# 2. Card

## Purpose

Display grouped content.

Examples:

- User Profile
- Theory Entry
- Debate Summary
- Project Card

---

## Import

```tsx
import {

    Card,

    CardContent,

    CardHeader,

    CardTitle

}
from "@/components/ui/card";
```

---

## Example

```tsx
<Card>

    <CardHeader>

        <CardTitle>

            TypeAtlas

        </CardTitle>

    </CardHeader>

    <CardContent>

        Theory Database

    </CardContent>

</Card>
```

---

## Visual

```text
+----------------------+
| TypeAtlas            |
|                      |
| Theory Database      |
+----------------------+
```

---

# Mental Model

```text
Card
 ↓
Container
 ↓
Related Information
```

---

# 3. Dialog

## Purpose

Popup window.

Examples:

- Login
- Confirm Delete
- Settings
- Profile Edit

---

## Import

```tsx
import {

    Dialog,

    DialogContent,

    DialogTrigger

}
from "@/components/ui/dialog";
```

---

## Example

```tsx
<Dialog>

    <DialogTrigger>

        Open

    </DialogTrigger>

    <DialogContent>

        Hello World

    </DialogContent>

</Dialog>
```

---

## Visual

```text
[ Open ]

      ↓

+---------------+
| Hello World   |
+---------------+
```

---

# Mental Model

```text
Button
  ↓
Dialog Opens
  ↓
Popup Appears
```

---

# 4. Table

## Purpose

Display structured data.

Examples:

- Users
- Profiles
- Debates
- Rankings

---

## Import

```tsx
import {

    Table,

    TableBody,

    TableCell,

    TableHead,

    TableHeader,

    TableRow

}
from "@/components/ui/table";
```

---

## Example

```tsx
<Table>

    <TableHeader>

        <TableRow>

            <TableHead>

                Name

            </TableHead>

            <TableHead>

                Age

            </TableHead>

        </TableRow>

    </TableHeader>

    <TableBody>

        <TableRow>

            <TableCell>

                Gourav

            </TableCell>

            <TableCell>

                21

            </TableCell>

        </TableRow>

    </TableBody>

</Table>
```

---

## Visual

```text
+---------+------+
| Name    | Age  |
+---------+------+
| Gourav  | 21   |
+---------+------+
```

---

# Mental Model

```text
Rows
 ↓
Records

Columns
 ↓
Fields
```

---

# 5. Form

## Purpose

Collect user input.

Examples:

- Login
- Registration
- Profile Edit
- Theory Submission

---

## Common Components

```tsx
Input

Label

Button

Form
```

---

## Input Import

```tsx
import {

    Input

}
from "@/components/ui/input";
```

---

## Example

```tsx
<Input
    placeholder="Username"
/>
```

---

## Login Form

```tsx
<form
    className="space-y-4"
>

    <Input
        placeholder="Username"
    />

    <Input
        type="password"
        placeholder="Password"
    />

    <Button>

        Login

    </Button>

</form>
```

---

## Visual

```text
+----------------+
| Username       |
+----------------+

+----------------+
| Password       |
+----------------+

[ Login ]
```

---

# Mental Model

```text
Input
 ↓
User Data

Button
 ↓
Submit

Form
 ↓
Group Inputs
```

---

# 6. Dropdown Menu

## Purpose

Hidden options menu.

Examples:

- Profile Menu
- Settings
- Actions
- User Controls

---

## Import

```tsx
import {

    DropdownMenu,

    DropdownMenuContent,

    DropdownMenuItem,

    DropdownMenuTrigger

}
from "@/components/ui/dropdown-menu";
```

---

## Example

```tsx
<DropdownMenu>

    <DropdownMenuTrigger>

        Menu

    </DropdownMenuTrigger>

    <DropdownMenuContent>

        <DropdownMenuItem>

            Profile

        </DropdownMenuItem>

        <DropdownMenuItem>

            Settings

        </DropdownMenuItem>

    </DropdownMenuContent>

</DropdownMenu>
```

---

## Visual

```text
[ Menu ]

     ↓

Profile

Settings
```

---

# Typical TypeAtlas Components

## Profile Card

```tsx
<Card>

    <CardHeader>

        <CardTitle>

            INTP

        </CardTitle>

    </CardHeader>

    <CardContent>

        Analyst

    </CardContent>

</Card>
```

---

## Debate Table

```tsx
<Table>
...
</Table>
```

---

## Login Dialog

```tsx
<Dialog>
...
</Dialog>
```

---

## User Menu

```tsx
<DropdownMenu>
...
</DropdownMenu>
```

---

# Typical Page Composition

```text
Page

├── Button
├── Card
├── Card
├── Card
├── Table
├── Dialog
└── Dropdown Menu
```

---

# 90% of shadcn/ui You'll Use

## Button

```tsx
<Button>
    Save
</Button>
```

---

## Card

```tsx
<Card>
    ...
</Card>
```

---

## Dialog

```tsx
<Dialog>
    ...
</Dialog>
```

---

## Table

```tsx
<Table>
    ...
</Table>
```

---

## Input

```tsx
<Input />
```

---

## Dropdown Menu

```tsx
<DropdownMenu>
    ...
</DropdownMenu>
```

---

# Core Memory

```text
Button
 ↓
Action

Card
 ↓
Content Container

Dialog
 ↓
Popup Window

Table
 ↓
Structured Data

Form
 ↓
User Input

Dropdown Menu
 ↓
Hidden Actions
```

---

# Most Important Pattern

```tsx
<Card>

    <CardHeader>

        <CardTitle>

            Title

        </CardTitle>

    </CardHeader>

    <CardContent>

        Content

    </CardContent>

</Card>
```

A large percentage of modern Next.js dashboards, admin panels, SaaS applications, and content platforms are built from combinations of:

```text
Card
+
Button
+
Form
+
Table
+
Dialog
+
Dropdown Menu
```

These are the first shadcn/ui components worth mastering.