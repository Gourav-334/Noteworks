# $\fbox{Chapter 4: X86 ASSEMBLY AND C}$





## **Topic - 1: `objdump`**

- `objdump` displays info about object files.
- It could be used on executables, archive, and shared objects too.
- For demonstration, let's say we have an executable `hello`.

```sh
objdump -d hello               # '-d' disassembles only '.text' section
objdump hello                  # Defaults to use '-d'
objdump -D hello               # '-D' disassembles all the sections
objdump -d hello | less        # '| less' shows output on scrollable page
objdump -S hello               # Shows source code & disassembly both (if -g used)
```
