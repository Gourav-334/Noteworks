# $\fbox{Chapter 7: SPINOFF SUMMARIES}$





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
- **`.got` -** Contains addresses of shared symbols.
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
