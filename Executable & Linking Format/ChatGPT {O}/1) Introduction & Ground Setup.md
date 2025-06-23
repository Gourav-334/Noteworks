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
