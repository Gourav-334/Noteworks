# $\fbox{Chapter 10: ADDRESSING MODES}$





## **Topic – 1: Operands**

>**<u>NOTE</u>:**
>The operands we pass by name, are actually their memory addresses.


### <u>Basic Modes Of Addressing</u>

- Register addressing
- Immediate addressing
- Memory addressing


### *<u>Register Addressing</u>

- These are instructions which involve a register & a variable or two registers.


### <u>Immediate Addressing</u>

- Involves moving an immediate constant to a register or a reserved variable.

```gas
addl $96, num(%rip)
movl 0x78, %rcx
```


### <u>Direct Memory Addressing</u>

- In direct memory addressing mode, the named variable is searched all over the main memory.
- This address after reaching the offset of that variable, is stored in DS register.
- **<u>Effective address</u>:** Offset
- As we mention more variables in the program, their offset values are stored in a symbol table.

```gas
movq %rax, 0x800
movw 0x5000, %ax
```


### <u>Direct-Offset Addressing</u>

- Uses arithmetic operators to modify addresses.

```gas
my_table: .word 4,5,6,7,8        # Our table (array)

movw my_table + 2, %cx           # Moves third element to CX
movb my_table, %cl               # Move first byte only to CL
```


### <u>Indirect Memory Addressing</u>

- We mostly use base registers of BX, BP series & index registers of DI, SI series for this purpose.
- This way of addressing is used in structures containing multiple elements.
- Like arrays/tables etc.
- We use `[]` around register to refer to the element that is in address in register.
- And without it, we are referring to the memory address it is storing.

```gas
movl my_array, %ebx    # Offset of array moved to EBX
movl $100, %ebx        # array[0] = 100
movl $2, %ebx          # RBX = RBX + 2 (next element)
movl $200, %ebx        # array[1] = 200
```

- The 3rd line moves by just one element because size of a WORD is 2 bytes.



## **Topic – 2: MOV Instruction Ambiguity**

### <u>Type Specification</u>

- When using the MOV instruction, the size of both operands must be **same**.
- But it can cause some ambiguity like we **don’t** specify the type of value we are moving into the register.

```gas
movl $100, %ebx
movw $100, my_table + (%ebx * 2)
```

- `my_table + (%ebx * 2)` because each element is of a word i.e. 2 bytes.
- So, we multiple `%ebx` with `2` to skip by that much of memory.

---
