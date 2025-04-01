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

|    Model    | Year | New Features                                                                                                                                     |
| :---------: | :--: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|  8086/8087  | 1978 | Intel's first 16-bit microprocessor, 20-bit address bus.                                                                                         |
|    8088     | 1979 | A cheaper model with 8-bit address bus.                                                                                                          |
| 80186/80187 | 1982 | 186 was microprocessor while 187 was floating point coprocessor, some instructions were added & some were optimized, improvement in clock speed. |
| 80286/80287 | 1982 | Protected & real modes were introduced.                                                                                                          |
|    80386    | 1985 | Introduced 32-bit word, 32-bit address bus, flat memory model where a register can hold entire address, had unreal mode.                         |
|    80486    | 1989 | Integrated floating point unit, cooling fans in CPU.                                                                                             |
|   Pentium   | 1993 | Named instead of 80586 for trademark issues, faster than 80486, integrated MMX instruction set.                                                  |
| Pentium Pro | 1995 | 6th generation architecture, used as server chip & high-end desktop chip.                                                                        |
| Pentium II  | 1997 | Improved performance, introduction of MMX SIMD.                                                                                                  |
|   Celeron   | 1998 | Design similar to Pentium but cheaper.                                                                                                           |
|    Xeon     | 1998 | Used in servers, cache size measure in MiBs instead of KiBs.                                                                                     |
| Pentium III | 1999 | SSE instructions were added.                                                                                                                     |
|  Pentium 4  | 2000 | 7th generation NetBurst architecture, introduced hyper-threading & multi-core concepts.                                                          |
|    Core     | 2006 | Advanced 6th generation architecture, efficient but lower clock speed, uses two cores.                                                           |
|   Core 2    | 2006 | 64-bit core architecture.                                                                                                                        |
|  i Series   | 2008 | i7 introduced hyper-threading.                                                                                                                   |


### <u>AMD x86 Microprocessors</u>

|  Model  | New Features                                                                                                                 |
| :-----: | ---------------------------------------------------------------------------------------------------------------------------- |
| Athlon  | Group of AMD chips, Athlon Classic was first 7th generation x86 processor, better performance than contemporary Intel chips. |
| Turion  | For 64-bit low power (mobile) processors, 512-1024 KiB L2 cache, 800 MHz hyper transport bus.                                |
|  Duron  | Cheaper alternative to Athlon, competitor of Pentium III & Celeron.                                                          |
| Sempron | Competitor of Celeron D processor.                                                                                           |
| Opteron | 8th generation processor, 8 cores, first 64-bit version, competing Xeon in server market.                                    |

---
