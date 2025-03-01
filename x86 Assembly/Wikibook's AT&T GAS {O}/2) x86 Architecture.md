# $\fbox{Chapter 2: x86 ARCHITECTURE}$





## **Topic - 1: Registers**

### <u>Register Groups</u>

- 8 general purpose registers (GPR).
- 6 segment registers (SR).
- 1 flag register (EFLAGS).
- 1 instruction pointer (IP).

>**<u>NOTE</u>:**
>64-bit architecture contains even more registers.


### <u>General Purpose Registers (GPRs)</u>

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
>5. For registers like stack pointer, stack base pointer, destination & source, higher 8-bits can not be addressed.


### <u>Segment Registers (SRs)</u>

1. **<u>Stack segment (SS)</u>:** Pointer to the stack.
2. **<u>Code segment (CS)</u>:** Pointer to the code.
3. **<u>Data segment (DS)</u>:** Pointer to the data.
4. **<u>Extra segment (ES)</u>:** Pointer to extra data.
5. **<u>F segment (FS)</u>:** Pointer to more extra data.
6. **<u>G segment (GS)</u>:** Pointer to even more extra data.

>**<u>NOTE</u>:**
>Notice how all the data pointing segment registers are in order D, E, F & G.


### <u>EFLAGS Register</u>

- EFLAGS register has a capacity of storing 32-bits.
- Each of its bit represents a different flag.

![EFLAGS Register](x86%20Assembly/Wikibook's%20AT&T%20GAS%20{O}/media/image1.png)

>**<u>WARNING</u>:**
>Bits named 0 and 1 shouldn't be changed.

#### Use cases of flags:

| Bit Number | Flag Symbol |           Flag Name            | Usage                                                                               |
| :--------: | :---------: | :----------------------------: | :---------------------------------------------------------------------------------- |
|     0      |     CF      |           Carry flag           | Set to 1 if last arithmetic operation led to borrow which is beyond register limit. |
|     2      |     PF      |          Parity flag           | Set if number of bits set in LSB are in multiple of 2.                              |
|     4      |     AF      |          Adjust flag           | Carry of arithmetic calculation among BCD numbers.                                  |
|     6      |     ZF      |           Zero flag            | Set if result of last operation was zero.                                           |
|     7      |     SF      |           Sign flag            | Set if result of last operation was negative.                                       |
|     8      |     TF      |           Trap flag            | Set if debugging step-by-step.                                                      |
|     9      |     IF      |       Interruption flag        | Set if interrupts are enabled.                                                      |
|     10     |     DF      |         Direction flag         | If set, memory will now be read backwards.                                          |
|     11     |     OF      |         Overflow flag          | Set if signed arithmetic operation results in too large value for contain.          |
|   12,13    |    IOPL     |       I/O privilege flag       | Sets I/O privilege level in 2-bits.                                                 |
|     14     |     NT      |        Nested task flag        | Set if current process is linked to upcoming process.                               |
|     16     |     RF      |          Resume flag           | Gives response to debug exceptions.                                                 |
|     17     |     VM      |       Virtual-8086 mode        | Set if in 8086 compatibility.                                                       |
|     18     |     AC      |        Alignment check         | Set if memory alignment checking has been done.                                     |
|     19     |     VIF     |     Virtual interrupt flag     | Virtual image of IF.                                                                |
|     20     |     VIP     | Virtual interrupt pending flag | Set if an interrupt is pending.                                                     |
|     21     |     ID      |      Identification flag       | Support for CPUID.                                                                  |


### <u>Instruction Pointer (IP)</u>

- EIP register contains address of next instruction to be executed.
- Can be read only after `call` instruction.


### <u>Memory</u>

- x86 architecture is little-endian.
- **<u>Little-endian</u>:** Bytes get placed from LSB.

#### Little-endian example:

- Let there be a hex number $(H_{4}H_{3}H_{2}H_{1})_{16}$.
- Its representation in memory will be as follows.

$$ \fbox{ H1 | H2 | H3 | H4 } $$


### <u>2's Complement</u>

- Any binary number's 2's complement gives us its negative form.
- But we do so with digits in multiple of 4.

#### Example:

$$ Positive\;=\;0001 $$
$$ 2^3(0)\;+\;2^2(0)\;+\;2^1(0)\;+\;2^0(1)\;=\;1 $$
$$ $$
$$ 2's\;complement\;=\;1111 $$
$$ -2^3(1)\;+\;2^2(1)\;+\;2^1(1)\;+\;2^0(1)\;=\;-1 $$



## **Topic - 2: Addressing Modes**

### <u>Register Addressing</u>

- Register to register transfer.

```asm
mov %bx, %ax
```


### <u>Immediate Addressing</u>

- Move a constant value to a register (with any base).

```asm
mov $0xa, %ax
```


### <u>Direct Addressing Mode</u>

- Moving a constant value to a register, through its memory address.

```asm
my_var: .word 1234

movw my_var, %ax
```

- `my_var(%rip)` tells instruction pointer `rip` about memory address of `my_var`.


### <u>Direct Offset Addressing</u>

- Using arithmetic operations to tell address to point.

```asm
my_table: .byte 10,20,30,40

mov my_table+2, %al
```


### <u>Register Indirect Addressing</u>

```asm
mov (%di), %al
```

| Syntax  | Meaning                                                             |
| :-----: | ------------------------------------------------------------------- |
|  `%di`  | Accessing value stored in `di` register.                            |
| `(%di)` | Value at the memory address, address being stored in `di` register. |
|  `$di`  | Accessing value represented by the label `di`.                      |

- Registers used for indirect addressing are BX, BP, SI & DI.



## **Topic - 3: 64-Bit GPRs**

### <u>Introduction</u>

#### R-series registers:

- 64-bit architecture was introduced with eight more registers.
- These are named R8-R15.
- R8D-R15D are lower 32-bits of them.
- R8W-R15W are lower 16-bits of them.
- R8B-R15B are lower 8-bits of them.

#### XMM registers:

- There are more registers named as XMM0-XMM7 which are 128-bits wide.
- They can be accessed through SSE instruction only.
- And they can't be used for high-precision floating point operations.
- Newer Intel & AMD processors however have YMM0-YMM7 which are 256-bits wide.
- They can be accessed using AVX instruction.



## **Topic - 4: Stack**

```asm
movw $0x006a, %ax
movw $0xf79a, %bx
movw $0x1124, %cx

pushw %ax        # Push value in AX to stack.
pushw %bx
pushw %cx

call my_func     # A function never saves state of registers.

popw %cx         # Pop top element of stack & save it to CX.
popw %bx
popw %ax
```



## **Topic - 5: CPU Operation Modes**

### <u>Real Mode</u>

- A real mode is required to directly interact with the BIOS.
- In this, two registers (segment & offset) are used to store a single memory address.
- An address is of 8-bits, so both fetch 4-bits each.
- The segment register fetches first 8-bits & multiplies the result by 16, to shift intermediate result 4-bits to the left.
- Then the remaining 4-bit of address in offset register is added to it.
- Real mode allows up to 1MB of usable address space, which can be extended only if address location of `0xFFFF` is occupied.
- This limit from 80286 to now is of 65520 bytes (64 KB), only if the A20 address line is enabled on the processor.
- Both real mode & protected mode's multi-memory segment memory model can calculate relative addresses from a segment address.
- This was highly used in DOS.


### <u>Protected Mode</u>

#### Flat memory model:

- Done in 32-bit computer OS.
- Uses 32-bit registers.
- Use of segment registers isn't compulsory.
- Also using segment registers isn't a good practice either.

#### Multi-segmented memory model:

- This model also uses 32-bit registers.
- Can access almost all available computer memory.
- CS, DS & ES are used for pointing to these memory locations.

#### Long mode:

- This is the 64-bit mode.



## **Topic - 6: Comments**

- Comments are discarded when converting assembler or source code to machine code.
- Other than GNU Assembler & HLA, all assemblers use `;` for comment.
- GAS uses `#` for single-line comment & `\* ... *\` for multiline comment.
- While HLA uses C/C++ styled comments.



## **Topic - 7: Architectural Differences**

### <u>16-Bit</u>

- On DOS & 32-bit Windows systems, there is a program called $program.exe$.
- It is useful for learning 8086 assembly.
- It can be accessed through DOS shell.



## **Topic - 8: Addressing Memory**

### <u>8086 And 80186</u>

- Original 8086 had 16-bit long registers.
- But the address bus in it was 20-bit long.
- To solve this problem, engineers at Intel introduced segment registers (CS, DS, ES & FS).

#### Reading data from address bus:

1. Divide the address bus by `16`.
2. Store its quotient in segment register (of 16-bits).
3. Then store its remainder in offset register.

#### Writing data to address bus:

1. For writing address to address bus, add 16-bits from segment register.
2. Move the bits in address bus by `4` bits.
3. Now fill those 4-bits with content in offset register.

#### Outro:

- **CS:IP** represents 20-bit address of the physical memory.
- **SS:SP** represents 20-bit absolute address of stack top.
