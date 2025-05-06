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

```s
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

```s
fst %st(n)        # ST(n) = ST(0)

fsts val1         # val1 = ST(0) ['val1' is single-precision.]
fstl val2         # val2 = ST(0) ['val2' is double-precision.]

fstp val1         # val1 = ST(0) & pop ST(0)
fstp val2         # val2 = ST(0) & pop ST(0)
fstpt val3        # Specifically for extended-precision floats
```


### <u>Exchanging Stack Values</u>

```s
fxch %st(n)        # Swap ST(0) & ST(n)
```


### <u>Arithmetic Operations</u>

#### Addition:

- For arithmetic operations, we can't directly involve float variables.
- So we use the FP stack elements instead.

```s
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

```s
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

```s
fsqrt        # Replaces ST(0) with its square root.
fabs         # Replaces ST(0) with its absolute value.
fchs         # Changes sign of ST(0).
```


### <u>Comparison Opcodes</u>

```s
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

```s
fstsw %ax        # Copy the whole FP flag word to AX.
fnstsw           # Same as above but "non-waiting".
```


### <u>Miscellaneous</u>

```s
fldpi          # Load PI to ST(0)
fld1           # Load 1.0 to ST(0)
fldz           # Load 0.0 to ST(0)
fldl2t         # Load log base 2 of 10 to ST(0)
fldl2e         # Load log base 2 of e to ST(0)
fldlg2         # Load log base 10 of 2 to ST(0)
fldln2         # Load natual log of 2 to ST(0)
```



## **Topic - 3: Streaming SIMD Expressions (SSE)**
