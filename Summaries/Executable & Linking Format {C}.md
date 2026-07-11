# $\fbox{EXECUTABLE \& LINKING FORMAT}$





## **Topic - 1: Introduction & Ground Setup**

### <u>Loader's Working</u>

1. Loader reads ELF header.
2. Then maps memory as per read header.
3. Finally jumps to `.text` section for execution.

>**<u>NOTE</u>:**
>`.text` in assembly is like `main()` in C.


### <u>Basic ELF Structure</u>

```
+-----------------+
| ELF Header      |
| Program Headers |
| Section Headers |
| .text           |
| .data           |
| .bss            |
| .rodata, etc    |
+-----------------+
```


### <u>Clarity Of Roles</u>

- **<u>Assembler</u>:** Generates machine code (relocatable).
- **<u>Linker</u>:** Resolves symbols, patches addresses & arranges binary layout.
- **<u>Loader</u>:** Loading binary to memory & executing it as per its type.


### <u>ELF Tools</u>

|    Tool    | Role                                              |
| :--------: | :------------------------------------------------ |
| `readelf`  | Reading ELF specific fields.                      |
| `objdump`  | Disassembles hex machine code to assembly.        |
| `hexdump`  | Disassembles hex machine code to raw binary form. |
| `patchelf` | ELF modifying tool.                               |



## **Topic - 2: ELF File Format Internals**

### <u>ELF Header Types</u>

- **Core ELF header (`e_`) -** Basic metadata
- **Program header (`ph_`/`p_`) -** Tells loader how to map binaries.
- **Section header (`sh_`) -** Required by linker & aids debuggers.


### <u>Primary Sections</u>

- `.text`
- `.data`
- `.bss`
- `.rodata`
- `.symtab`
- `.strtab`
- `.shstrtab`


### <u>32-Bit v/s 64-Bit ELF</u>

| Header               | 32-Bit ELF (in bytes) | 64-Bit ELF (in bytes) |
| :------------------- | :-------------------: | :-------------------: |
| Address field        |           4           |           8           |
| ELF Header           |          52           |          64           |
| Program header table |          32           |          56           |
| Section header table |          40           |          64           |


### <u>Dynamic Sections</u>

- **`.dynamic` -** Contains metadata for dynamic linker.
- **`.got` -** Contains addresses of external symbols & global variables.
- **`.plt` -** Stubs to register unresolved shared symbols into `.got`.
- **`.symtab` -** Contains record of all static symbols.
- **`.dynsym` -** Contains record of all dynamic symbols.


### <u>Structs For ELF</u>

- These are the structures for aiding ELF operations using `<elf.h>`.

| Use                      |  Identifier  |     Category     | Note                                                      |
| :----------------------- | :----------: | :--------------: | :-------------------------------------------------------- |
| ELF header               | `Elf64_Ehdr` | File information | Contains metadata for the ELF file.                       |
| Program header entry     | `Elf64_Phdr` | File information | Contains metadata for program header.                     |
| Section header entry     | `Elf64_Shdr` | File information | Contains metadata for section header.                     |
| Dynamic section          | `Elf64_Dyn`  |    Code data     | Each instance contains metadata for a dynamic entry.      |
| Symbol information       | `Elf64_Sym`  |    Code data     | Each instance contains metadata for a symbol.             |
| Relocation info (32-bit) | `Elf64_Rel`  |    Code data     | Contains information about loading 32-bit symbols to RAM. |
| Relocation info (64-bit) | `Elf64_Rela` |    Code data     | Contains information about loading 64-bit symbols to RAM. |



## **Topic - 3: Writing Executables By Hand**

### <u>Clarity</u>

#### How loader recognizes start of sections?

- Information about offset of each section is already packed into program header file.
- But its on us to select offset for the sections.

#### How instruction breaks to binaries?

- **Parts -** Opcodes, operands, addressing mode, prefixes
- Formal breakdown for x86 processors will be as shown below.

```out
[prefixes][opcode][ModR/M][SIB][displacement][immediate]
```



## **Topic - 4: System V ABI Deep Dive**

### <u>SysV Conventions</u>

- Stack layout during function calls
- Way of using registers
- Argument & return value passing
- Caller/callee responsibilities


### <u>Arguments In Order</u>

- **1st to 6th Order -** `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`
- **Rest -** Pushed to stack


### <u>Value Returning</u>

| Return Type                  | Where It's Returned             |
| :--------------------------- | :------------------------------ |
| Integer/pointer (any scalar) | `rax`                           |
| 128-bit values               | `rax`:`rdx`                     |
| Floating point value         | `xmm0`:`xmm1`                   |
| Structures                   | Hidden pointer or memory layout |


### <u>GPR Usage</u>

|     Register      | Name                | Usage                                                |
| :---------------: | :------------------ | :--------------------------------------------------- |
|       `rax`       | Accumulator         | Arithmetic operations, return value.                 |
|       `rbx`       | Base register       | General purpose, point to data.                      |
|       `rcx`       | Count register      | Loop counter, 4th argument.                          |
|       `rdx`       | Data register       | I/O, 3rd argument.                                   |
|       `rsi`       | Source index        | Source memory address, 2nd argument.                 |
|       `rdi`       | Source destination  | Destination memory address, 1st argument.            |
|       `rbp`       | Base pointer        | Points to base of current function's frame in stack. |
|       `rsp`       | Stack pointer       | Points to the top of stack.                          |
|       `r8`        | General purpose     | 5th argument.                                        |
|       `r9`        | General purpose     | 6th argument.                                        |
|    `r10`-`r11`    | General purpose     | Scratch, system call temporary.                      |
|    `r12`-`r15`    | General purpose     | Preserved across call.                               |
|       `rip`       | Instruction pointer | Points to address of next instruction.               |
| `eflags`/`rflags` | Flag register       | Contains statuses.                                   |

- **Caller saved (scratch) -** RAX, RCX, RDX, RSI, RDI, R8-R11
- **Callee saved (preserved) -** RBX, RBP, R12-R15, RSP


### <u>Stack Layout</u>

#### Activation record:

```
HIGHER ADDRESS
|
|
+------------------------------------+
| argN+2 (if needed)                 |
| arg7 (stack-passed args)           |
+------------------------------------+
| Return address (from `call`)       |
+------------------------------------+
| Previous RBP (saved frame pointer) |
+------------------------------------+
| Local variables (pushed by callee) |
| (aligned to 16 bytes)              |
+------------------------------------+
|
|
LOWER ADDRESS
```

#### Signal frame:

```
HIGHER ADDRESS
|
|
+-------------+   <- RSP at signal entry
| siginfo_t   |      (optional if SA_SIGINFO set)
+-------------+
| ucontext_t  |   <- Saved GPRs, FPUs, sigmasks, etc.
+-------------+
| return addr |   <- Trampoline / restorer
+-------------+
|
|
LOWER ADDRESSES
```


### <u>Warnings</u>

- Red zones mustn't be used in signal handling.
- Stack must be marked with `PROT_EXEC` to work during execution.



## **Topic - 5: Dynamic Linker & Loader**

### <u>Loader Responsibilities</u>

- To parse dynamic sections.
- To resolve symbols & load `.so` (if required).
- To relocate sections.
- Lazy & eager symbol resolution.
- To run initializers.
- To jump to `_start` section.


### <u>RPATH v/s RUNPATH</u>

- Both contain paths to many shared libraries.
- There are other options to encode paths, but with an order of preference.
- `DT_RPATH` is deprecated while `DT_RUNPATH` is modern.
- Both are of `char*` type & point to strings in `.dynstr`.
- We can encode a path to ELF executable using the commands given below.

```sh
# RPATH
gcc -Wl,-rpath,/custom/path myprog.c -o myprog

# RUNPATH
gcc -Wl,--enable-new-dtags -Wl,-rpath,/custom/path myprog.c -o myprog

patchelf --set-rpath /new/lib ./myBin        # Set/modify path
patchelf --remove-rpath ./binary             # Remove path
```



## **Topic - 6: Advanced ELF Topics**

### <u>Stripping Binaries</u>

- **Removed sections -** `.symtab`, `.strtab`, `.debug_*`, `.comment`, `.note.*`, `.rel.*`, `.rela.*`
- **Retained sections -** `.text`, `.data`, `.bss`, `.rodata`, `.dynsym`, `.dynstr`, `.interp`, `.dynamic`, `.got`, `.plt`
- We can also selectively remove any section we want to.


### <u>Symbol Versioning</u>

#### Sections:

|   Section Name   | Description                                                   |
| :--------------: | :------------------------------------------------------------ |
|  `.gnu.version`  | Contains mapping of each dynamic symbols with their versions. |
| `.gnu_version_n` | Lists required versions from dependency shared objects.       |
| `.gnu_version_d` | Describes supported versions by the shared object.            |

#### Version script:

```
VER_1.0 {
	global:
		foo;
		
	local:
		*;
};

VER_2.0 {
	global:
		foo@@VER_1.0;        // 'foo' is aliased to version 1.0
		bar;
};
```


### <u>TLS Sections</u>

|      Section       | Purpose                            |
| :----------------: | ---------------------------------- |
|      `.tdata`      | Initialized TLS data               |
|      `.tbss`       | Uninitialized TLS data             |
| `.init_array`, etc | Used during dynamic TLS allocation |



## **Topic - 7: Binary Code Translation**

### <u>Machine Code & Binary Representation</u>

- For an x86 instruction, it has range of $[1,15]$ bytes.
- **Operand:** Involved data in an operation.
- **Immediate:** A literal value in instruction.
- **Displacement:** A memory offset
- For registers & certain assembly instructions, their binary size & involved encodings may vary.


### <u>x86 Instruction Set Architecture</u>

| Element           | About                                            |
| :---------------- | :----------------------------------------------- |
| Optional prefixes | For segment override, repeat, operand size, etc. |
| Opcode byte(s)    | Takes about 1-3 bytes.                           |
| ModR/M byte       | If operand has register or memory.               |
| SIB byte          | If complex addressing is required.               |
| Displacement      | If memory offset is required.                    |
| Immediate         | A literal value.                                 |

| Part | Size  | Usage                   |
| :--: | :---: | :---------------------- |
| Mod  | 2-bit | Addressing mode         |
| Reg  | 3-bit | Register operand        |
| R/M  | 3-bit | Memory/register operand |


### <u>Instruction Example</u>

- `mov eax, ebx` $\rightarrow$ `MOV r/m32, r32` $\rightarrow$ `89 D8`
- `89` = `mov`
- `D8` = `eax, ebx`

>**<u>NOTE</u>:**
>1. Little-endian ***only*** affects the order of how values in containers are read, i.e. backwards.
>2. It ***doesn't*** affect how the instructions are read, i.e. forward.



## **Topic - 8: Structure Of ELF**

### <u>ELF File Overview</u>

- **Logical/programmer view:** Set of *sections* useful for compilers/linkers.
- For example, `.text`, `.data`, `.bss`, `.rodata`, etc.
- **Runtime/loader view:** Set of *segments* useful for OS loader.
- For example, `LOAD`, `DYNAMIC`, etc.


### <u>ELF Header</u>

- Starts from `0` and of $64$ bytes.
- It describes file type, architecture, entry point, address to program/section header.
- **Embedded fields -** `e_ident`, `e_type`, `e_machine`, `e_entry`, `e_phoff`, `e_phoff`, `e_flags`, `e_ehsize`, `e_phentsize`, `e_phnum`, `e_shentsize`, `e_shnum`, `e_shstrndx`.


### <u>Program Header Table</u>

- Starts from the address stored at `phoff`.
- It guides loader to map segments to memory (one PHT for each segment).
- **Embedded fields -** `p_type`, `p_offset`, `p_vaddr`, `p_paddr`, `p_filesz`, `p_memsz`, `p_flags`, `p_align`.


### <u>Section Header Table</u>

- Starts from the address stored at `e_shoff`.
- Guides linkers & debuggers in linking & symbol resolution (one SHT for each section).
- **Embedded fields -** `sh_name`, `sh_type`, `sh_flags`, `sh_addr`, `sh_offset`, `sh_size`, `sh_link`, `sh_info`, `sh_addralign`, `sh_entsize`.


### <u>Symbol Table</u>

- Used by linker & debugger to map functions & variables to their addresses.
- **Embedded fields -** `st_name`, `st_info`, `st_info`, `st_other`, `st_shndx`, `st_value`, `st_size`.


### <u>Relocation Entries</u>

- Used by linker to patch addresses.
- **Format -** `.rela.<section>` or `.rel.<section>`
- **Embedded fields -** `r_offset`, `r_info`, `r_addend`.


### <u>Dynamic Section</u>

- Used by dynamic linker for shared libraries.
- **Embedded tags -** `DT_NEEDED`, `DT_PLTRELSZ`, `DT_JMPREL`, `DT_SYMTAB`, `DT_STRTAB`.


### <u>ELF Binary Organization</u>

```
ELF Header
Program Header Table
Section Header Table (for linker/debugger)

+----------------+  
| .text          |  <- executable code
| .rodata        |  <- constants
| .data          |  <- initialized vars
| .bss           |  <- zero-initialized vars
| .symtab/.strtab|  <- symbols
| .rela/.rel     |  <- relocations
| .dynamic       |  <- dynamic linking info
+----------------+
```

---