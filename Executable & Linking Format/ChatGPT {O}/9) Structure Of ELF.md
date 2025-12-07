# $\fbox{Chapter 9: STRUCTURE OF ELF}$





## **Topic - 1: ELF File Overview**

### <u>Views</u>

- **<u>Logical/programmer view</u>:** Contains **sections** useful for compilers & linkers.
- For example, `.text`, `.data`, `.bss`, `.rodata`, etc.
- **<u>Runtime/loader view</u>:** Contains **segments** useful for OS loader.
- For example, `LOAD`, `DYNAMIC`, etc.



## **Topic - 2: ELF Header (`Elf64_Ehdr`)**

### <u>Introduction</u>

- **Location -** Start of file (offset `0`)
- **Size -** 64 bytes (for 64-bit ELF)


### <u>Purpose</u>

- Describes file type,
- Architecture,
- Entry point,
- Address to program/section header, etc.


### <u>Important Fields</u>

| Field         | What It Stores?                 |
| :------------ | :------------------------------ |
| `e_ident`     | Magic number, class, endianness |
| `e_type`      | Type of binary                  |
| `e_machine`   | Target CPU architecture         |
| `e_entry`     | Virtual memory address          |
| `e_phoff`     | PHT offset (for loader)         |
| `e_shoff`     | SHT offset (for linker)         |
| `e_flags`     | Processor flags                 |
| `e_ehsize`    | ELF header size                 |
| `e_phentsize` | PHT size                        |
| `e_phnum`     | Total PHT count                 |
| `e_shentsize` | SHT size                        |
| `e_shnum`     | Total SHT count                 |
| `e_shstrndx`  | Section name string table index |



## **Topic - 3: Program Header Table (`Elf64_Phdr`)**

### <u>Introduction</u>

- **Location -** `e_phoff`
- **Purpose -** Guides loader in mapping sections to memory.
- **Entries -** One for each segment


### <u>Important Fields</u>

| Field      | What It Stores?         |
| :--------- | :---------------------- |
| `p_type`   | Type of segment         |
| `p_offset` | PHT offset              |
| `p_vaddr`  | Virtual address offset  |
| `p_paddr`  | Physical address offset |
| `p_filesz` | Segment size            |
| `p_memsz`  | Size in memory          |
| `p_flags`  | Permissions             |
| `p_align`  | Memory alignment        |



## **Topic - 4: Section Header Table (`Elf64_Shdr`)**

### <u>Introduction</u>

- **Location -** `e_shoff`
- **Purpose -** Guides linkers & debuggers in linking & symbol resolution.
- **Entries -** One for each section


### <u>Important Fields</u>

| Field          | What It Stores?               |
| :------------- | :---------------------------- |
| `sh_name`      | Index in section string table |
| `sh_type`      | Type of section               |
| `sh_flags`     | Attributes                    |
| `sh_addr`      | Memory address                |
| `sh_offset`    | SHT offset                    |
| `sh_size`      | Section size                  |
| `sh_link`      | Index of related section      |
| `sh_info`      | Extra info                    |
| `sh_addralign` | Memory alignment              |
| `sh_entsize`   | Entry size                    |



## **Topic - 5: Symbol Table (`Elf64_Sym`)**

### <u>Introduction</u>

- **Used by -** Linker & debugger
- **Significance -** Maps function/variable names to addresses.


### <u>Fields</u>

| Field      | What It Stores?              |
| :--------- | :--------------------------- |
| `st_name`  | Index in symbol string table |
| `st_info`  | Type & binding               |
| `st_other` | Visibility                   |
| `st_shndx` | Section index                |
| `st_value` | Offset of symbol             |
| `st_size`  | Symbol size                  |



## **Topic - 6: Relocation Entries (`Elf64_Rel` / `Elf64_Rela`)**

### <u>Introduction</u>

- **Used by -** Linker to patch address.


### <u>Fields</u>

| Field                  | What It Stores?            |
| :--------------------- | :------------------------- |
| `r_offset`             | Relocation location        |
| `r_info`               | Type of relocation / index |
| `r_addend` (in `Rela`) | Extra offset               |



## **Topic - 7: Dynamic Section (`.dynamic`)**

### <u>Introduction</u>

- **Used by -** Dynamic linker for shared libraries.


### <u>Tags</u>

| Tag                        | Meaning                   |
| :------------------------- | :------------------------ |
| `DT_NEEDED`                | Required shared libraries |
| `DT_PLTRELSZ`, `DT_JMPREL` | PLT relocations           |
| `DT_SYMTAB`, `DT_STRTAB`   | Symbol & string table     |



## **Topic - 8: ELF Binary Organization**

### <u>Sections</u>

- `.data` - Actual file values
- `.bss` - Zero-filled reserved memories
- `.rodata` - Constants


### <u>Quick Visual Layout</u>

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



## **Topic - 9: Relocation Entries**

### <u>Introduction</u>

- Relocation entries are stores in separate sections.
- **Format -** `.rela.<section>` or `.rel.<section>`


### <u>Reference From Headers</u>

- **`sh_link` -** Index of symbol table that contains symbols mentioned in relocation.
- **`sh_info` -** Index of target section where relocations are applied (mostly `.text`).
- `sh_entsize` = `sizeof(Elf64_Rel)` or `sizeof(Elf64_Rela)`.

---
