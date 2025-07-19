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



## **Topic - 4: Symbol Versioning**

### <u>Introduction</u>

- ***Symbol versioning*** is performed to maintain backward compatibility.
- Done when updates are being made to symbols, but older ones still need to run.
- Basically, newer & older functions coexist together after so.
- Primarily done in shared libraries.


### <u>Motivations & Problems</u>

- Symbol versioning helps in older programs still running on legacy library.
- So, linker & loader can clearly distinguish among these versions.


### <u>Version Indexes</u>

- In `.dynsym`, every symbol is assigned a version index.
- For example, `0` means **no version**, `1` means **local symbol**, and more.


### <u>Symbol Versioning Sections</u>

|   Section Name   | Description                                                   |
| :--------------: | :------------------------------------------------------------ |
|  `.gnu.version`  | Contains mapping of each dynamic symbols with their versions. |
| `.gnu_version_r` | Lists required versions from dependency shared objects.       |
| `.gnu_version_d` | Describes supported versions by the shared object.            |


### <u>Version Scripts</u>

- **<u>Version scripts</u>:** Scripts used to assign symbols their respective version names.
- This script is saved with `.map` extension.
- It also defines scope & visibility of its symbols.

```map
VER_1.0 {
	global:
	    foo;
	
	local:
	    *;
};


VER_2.0 {
	global:
	    foo@@VER_1.0;        // foo is aliased to version 1.0
	    bar;
};
```


### <u>Dynamic Linker Behavior</u>

- `ld.so` matches mentioned symbols with correct version.
- This is done by looking up at which version of symbol the binary was linked with.


### <u>Inspecting Symbol Versions</u>

```sh
readelf --symbols --wide --use-dynamic yourlib.so
readelf --version-info yourlib.so
objdump -T yourlib.so
```



## **Topic - 5: Thread Local Storage (TLS)**

### <u>Introduction</u>

- **<u>TLS</u>:** A feature that lets each thread have its own instance/copy for variables.
- This ensures safety as shared global data is dangerous due to race conditions.
- Also there is no requirement of synchronization due to unshared common data.
- The local instances of variables made through TLS act as global, but isolated.
- Alternative to using TLS are mutexes guarding each global variable.


### <u>Code Example</u>

```c
__thread int tls_var = 42;             // Older GCC version
_Thread_local int tls_var = 42;        // GCC C11+
```

- Each thread will get a copy of `tls_var`.


### <u>TLS Sections</u>

- In PHT, TLS sections are marked with `PT_TLS`.

|      Section       | Purpose                            |
| :----------------: | ---------------------------------- |
|      `.tdata`      | Initialized TLS data               |
|      `.tbss`       | Uninitialized TLS data             |
| `.init_array`, etc | Used during dynamic TLS allocation |


### <u>Thread Pointer</u>

- TLS variables are accessed relative to **thread pointer**.
- Thread pointer's location depends on the OS & architecture.
- `x86_64` uses `%fs` or `%gs` base register.
- While ARM uses dedicated register `TPIDR_EL0`.


### <u>TLS Access Models</u>

- TLS access models are used by compilers.
- In GCC, a model is picked as per context of linking & optimization level.

|Model|Description|Use Case|
|---|---|---|
|**Local Exec**|Direct access if TLS is known at link time|Static, fastest|
|**Initial Exec**|Access via GOT if linked to dynamic but loaded early|Efficient fallback|
|**General Dynamic**|Access via `__tls_get_addr` via PLT|Fully dynamic TLS|
|**Local Dynamic**|Optimized dynamic access within one module|Modern compromise|


### <u>Inspecting TLS</u>

```sh
readelf -l your_binary | grep TLS                  # Check present TLS segments
readelf -S your_binary | grep '\.tdata\|\.tbss'    # Check symbols in TLL section
objdump -x your_binary | grep TLS                  # See usage of TLS
```


### <u>Real Application Usage</u>

- `errno`
- Thread-specific caches
- Logging buffers



## **Topic - 6: Binary Layout Differences**

### <u>Introduction</u>

- We will learn about binary layout differences between static & dynamic linking.
- **<u>Dynamic linking</u>:** Only references are stored as `.so` & loaded at runtime.


### <u>Structural Differences</u>

| Aspect                    | Static Linking                          | Dynamic Linking                      |
| ------------------------- | --------------------------------------- | ------------------------------------ |
| **ELF Type**              | `ET_EXEC`                               | `ET_DYN` (PIE), `ET_EXEC` (non-PIE)  |
| **Symbol Table**          | Usually stripped, no unresolved symbols | Contains unresolved dynamic symbols  |
| **`.dynsym` / `.dynstr`** | Absent                                  | Present                              |
| **`.got` / `.plt`**       | Absent                                  | Present                              |
| **Relocation Sections**   | Resolved at link-time, then discarded   | Present (`.rela.plt`, `.rela.dyn`)   |
| **`.interp` Section**     | Not needed                              | Required (points to dynamic linker)  |
| **Shared Libs Needed**    | No                                      | Yes (`NEEDED` entries in `.dynamic`) |
| **Startup Time**          | Faster                                  | Slower (runtime symbol resolution)   |
| **Binary Size**           | Larger                                  | Smaller                              |
| **Memory Sharing**        | No                                      | Yes (shared `.so` mapped by OS)      |
| **Behavior**              | Predictable                             | Unpredictable                        |
| **Versioning**            | Equal among symbols                     | Versioning hell                      |
| **Updating**              | Easier to update                        | Difficult to update                  |

- Static files are self-contained, so they don't require GOT or PLT.
- Archive (`.a`) files are just bundle of `.o` files, nothing else.

>**<u>NOTE</u>:**
>1. `PT_INTERP` points to `/lib64/ld-linux-x86-64.so.2`.
>2. `PT_LOAD` & `PT_GNU_RELRO` are used for protecting memory.


### <u>Both Compilations</u>

```sh
gcc -static -o static_bin test.c        # Contains '-static' flag.
gcc -o dyn_bin test.c                   # No special flag required.
```

---
