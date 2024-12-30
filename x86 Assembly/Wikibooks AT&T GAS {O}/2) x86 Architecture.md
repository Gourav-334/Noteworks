# $\fbox{Chapter 2: x86 ARCHITECTURE}$





## **Topic - 1: Basic Information**

### <u>Register Groups</u>

- 8 general purpose registers (GPR).
- 6 segment registers (SR).
- 1 flag register (FR).
- 1 instruction pointer (IP).

>**<u>NOTE</u>:**
>64-bit architecture contains even more registers.


### <u>General Purpose Registers</u>

1. **<u>Accumulator register (AX)</u>:** Used in arithmetic operations.
2. **<u>Base register (BX)</u>:** Pointer to data.
3. **<u>Counter register (CX)</u>:** Used in shift, rotate & loop instructions.
4. **<u>Stack pointer register (SP)</u>:** Pointer to top of the stack.
5. **<u>Stack base pointer register (BP)</u>:** Pointer to base of the stack.
6. **<u>Destination index register (DI)</u>:** Pointer to destination in stream operations.
7. **<u>Source index register (SI)</u>:** Pointer to source in stream operations.
8. **<u>Data register (DX)</u>:** Used in arithmetic & I/O operations.

>**<u>NOTE</u>:**
>1. The order above is used in push-to-stack operations.
>2. In 16-bit addressing, we address lower significant byte as AL, BL, CL etc.
>3. And AH, BH, CH etc when addressing most significant byte.
>4. 'R' in RAX, RBX, RCX etc stands for 'register'.

