# $\fbox{Chapter 7: BINARY CODE TRANSLATION}$





## **Topic - 1: Machine Code & Binary Representation**

### <u>Concept</u>

- There is no delimiters among instructions.
- Instead, CPU decodes instructions as per encoding rules.
- For x86 instructions, their size can range from 1 to 15 bytes.


### <u>Abstracted Terms</u>

- **<u>Operand</u>:** Involved data in an operation. Could be register, immediate, or memory.
- **<u>Immediate</u>:** A literal value in instruction.
- **<u>Displacement</u>:** A memory offset.


### <u>Data Comparison Table</u>

| Assembly Instruction | Encoding (Hex)   | Breakdown                                                                                         |
| :------------------- | :--------------- | :------------------------------------------------------------------------------------------------ |
| `mov eax, 1`         | `B8 01 00 00 00` | `B8` is opcode for `MOV r32, imm32`, `01 00 00 00` is immediate value `1` (in little-endian hex). |
| `int 0x80`           | `CD 80`          | `CD` is opcode for software interrupt, `80` is Linux syscall (`128` in hex).                      |
| `nop`                | `90`             | Single-byte instruction.                                                                          |
| `add eax, ebx`       | `01 D8`          | `01` is opcode for `ADD r/m32, r32`, `D8` is ModR/M `EAX = EAX + EBX` operation.                  |

- Knowing these few breakdowns help in referencing any kind of instruction in future with super ease.


### <u>Pseudo/Memory Representation</u>

```
Address     Bytes          Meaning
0x08048000  B8 01 00 00 00 mov eax, 1
0x08048005  CD 80          int 0x80
```

- The instruction decoder reads the binary code byte-by-byte.