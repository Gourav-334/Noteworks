# $\fbox{Chapter 5: DYNAMIC LINKING \& LOADERS}$





## **Topic - 1: Role Of Dynamic Loader**

### <u>Introduction</u>

- Dynamic loader in Linux is named as `ld.so` or `ld-linux.so`.
- It is visible to use because it's a user-space binary.
- Kernel loads ELFs with `PT_INTERP` & then executes `ld.so`.


### <u>Transfer Of Control</u>

- ELF binaries contain path to the loader.
- When kernel reads it, it transfers control to the loader.


### <u>Loader Responsibilities</u>

1. To **parse dynamic sections** (`.dynamic`, `.dynsym`, `.rel[a]`, `.got`, `.plt`).
2. To **resolve symbols** after scanning `DT_NEEDED` & loading `.so` when required.
3. To **relocate sections** (like `.got`, `.plt`, `.rel[a]`).
4. **Symbol resolution** - Lazy (`.got` & `.plt`) and eager (`LD_BIND_NOW=1`).
5. To **run initializers** (`.init`, `DT_INIT`, `DT_INIT_ARRAY`).
6. To jump to `main()` section of binary.


### <u>Step-By-Step Flow</u>

1. Kernel maps ELF
2. Kernel notices `PT_INTERP`
3. Kernel loads dynamic interpreter `ld.so`
4. `ld.so` resolves & relocates
5. Finally, kernel jumps to the entry point.


### <u>Involved Files</u>

| File Type        | Path (x86_64)                      |
| ---------------- | ---------------------------------- |
| Dynamic loader   | `/lib64/ld-linux-x86-64.so.2`      |
| Shared libraries | `/lib`, `/lib64`, `/usr/lib`, etc. |
| Target ELF       | Compiled binary & `libc`.          |



## **Topic - 2: Lazy Symbol Resolution (LSR)**

### <u>Purpose</u>

- To support dynamic linking with deferred symbol resolution.
- **<u>Resolution</u>:** Finding actual memory address of symbols (dynamically).
- **<u>Deferred symbol resolution</u>:** Not looking up for symbols until they are used for first time.
- To not resolve external function addresses until called at least once.


### <u>Example Of Working</u>

1. Program calls an external function `foo()`.
2. Function `foo()` calls corresponding stub in `.plt`.
3. Stub in `.plt` carrying symbol info, jumps to dynamic loader resolver.
4. `.so` for `foo()` is loaded to DRAM.
5. Actual address for `foo()` is searched & `.got` is updated accordingly.
6. Now whenever `foo()` is called, function is run from `.so`.


### <u>GOT Table</u>

- `.got` holds address for external functions & global variables.
- Addresses for external functions are resolved at runtime.
- While those for global variables in `.so` are required for dynamic linking.
- By default, `.got` contains empty spaces to store addresses later.


### <u>Benefits Of LSR</u>

- Faster startup, as less symbols are loaded initially.
- Reduced runtime memory usage.



## **Topic - 3: `DT_*` Entries (`readelf -d`)**

### <u>Introduction</u>

- `DT_*` entries are found in `.dynamic` section.
- `ld.so` contains some key-value pairs which - Locate dependencies, resolve symbols, perform relocations & control linking behaviors.


### <u>Structure Layout</u>

- `.dynamic` section can be seen as an array of `Elf64_Dyn` structures.
- Each instance of this structure represents an instruction to loader.

```c
typedef struct {
    int64_t d_tag;            // Type (e.g., DT_NEEDED, DT_INIT)
    union {
        int64_t d_val;        // Value (size, flags)
        int64_t d_ptr;        // Address (e.g., symbol table)
    } d_un;
} Elf64_Dyn;

```


### <u>Common DT_* Tags</u>

| Tag                    | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| `DT_NEEDED`            | Name of required `.so` file                      |
| `DT_RPATH`             | Deprecated, runtime `lib` search path            |
| `DT_RUNPATH`           | Preferred `lib` search path                      |
| `DT_PLTRELSZ`          | Size of PLT relocation entries                   |
| `DT_PLTGOT`            | Address of Global Offset Table for PLT           |
| `DT_SYMTAB`            | Address of dynamic symbol table                  |
| `DT_STRTAB`            | Address of dynamic string table                  |
| `DT_STRSZ`             | Size of `.dynstr` (used with `DT_STRTAB`)        |
| `DT_REL`, `DT_RELSZ`   | Static relocation table & size                   |
| `DT_RELA`, `DT_RELASZ` | Relocation with addends (**64-bit** usually)     |
| `DT_JMPREL`            | Relocations specific to `.plt`                   |
| `DT_INIT`              | Address of initialization function               |
| `DT_FINI`              | Address of termination function                  |
| `DT_FLAGS`             | Runtime flags (e.g. `DF_SYMBOLIC`, `DF_TEXTREL`) |



## **Topic - 4: RPATH v/s RUNPATH**

### <u>Introduction</u>

- `RPATH` & `RUNPATH` are fields in ELF.
- They are searched by dynamic loader to know location of shared libraries.
- This is to search for them during runtime (if required).
- Actually, standard system directories are searched during linking, but `RPATH` & `RUNPATH` provide additional places to look for.


### <u>Places To Define</u>

- These are stored in `.dynamic` section.
- `DT_RPATH` is deprecated version, while `DT_RUNPATH` is modern alternative.
- Both are of `char*` type & point to strings in `.dynstr` section, which represent paths.


### <u>Usage Syntax</u>

#### `RPATH`:

```sh
gcc -Wl,-rpath,/custom/path myprog.c -o myprog
```

- `-Wl` passes flags after it directly to linker.
- Commas split flags/tags before passing them to `ld` (in this case).

#### `RUNPATH`:

```sh
gcc -Wl,--enable-new-dtags -Wl,-rpath,/custom/path myprog.c -o myprog
```

- `--enable-new-dtags` tells linker to use the newer `DT_RUNPATH`.


### <u>Search Order</u>

1. `LD_RUNPATH_PATH` - The environment variable
2. `DT_RUNPATH` - If written by programmer
3. `DT_RPATH` - If written & `RUNPATH` isn't written
4. `/etc/ld.so.cache` - Operated by `ldconfig`
5. Default system paths - `/lib`, `/usr/lib` or `/usr/lib64` etc.


### <u>Deprecation Reasons</u>

- The reason behind `RPATH`'s deprecation is that it gave itself highest priority.
- While `RUNPATH` was introduced to give priority to rest of the options before itself.


### <u>Viewing & Modifying Path</u>

#### `RPATH`:

```sh
readelf -d ./myBin | grep -i path            # View path

patchelf --set-rpath /new/lib ./myBin        # Set/modify path
patchelf --remove-rpath ./binary             # Remove path
```

#### `RUNPATH`:

```sh
objdump -p ./myBin | grep -i path        # View path
```


### <u>Memory-Level View</u>

#### Structure:

```c
{
	d_tag = DT_RUNPATH,
	d_un.d_ptr = 0x0000000000400500
}
```

#### `.dynstr`:

```
/custom/path/to/libs\0
```



## **Topic - 5: Writing Minimal Dynamic Binary**

### <u>Goals/Objectives</u>

- Create a simple dynamically linked ELF executable.
- Use dynamic linking only with `.so` files.
- Trigger runtime loader `ld.so` to run.


### <u>Involved Sections</u>

|  Section   | Purpose                                                     |
| :--------: | ----------------------------------------------------------- |
| `.interp`  | Path to dynamic loader                                      |
| `.dynamic` | Metadata for dynamic linker (relocations, libraries, paths) |
|   `.plt`   | Stub for dynamic calls                                      |
|   `.got`   | Holds addresses of functions/data                           |
| `.dynsym`  | Symbol table for dynamic linking                            |
| `.dynstr`  | Strings for symbol names                                    |

- **Path to dynamic loader -** `/lib64/ld-linux-x86-64.so.2`.


### <u>Example</u>

#### Code:

```gas
.section .data
	msg: .asciz "Hello, World!\n"
	len = .- msg


.section .text
.global _start

_start:
	mov $1, %rax
	mov $1, %rdi
	lea msg(%rip), %rsi
	mov $len, %rdx
	call write@PLT        # Calling 'write' dynamically from GOT.
	
	mov $60, %rax
	xor %rdi, %rdi
	syscall
```

#### Compile & run:

```sh
ld dynelf.s -o dynelf.o

ld dynelf.o -o dynelf \
	-dynamic-linker /lib64/ld-linux-x86-64.so.2 \
	-lc
```

- `-dynamic-linker <PATH>` - Path to dynamic linker.
- `-lc` - Link against `libc` (for `write`).

---
