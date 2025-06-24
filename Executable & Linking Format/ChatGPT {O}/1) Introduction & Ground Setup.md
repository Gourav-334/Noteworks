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
