# $\fbox{Chapter 1: OBJECT FILES}$





## **Topic - 1: Introduction To Object Files**

### <u>Introduction</u>

- ELF is an object file format.

#### Types of object files:

1. **<u>Relocatable file</u>:** Object file which with other object files can be linked to form an executable.
2. **Executable file**
3. **<u>Shared object file</u>:** Aids other object files to create another object file, or integrates with them and an executable to form single process image.


### <u>File Format</u>

<img src="./media/image1.png" style="width:6in;height:4in" />

- As we can see, an ELF header is compulsory in all object files.
- While sections hold most information like instructions, data, relocation information etc.
- **<u>Program header table</u>:** Tells system how to create a process image i.e. how to execute a program.
- **<u>Section header table</u>:** Contains information about each section.
- Moreover, for each section or segment in diagram, the ordering may vary.


### <u>Data Representation</u>

- Object files support all architectures, from 8-bit to 64-bit.
- This is because its format is machine independent.

| Name            | Size | Alignment | Purpose                  |
| :-------------- | :--: | :-------: | :----------------------- |
| `Elf32_Addr`    |  4   |     4     | Unsigned program address |
| `Elf32_Half`    |  2   |     2     | Unsigned medium integer  |
| `Elf32_Off`     |  4   |     4     | Unsigned file offset     |
| `Elf32_Sword`   |  4   |     4     | Signed large integer     |
| `Elf32_Word`    |  4   |     4     | Unsigned large integer   |
| `unsigned char` |  1   |     1     | Unsigned small integer   |

- These are size of variables using these data types with natural padding.


### <u>Character Representation</u>

- ELF represents characters in 7-bit ASCII form.
- **<u>Multibyte character</u>:** Characters outside range of $[0,127]$ that may occupy multiple bytes.
- Multibyte characters mustn't include any 7-bit pattern than resembles an existing character.
- They must also be self-identifying, meaning they don't change if we insert them among two other characters for example.
- ELF might follow some naming conventions as per processor.



## **Topic - 2: ELF Header**

### <u>Introduction</u>

- Parts of object files may grow or shrink as per condition.

```c
#define EI_NIDENT        16

typedef struct
{
	unsigned char        e_ident[EI_NIDENT];
	Elf32_Half           e_type;
	Elf32_Half           e_machine;
	Elf32_Word           e_version;
	Elf32_Addr           e_entry;
	Elf32_Off            e_phoff;
	Elf32_Off            e_shoff;
	Elf32_Word           e_flags;
	Elf32_Half           e_ehsize;
	Elf32_Half           e_phentsize;
	Elf32_Half           e_phnum;
	Elf32_Half           e_shentsize;
	Elf32_Half           e_shnum;
	Elf32_Half           e_shstrndx;
} Elf32_Ehdr;
```

#### `e_ident`: 

- `e_ident` represents the initial bytes in file identifying it as object file.

#### `e_type`:

- `e_type` tells the type of object file.

| Name        |  Value   | Meaning            |
| :---------- | :------: | :----------------- |
| `ET_NONE`   |   `0`    | No file type       |
| `ET_REL`    |   `1`    | Relocatable file   |
| `ET_EXEC`   |   `2`    | Executable file    |
| `ET_DYN`    |   `3`    | Shared object file |
| `ET_CORE`   |   `4`    | Core file          |
| `ET_LOPROC` | `0xff00` | Processor-specific |
| `ET_HIPROC` | `0xffff` | Processor-specific |

- **<u>Core file</u>:** File whose contents are unspecified.
- While `ET_NONE` is used when the file is specified, but it doesn't fit in any other category.

#### `e_machine`:

- `e_machine` is used to label an object file being compatible with a particular architecture.

| Name             |    Value    | Meaning                 |
| :--------------- | :---------: | :---------------------- |
| `ET_NONE`        |     `0`     | No machine              |
| `EM_M32`         |     `1`     | AT&T WE 32100           |
| `EM_SPARC`       |     `2`     | SPARC                   |
| `EM_386`         |     `3`     | Intel Architecture      |
| `EM_68K`         |     `4`     | Motorola 68000          |
| `EM_88K`         |     `5`     | Motorola 88000          |
| `EM_860`         |     `7`     | Intel 80860             |
| `EM_MIPS`        |     `8`     | MIPS RS3000 Big-Endian  |
| `EM_MIPS_RS4_BE` |    `10`     | MIPS RS4000 Big-Endian  |
| Reserved         | `11` - `16` | Reserved for future use |

- Flags for specific processor uniquely identify themselves by a convention.
- For example, for `EM_XYZ` processor, the widget would be `EM_XYZ_WIDGET`.

#### `e_version`:

- `e_version` tells version of the object file.

| Name         | Value |     Meaning     |
| :----------- | :---: | :-------------: |
| `EV_NONE`    |  `0`  | Invalid version |
| `EV_CURRENT` |  `1`  | Current version |

- `1` is the default value of the object file when created newly.
- Their value can increase as the version goes up.

#### `e_entry`:

- `e_entry` holds value of virtual address where process (object file) would be run.
- If there is no such point, the value must be kept `0`.

#### `e_phoff`:

- `e_phoff` holds value of file's program header table's offset (in bytes).
- If there is no program header table, then its value must be kept `0`.

#### `e_shoff`:

- `e_shoff` holds value of file's section header's offset (in bytes).
- And `0` is there is none.

#### `e_flags`:

- `e_flags` contains flags associated with our object file, which are specific to processor.
- Flags are named in format of `EF_{flag_name}`.

#### `e_ehsize`

- `e_ehsize` contains ELF header's size.

#### `e_phentsize`:

- `e_phentsize` contains size of an entry in program header table.
- Size of each entry is same & thus defined by it alone.

#### `e_phnum`:

- `e_phnum` contains how many entries are there is program header table.
- And holds `0` is there is none.

>**<u>NOTE</u>:**
>`e_phentsize` $\times$ `e_phnum` $=$ Table's size

- Now we know the use of `e_shentsize` & `e_shnum` similarly.

#### `e_shstrndx`:

- ***Section name string table*** contains names of tables in form of string.
- `e_shstrndx` contains index of one of those entries.


### <u>ELF Identification</u>

- Initial few bytes of an object file tell how to interpret the file.
- This specification is independent of the processor.

#### Indexes in `e_ident[]`:

| Name         | Value | Purpose                |
| :----------- | :---: | :--------------------- |
| `EI_MAG0`    |  `0`  | File identification    |
| `EI_MAG1`    |  `1`  | File identification    |
| `EI_MAG2`    |  `2`  | File identification    |
| `EI_MAG3`    |  `3`  | File identification    |
| `EI_CLASS`   |  `4`  | File class             |
| `EI_DATA`    |  `5`  | Data encoding          |
| `EI_VERSION` |  `6`  | File version           |
| `EI_PAD`     |  `7`  | Start of padding bytes |
| `EI_NIDENT`  | `16`  | Size of `e_ident[]`    |

- Each value at these indexes are of 1 byte each.

#### `EI_MAG0` to `EI_MAG3`:

- 4 bytes from `ET_MAG0` to `EI_MAG3` are called **magic number**.
- They identify a file as object file.

| Name      | Value  | Position           |
| :-------- | :----: | ------------------ |
| `ELFMAG0` | `0x7f` | `e_ident[EI_MAG0]` |
| `ELFMAG1` | `'E'`  | `e_ident[EI_MAG1]` |
| `ELFMAG2` | `'L'`  | `e_ident[EI_MAG2]` |
| `ELFMAG3` | `'F'`  | `e_ident[EI_MAG3]` |

#### `EI_CLASS`:

- `EI_CLASS` is index of byte that tells class of object file.

| Name          | Value | Meaning        |
| :------------ | :---: | :------------- |
| `ELFCLASSONE` |  `0`  | Invalid class  |
| `ELFCLASS32`  |  `1`  | 32-bit objects |
| `ELFCLASS64`  |  `2`  | 64-bit objects |

- `ELFCLASS32` is used for machines where file & virtual address spaces can occupy up to 4 GBs.

#### `EI_DATA`:

- Byte at index `EI_DATA` tells the kind of encoding used for processor-specific data in file.

| Name          | Value | Meaning                       |
| :------------ | :---: | :---------------------------- |
| `ELFDATANONE` |  `0`  | Invalid data encoding         |
| `ELFDATA2LSB` |  `1`  | *\*Will be discussed soon...* |
| `ELFDATA2MSB` |  `2`  | *\*Will be discussed soon...* |

- There are more possible values at `EI_DATA` but reserved for future use.

#### `EI_VERSION`:

- Byte at `EI_VERSION` stores version number of ELF header.
- By default, it must be set to `EV_CURRENT` like that in `e_version`.

#### `EI_PADS`:

- Index `EI_PADS` is from where the unused bytes start.
- They are set to `0` by default & are subject to change in future.
- And they must be ignored by object file readers.
