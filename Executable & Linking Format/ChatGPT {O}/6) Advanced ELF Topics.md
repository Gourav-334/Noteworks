# $\fbox{Chapter 6: ADVANCED ELF TOPICS}$





## **Topic - 1: Position Independent Executables (PIE)**

### <u>Introduction</u>

- **<u>PIE</u>:** An executable that can be loaded anywhere in the memory, without requiring modification.
- Otherwise, executables are expected to be loaded at a fixed address.
- So, in PIE, loader is allowed to perform ASLR (which is otherwise for `.so` only).
- **<u>ASLR</u>:** Address Space Layout Randomization
- This mitigates a major security vulnerability where malware target a particular address in memory.


### <u>Technical Details</u>

- PIE are linked to `-pie` library & compiled with `-fPIE` flag.
- Uses relative addressing, not absolute addressing.
- Meaning it accesses relative offsets via RIP register.
- PIE takes help from `.got` & `.plt` for symbol resolution.
- And it uses `ET_DYN` as `e_type`, not `ET_EXEC`, like `.so`.

```sh
gcc -fPIE -pie test.c -o test
```


### <u>PIE v/s Shared Object</u>

| Aspect                      | PIE Executable                  | Shared Object (`.so`)           |
| --------------------------- | ------------------------------- | ------------------------------- |
| **Purpose**                 | Position independent executable | Dynamically loadable libraries  |
| **Loadable at any address** | Yes                             | Yes                             |
| **Entry Point**             | `_start`                        | `init` functions, no main entry |
| **Linking**                 | Relocatable, fully linked       | Relocatable, loaded at runtime  |


### <u>Example</u>

- For writing a PIE in assembly, just add the `-pie` flag during linking.
- No need to add `-fPIE` as we did with `gcc`.



## **Topic - 2: Relocation Mechanism Internals**

### <u>Introduction</u>

- **<u>Relocation</u>:** Adjusting addresses in binary files & point to correct runtime location.
- For **static** linking, relocating is done by **linker** (`.o` $\rightarrow$ Single ELF).
- For **dynamic** linking, relocating is done by **loader** (Single ELF $\rightarrow$ Memory).


### <u>Data Structures Involved</u>

#### Symbol table:

- Symbol table contains symbols like functions & variables.
- Each symbol possesses name, type, section, offset, size.

#### Relocation table:

- Contains sections like `.rel.text` & `.rela.text`.
- Related structs are `Elf64_Rel` & `Elf64_Rela`.
- Structs contain `r_offset`, `r_info` & `r_addend`.

#### Global offset table:

- Contains runtime addresses of global symbols.
- Used for lazy/dynamic linking.


### <u>Relocation Entry Fields (RELA)</u>

```c
typedef struct {
	Elf64_Addr r_offset;      // Where to apply relocation
	Elf64_Xword r_info;       // Symbol and type
	Elf64_Sxword r_addend;    // Constant addend (RELA only)
} Elf64_Rela;
```

- In `r_info`, higher bits denote the symbol & lower bits denote type.


### <u>Relocations Types</u>

|   Relocation Type   | Meaning                                       |
| :-----------------: | --------------------------------------------- |
|    `R_X86_64_64`    | Replace with full **64-bit** symbol address   |
|   `R_X86_64_PC32`   | **32-bit** PC-relative address                |
|  `R_X86_64_PLT32`   | Call/jump to symbol in PLT (dynamic call)     |
| `R_X86_64_GOTPCREL` | Offset from RIP to GOT entry                  |
| `R_X86_64_RELATIVE` | Add base address to value (used for PIE, DSO) |

- `R_X86_64_RELATIVE` is used in PIE to relocate data relative to base address.
- And it doesn't require symbol lookup & thus faster.


### <u>Examples</u>

#### Static linking:

```gas
mov foo(%rip), %rax
```

- When this instruction is read, linker resolves address for `foo`.
- And then inserts its address in instruction.

#### Dynamic linking:

- Let's say a symbol is found & its address is not known.
- So, dynamic linker (`ld.so`) will look for it in `.rela.plt` & `.dynsym`.
- For example, `printf` is searched in `libc` & then patched to GOT or PLT.


### <u>Inspecting Relocation</u>

```sh
readelf -r your.o        # Shows relocation entries
objdump -r your.o        # Same with additional symbols
```



## **Topic - 3: Stripping Binaries; What Gets Removed?**

### <u>Purpose</u>

- To reduce file size.
- To obfuscate the binary.
- To prevent reverse engineering.

>**<u>NOTE</u>:**
>**<u>Obfuscating</u>:** Purposely making something more confusing.


### <u>What Gets Removed?</u>

| Removed Section      | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `.symtab`            | Everything in symbol table.                               |
| `.strtab`            | Function or variable names as string.                     |
| `.debug_*`           | All debugging information.                                |
| `.comment`           | Metadata for compiler (e.g. GCC version).                 |
| `.note.*` (optional) | Build notes, OS info, etc. (depending on flags).          |
| `.rel.*` / `.rela.*` | Relocation entries (only in non-PIE, non-final binaries). |


### <u>What Is Retained?</u>

|  Section   | Why it remains            |
| :--------: | ------------------------- |
|  `.text`   | Actual code               |
|  `.data`   | Static data               |
|   `.bss`   | Uninitialized memory      |
| `.rodata`  | Constant data             |
| `.dynsym`  | Dynamic symbol table      |
| `.dynstr`  | Dynamic string table      |
| `.interp`  | Dynamic linker path       |
| `.dynamic` | Dynamic linking info      |
|   `.got`   | Needed for GOT resolution |
|   `.plt`   | Needed for PLT resolution |

- All dynamic sections in table above are required only in dynamic linking/loading.


### <u>Selectively Stripping</u>

```sh
strip --strip-debug           # Remove the debug section only.
strip --strip-unneeded        # Remove everything unrequired during runtime.
```

- In MacOS, `strip -x` removes local symbols but keeps global ones.
