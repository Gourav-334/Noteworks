# $\fbox{Chapter 3: WRITING EXECUTABLES BY HAND}$





## **Topic - 1: Minimal 64-Bit "Hello, World!"**

### <u>Goals/Objectives</u>

- Writing `"Hello, World!"` to terminal without `libc` or `ld`.
- We will do this using GNU assembler (`as`).
- And permission to run the executable will be provided using `chmod`.


### <u>Code</u>

```gas
.section .text
.global _start


_start:
    mov     $1, %rax               # syscall: write
    mov     $1, %rdi               # fd: stdout
    lea     message(%rip), %rsi    # Buffer
    mov     $14, %rdx              # Count/size
    syscall

    mov     $60, %rax              # syscall: exit
    xor     %rdi, %rdi             # status = 0
    syscall


.section .data
	message: .ascii "Hello, World!\n"
```

- RAX holds the system call number.
- RDI & RSI contain 1st & 2nd argument respectively.
- `syscall` as `$1` means `write(fd, buff, count)`.
- `syscall` as `$60` means `exit(status)`.

>**<u>NOTE</u>:**
>1. Notice that we used `leaq` for loading `message`, not `movq`.
>2. Its `leaq`'s responsibility to load values of labels into registers.


### <u>Compiling & Running</u>

```sh
as -o hello.o hello.s
ld -o hello hello.o -nostdlib -static

chmod +x hello
./hello
```

- Linking line discards `.symtab` & `.strtab`, as it doesn't use `stdlib`.
- System calls we wrote are being passed directly to ABI, no `libc` used.
- ELF header is generated only when `ld` links `hello.o`.
- Disassembled code via `objdump` has no labels, as they are replaced by their offsets.



## **Topic - 2: Manual Segment Construction**

### <u>Goals/Objectives</u>

- Understanding how ELF segments are made & structured.
- Understanding segment permissions.
- Knowing what loader maps into memory.


### <u>ELF Program Headers</u>

```c
typedef struct {
    Elf64_Word   p_type;      // PT_LOAD (1)
    Elf64_Word   p_flags;     // PF_X | PF_W | PF_R
    Elf64_Off    p_offset;    // File offset where segment starts
    Elf64_Addr   p_vaddr;     // Virtual address where loaded
    Elf64_Addr   p_paddr;     // (for physical loading - unused)
    Elf64_Xword  p_filesz;    // Number of bytes in file
    Elf64_Xword  p_memsz;     // Number of bytes in memory
    Elf64_Xword  p_align;     // Page alignment
} Elf64_Phdr;
```


### <u>Segment Mapping</u>

```txt
+-------------------------+  <--- 0x400000 (virtual address start)
| ELF Header              |
+-------------------------+  <-- p_offset = 0
| Program Header Table    |
+-------------------------+
| .text (code)            |
| _start                  |  <-- p_flags = R + E
+-------------------------+
| .data (initialized)     |  <-- p_flags = R + W
+-------------------------+
| .bss (uninitialized)    |  <-- in memory only!
+-------------------------+
```

- We don't need section header for now.


### <u>Assembly Example</u>

- We will declare section `.text`, `.data` & `.bss`.

```gas
.section .text
.global _start


_start:
    movq $1, %rax          # sys_write
    movq $1, %rdi          # stdout
    movq $message, %rsi    # Address of 'message'
    movq $14, %rdx         # Length of 'message'
    syscall
	
    movq $60, %rax         # sys_exit
    xor  %rdi, %rdi        # status = 0
    syscall


.section .data
message:
    .asciz "Hello, ELF!\n\0"


.section .bss
.lcomm buffer, 4096        # Reserve 4KB (0-initialized at runtime)
```

- Assemble & link it just like how it was done in previous topic.
- `.lcomm` doesn't reserve space on disk, but on memory by loader.
- We can name `buffer` as something else too.


### <u>Inspecting Binary</u>

- Read the executable ELF from previous sub-topic with `-S`.
- You will notice how address is assigned only to `.text`, `.data` & `.bss` sections.
- This because we used only those sections & stripped the unrequired rest with `-static` & `-nostdlib`.
- `.text` is marked with flag `AX` (executable), while `.data` & `.bss` are marked with `WX` (writable).


### <u>About .bss Mapping</u>

- `.bss` are loaded to virtual memory but not to file.


### <u>Summary Table</u>

| Segment | Section | Purpose                 | File Size | Mem Size | Permissions |
| :-----: | :-----: | ----------------------- | :-------: | :------: | :---------: |
| `.text` | `.text` | Code & syscalls         |     ✅     |    ✅     |    R + E    |
| `.data` | `.data` | Initialized globals     |     ✅     |    ✅     |    R + W    |
| `.bss`  | `.bss`  | Uninitialized variables |     ❌     |    ✅     |    R + W    |
