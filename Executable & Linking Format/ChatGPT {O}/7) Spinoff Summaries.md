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