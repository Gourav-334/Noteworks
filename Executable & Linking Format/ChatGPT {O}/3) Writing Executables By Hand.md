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

```
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
- `type` for section `.bss` will be `SHT_NOBITS`, meaning it doesn't occupy any space in file.


### <u>About .bss Mapping</u>

- `.bss` is present in virtual memory but not to file.
- This is because it is uninitialized & upcoming instruction will use it if required, while parsing.
- We just need to reserve space for it in memory, there is no data to write in ELF file, `.bss` doesn't contain anything at the compile time.

```
p_filesz = 512           -> size of .data (in file)
p_memsz  = 512 + 4096    -> total memory required: .data + .bss
```

- And because `.bss` is not present in file, the reserved `4096` bytes are `memset` to `0` in memory.
- Both `p_filesz` & `p_memsz` are part of `PT_LOAD` segment.


### <u>Summary Table</u>

| Segment | Section | Purpose                 | File Size | Mem Size | Permissions |
| :-----: | :-----: | ----------------------- | :-------: | :------: | :---------: |
| `.text` | `.text` | Code & syscalls         |     ✅     |    ✅     |    R + E    |
| `.data` | `.data` | Initialized globals     |     ✅     |    ✅     |    R + W    |
| `.bss`  | `.bss`  | Uninitialized variables |     ❌     |    ✅     |    R + W    |



## **Topic - 3: Writing Header Manually**

### <u>Goals/Objectives</u>

- Manually crafting ELF header (`Elf64_Ehdr`).
- Defining program header (`Elf64_Phdr`).
- Writing system calls in machine code & saving as binary.


### <u>ELF File Layout</u>

```
+----------------------------+ ← File offset 0x00
| ELF Header (64 bytes)      |
+----------------------------+ ← File offset 0x40
| Program Header (56 bytes)  |
+----------------------------+ ← File offset 0x78
| Code Segment (text)        | ← Entry point
+----------------------------+
```


### <u>Writing Binary In C</u>

#### Headers:

```c
/* raw_elf.c */

#include <stdio.h>
#include <stdint.h>
```

#### Variables (`main()` starts):

```c
FILE *fptr = fopen("raw_elf", "wb");    // Writing in binary mode.
```

#### ELF header:

```c
uint8_t elf_header[64] = {
	0x7f, 'E', 'L', 'F',   // Magic number
	
	// 64-bit, little endian, v1, OS ABI = System V
	2, 1, 1, 0,            
	0,0,0,0,0,0,0,0,       // Padding
	2, 0,                  // e_type = ET_EXEC (2)
	0x3e, 0x00,            // e_machine = AMD64 (0x3E)
	1,0,0,0,               // e_version = 1
	
	// e_entry = 0x400078
	0x78, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// e_phoff = 64 (0x40)
	0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	0,0,0,0,0,0,0,0,       // e_shoff = 0 (no section headers)
	0,0,0,0,               // e_flags = 0
	64, 0,                 // e_ehsize = ELF header size
	56, 0,                 // e_phentsize = size of program header
	1, 0,                  // e_phnum = 1
	0,0,                   // e_shentsize = 0
	0,0,                   // e_shnum = 0
	0,0                    // e_shstrndx = 0
};
```

- `uint8_t` represents a single byte, without any padding or alignment.

#### Program header:

```c
uint8_t program_header[56] = {
	1,0,0,0,                    // p_type = PT_LOAD
	5,0,0,0,                    // p_flags = R + X
	
	// p_offset = 0
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// p_vaddr = 0x400000
	0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// p_paddr (same)
	0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// p_filesz = 144
	0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// p_memsz = 144
	0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	
	// p_align = 0x1000
	0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 
};
```

#### Segment code:

```c
uint8_t code[] = {
	0xb8, 0x01, 0x00, 0x00, 0x00,   // mov eax, 1      (sys_write)
	0xbf, 0x01, 0x00, 0x00, 0x00,   // mov edi, 1      (stdout)
	0x48, 0x8d, 0x35, 0x0a, 0x00, 0x00, 0x00, // lea rsi,[rip+0xa]
	0xba, 0x0e, 0x00, 0x00, 0x00,   // mov edx, 14
	0x0f, 0x05,                     // syscall
	0xb8, 0x3c, 0x00, 0x00, 0x00,   // mov eax, 60     (sys_exit)
	0x31, 0xff,                     // xor edi, edi
	0x0f, 0x05,                     // syscall
	
	// message (offset = 0x2a from code start)
	'H', 'e', 'l', 'l', 'o', ',', ' ',
	'E', 'L', 'F', '!', '\n', 0
};
```

- Though each instruction varies in length (in bytes), the loader differentiates by reading the first byte.
- The first byte tells which opcode is being used.

#### Writing byte streams:

```c
fwrite(elf_header, 1, sizeof(elf_header), fp);
fwrite(program_header, 1, sizeof(program_header), fp);
fwrite(code, 1, sizeof(code), fp);
```

#### Closing (still in `main()`):

```c
fclose(fp);
return 0;
```


### <u>Compile & Run</u>

1. Compile the `raw_elf.c` directly into ELF executable.
2. Run the generated executable `raw_elf`.
3. Provide permission to run the new executable created.
4. Run the new executable.



## **Topic - 4: Writing ELF Generator**

### <u>Directory Layout</u>

```
/elfgen
  ├── gen_elf.c        -> Our ELF generator
  ├── Makefile         -> Optional
  └── out/
      └── hello        -> Output ELF binary
```



### <u>Assembly Code</u>

#### Headers:

```c
/* elf_gen.c */

#include <stdio.h>
#include <stdint.h>
#include <string.h>
```

#### Macros:

```c
#define PAGE_SIZE 0x1000


/* ELF constants */

#define EI_NIDENT 16
#define PT_LOAD   1
#define ET_EXEC   2
#define EM_X86_64 62
#define EV_CURRENT 1


/* File permissions */

#define PF_X 0x1
#define PF_W 0x2
#define PF_R 0x4
```

#### Binary instructions:

```c
uint8_t code[] = {
  0xb8, 0x01, 0x00, 0x00, 0x00,       // mov eax, 1
  0xbf, 0x01, 0x00, 0x00, 0x00,       // mov edi, 1
  0x48, 0x8d, 0x35, 0x0e, 0x00, 0x00, 0x00, // lea rsi, [rip+0xa]
  0xba, 0x0e, 0x00, 0x00, 0x00,       // mov edx, 14
  0x0f, 0x05,                         // syscall
  0xb8, 0x3c, 0x00, 0x00, 0x00,       // mov eax, 60
  0x31, 0xff,                         // xor edi, edi
  0x0f, 0x05,                         // syscall
  // message
  'H','e','l','l','o',',',' ',
  'w','o','r','l','d','\n', 0
};
```

#### ELF header structure:

```c
struct __attribute__((packed)) Elf64_Ehdr {
  uint8_t  e_ident[EI_NIDENT];
  uint16_t e_type;
  uint16_t e_machine;
  uint32_t e_version;
  uint64_t e_entry;
  uint64_t e_phoff;
  uint64_t e_shoff;
  uint32_t e_flags;
  uint16_t e_ehsize;
  uint16_t e_phentsize;
  uint16_t e_phnum;
  uint16_t e_shentsize;
  uint16_t e_shnum;
  uint16_t e_shstrndx;
};
```

#### Program header structure:

```c
struct __attribute__((packed)) Elf64_Phdr {
  uint32_t p_type;
  uint32_t p_flags;
  uint64_t p_offset;
  uint64_t p_vaddr;
  uint64_t p_paddr;
  uint64_t p_filesz;
  uint64_t p_memsz;
  uint64_t p_align;
};
```

#### Accessing executable (in `main()`):

```c
FILE *fp = fopen("out/hello", "wb");

if (!fp) {
	perror("fopen");
	return 1;
}
```

#### ELF header instance:

```c
struct Elf64_Ehdr ehdr = {0};
memcpy(ehdr.e_ident, "\x7f""ELF", 4);    // 2nd arg = "\x7fELF"

ehdr.e_ident[4] = 2;        // 64-bit
ehdr.e_ident[5] = 1;        // Little endian
ehdr.e_ident[6] = 1;        // ELF version
ehdr.e_type = ET_EXEC;
ehdr.e_machine = EM_X86_64;
ehdr.e_version = EV_CURRENT;
ehdr.e_entry = 0x400078;
ehdr.e_phoff = sizeof(ehdr);
ehdr.e_ehsize = sizeof(ehdr);
ehdr.e_phentsize = sizeof(struct Elf64_Phdr);
ehdr.e_phnum = 1;
```

#### Program header instance:

```c
struct Elf64_Phdr phdr = {
	.p_type = PT_LOAD,
	.p_flags = 5 | 1 << 1,        // PF_X | PF_R
	.p_offset = 0,
	.p_vaddr = 0x400000,
	.p_paddr = 0x400000,
	.p_filesz = sizeof(ehdr) + sizeof(phdr) + sizeof(code),
	.p_memsz = sizeof(ehdr) + sizeof(phdr) + sizeof(code),
	.p_align = PAGE_SIZE
};
```

#### Writing to executable:

```c
fwrite(&ehdr, sizeof(ehdr), 1, fp);
fwrite(&phdr, sizeof(phdr), 1, fp);
fwrite(code, sizeof(code), 1, fp);
```

#### Closing statements:

```c
fclose(fp);
printf("ELF binary 'hello' generated in out!\n");

return 0;
```
