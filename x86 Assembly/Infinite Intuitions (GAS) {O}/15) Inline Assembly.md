# $\fbox{Chapter 15: INLINE ASSEMBLY}$





## **Topic - 1: That's What We Need**

### <u>Introduction</u>

- Inline assembly is usually required to access features inaccessible by C.
- This includes fine tuning performance critical sections.


### <u>Function Format</u>

```c
asm [volatile] ("assembly template"
	: [output operands]
	: [input operands]
	: [clobbers]
);
```

- Instead of `asm`, we can also use `__asm__`.
- `volatile` is optional but recommended to not interfere with assembly code.
- `[input operands]` are optional C variables we are passing to assembler.
- `[clobbers]` are resources that need to be changed by assembler.
- Clobbers however need not to mention flag registers.


### <u>Example</u>

#### Basic addition:

```c
asm volatile (
	"addl %%ebx, %%eax;"
	: "=a" (sum)              // Output operand
	: "a" (a), "b" (b)        // Input operands in EAX & EBX
	: // No clobber, just output
);
```

- Notice double percentage `%%` written to allow `%` in C string.
- `=` means the operand is write-only.
- `"a"` means EAX/RAX whereas `"b"` means EBX/RBX.

#### SSE operation:

```c
float a[4] = {1.0f, 2.0f, 3.0f, 4.0f};
float b[4] = {5.0f, 6.0f, 7.0f, 8.0f};
float result[4];


/* Load the input arrays into SSE registers. */

__asm__ volatile (
	"movups   (%[a]), %%xmm0  \n"         // Load 'a' into XMM0
	"movups   (%[b]), %%xmm1  \n"         // Load 'b' into XMM1
	"addps    %%xmm1, %%xmm0  \n"         // Add XMM1 to XMM0
	"movups   %%xmm0, (%[result]) \n"     // Store the result
	
	: // No output operands, result is written to memory directly
	: [a] "r" (a), [b] "r" (b), [result] "r" (result) // Inputs
	: "xmm0", "xmm1"         // Clobbered registers: XMM0, XMM1
);


printf("Result: %f %f %f %f\n",
	result[0],
	result[1],
	result[2],
	result[3]
);
```

- Notice the use of `[a] "r" (a)` etc, where `[a]` is symbolic representation of `a` for example.
- `"r"` means place variable `a` in any suitable GPR.


### <u>Clobbered Flags</u>

|               Flag               | String |
| :------------------------------: | :----: |
|  General purpose register (any)  | `"r"`  |
|           Accumulator            | `"a"`  |
|               Base               | `"b"`  |
|             Counter              | `"c"`  |
|          Memory operand          | `"m"`  |
|    Immediate integer operand     | `"i"`  |
| Immediate floating-point operand | `"e"`  |

---
