# $\fbox{Chapter 8: CODE GENERATION}$





## **Topic - 1: Code Generator**

### <u>Introduction</u>

- **<u>Code generator</u>:** Produces target code for three-address statement, using registers to store operands.
- **<u>Three-address statement</u>:** An equation involving three operands (representing their addresses).
- Any bigger equation can be broken into many three-address statement.


### <u>Example</u>

#### Source code:

```c
x = y + z
```

#### Target code:

```asm
MOV x, r0
MOV y, r0
```


### <u>Register & Address Descriptor</u>

- **<u>Register descriptor</u>:** Tracks what's currently in the register.
- **<u>Address descriptor</u>:** Stores address for a variable.


### <u>Code Generation Algorithm</u>

```
a := b op c
```

1. A function is called to find storage location for result.
2. Add addresses of values in address descriptors if not there.
3. Empty descriptors from old values if required.
4. After the operation, empty the involved registers.


### <u>Example 2</u>

#### Source code:

```c
d = (a - b) + (a - c) + (a - c)
```

$$ d\;=\;(3\;*\;a)\;-\;b\;+\;(2\;*\;c) $$

#### Target code:

```asm
movl $a, %rax
mull $3
subl $b, %rax
xorl %rbx, %rbx
addl $c, %rbx
imul $2, %rbx
addl %rbx, %rax
```



## **Topic - 2: Design Issues**

### <u>Possible Issues</u>

1. Input to code generator
2. Target program
3. Memory management
4. Instruction selection
5. Register allocation
6. Evaluation order


### <u>Input To The Code Generator</u>

- This input contains intermediate generated code & symbol table.
- This intermediate generation can be in form of postfix notation, syntax tree or three-address code.
- These intermediate representations can be manipulated directly by machine instructions.
- Any design issue at this level might affect translation to machine instructions.


### <u>Target Program</u>

- There are three possibilities when converting to target program.

#### Possibilities:

1. Target program is assembly, which takes control for the rest of execution.
2. **<u>Relocatable machine language</u>:** Allocates memory for program at a suitable location, which is better.
3. **<u>Absolute machine language</u>:** Allocates memory for program at a fixed location.


### <u>Memory Management</u>

- When code is being generated, the symbol tables are mapped to actual physical addresses.
- Identifier names are too mapped in the memory.


### <u>Instruction Selection</u>

- There must be no ambiguity in generated instruction set.
- Quality of generated instruction set is determined by its speed & size.


### <u>Register Allocation</u>

- Instructions which use register operands instead of memory operands are faster.
- **<u>Register allocation</u>:** Moving a variable to register.
- **<u>Register assignment</u>:** Accessing a register containing a variable.
- Some instruction set contain even & odd registers to store different parts of result.
- For example, in division an odd register might contain quotient & even might contain remainder.


### <u>Evaluation Order</u>

- Order of evaluating instruction matters as it affects of speed.
- Also it depends on how many registers are involved in whole operation.



## **Topic - 3: Target Machine**

### <u>Introduction</u>

- Target machine must be byte addressable, have general purpose registers & two-address instructions.
- In layman's language, it must be similar to x86 architecture.

```asm
op-code source, destination
```


### <u>Operation Cost</u>

|  Addressing Mode  | Example                | Added Cost |
| :---------------: | :--------------------- | :--------: |
|     Absolute      | `addl %rbx, %rax`      |    $1$     |
|     Register      | `addl $temp, %rax`     |    $0$     |
|      Indexed      | `addl 100(%rcx), %rbx` |    $1$     |
| Indirect register | `addl *100`            |    $0$     |
| Indirect indexed  | `%rbx, (%rcx)`         |    $1$     |
|      Literal      | `addl $3, %rbx`        |    $1$     |

- Cost as $1$ means the particular instruction occupies one word in memory.
- Cost also depends on the source & destination.


### <u>Example</u>

```asm
MOV R0, M
```

$$ Cost\;=\;1\;+\;1\;+\;1 $$

- One cost belongs to the memory which is of one word, another to the result we get & final one is the instruction itself.



## **Topic - 4: Runtime Storage Management**

### <u>Types Of Allocations</u>

1. **<u>Static allocation</u>:** Position of activation records are fixed in memory.
2. **<u>Stack allocation</u>:** Whenever the running program encounters execution of procedure, a new activation record is pushed to the stack.


### <u>Associated Runtime Statements</u>

1. Call
2. Return
3. Halt
4. Action (set of statements)


### <u>Runtime Memory Owners</u>

1. Code
2. Static data
3. Stack



## **Topic - 5: Basic Block**

- **<u>Basic block</u>:** A block containing sequence of statements to execute.
- For example, the `if` block or `while` block etc.
- **<u>Leader</u>:** The first statement in a block, which can be conditional or non-conditional.
- For example, `if (state==2)`.
- In assembly, its equivalent code is written using `goto <section>`.



## **Topic - 6: Flow Graph**

- **<u>Flow graph</u>:** Representing flow diagrams of basic blocks, using just rectangle & arrows.
- Rectangles here represent blocks with their codes inside them.
- Arrows show the flow of program.
