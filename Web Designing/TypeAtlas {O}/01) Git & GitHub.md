# Git & GitHub Cheat Sheet

## Mental Model

```text
Working Directory
       |
       | git add
       v
     Staging
       |
       | git commit
       v
   Local Repository
       |
       | git push
       v
 Remote Repository (GitHub)
```

---

# 1. Clone

## Concept

Copy an existing remote repository to your machine.

## When?

First time downloading a project.

## Command

```bash
git clone https://github.com/user/project.git
```

## Result

```text
GitHub Repo
      ↓
Your Computer
```

---

# 2. Add

## Concept

Move changed files into the staging area.

## When?

After editing files.

## Commands

Add one file:

```bash
git add main.c
```

Add everything:

```bash
git add .
```

## Result

```text
Working Directory
      ↓
    Staging
```

---

# 3. Commit

## Concept

Create a snapshot (checkpoint) of staged changes.

## When?

After finishing a logical piece of work.

## Command

```bash
git commit -m "Implemented login system"
```

## Result

```text
Staging
    ↓
Commit
```

Think of it as:

```text
Save Game
```

---

# 4. Push

## Concept

Upload local commits to GitHub.

## When?

After committing.

## Commands

```bash
git push
```

First push of a new branch:

```bash
git push -u origin feature-login
```

## Result

```text
Local Repo
     ↓
 GitHub
```

---

# 5. Pull

## Concept

Download the latest changes from GitHub.

## When?

Before starting work.

## Command

```bash
git pull
```

## Result

```text
GitHub
   ↓
Local Repo
```

---

# 6. Branch

## Concept

An independent line of development.

## Why?

Allows you to work without affecting the main codebase.

### Create Branch

```bash
git branch feature-login
```

### Switch Branch

```bash
git checkout feature-login
```

Modern way:

```bash
git switch feature-login
```

### Create and Switch

```bash
git switch -c feature-login
```

### View Branches

```bash
git branch
```

## Result

```text
main
  \
   feature-login
```

---

# 7. Merge

## Concept

Combine changes from one branch into another.

## Example

Current state:

```text
main
  \
   feature-login
```

### Step 1: Switch to Main

```bash
git switch main
```

### Step 2: Merge

```bash
git merge feature-login
```

## Result

```text
main ---------
  \          /
   feature---
```

---

# 8. Pull Request (PR)

## Concept

Request review and approval before merging code.

## Workflow

```text
Create Branch
      ↓
Make Changes
      ↓
Commit
      ↓
Push
      ↓
Open Pull Request
      ↓
Review
      ↓
Merge
```

## Command

Push branch:

```bash
git push -u origin feature-login
```

Then on GitHub:

```text
New Pull Request
```

GitHub CLI:

```bash
gh pr create
```

---

# Daily Solo Developer Workflow

```bash
git pull

# work...

git add .

git commit -m "Added new feature"

git push
```

---

# Team Workflow

```bash
git pull

git switch -c feature-x

# work...

git add .

git commit -m "Implemented feature x"

git push -u origin feature-x
```

Then:

```text
GitHub → Open Pull Request
```

---

# Emergency Commands

## Check Status

```bash
git status
```

Shows:

- Modified files
- Staged files
- Current branch

---

## View Commit History

```bash
git log
```

Compact view:

```bash
git log --oneline
```

---

## Undo Staging

```bash
git restore --staged file.c
```

---

## Undo File Changes

```bash
git restore file.c
```

---

## Delete Branch

Local:

```bash
git branch -d feature-login
```

Remote:

```bash
git push origin --delete feature-login
```

---

# 90% Commands You'll Use

```bash
git clone <repo>

git status

git add .

git commit -m "message"

git push

git pull

git switch -c branch-name

git switch main

git merge branch-name

git log --oneline
```

---

# Quick Reference Table

| Concept | Command |
|----------|----------|
| Clone Repo | `git clone <url>` |
| Check Status | `git status` |
| Stage Files | `git add .` |
| Commit | `git commit -m "msg"` |
| Push | `git push` |
| Pull | `git pull` |
| Create Branch | `git switch -c branch` |
| Switch Branch | `git switch branch` |
| Merge Branch | `git merge branch` |
| View History | `git log --oneline` |
| Delete Branch | `git branch -d branch` |

---

# Core Memory

```text
Edit File
    ↓
git add .
    ↓
git commit -m "message"
    ↓
git push
```

Everything else is built around this flow.