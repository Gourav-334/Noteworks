# $\fbox{Chapter 5: ANATOMY OF A PROGRAM}$





## **Topic - 1: Executable & Linkable Format**

### <u>Composition</u>

- **<u>ELF header</u>:** Describes file's organization
- **<u>Program header table</u>:** Array of fixed-size structures describing segments of executables.
- **<u>Section header table</u>:** Array of fixed-size structures describing sections of executables.


### <u>Segment & Sections</u>

- **<u>Segment</u>:** Combination of zero or more *sections*.
- **<u>Section</u>:** Contains code, data, or metadata.
- Linkers use sections to build segments.

![ELF Structure](./media/image25.png)


### <u>Later Project</u>

- We will later write a kernel and compile it as ELF using GCC.
- Also we will specify how segments are created and where they are loaded.
- Those will be loaded using linker scripts.



## **Topic - 2: Reference Documents**

```sh
man elf        # ELF manual
```



## **Topic - 3: ELF Header**

### <u>Command</u>

```sh
readelf -h hello
```

```
ELF Header:
    Magic:             7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
    Class:                             ELF64
    Data:                              2’s complement, little endian
    Version:                           1 (current)
    OS/ABI:                            UNIX - System V
    ABI Version:                       0
    Type:                              EXEC (Executable file)
    Machine:                           Advanced Micro Devices X86-64
    Version:                           0x1
    Entry point address:               0x400430
    Start of program headers:          64 (bytes into file)
    Start of section headers:          6648 (bytes into file)
    Flags:                             0x0
    Size of this header:               64 (bytes)
    Size of program headers:           56 (bytes)
    Number of program headers:         9
    Size of section headers:           64 (bytes)
    Number of section headers:         31
    Section header string table index: 28
```


### <u>Magic</u>

```
Magic: 7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
```

| Bytes                     | Description                       |
| :------------------------ | :-------------------------------- |
| `7f 45 4c 46`             | Predefined values                 |
| `02`                      | Information about *Class* field   |
| `01`                      | Information about *Data* field    |
| `01`                      | Information about *Version* field |
| `00`                      | Information about *OS/ABI* field  |
| `00 00 00 00 00 00 00 00` | Unused bytes added for padding    |


### <u>Class</u>

- **<u>Class</u>:** Capacity of a file.

| Value | Description    |
| :---: | :------------- |
|  `0`  | Invalid class  |
|  `1`  | 32-bit objects |
|  `2`  | 64-bit objects |


### <u>Data</u>

- **<u>Data</u>:** Data encoding of the processor-specific data in the object file.

| Value | Description                   |
| :---: | :---------------------------- |
|  `0`  | Invalid data encoding         |
|  `1`  | Little endian, 2's complement |
|  `2`  | Big endian, 2's complement    |


### <u>Version (ELF)</u>

- **<u>Version (ELF)</u>:** ELF header version number.

| Value | Description     |
| :---: | :-------------- |
|  `0`  | Invalid version |
|  `1`  | Current version |


### <u>OS/ABI</u>

- **<u>OS/ABI</u>:** Target OS, was used as padding byte before.
- ABI document lists all the compatible OS.


### <u>Type</u>

- **<u>Type</u>:** Object file type

|  Value   | Description                     |
| :------: | :------------------------------ |
|   `0`    | No file type                    |
|   `1`    | Relocatable file                |
|   `2`    | Executable file                 |
|   `3`    | Shared object file              |
|   `4`    | Core file                       |
| `0xff00` | Processor specific, lower bound |
| `0xffff` | Processor specific, upper bound |

- Basically, values from `0xff00` to `0xffff` are reserved to define additional file types, if processor has such specific to it.


### <u>Version (Object File)</u>

- **<u>Version (object files)</u>:** Version number of current object file.


### <u>Entry Point Address</u>

- **<u>Entry point address</u>:** Address to the start of first instruction to be executed.
- By default, its `main` function where the first instruction is expected.
- But the default function could be configured by specifying it to GCC.


### <u>Start Of Program Header</u>

- **<u>Start of program header</u>:** Number of bytes in ELF before offset of *program header*.
- For example, the program header starts at 65th byte, then *start of program header* will be `64` as there are $64$ bytes before the offset.


### <u>Flags</u>

- **<u>Flags</u>:** The way processor flags need to be set when the program is loaded.
- `0x0` means EFLAG register is set to clear state.


### <u>Number Of Section Headers</u>

- In a section header, the first entry is always an empty section.


### <u>Section Header String Table Index</u>

- **<u>Section header string table index</u>:** The index or the sequence number of *string table* in *section header*.



## **Topic - 4: Section Header Table**

### <u>ELF Conditions To Satisfy</u>

- Every *section* can have just one *section header*.
- A *section header* can have no *section*.
- Every *section* has its contents arranged contiguously, not distributed.
- No content in file is stored at more than one *section*.


### <u>Getting All Headers</u>

```sh
readelf -S hello        # Gets all headers from a object file.
```
