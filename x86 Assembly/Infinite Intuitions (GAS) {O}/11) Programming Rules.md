# $\fbox{Chapter 12: PROGRAMMING RULES}$





## **Topic – 1: Macros**

### <u>EQU</u>

- `.equ` is used for representing symbolic constants.
- Defined under `.text` section, before & after `_start`.
- Similar to `#define` in C.

```s
.equ MAX_SIZE, 64
.equ ERR_CODE, 404

movl $MAX_SIZE, %edx
```

- Not `MAX_SIZE(%rip)` because the symbol is replaced by value directly.


### <u>SET</u>

- Similar to `.equ` but redefinable.

```s
.equ COUNTER, 10
movl $COUNTER, %ecx
.equ COUNTER, 20
```

- It can be changed or manipulated other ways too.


### <u>ASCII</u>

- `.ascii` - Null terminated string.
- `.asciz` - Not null terminated string.


### <u>ALIGN</u>

- Used for defining size of unit block in memory.
- Define under `.data` section.

```s
.byte 0x01             # Filling memory without any label.
.align 3               # 2^3 bytes alignment.
myWord: .word 0x257    # Placed at the next 8-byte block start.

.byte 9
.align 4        # Realignment
```


### <u>SECTION</u>

- Sections can be defined multiple times & work well.

```s
.section .data
	# Some code

.section .text
	# Some code

.section .data        # Repeated
	# Some code

.section .bss
	# Some code

.section .text        # Repeated
	# Some code
```


### <u>MACRO & ENDM</u>

- Similar to subroutines & functions, a piece of code is written between `.macro` & `.endm`.

```s
.macro add_two x, y, res
	movl \x, %eax
	addl \y, %eax
	movl %eax, \res
.endm

add_two $3, $4, $buff
```

- Notice how `\` was used for parameters.
- We can write default value of parameters too.
- For example, `res = 6`.

>**<u>NOTE</u>:**
>1. Macro & subroutines/functions are slightly different in functioning.
>2. Macros are scanned first during assembling/compiling.
>3. In macros, the macros are replaced with the code, unlike subroutines.
>4. This leads to duplication in such cases.
>5. Macros are generally faster for having no return overhead.


### <u>Conditional Directives</u>

```s
#define CPU "x86"

.if CPU == "x86"
	; Code for x86
	movl $1, %eax

.else
	; code for other CPU
	movl $2, %eax

.endif
```


### <u>Definition</u>

```s
.ifndef CPU
	#define CPU "x86"

.ifdef CPU
	movq $0, %rax
```



## **Topic - 2: Data Transfer Instruction**

### <u>Introduction</u>

- Includes `mov`, `push`, `pop` & `lea`.


### <u>PUSH & POP</u>

- Used for pushing data to a thread's stack.
- Stack is used for storing data temporarily for later use & corruption avoidance.

```s
pushq -4(%rax)        # Push data at (RAX-4).
popq %rbx             # Pop last pushed data to RBX.
```



## **Topic - 3: Arithmetic & Logic Instructions**

### <u>Introduction</u>

- Arithmetic - `add`, `sub`, `mul`, & `div`.
- Logical - `and`, `or`, `xor` & `not`.
- Bitwise - `shl`, `shr`, `sal` & `sar`.
- Special - `inc`, `dec`, `neg`, `cmp` & `test`.


### <u>SHL</u>

- **<u>SHL</u>:** Shift Left Logical
- Bits are shifted left by a certain position.
- Zeroes are added from right & MSBs are popped to CF.
- Flags can be accessed through `%eflags` or `%rflags` etc.

```s
movq $1001011, %rax        # Moving because const-to-const can't.
shlq $2, %rax              # Shift 1001011 left by 2 bits.
```

- Alternative mnemonic for `shl` is `sal`.


### <u>SHR</u>

- Similar to SHL but done toward right.
- Alternative mnemonic for `shr` is `sar`.


### <u>NEG</u>

- Performs 2's complement on the target.

```s
negl %eax        # 2's complement is applied on EAX.
```


### <u>CMP</u>

- Used to compare two values.
- This value isn't stored anywhere, but the result is used in the conditional statements immediately after it.

```s
cmp %56, %edx
```


### <u>TEST</u>

- Same as `and` mnemonic but like `cmp`, it doesn't store its value anywhere.



## **Topic - 4: Conditional Flow Instructions**

### <u>Introduction</u>

- This comparison is always between destination & source.

```s
jmp destination, source
```

#### Categories:

- Unconditional jump - `jmp`
- Conditional jump - `je`, `jne`, `jz`, `jnz`, `jl`, `jnl`, `jle`, `jnle` `jg` & `jng`, `jge`, `jnge`.
- Similar wild combinations with `ja` (jump if above) & `jb` (jump if below).
- Many other are related to flags.
- Functional - `call` & `ret`


### <u>JMP</u>

- Used for jumping to a label without any condition.
- Labels can be written before or after.

```s
jmp *my_label      # Jump to address stored in 'my_label'.
jmp *%rax          # Jump to address stored in RAX.
```

- Notice the `*` used for referring to address.



## **Topic - 5: Subroutines**
