# $\fbox{Module 1: BOOLEAN LOGIC}$

>**Purpose**
>Understand Boolean logic as **constraints on system states**, not algebraic manipulation.

---

## 1. What a Digital Signal _Is_

- A digital signal allows **only two valid states**: `0` or `1`
- These are **regions**, not exact voltages
- Digital reliability comes from **noise margins**, not precision

> A digital signal answers: _Is the condition satisfied or not?_

---

## 2. Boolean Variables

- A Boolean variable represents a **condition**
- `1` → condition true / allowed
- `0` → condition false / disallowed

#### Examples:

- `POWER_OK = 1` → supply is valid
- `RESET = 0` → system not allowed to run

Boolean variables are **logical flags**, not numbers.

---

## 3. Logic Gates as Constraints

### AND gate

- Output = 1 **only if all conditions are satisfied**
- Constraint: `A = 1 ∧ B = 1`

### OR gate

- Output = 1 if **any condition is satisfied**
- Constraint: `A = 1 ∨ B = 1`

### NOT gate

- Output = opposite of input
- Constraint inversion

> Gates do not _compute_ — they **enforce rules**.

---

## 4. Truth Tables = Constraint Tables

#### A truth table lists:

- Allowed input combinations
- Forbidden combinations

#### Think of it as:

> “Which system states are permitted?”

#### Not:

> “What math gives this output?”

---

## 5. Boolean Expressions

- A Boolean expression is a **compact rule description**

#### Example:

```
Y = A · B̅
```

#### Means:

- `A` must be true
- `B` must be false

That’s a **policy**, not a calculation.

---

## 6. Laws of Boolean Algebra (Why They Exist)

|Law|Meaning|
|---|---|
|Idempotent|Repeating a condition changes nothing|
|Complement|A condition and its negation cannot coexist|
|De Morgan|Constraints can be rewritten, not changed|

These laws preserve **allowed state sets**.

---

## 7. Hardware Interpretation

- Transistors act as **switches enforcing constraints**
- Logic gates are **physical rule enforcers**
- Circuits reject invalid states automatically

Digital electronics works because **physics enforces logic**.

---

## 8. Mental Model (Use This)

> **Boolean logic = rules about which combinations of conditions are allowed to exist simultaneously.**

If you can state the rule in words, the logic is already understood.

---

## Module 1 End

**Invariant learned:** Digital systems are about **valid states**, not arithmetic.