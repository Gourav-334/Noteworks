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

