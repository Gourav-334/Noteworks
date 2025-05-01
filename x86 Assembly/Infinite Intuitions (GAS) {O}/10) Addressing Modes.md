**<u>Chapter 10</u>: ADDRESSING MODES**

**Topic – 1: Operands**

**<u>Note</u>!**

**🡪 The operands we pass by name, are actually their memory addresses.**

**<u>Basic Modes Of Addressing</u>**

- Register addressing

- Immediate addressing

- Memory addressing

**<u>Register Addressing</u>**

- These are instructions which involve **a** **register** & **a**
  **variable** or **two registers**.

**<u>Immediate Addressing</u>**

- Involves moving an **immediate constant** to a **register** or a
  **reserved variable**.

***add num, 96***

***mov rcx, 78h***

**<u>Direct Memory Addressing</u>**

- In **direct memory addressing** mode, the named **variable** is
  searched all over the main memory.

- This address after reaching the **offset** of that variable, is stored
  in **DS** register.

- **<u>Effective address</u>:** Offset

- As we mention more variables in the program, their **offset** values
  are stored in a **symbol table**.

***mov \[0x800\], rax***

***mov ax, \[0x5000\]***

**<u>Direct-Offset Addressing</u>**

- Uses **arithmetic operators** to modify addresses.

***my_table dw 4,5,6,7,8 ; Our table (same as array in C)***

***mov cl, my_table\[2\] ; Moves third element to CL***

***mov cl, my_table + 2 ; Same as above***

**<u>Indirect Memory Addressing</u>**

- We mostly use **base registers** of **BX**, **BP** series & **index
  registers** of **DI**, **SI** series for this purpose.

- This way of addressing is used in structures containing **multiple
  elements**.

- Like **arrays/tables** etc.

- We use **\[ \]** around register to refer to the **element** that is
  in address in register.

- And **without** it, we are referring to the **memory address** it is
  storing.

***mov ebx, \[my_array\] ; Offset of array moved to RBX***

***mov \[ebx\], 100 ; array\[0\] = 100***

***mov ebx, 2 ; rbx = rbx + 2 (next element)***

***mov \[ebx\], 200 ; array\[1\] = 200***

- The **3<sup>rd</sup> line** moves by just **one element** because size
  of a **WORD** is **2-bytes**.

**Topic – 2: MOV Instruction Ambiguity**

**<u>Type Specification</u>**

- When using the **MOV** instruction, the **size** of **both operands**
  must be **same**.

- But it can cause some ambiguity like we **don’t** specify the **type**
  of value we are moving into the register.

***mov \[ebx\], 100 ; Unspecified type***

***mov WORD\[ebx\], 100 ; Specified and safe***

**<u>Constant Types Table</u>**

| **Type Specifier** | **Bytes Addressed** | **Definition Keyword** |
|:------------------:|:-------------------:|:----------------------:|
|      **BYTE**      |        **1**        |         **DB**         |
|      **WORD**      |        **2**        |         **DW**         |
|     **DWORD**      |        **4**        |         **DD**         |
|     **QWORD**      |        **8**        |         **DQ**         |
|     **TBYTE**      |       **10**        |         **DT**         |

**<u>Variable Types Table</u>**

| **Type Specifier**  | **Bytes Addressed** | **Definition Keyword** |
|:-------------------:|:-------------------:|:----------------------:|
| **BYTE (reserve)**  |        **1**        |        **RESB**        |
| **WORD (reserve)**  |        **2**        |        **RESW**        |
| **DWORD (reserve)** |        **4**        |        **RESD**        |
| **QWORD (reserve)** |        **8**        |        **RESQ**        |
| **TBYTE (reserve)** |       **10**        |        **REST**        |
