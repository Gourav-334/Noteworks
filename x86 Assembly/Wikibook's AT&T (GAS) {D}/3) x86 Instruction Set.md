# $\fbox{Chapter 2: x86 INSTRUCTION SET}$





## **Topic - 1: Summary**

- Data transfer instructions
- Control flow instructions
- Arithmetic instructions
- Logic instructions
- Shift & rotate instructions
- Other instructions
- x86 interrupts



## **Topic - 2: Conventions**

### <u>Templates</u>

- **<u>Argument</u>:** The operand in instructions requiring single operand.
- **<u>Auxiliary operand</u>:** Third operand in instructions requiring three operands.

```asm
instr aux, src, dest        # AT&T syntax
instr dest, src, aux        ; Intel syntax
```


### <u>Suffixes</u>

- `b` - Byte (8-bits)
- `w` - Word (16-bits)
- `l` - Long/doubleword (32-bits)
- `q` - Quadword (64-bits)



## **Topic - 3: Data Transfer**

### <u>Data Transfer Instruction</u>

- No bit in flag register is modified by `MOV` instruction.
- Example for syntax is given below.

```S
.data
	value: .long 2

.text
	.globl _start

_start:
	movl $6, %eax           # EAX = 6
	movw %eax, value        # VALUE = EAX = 6
	movl $0, %ebx           # EBX = 0
	movb %al, %bl           # BL = AL
	
	movl value, %ebx        # EBX = VALUE
	movl $value, %esi       # ESI = &VALUE
	
	
	# Exit the program (in Linux)
	mov $1, %eax
	xorl %ebx, %ebx
	int $0x80
```


### <u>Swap/Exchange Data</u>

```S
xchg src, dest
```

- `XCHG` is operationally equivalent to three `MOV` statements.
- But `XCHG` are costlier & slower than three `MOV` statements.
- `XCHG` sometimes requires more than three clock cycles.
- We can't exchange two memory blocks with it, though.

#### Example:

```S
xchgw value(%eax), %ax    # [value + %eax], %ax
```
