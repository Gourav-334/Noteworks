# $\fbox{Chapter 2: ELF FILE FORMAT INTERNALS}$





## **Topic - 1: Header Overview & Fields**

### <u>Introduction</u>

- ELF header composes of 64-bytes, which tells OS how to interpret the file.
- It tells about architecture, endianness, file type, entry point address, offsets etc.

| Offset (in hex) |       Field       | Size (in bytes) | Description                            |
| :-------------: | :---------------: | :-------------: | :------------------------------------- |
|     `0x00`      | `e_ident[ET_MAG]` |        4        | Magic numbers                          |
|     `0x04`      |  `e_ident[...]`   |       12        | Class (32/64), endian, ABI information |
|     `0x10`      |     `e_type`      |        2        | File type                              |
|     `0x12`      |    `e_machine`    |        2        | Target ISA's code                      |
|     `0x14`      |    `e_version`    |        4        | ELF format version                     |
|     `0x18`      |     `e_entry`     |        8        | Entry point virtual address            |
|     `0x20`      |     `e_phoff`     |        8        | Program header tables's offset         |
|     `0x28`      |     `e_shoff`     |        8        | Section header table's offset          |
|     `0x30`      |     `e_flags`     |        4        | Architecture-specific flags            |
|     `0x34`      |    `e_ehsize`     |        2        | ELF header size                        |
|     `0x36`      |   `e_phentsize`   |        2        | Program header entry size              |
|     `0x38`      |     `e_phnum`     |        2        | Number of program header entries       |
|     `0x3A`      |   `e_shentsize`   |        2        | Section header entry size              |
|     `0x3C`      |     `e_shnum`     |        2        | Number of section header entries       |
|     `0x3E`      |   `e_shstrndx`    |        2        | Section header string index            |

- Some fields like `e_machine`, `e_entry`, and more varies processor-to-processor.
- Anything starting with `e_` is metadata about whole ELF file.
- While those starting from `ph_` & `sh_` are...


### <u>Prefix Meaning</u>

| Prefix        | Scope                | Belongs To               | Purpose                          |
| ------------- | -------------------- | ------------------------ | -------------------------------- |
| `e_`          | ELF Header           | `Elf64_Ehdr`             | Metadata about the whole ELF     |
| `ph_` or `p_` | Program Header Entry | `Elf64_Phdr` (its array) | Loader-level segment descriptors |
| `sh_`         | Section Header Entry | `Elf64_Shdr` (its array) | Linker-level symbolic layout     |


### <u>Inspecting Binary</u>

#### Inspecting with `readelf`:

```sh
readelf -h /bin/ls
```

#### Output:

- The output below isn't complete & trimmed for understanding.

```
ELF Header:
  Magic:   7f 45 4c 46 ...
  Class:                             ELF64
  Data:                              2's complement, little endian
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Entry point address:               0x4010b0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          8840 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
```


### <u>Minimal ELF Header</u>

- This code isn't complete, just shows how generating ELF headers would look like.

```c
unsigned char elf_header[64] = {
	0x7f, 'E', 'L', 'F',           // Magic number
	2, 1, 1, 0,                    // 64-bit class, little endian
	0, 0, 0, 0, 0, 0, 0, 0,        // Padding
	2, 0,                          // e_type = EXEC
	0x3e, 0x00,                    // e_machine = x86_64
	1, 0, 0, 0                     // e_version
	
	/* ...more fields... */
}
```

>**<u>NOTE</u>:**
>Fields like `e_entry`, `e_phoff` & `e_shoff` are necessary to know from where to start execution, mapping segments & parsing internals.



## **Topic - 2: Program Header Table (PHT)**

### <u>Introduction</u>

- PHT tells loader how to map ELF binaries in memory, thus mandatory for execution unlike SHT.
- Section header table (SHT) is used to aid linkers & debuggers.
- Each entry in PHT represents a segment.
- **<u>Segment</u>:** Contiguous block of data that is loaded into memory.


### <u>Structure Of ELF64 PHT</u>

| Offset (in hex) |   Field    | Size (in bytes) | Description                         |
| :-------------: | :--------: | :-------------: | :---------------------------------- |
|     `0x00`      |  `p_type`  |        4        | Segment type                        |
|     `0x04`      | `p_flags`  |        4        | Access flags - `R`, `W` or `X`      |
|     `0x08`      | `p_offset` |        8        | Offset of segment                   |
|     `0x10`      | `p_vaddr`  |        8        | Virtual address                     |
|     `0x18`      | `p_paddr`  |        8        | Physical address (ignored on Linux) |
|     `0x20`      | `p_filesz` |        8        | Size in file                        |
|     `0x28`      | `p_memsz`  |        8        | Size in memory                      |
|     `0x30`      | `p_align`  |        8        | Alignment requirements              |

- This table is read by the kernel i.e. `ld-linux.so`.

>**<u>NOTE</u>:**
>`e_phentsize` $\times$ `e_phnum` $=$ $\text{Total table size}$


### <u>Common P-TYPE Values</u>

- These are common values for `p_type` field.

| `p_type`     | Value | Meaning                                       |
| :----------- | :---: | --------------------------------------------- |
| `PT_NULL`    |  `0`  | Unused                                        |
| `PT_LOAD`    |  `1`  | Loadable segment (`.code`, `.data`, `.bss`)   |
| `PT_DYNAMIC` |  `2`  | Dynamic linking info                          |
| `PT_INTERP`  |  `3`  | Interpreter path (e.g., `/lib64/ld-linux...`) |
| `PT_NOTE`    |  `4`  | Auxiliary info like build ID                  |
| `PT_PHDR`    |  `6`  | Location of the PHT itself                    |
| `PT_TLS`     |  `7`  | Thread-local storage segment                  |

- Loaders only use `PT_LOAD` as `p_type`.
- That means `PT_LOAD` is already mapped in memory.


### <u>Inspecting ELF Segments</u>

#### Shell command:

- `-l` with `readelf` is used to view segments mappings.

```sh
readelf -l /bin/ls
```

#### Output:

- Not all columns are shown here, for maintaining structure.

```
Program Headers:
  Type           Offset   VirtAddr           PhysAddr          
  LOAD           0x000000 0x0000000000400000 0x0000000000400000 
  LOAD           0x0017e8 0x0000000000601e8 0x0000000000601e8 
```

- Try it out, it provides various details about the binary.


### <u>PHT v/s SHT</u>

|        Feature         | Program Header Table     | Section Header Table       |
| :--------------------: | ------------------------ | -------------------------- |
|        Purpose         | Execution                | Linking/Debugging          |
|        Used By         | Loader (OS)              | Linker, `objdump`, `nm`    |
| Required in Executable | Yes                      | No                         |
|      Format Focus      | Segments (file ↔ memory) | Sections (symbolic layout) |

- In minimal executables, SHT can be skipped but PHT can't be.


### <u>Sample PT-LOAD Segment</u>

- A segment, `PT_LOAD` segment for loaders in particular, might look like this.

```c
struct Elf64_Phdr phdr = {
	.p_type   = PT_LOAD,
    .p_flags  = PF_R | PF_X,
    .p_offset = 0x1000,
    .p_vaddr  = 0x400000,
    .p_filesz = 0x200,
    .p_memsz  = 0x200,
    .p_align  = 0x1000
};
```



## **Topic - 3: Section Header Table (SHT)**

### <u>Introduction</u>

- SHT breakdowns ELF binary into various sections.
- We will learn how symbols & sections are tracked by certain tools.
- These tools include linkers, debuggers, `nm`, `objdump`, and more.


### <u>Sections</u>

#### List:

|   Section   | Description                       |      Type      |
| :---------: | --------------------------------- | :------------: |
|   `.text`   | Code                              | `SHT_PROGBITS` |
|   `.data`   | Initialized global variables      | `SHT_PROGBITS` |
|   `.bss`    | Uninitialized data (no file size) |  `SHT_NOBITS`  |
|  `.rodata`  | Read-only constants               | `SHT_PROGBITS` |
|  `.symtab`  | Symbol table (for linking)        |  `SHT_SYMTAB`  |
|  `.strtab`  | Strings used in `.symtab`         |  `SHT_STRTAB`  |
| `.shstrtab` | Section names as strings          |  `SHT_STRTAB`  |

#### Types:

1. **<u>File contained</u>:** Written to file, but not not necessarily to memory. For example, code under `.text`.
2. **<u>Logical only</u>:** Consistently maintained in memory during programs lifespan. For example, constants defined in `.bss`.


### <u>Structure Of ELF64 SHT</u>

| Offset (in hex) |     Field      | Size (in bytes) | Description                                |
| :-------------: | :------------: | :-------------: | ------------------------------------------ |
|     `0x00`      |   `sh_name`    |        4        | Offset of section name in `.shstrtab`      |
|     `0x04`      |   `sh_type`    |        4        | Section type (`PROGBITS`, `NOBITS`, etc)   |
|     `0x08`      |   `sh_flags`   |        8        | Flags (`ALLOC`, `WRITE`, `EXEC`)           |
|     `0x10`      |   `sh_addr`    |        8        | Virtual address (if allocated)             |
|     `0x18`      |  `sh_offset`   |        8        | Section's offset in file                   |
|     `0x20`      |   `sh_size`    |        8        | Section size (in file or memory)           |
|     `0x28`      |   `sh_link`    |        4        | Links to other section (used by `.symtab`) |
|     `0x2C`      |   `sh_info`    |        4        | Extra info (like `#` of symbols)           |
|     `0x30`      | `sh_addralign` |        8        | Alignment constraints                      |
|     `0x38`      |  `sh_entsize`  |        8        | Size of each entry if section is table     |


### <u>Pointer Fields In SHT</u>

|  Field Name   | Description                          |
| :-----------: | :----------------------------------- |
|   `e_shoff`   | SHT offset in file                   |
| `e_shentsize` | Size of a section header             |
|   `e_shnum`   | Number of entries                    |
| `e_shstrndx`  | Index of each section name as string |


### <u>Binary Blueprint</u>

- Various binary codes are linked to a symbol in symbol table.
- This symbol is represented with human readable name.
- For example, `main` & `printf` etc.
- These are not necessary for execution but for purpose of linking, debugging & analysis.
- That's why some toolchains strip SHT from ELF using `strip`.


### <u>Inspecting SHT</u>

#### Command:

```sh
readelf -S /bin/ls
```

We can alternatively use `objdump -h <file_name>`.

#### Output:

- A few columns are excluded to maintain readability.

```
Section Headers:
  [Nr] Name       Type         Addr     Off    Size   ES Flg Lk
  [ 0]            NULL         00000000 000000 000000 00      0
  [ 1] .interp    PROGBITS     00000000 0000e0 00001c 00   A  0   
  [ 2] .note.ABI  NOTE         00000000 000100 000020 00   A  0   
  [ 3] .text      PROGBITS     00000000 000200 001000 00  AX  0   
  [ 4] .data      PROGBITS     00001000 001200 000080 00  WA  0   
```


### <u>Creating SH Entry</u>

- We are doing so by creating an instance of structure `Elf64_Shdr`.

```c
struct Elf64_Shdr sh_text = {
    .sh_name      = 1,              // Offset in '.shstrtab'
    .sh_type      = SHT_PROGBITS,
    .sh_flags     = SHF_ALLOC | SHF_EXECINSTR,
    .sh_addr      = 0x400000,
    .sh_offset    = 0x1000,
    .sh_size      = 0x200,
    .sh_addralign = 0x10
};
```



## **Topic - 4: ELF Classes & Endianness**

### <u>Introduction</u>

- Two indexes of array `e_ident` define class & endianness.

|   Field    | Index In `e_ident[]` | Meaning                         |
| :--------: | :------------------: | ------------------------------- |
| `EI_CLASS` |     `e_ident[4]`     | Address size (32-bit or 64-bit) |
| `EI_DATA`  |     `e_ident[5]`     | Endianness (little or big)      |


### <u>Values Of ELF Class</u>

| `e_ident[EI_CLASS]` |    Value     | Meaning | Typical Architecture      |
| :-----------------: | :----------: | :-----: | ------------------------- |
|       `0x01`        | `ELFCLASS32` | 32-bit  | x86, ARM32                |
|       `0x02`        | `ELFCLASS64` | 64-bit  | x86_64, AArch64, RISC-V64 |


### <u>Values Of ELF Endianness</u>

| `e_ident[EI_DATA]` |     Value     |    Meaning    | Affected Architectures |
| :----------------: | :-----------: | :-----------: | ---------------------- |
|       `0x01`       | `ELFDATA2LSB` | Little Endian | x86, RISC-V, AArch64   |
|       `0x02`       | `ELFDATA2MSB` |  Big Endian   | Some MIPS, PowerPC     |

- **<u>Little endianness</u>:** Least significant byte comes first in memory (reversed).


### <u>Field Sizes & Layout</u>

#### ELFCLASS32:

- Address fields are of **4 bytes** each.
- This includes `e_entry`, `p_vaddr`, and more.

|        Header        | Size (in bytes) |
| :------------------: | :-------------: |
|      ELF header      |       52        |
| Program header table |       32        |
| Section header table |       40        |

#### ELFCLASS64:

- Address fields are of **8 bytes** each.

|        Header        | Size (in bytes) |
| :------------------: | :-------------: |
|      ELF header      |       64        |
| Program header table |       56        |
| Section header table |       64        |


### <u>Checking Class & Endianness</u>

- We can check class & endianness through `readelf -h`.
- Two of the listed details is about class & endianness.


### <u>Assembling E-IDENT</u>

```c
unsigned char e_ident[16] = {
  0x7f, 'E', 'L', 'F',   // Magic number
  0x02,                  // ELFCLASS64 (64-bit)
  0x01,                  // ELFDATA2LSB (little endian)
  0x01,                  // ELF version
  0x00,                  // System V ABI
  ...
};
```


### <u>Mismatch Consequences</u>

| Design Aspect       | Implication                                      |
| ------------------- | ------------------------------------------------ |
| `ELFCLASS` mismatch | Loader will reject the binary.                   |
| Endianness mismatch | You'll get corrupted fields on read.             |
| Cross-compiling     | Must write ELF headers in target class & endian. |
