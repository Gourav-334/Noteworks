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
