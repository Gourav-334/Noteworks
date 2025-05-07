# $\fbox{Chapter 12: Floating-Point Instructions}$





## **Topic - 1: FPU Registers History**

- There are two type of register groups in x86-64 systems for floating-point arithmetic.
- One is **x87 Floating-Point Instructions**, which is legacy.
- While the more modern one is **SSE/AVX**.



## **Topic - 2: x87 Floating-Point Unit**

### <u>Introduction</u>

- x87 contains eight **80-bit** registers stacked.
- These are `st(0)` to `st(7)` through.

#### Float types:

| Sno | Type                     | Short Name  |  Size   | Macro         |
| :-: | ------------------------ | ----------- | :-----: | ------------- |
|  1  | Single-precision float   | Float       | 32-bits | `.float`      |
|  2  | Double-precision float   | Double      | 64-bit  | `.double`     |
|  3  | Extended-precision float | Long double | 80-bit  | `.longdouble` |


### <u>Loading Values</u>

- When an element is pushed to FP stack, the elements are pushed down & new element comes at `st(0)`.
- We will load FP variables to FP stack.

```gas
	.section .data
val1: .float 3.14
val2: .double 2.71828
val3: .longdouble 1.6180339887

	.section .text
	.globl _start

_start:
	fld %st(n)        # ST(0) = ST(n)
	flds val1         # Load/push 'val1' at ST(0).
	fldl val2         # Load/push 'val2' at ST(0).
	fldt val3         # Load/push 'val3' at ST(0).
```

- Suffix `s`, `l` & `t` mean single-precision, double-precision (long) & extended-precision (long double) respectively.


### <u>Storing Values</u>

- Now we will load values from FP stack to FP variables.

```gas
fst %st(n)        # ST(n) = ST(0)

fsts val1         # val1 = ST(0) ['val1' is single-precision.]
fstl val2         # val2 = ST(0) ['val2' is double-precision.]

fstp val1         # val1 = ST(0) & pop ST(0)
fstp val2         # val2 = ST(0) & pop ST(0)
fstpt val3        # Specifically for extended-precision floats
```


### <u>Exchanging Stack Values</u>

```gas
fxch %st(n)        # Swap ST(0) & ST(n)
```


### <u>Arithmetic Operations</u>

#### Addition:

- For arithmetic operations, we can't directly involve float variables.
- So we use the FP stack elements instead.

```gas
fadd %st(n), %st(0)
faddp %st(n), %st(0)

fadds val1        # ST(0) += val1 [For single-precision.]
faddl val2        # ST(0) += val2 [For double-precision.]
```

- Two non-ST(0) registers can't be compared.
- Operands in first two lines can be reversed.

#### Subtraction:

- Just like FP addition, FP subtraction supports similarly named opcodes.
- Opcodes - `fsub`, `fsubp`, `fsubs`, `fsubl` etc.
- But subtraction additionally supports reverse opcodes with `r` as/with suffix.
- Reverse opcodes swap the right side of equation.

```gas
fsub                         # ST(1) = ST(1) - ST(0) & pop ST(0)
fsubr                        # ST(1) = ST(0) - ST(1) & pop ST(0)
fsubr %st(n), %st(0)         # ST(n) = ST(m) - ST(n)
fsubrp %st(n), %st(0)

fsubrs %st(n)                # ST(0) = ST(n) - ST(0)
fsubrl %st(n)
```

#### Multiplication:

- Similar to FP addition & subtraction, it has similarly named opcodes.
- Opcodes - `fmul`, `fmuls`, `fmull` & `fmulp`.

#### Division:

- Like rest of the arithmetic opcodes, specially subtraction, FP division opcodes have similar naming.
- Regular opcodes - `fdiv`, `fdivs`, `fdivl` & `fdivp`.
- Reverse opcodes - `fdivr`, `fdivrs`, `fdivrl` & `fdivrp`.

#### Miscellaneous:

```gas
fsqrt        # Replaces ST(0) with its square root.
fabs         # Replaces ST(0) with its absolute value.
fchs         # Changes sign of ST(0).
```


### <u>Comparison Opcodes</u>

```gas
fcom               # Compare ST(0) with ST(1)
fcom %st(i)        # Compare ST(0) with ST(i)
fcom val           # Can be single or double precision

fcomp
fcomp %st(i)
fcomp val

fcompp             # Same as 'fcomp' but also pops ST(1)

fcomi %st(i), %st(0)         # Also sets CPU flags
fcomip %st(i), %st(0)
```

- Similarly, we have opcodes for "unordered" comparison.
- Unordered opcodes - `fucom`, `fucomp` & `fucompp`.
- `fcomi` & `fcomip` opcodes are valid only in **P6** & above processors.
- Results for these comparisons are stored in **FPU status word**.

#### Accessing FPU status word:

```gas
fstsw %ax        # Copy the whole FP flag word to AX.
fnstsw           # Same as above but "non-waiting".
```


### <u>Miscellaneous</u>

```gas
fldpi          # Load PI to ST(0)
fld1           # Load 1.0 to ST(0)
fldz           # Load 0.0 to ST(0)
fldl2t         # Load log base 2 of 10 to ST(0)
fldl2e         # Load log base 2 of e to ST(0)
fldlg2         # Load log base 10 of 2 to ST(0)
fldln2         # Load natual log of 2 to ST(0)
```



## **Topic - 3: Streaming SIMD Expressions (SSE)**

### <u>Introduction</u>

- **<u>SIMD</u>:** Single Instruction, Multiple Data
- SSE allows performing simultaneous operations on multiple data elements.
- This significantly contributes to high-performance of operations.


### <u>SSE Registers</u>

- SSE instructions use XMM registers.
- XMM are **128-bit** long & are sixteen in total.
- These are named `xmm0` to `xmm15` through.
- So it can store multiple data types which are occupy equal or lesser space than **128-bit**.
- Also we can store multiple data there to efficiently use their spaces.
- By storing multiple data in XMM, we can simultaneously manipulate them.


### <u>Data Movements</u>

```gas
movaps %xmm1, %xmm2        # Move aligned packed single-precision
movups %xmm1, %xmm3        # Same as previous, but for unaligned

movapd %xmm4, %xmm5        # For double-precision floats
movupd %xmm4, %xmm6

movdqa %xmm7, %xmm8        # For double quadword values
movdqu %xmm7, %xmm9

movss mem, %xmm0           # Memory to XMM (single-precision)
movss %xmm1, mem

movsd mem, %xmm0
movsd %xmm1, mem
```

- These can be used only among XMM registers.
- **"Aligned"** means that the memory block being accessed in a multiple of **16 byte**.


### <u>Arithmetic Operations (Packed)</u>

- These are applied on all the stored elements in desired XMM register.

```gas
addps %xmm1, %xmm0        # Add single-precision float
subps %xmm1, %xmm0        # Prefix 'p' means 'packed'
mulps %xmm1, %xmm0
divps %xmm1, %xmm0
```

- Similarly we have opcodes for double-precision floats.
- Opcodes - `addpd`, `subpd`, `multpd` & `divpd`.
- Also there are opcodes for integer types.
- Integer types - Bytes, word, ... & quadword.
- Opcodes - `paddb`, `paddw`, `paddd` & `paddq`.


### <u>Arithmetic Operations (Scalar)</u>

- These are applied on the lowest element in the XMM register.

```gas
addss %xmm1, %xmm0        # Prefix 's' means 'scalar'
subss %xmm1, %xmm0
mulss %xmm1, %xmm0
divss %xmm1, %xmm0
```

- Similar opcode names go for double-precision floats.
- Opcodes - `addsd`, `subsd`, `mulsd` & `divsd`.


### <u>Comparison Operations (Packed)</u>

- These comparisons set all bits in destination register to 0s or 1s.
- **<u>Predicate</u>:** A value telling the type of comparison to perform.

| Predicament |           Meaning           |
| :---------: | :-------------------------: |
|     `0`     |            Equal            |
|     `1`     |          Less than          |
|     `2`     |     Less than or equal      |
|     `3`     | True if any operand in null |
|     `4`     |          Not equal          |
|     `5`     |        Not less than        |
|     `6`     |   Not less than or equal    |
|     `7`     | True if non operand is null |

```gas
# XMM0 set as per predicate in 'my_byte'
cmpps $my_byte, %xmm1, %xmm0
```

- Similarly we use `cmppd` for double-precision floats.
- For integers - `pcmpeqb`, `pcmpeqw`, `pcmpeqd`, `pcmpgtb`, `pcmpgtw` & `pcmpgtd`.


### <u>Comparison Operations (Scalar)</u>

```gas
comiss %xmm1, %xmm0        # Compare single-precision & set EFLAGS
ucomiss %xmm1, %xmm0       # Unordered compare
```

- Similarly we have `comisd` & `ucomisd` for double-precision floats.


### <u>Logical Operations</u>

```gas
pand %xmm1, %xmm0        # Packed bitwise AND
por %xmm1, %xmm0
pxor %xmm1, %xmm0
pandn %xmm1, %xmm0
```


### <u>Shuffle Operations</u>

```gas
# Selective elements from XMM1 are transferred to XMM0, as per 'my_byte'
shufps $my_byte, %xmm1, %xmm0        # For single-precision
```

- Similarly we have `shufpd` for double-precision floats.


### <u>Unpack Operations</u>

- `unpcklps` is for placing lower order elements together.
- While `unpckhps` is for higher-order.

```gas
# %xmm0 = [a1, a2, a3, a4], %xmm1 = [b1, b2, b3, b4]
unpcklps %xmm1, %xmm0  # %xmm0 becomes [a1, b1, a2, b2]

# %xmm0 = [a1, a2, a3, a4], %xmm1 = [b1, b2, b3, b4]
unpckhps %xmm1, %xmm0  # %xmm0 becomes [a3, b3, a4, b4]
```


### <u>Conversions</u>

```gas
cvtps2pd %xmm1, %xmm0        # Single to double-precision
cvtpd2ps %xmm1, %xmm0        # Double to single-precision

cvtsi2ss mem, %xmm0          # Scalar integer to single-precision
cvttss2si %xmm1, reg
cvtsi2sd mem, %xmm0         # Scalar integer to double-precision
cvttsd2si %xmm1, reg
```

- `t` in `cvttss2si` & `cvttsd2si` stands for **truncate**.
- This is because larger size is being converted to smaller.
