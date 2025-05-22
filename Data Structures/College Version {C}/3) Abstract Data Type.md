# $\fbox{Chapter 3: ABSTRACT DATA TYPES}$





### <u>Stacks</u>

- Stack is an **Abstract Data Type** (ADT).
- ADT are data types which contain values, and we can apply certain special operations on it.
- It is called abstract as information are hidden from user.
- ADT is made with primitive data types.
- `peek()` - Returns top element without removing it.
- `isFull()` - Checks if stack is full.
- `isEmpty()` - Checks is stack is empty.
- In any `push()` or `pop()` operation, always print if stack is full/ empty/ successful/ failure etc.


### <u>Application Of Stacks</u>

- Recursion
- Polish expression
- Reverse Polish expression


### <u>Recursion</u>

- Base case is the piece of code used to avoid infinite loops by terminating it.
- Recursive call is the piece of code executed during iterations.

#### Two types:

1. **<u>Direct recursion</u>:** Function calls itself inside it.
2. **<u>Indirect recursion</u>:** Two functions calling each other.


### <u>Tower Of Henoi</u>

- Chinese/Japanese game resembling appearance of a stack.
- 3 rods are there, 1st with the rings (small, normal, large etc).
- 2nd rod for temporary storage.
- 3rd rod to prepare final result.
- Larger rings must be below and smaller rings must be above.
- Minimum number of moves is $(2^{n} - 1)$


### <u>Expression Parsing</u>

- The way to write arithmetic expression, or use arithmetic operators is known as a notation.
- 3 ways to write it without changing the output - Infix notation, prefix (polish), postfix (reverse polish).
- **<u>Infix notation</u>:** $a+b$ (normal in between operators)
- **<u>Prefix notation</u>:** $+ab$ (operator before expression)
- **<u>Postfix notation</u>:** $ab+$

| Operator                                 |  Precedence  | Value |
| :--------------------------------------- | :----------: | :---: |
| Exponentiation ($\$$ or $\uparrow$ or ^) |   Highest    |   3   |
| $*$, $/$                                 | Next highest |   2   |
| $+$, $-$                                 |    Lowest    |   1   |


### <u>Infix To Postfix Conversion</u>

- Operators are symbols, operands are values involved.
- Use `push()` and `pop()` logics to store operators in stack and output operands.
- Go from left to right of expression.
- Lowest priority $(()),$ higher $(+,-),$ highest $(*,/)$.
- Make two columns - **stack** and **postfix string**.
- Write operands in postfix string and operators in stack column one by one.
- Add symbols to right in both columns.
- Two operators of same precedence can’t be together in postfix column, so if such situation comes, pop the operator on left side out of the two from postfix, and add it to the rightmost of stack.
- If an operator comes between brackets, then pop both the brackets and the operator between it, and add the operator between to the stack.
- Our goal is to obtain the final postfix answer.


### <u>Infix To Prefix Conversion</u>

- Reverse the given infix expression.
- Solve it by making: **stack** and **postfix column**
- Now **reverse the final postfix** solution expression, that’s our required prefix solution.


### <u>Evaluation Of Postfix Expression</u>

- Make two columns: **symbol scanned** and **stack**
- Go left to right.
- If an operand is scanned, add it to the stack.
- If an operator is scanned, then pop and perform that symbol operation between the last two operands. Replace the last two operand with the result.


### <u>Types Of Queues</u>

- Simple queue
- Circular queue
- Priority queue
- **<u>Queue</u>:** Insertion in front, deletion in rear.


### <u>Application Of Queue</u>

- Process scheduling, the round robin algorithm.
- **Spooling**, copying of data from one device to another.


### <u>Operations On Queue</u>

- `initialize()` - Empties the queue.
- `empty()` - Gives answer in binary.
- `full()` - *\*same as above*
- `print()` - Prints all queue elements.
- `enqueueF`/`enqueueR`/`dequeueF`/`dequeueR` (front/rear)
- If you delete any queue element from front, nothing can occupy the empty space, a major disadvantage.
- **<u>Circular queue</u>:** Elements deleted in an order (right to left) and are added in the empty spaces, from left to right.
- **<u>Input restriction</u>:** Enabling deletion at both ends in a queue, but input at one only.
- **<u>Output restriction</u>:** *\*Now you know*


### <u>Methods To Implement Dequeue</u>

- Circular array
- Singly linked list
- Doubly linked list
- Singly circular linked list
- Doubly circular linked list


### <u>Priority queue</u>

- Operations done on the basis of priority given in problem, also for multiple elements of same priority its first come first serve.


### <u>Implementation Of Priority Queues</u>

#### Unsorted:

- Insert - $O(1)$
- Delete - $O(n)$

#### Sorted:

- Insert - $O(n)$
- Sorted - $O(1)$

---
