# $\fbox{Chapter 1: INTRODUCTION}$





## **Topic - 1: Basic Information**

### <u>Usage</u>

- Assembly is preferred to write bootloaders & low-level kernel components.
- This is for being faster than medium-level languages like C.
- New features & instructions added by processor manufacturers can often be accessed only with assembly.


### <u>About The Book</u>

- ***"x86 Assembly (AT&T GAS) by Wikibooks"*** introduces both basic & advanced topics for all type of readers.
- Whether beginner or experienced, everyone is encouraged to read the book.


### <u>Book Sections</u>

1. Family of x86 chips & basic instruction set.
2. Differences among various assembler syntaxes.
3. Additional instruction sets.
4. Advanced low-level programming & inline assembly.
5. x86 computer architecture & hardware.



## **Topic - 2: Frequently Asked Questions**

### <u>How Computer Understands Assembly?</u>

$$ \xrightarrow{Assembly\;Code}\fbox{Assembler}\xrightarrow{Binary\;Code}\fbox{Computer} $$

>**<u>NOTE</u>:**
>**Steve Wozniak** hand assembled machine codes for making "Integer BASIC" interpreter on 6502 (for **Apple - I**).


### <u>Do I Need To Know Assembly?</u>

- Bootloaders, device drivers & kernels often use assembly.
- Inline assembly can be used for optimizing code sections but better to use good optimization techniques before that.
- Learning assembly can help one write optimized code in higher level too.


### <u>How To Format My Code?</u>

- Assembly lines are separated by carriage return.
- **<u>Carriage return</u>:** Represented by `\r`, throws pointer back to beginning of the same line.



## **Topic - 3: x86 Family**

### <u>Introduction</u>

- We call it **x86 family** because Intel's early processors had endings with **86**.
- x86 is both, the family of processors & its instruction set architecture.
- x86 refers to both 32-bit & 64-bit architectures.
- 32-bit architecture is known as IA-32 (Intel Architecture, 32-bit).
- While 64-bit architecture is known as x86-64.
- Other vendors like AMD follow same architecture.


### <u>Intel x86 Microprocessors</u>
