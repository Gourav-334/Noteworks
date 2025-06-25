# $\fbox{Chapter 1: INTRODUCTION \& GROUND SETUP}$





## **Topic - 1: What Is An ELF Binary?**

### <u>Introduction</u>

- ELF is standard binary format used in UNIX-like OSes.
- It contains machine instructions, symbols, metadata, and more in highly structured format.
- It is structured in such a way that it can be easily processed by the linker, loader & tools like GDB.
- So, ELF is also used for intermediate purposes & not just final executable.


### <u>Types Of ELF Binaries</u>

1. Executables - `a.out`, `ls`, `vim`
2. Object files - `*.o`
3. Shared libraries - `*.so`
4. Core dumps - `core`, `core.pid`


### <u>Terminologies</u>

- **<u>Linkable</u>:** Binary that can be linked with other binaries.
- **<u>Portable executable (PE)</u>:** Windows format for executables.
- Mach-O stands for **Mac Object**.
- PE contains only sections, Mach-O contains only segments, while ELF contains both sections & segments.
- Loader comes into play during runtime.


### <u>Recognizing ELF Files</u>

#### Using `file` command:

- Let's check for `ls` executable's type.

```sh
file /bin/ls

# Output: ELF 64-bit LSB executable, x86-64, ...
```

#### Inspecting first few bytes:

```sh
hexdump -C /bin/ls | head -n 1

# Output: 7f 45 4c 46 ...
```

- Output is ELF magic number i.e. `0x7f` followed by `E`, `L`, `F`.


### <u>Code Insight</u>

```c
int main() {
    write(1, "Hello\n", 6);
    return 0;
}
```

- When we compile this source code into executable, the output contains section `.text`.
- This section is the entry point to the code we wrote.
- The OS loader reads ELF header, maps memory as per that & jumps to `.text` section for execution.



## **Topic - 2: Comparing Binary Formats**

### <u>Why Compare Formats?</u>

- Comparing helps in making portable compilation tool.
- Understand effects of loader & ABI on code execution.


### <u>Comparison Table</u>

|      Feature       | ELF                                                 | PE                                                                 | Mach-O                                                             |
| :----------------: | :-------------------------------------------------- | :----------------------------------------------------------------- | :----------------------------------------------------------------- |
|     OS Family      | Linux, BSD                                          | Windows                                                            | macOS, iOS                                                         |
|  File Extensions   | `.o`, `.so` (but not fixed)                         | `.exe`, `.dll`, `.sys`                                             | `.o`, `.dylib`, `.bundle`                                          |
|      Metadata      | Sections, symbols, notes                            | Import table, export table                                         | Load commands, LC_SEGMENT, LC_MAIN                                 |
|   Linker Output    | Position dependent/ independent executable          | Always relocatable if not flagged                                  | Mostly position independent                                        |
|  Dynamic Linking   | Done via `.plt`, `.got`, `.dynamic`                 | Via IAT (Import Address Table)                                     | Via dynamic loader, `dyld`                                         |
| Signature Support  | No native signing                                   | Requires **Authenticode**                                          | Mandatory to sign code                                             |
| Debug Infor Format | DWARF (standard)                                    | PDB (external component)                                           | DWARF                                                              |
|   First Byte(s)    | `0x7f 45 4C 46`                                     | `MZ PE\0\0`                                                        | `0xFEEDFACE`, `0xCAFEBABE` etc                                     |
|     Tools Used     | `readelf`, `objdump`, `strip`                       | `dumpbin`, `dependencyWalker`                                      | `otool`, `nm`, `codesign`, `lipo`                                  |

- ELF is open-source, highly customizable, clean & modular.
- PE is strictly packed, GUI-driven & heavily tooled.
- Mach-O is developer-centric & security focused.


### <u>Structure Models Comparison</u>

#### ELF:

```out
+-------------------+
| ELF Header        |
| Program Headers   |
| Section Headers   |
| .text, .data, etc |
+-------------------+
```

#### PE:

```exe
+------------------+
| DOS Header (MZ)  |
| PE Header        |
| Section Table    |
| .text, .rdata    |
+------------------+
```

#### Mach-O:

```dylib
+--------------------+
| Mach Header        |
| Load Commands      |
| Segment & Sections |
+--------------------+
```



## **Topic - 3: Toolchain Overview**

### <u>Introduction</u>

- **<u>Toolchain</u>:** Set of tools that convert source code into runnable binary.

$$ \framebox[7cm]{1) Source Code} $$
$$ \downarrow $$
$$ \framebox[7cm]{2) Preprocessor} $$
$$ \downarrow $$
$$ \framebox[7cm]{3) Compiler} $$
$$ \downarrow $$
$$ \framebox[7cm]{4) Assembler} $$
$$ \downarrow $$
$$ \framebox[7cm]{5) Linker} $$
$$ \downarrow $$
$$ \framebox[7cm]{6) Loader} $$
$$ \downarrow $$
$$ \framebox[7cm]{7) Program Runs In Memory} $$


### <u>Phase Descriptions</u>

- **<u>Preprocessor</u>:** Expands directives like headers.
- **<u>Assembler</u>:** Outputs relocatable machine code.
- **<u>Linker</u>:** Resolves symbols, patches addresses & arranges memory layout.
- **<u>Loader</u>:** Parses ELF header in runtime & maps segments to memory before transferring control to entry point.

>**<u>NOTE</u>:**
>Preprocessed syntax of C source files are stored with `.i` extension.


### <u>Sample Demonstration</u>

#### Test code:

```c
/* hello.c */

int main() {
	return 42;
}
```

#### Manual processing:

```sh
gcc -E hello.c -o hello.i        # Preprocessing
gcc -S hello.i -o hello.s        # Compilation
gcc -c hello.s -o hello.o        # Assembly
ld hello.o -o hello              # Linking

readelf -h hello                 # Provides information about file
```

- `-h` in last line stands for **file header** (`--file-header`).
- ELF is not just the final product but something that is used & produced anywhere after assembly.



## **Topic - 4: Required Tools Setup**

### <u>Compilers & Assemblers</u>

|  Tool   | About                            | Install               |
| :-----: | :------------------------------- | :-------------------- |
|  `gcc`  | -                                | -                     |
| `clang` | Alternative to `gcc`, LLVM-based | -                     |
| `nasm`  | -                                | -                     |
|  `as`   | GNU assembler                    | Comes with `binutils` |

- With `clang`, assembly code can be generated using `clang -S`.


### <u>Linker</u>

|  Tool  | About                                           | Install                          |
| :----: | :---------------------------------------------- | :------------------------------- |
|  `ld`  | GNU linker                                      | -                                |
| `gold` | Faster GNU linker                               | `sudo apt install binutils-gold` |
| `lld`  | Alternative to `ld`/`gold` LLVM linker (modern) | `sudo apt install lld`           |


### <u>Binary Inspection Tools</u>

|   Tool    | About                                       | Install               |
| :-------: | :------------------------------------------ | :-------------------- |
| `readelf` | Views ELF headers, symbols & segments       | Comes with `binutils` |
| `objdump` | Disassembles + Views symbols + Dumps header | Comes with `binutils` |
|   `nm`    | Lists symbols in object or ELF files        | Comes with `binutils` |
|  `file`   | Detects file types                          | Pre-installed         |


### <u>Hex & Byte-Level Tools</u>

|      Tool       | About                      | Install                |
| :-------------: | :------------------------- | :--------------------- |
|    `hexdump`    | Displays bytes in hex form | Pre-installed          |
|      `xxd`      | Hexdump & reverse hex      | -                      |
|      `hd`       | Alternative to `hexdump`   | Comes with `coreutils` |
| `bless`, `ghex` | GUI hex editors            | `apt install ghex`     |


### <u>Debuggers & Runtime Tools</u>

|    Tool    | About                     | Install |
| :--------: | :------------------------ | :------ |
|   `gdb`    | Debugger for ELF binaries | -       |
|  `strace`  | Traces system calls       | -       |
|  `ltrace`  | Traces library calls      | -       |
| `valgrind` | Detects memory errors     | -       |


### <u>Binary Editors</u>

|    Tool    | About                                  | Install                     |
| :--------: | :------------------------------------- | :-------------------------- |
| `patchelf` | Changes RPATH or interpreter           | -                           |
| `elfedit`  | Modifies ELF headers                   | `sudo apt install elfutils` |
| `objcopy`  | Extracts sections or strips debug info | Comes with `binutils`       |
|  `strip`   | Remove symbols                         | Comes with `binutils`       |


### <u>Optional Tools</u>

|   Tool    | About                             | Install                                 |
| :-------: | :-------------------------------- | :-------------------------------------- |
|  `qemu`   | Emulates non-native architectures | `sudo apt install qemu-user`            |
|  `lldb`   | LLVM debugger                     | -                                       |
| `radare2` | Reverse engineering toolkit       | -                                       |
| `ghidra`  | Suite for static analysis         | Manually download from Oracle's website |


### <u>Recommended Tools</u>

| **Category**  | **Default** | **Why?**                                      |
| :-----------: | :---------: | --------------------------------------------- |
|   Compiler    |    `gcc`    | Native, predictable ABI for ELF.              |
|   Assembler   |   `nasm`    | Clean Intel syntax, hand assembly friendly.   |
|    Linker     |    `ld`     | Lowest-level control for ELF generation.      |
| Disassembler  |  `objdump`  | Works natively with ELF.                      |
| Binary Reader |  `readelf`  | Deep inspection of ELF-specific fields.       |
|   Debugger    |    `gdb`    | Best for ELF-level source/assembly debugging. |
|   Hex Tool    |    `xxd`    | Cleanest output + reversible.                 |
| Runtime Trace |  `strace`   | Observes how your ELF interacts with kernel.  |
| ELF Modifier  | `patchelf`  | Simple and scriptable.                        |

---
