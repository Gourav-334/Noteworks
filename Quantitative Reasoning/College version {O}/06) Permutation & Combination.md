# $\fbox{Chapter 6: PERMUTATION \& COMBINATION}$





## **Topic - 1: Basic Concepts**

### <u>Introduction</u>

- **<u>Permutation</u>:** Set of all possible arrangements for some given elements or entities. Order matters.
- **<u>Combination</u>:** Set of all possible arrangements for some given elements or entities, but with possible repetition of same set of elements/entities.


### <u>Examples</u>

#### Permutation:

For a given set of elements: $\{a, b, c\}$

$$ \{a\},\;\{b\},\;\{c\} $$
$$ \{a,\;b\},\;\{b,\;c\},\;\{a,\;c\} $$
$$ \{a,\;b,\;c\} $$

#### Combination:

For same set of elements:

$$ \{a\},\;\{b\},\;\{c\} $$
$$ \{a,\;b\},\;\{b,\;a\},\;\{b,\;c\},\;\{c,\;b\},\;\{a,\;c\},\;\{c,\;a\} $$
$$ \{a,\;b,\;c\},\;\{a,\;c,\;b\},\;\{b,\;a,\;c\},\;\{b,\;c,\;a\},\;\{c,\;a,\;b\},\;\{c,\;b,\;a\} $$


### <u>Fundamental Principles Of Counting</u>

- Fundamental principles of counting are used to know number of possible outcomes.

#### Principle of multiplication:

- When one event can occur in $a$ ways & another one can occur $b$ ways.
- Then the total number of possibilities is $m \times n$.
- Similarly there is principle of addition.



## **Topic - 2: Permutation**

### <u>Theorem - I</u>

- $n$ is the number of elements/items.
- $r$ is the number of positions available.

$$ P(n,r)\;=\;_nP_r\;=\;^nP_r $$
$$ _nP_r\;=\;\frac{n!}{(n-r)!}\;\;\;\;\;\{ 0\;\le\;r\;\le\;n \} $$
$$ _nP_n\;=\;n! $$


### <u>Theorem - II</u>

Number of arrangements possible on a circular perimeter with $n$ objects:

$$ (n-1)! $$



## **Topic - 3: Combinations**

- Combinations can be called as subset of permutation.

$$ _nC_r\;=\;\frac{n!}{r!(n-r)!} $$



## **Topic - 4: Probability**

### <u>Introduction</u>

- **<u>Sure experiment/ trial</u>:** Experiments whose outcome is known to us in advance.
- **<u>Random event</u>:** Uncertain event with more than one possibility of outcomes.


### <u>Types Of Events</u>

- **<u>Certain event</u>:** Event that will happen, no matter what.
- **Impossible event**
- **<u>Mutually exclusive events</u>:** Events that can't happen simultaneously.

$$ P(A\;\cup\;B)\;=\;P(A)\;+\;P(B) $$

- **<u>Dependent events</u>:** Opposite of mutually exclusive events.
- **Equally likely events**
- **<u>Exhaustive events</u>:** Events which together include all the possibilities.


### <u>Classic Approach</u>

$$ P(A)\;=\;\frac{m}{n} $$
$$ P(A')\;=\;\frac{n-m}{n} $$

---
