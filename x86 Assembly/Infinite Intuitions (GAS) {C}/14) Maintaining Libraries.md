# $\fbox{Chapter 14: MAKING LIBRARIES}$





## **Topic - 1: Static Libraries**

### <u>Creating Static Library</u>

1. Write the first library assembly code.

```gas
	.section .text

.global mylib_add

mylib_add:
    movq %rdi, %rax        # Move the first argument to RAX
    addq %rsi, %rax        # Add the second argument to RAX
    ret
```

2. Now write the second one.

```gas
	.section .text

.global mylib_sub

mylib_sub:
    movq %rdi, %rax        # Move the first argument to RAX
    subq %rsi, %rax        # Subtract the second argument from RAX
    ret
```

3. Compile to intermediate object files.

```sh
as -c add.s -o add.o
as -c sub.s -o sub.o
```

4. Create static library.

```sh
ar rcs libmylib.a add.o sub.o
```

>**<u>NOTE</u>:**
>1. Separate header files are not required in assembly.
>2. We can link C object files with assembly object files.


### <u>Include Directive</u>

```gas
.include "filename.s"        # Custom/third-party file
.include <filename.s>        # Standard library file
```



## **Topic - 2: Dynamic Libraries**

### <u>Introduction</u>

- Dynamic libraries can't mention PIC in them.
- **<u>PIC</u>:** Position Independent Code
- Meaning, absolute addresses can't be mentioned as dynamic libraries are loaded at runtime.
- For example `0x00789ab1`.
- So, let's create dynamic library from the previous codes themselves.


### <u>Creating Dynamic Library</u>

1. Notice the `-fPIC` flag we added for compilation.

```sh
as -fPIC -c add.s -o add.o
as -fPIC -c sub.s -o sub.o
```

2. Make dynamic library with `-shared` flag.

```sh
ld -shared -o libmylib.so add.o sub.o
```



## **Topic - 3: Integration With GCC**

### <u>Steps</u>

1. Know which ABI your system uses (generally **x86-64 ABI** for UNIX).
2. Define symbols which represent imported elements with `.global`.
3. Load required arguments to appropriate registers or stacks.
4. Use `call` instruction to point at C library function's offset.

>**<u>NOTE</u>:**
>Mind the return value, which is kept in RAX in x86-64 processors.

---
