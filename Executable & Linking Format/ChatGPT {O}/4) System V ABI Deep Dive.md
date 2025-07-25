# $\fbox{Chapter 4: SYSTEM V ABI DEEP DIVE}$





## **Topic - 1: SysV Calling Convention**

### <u>Goals/Objectives</u>

- Understanding how function calls work in **SysV AMD64 ABI**.

#### SysV defines:

- Stack layout during function calls
- Register usage
- Argument & return value passing
- Caller/callee responsibilities

#### Use cases:

- Programming in C
- Assembly interoperability
- Hand-assembled binaries


### <u>Calling Convention</u>

- **Arguments** must be **passed** in a particular way.
- **Return** values must be **placed** in a particular way.
- Some **registers** should be **preserved**.
- **Stack** must be **managed** in a particular way.


### <u>Argument Passing Convention</u>

- **<u>Caller</u>:** The function making a call.
- **<u>Callee</u>:** The function being call.
- These are the order of arguments passed during a call.

| Argument | Register |
| :------: | :------: |
|   1st    |  `rdi`   |
|   2nd    |  `rsi`   |
|   3rd    |  `rdx`   |
|   4th    |  `rcx`   |
|   5th    |   `r8`   |
|   6th    |   `r9`   |

- While first six arguments are stored in registers, rest of them are pushed to stack in reverse order.
- For example - If 10 arguments are passed, 1-6 are pushed to register & rest are pushed to stack in order of 10, 9, 8, 7.
- And it is a strict register convention, not mandatory but required in serious projects that aim at interoperability.
- For example, using different registers for arguments in GCC would break the program.


### <u>Value Returning Convention</u>

| Return Type                   |       Where it's returned       |
| ----------------------------- | :-----------------------------: |
| Integer/pointer  (any scalar) |              `rax`              |
| 128-bit values                |            `rax:rdx`            |
| Structures                    | Hidden pointer or memory layout |

- **<u>Scalar</u>:** An entity having a single value, like floats.
- **<u>Aggregate</u>:** A group of entity having multiple values, like structures.
- The hidden pointer is passed using `rdi` which points to address we want to insert the structure.
- But still address would be returned using `rax` only, if required.

>**<u>NOTE</u>:**
>Even characters are scalars, but not string.


### <u>Activation Record</u>

- **<u>Activation record</u>:** Information required to run a procedure.
- Stack contains activation record in the following layout form.

```
Higher addresses
|
│--------------------------------------|
│ argN+2 (if needed)                   |
│ arg7 (stack-passed args)             |
├--------------------------------------|
│ Return Address (from `call`)         |
├--------------------------------------|
│ Previous %rbp (saved frame pointer)  |
├--------------------------------------|
│ Local variables (pushed by callee)   |
│ (aligned to 16 bytes)                |
│--------------------------------------|
|
V
Lower addresses
```

- Before making call, RBP must be pushed to stack by the procedure/ sub-routine.
- And RBX, RBP, R12-R15 must be left untouched, they are not involved in function calling.
- All argument registers might get overwritten by the callee/function.
- While RAX & registers passed as arguments can be altered after work.
- Creation of activation record is automated in compiler, but in assembler (including inline), a user needs to manually do that.
- **<u>Frame pointer</u>:** RBP, points to current functions start.


### <u>Assembly Example</u>

- `syscall` follows similar approach to calling a function.

```nasm
global _start

section .text
_start:
    mov rdi, 1              ; fd = stdout
    mov rsi, message
    mov rdx, 13             ; length
    mov rax, 1              ; sys_write
    syscall

    mov rax, 60             ; sys_exit
    xor rdi, rdi
    syscall

section .data
message: db "Hello, world", 10
```

- `rax` holds the system call number.
- Arguments passed - `rdi`, `rsi`, `rdx`

>**<u>NOTE</u>:**
>1. Stack reserves space for local variables & constants when used, but downward.
>2. For example, `sub rsp, 32` pushes RSP downward & space between becomes usable.
>3. But it is done by the ABI at kernel, user doesn't need to do that.


### <u>C Example</u>

```c
void greet(const char* name) {
    printf("Hello, %s\n", name);
}
```

- Whenever `greet()` is called, its first & only argument is passed using `rdi`.


### <u>Caller v/s Callee</u>

| Register                             |     Role     | Who saves/restores? |
| ------------------------------------ | :----------: | :-----------------: |
| `rbx`, `rbp`, `r12`-`r15`            | Callee-saved |       Callee        |
| `rax`                                | Return value |       Caller        |
| `rcx`, `rdx`, `rsi`, `rdi`, `r8–r11` |   Volatile   |       Caller        |


### <u>Stack Alignment</u>

- Before any call, stack must be aligned to 16-bytes.
- Meaning, it must be assumed that each compartment of stack is of 16-byte.
- So, all left digits of a smaller number must be filled with `0`.

>**<u>FACT</u>:**
>Pages can be allocated dynamically during runtime.



## **Topic - 2: Register Usage**

### <u>Terminologies</u>

- **<u>Scratch/volatile register</u>:** Caller-saved registers
- **<u>Preserved register</u>:** Callee-saved registers


### <u>Goals/Objectives</u>

- Understanding which registers are caller-saved.
- Understanding which registers are callee-saved.
- Their importance in functions & compilers.


### <u>Callee-Saved Registers</u>

- These registers serve their purpose as local variables of the callee.

| Register  | Usage         |
| :-------: | ------------- |
|   `rbx`   | General use   |
|   `rsp`   | Stack pointer |
|   `rbp`   | Frame pointer |
| `r12–r15` | General use   |

- RSP is not modified manually, except during stack operations.
- These values must be saved to stack before being used, and restored before being returned, to avoid corruption.
- And in caller-saved registers (argument registers), they must be saved before a call.
- All this saving & restoring work must be done by assembly programmer, whether in caller or callee.

>**<u>NOTE</u>:**
>1. Floating-point (`xmm0`-`xmm15`) registers are considered **volatile** registers.
>2. Any kind of errors that generate, must be programmed by assembler maker.



## **Topic - 3: Struct & Argument Passing ABI**

### <u>Goals/Objectives</u>

- Understanding how structs & arguments are passed to functions.
- Specific to **64-bit** Sys V ABI.


### <u>Struct Passing Rules</u>

- When a value is $\le$ 16 bytes, two GPR or SSE registers are enough.
- But when its $\gt$ 16 bytes, they're passed through a hidden pointer.
- Mixed/ unaligned types are passed using pointers.


### <u>Small Struct Example</u>

```c
struct Point {
    int x;
    int y;
};

void draw(struct Point p);
```

- Struct is of 8 bytes, can be easily passed via two registers for each member.
- Both the struct members `x` & `y` would be passed through `rdi` & `rsi` respectively.

```nasm
mov edi, 4        ; p.x = 4
mov esi, 5        ; p.y = 5
call draw
```


### <u>Large Struct Example</u>

```c
struct Big {
    int data[10];
};

void process(struct Big b);
```

- Whole struct is of 40 bytes.
- It will be passed via a hidden pointer which C can't see.
- On assembly level, instead a pointer to struct offset will be passed via RDI.


### <u>Returning Struct</u>

- If its $\le$ 16 bytes then it is passed via the RDX:RAX pair.
- For $\gt$ 16 bytes, it is passed a hidden pointer via RDI.
- For floating-point operations, results are returned in XMM0:XMM1.


### <u>Hidden Padding</u>

- The hidden padding in structs are aligned when number of arguments go beyond seven.
- They are aligned in stack & more significant bits are filled with zeroes.
- That's the padding we see in C structs.



## **Topic - 4: Return Values**

### <u>Goals/Objectives</u>

- Understanding how values are returned from function.
- Understanding where returned values are stored in memory.
- Types - Scalar & structs


### <u>Scalar Return Types</u>

|Return Type|Register(s) Used|
|---|---|
|`int`, `char`, `short`, `bool`, pointer|`rax`|
|`long`, `void *`|`rax`|
|`__int128`|`rdx:rax`|
|`float`|`xmm0`|
|`double`|`xmm0`|
|`long double`|`st0` (x87 FPU — legacy)|


### <u>Integer Example</u>

#### C:

```c
int add(int a, int b) {
    return a + b;
}
```

- `objdump` is very useful when viewing equivalent assembly code & cross-checking how returning is performed.

#### NASM:

```nasm
mov eax, edi        ; copy a
add eax, esi        ; add b
ret                 ; result in eax
```


### <u>Mixed Approach</u>

- If both `int` & `float` are used in a structure, both RAX & XMM0 are used.
- Complex numbers use XMM0 & XMM1 together.



## **Topic - 5: Stack Alignment & Red Zone**

### <u>Goals/Objectives</u>

- Understanding stack alignment requirements.
- Understanding concept of red zone.


### <u>Stack Alignment</u>

- Modern CPUs can handle 16-byte alignment fast.
- Both SSE & AVX require 16-byte alignment.
- Even the stack pointer (RSP) needs alignment to 16-bytes.


### <u>Stack Pointer</u>

- As said earlier, RSP register is aligned by 16-bytes before `call`.
- But after `call`, an 8-byte address might be pushed to RSP.
- This removes the 16-byte alignment we had earlier.


### <u>Red Zone</u>

- **<u>Red zone</u>:** 128-byte long area before RSP which interrupts can't affect.
- It allows leaf functions to use it for data storage, without RSP alignment.
- **<u>Leaf function</u>:** Function which doesn't call another function.
- Red zone is useful as it can be used by trivial leaf functions without stress to adjust RSP.
- Also red zone boosts leaf function's performance.

```gas
# Using red zone for locals without pushing/popping stack.
movq $42, -8(%rsp)        # Directly storing data
```

- `-8` means 8 bytes before RSP.

>**<u>NOTE</u>:**
>1. **Windows x64 ABI** doesn't contain red zone.
>2. Some kernel or low-level might not allow using red zone.


### <u>Common Doubt</u>

- One doubt would be that while RSP's value is variable, how could red zone be relative to it?
- Red zone is not a fixed memory space, but rather something that floats with RSP.
- Whatever the value of RSP is, 128-bytes before it is red zone.


### <u>Non-Leaf Function</u>

```nasm
sub rsp, 32        ; Allocate 32 bytes on stack (16B aligned)

...                ; Use [rsp], [rsp+8], etc.

call printf        ; Function call allowed
add rsp, 32        ; Deallocate
ret
```

- Notice that memory in stack is allocated via subtraction, meaning stack grows downward.



## **Topic - 6: Signal Frame ABI**

### <u>Introduction</u>

- **<u>Signal frame</u>:** An environment created to handle a received signal.
- Whenever a signal is received by a user-space process, the kernel interrupts the normal flow of program & signal frame is created.
- It is created at process's stack.
- This signal frame handles the received signal & then resumes the paused flow of program.

>**<u>NOTE</u>:**
>If there is no signal handler, then the OS performs default action.


### <u>Moment Of Signal Delivery</u>

#### What "kernel" does?

1. Saves current user context/state into struct `sigcontext` or `ucontext`.
2. Allocates space on stack for signal frame.
3. Pushes a fake return address to restorer function.
4. Control of process is transferred to the signal handler.

>**<u>NOTE</u>:**
>1. Saving user context/state includes saving resisters, signal numbers etc.
>2. Restorer is a function used to safely return from signal frame.
>3. Fake address is `ret`, which calls restorer & restorer calls `sigreturn`.

#### What "user process" does?

5. Executes signal handler.

#### What "kernel" does - II:

6. After return from signal frame, kernel restores user context/state back.
7. Resumes the normal execution of the program that was paused.

>**<u>NOTE</u>:**
>1. Return from signal frame is done using `sigreturn` syscall.
>2. Restorer function is provided by ***glibc*** or user manually.
>3. Restorer function makes the `sigreturn` syscall.


### <u>Signal Frame Layout</u>

```
(High Address)

|------------|    <- RSP at signal entry
| siginfo_t  |       (optional, if SA_SIGINFO set)
|------------|
| ucontext_t |    <- Saved GPRs, FPUs, sigmask, etc.
|------------|
| return addr|    <- Trampoline/restorer
|------------|

(Low Address)
```

- `siginfo_t` stores information about signal.
- Signal masks are stored as `sigset_t` at ***bitmask***, but inaccessible by users.
- **<u>Bitmask</u>:** 1024-bits (128 bytes) representing blocked signals.


### <u>Registers Involved</u>

| Register | Purpose                                  |
| :------: | ---------------------------------------- |
|  `%rsp`  | Points to signal frame (set by kernel)   |
|  `%rip`  | Set to signal handler address            |
|  `%rax`  | May be used for syscall like `sigreturn` |
|  Others  | Saved in `ucontext_t`                    |

- Signal handler's address is set by the programmer.

```c
struct sigaction sa;
sa.sa_handler = my_handler;

sigaction(SIGINT, &sa, NULL);
```


### <u>Related Syscalls</u>

|    Syscall     | Description                       |
| :------------: | --------------------------------- |
|  `sigaction`   | Register a signal handler         |
| `rt_sigaction` | Modern version (with `siginfo_t`) |
|  `sigreturn`   | Restore context, resume execution |


### <u>SA_SIGINFO v/s Legacy Mode</u>

#### SA_SIGINFO:

```c
void handler(int sig, siginfo_t *, void *);
```

- Pushed by user.
- More detailed for better debugging experience.
- Has larger frame.

#### Legacy mode:

```c
void handler(int sig);
```

- Pushed by kernel.
- Poor debugging experience.
- Smaller frame.

>**<u>WARNING</u>:**
>1. Red zone mustn't be used in signal handling!
>2. Stack must be marked with `PROT_EXEC` (meaning executable) to work.

---
