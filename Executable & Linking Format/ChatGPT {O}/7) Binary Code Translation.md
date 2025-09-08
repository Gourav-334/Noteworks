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


### <u>Memory Representation</u>

```
Address     Bytes          Meaning
0x08048000  B8 01 00 00 00 mov eax, 1
0x08048005  CD 80          int 0x80
```

- The instruction decoder reads a binary code byte-by-byte.
- For example, the representation above shows two instructions.
- For the first instruction i.e. `B8 01 00 00 00`, the decoder knows that there are four more bytes to be read.
- Its equivalent assembly code is shown below.

```gas
section .text
    global _start

_start:
    mov eax, 1        ; load constant into eax
    int 0x80          ; syscall: exit(1)
```



## **Topic - 2: x86 Instruction Set Architecture**

### <u>Parts Of Instructions</u>

| Element           | About                                            |
| :---------------- | :----------------------------------------------- |
| Optional prefixes | For segment override, repeat, operand size, etc. |
| Opcode byte(s)    | Takes about 1-3 bytes.                           |
| ModR/M byte       | If operand has register or memory.               |
| SIB byte          | If complex addressing is required.               |
| Displacement      | If memory offset is required.                    |
| Immediate         | A literal value.                                 |


### <u>Abstracted Terms</u>

#### ModR/M byte:

| Part | Size  | Usage                   |
| :--: | :---: | :---------------------- |
| Mod  | 2-bit | Addressing mode         |
| Reg  | 3-bit | Register operand        |
| R/M  | 3-bit | Memory/register operand |

#### SIB byte:

- Encodes **scale-index base** addressing (complex addressing).
- For example, `[EAX + EBX*4 + 8]`


### <u>Breakdown Examples</u>

#### `mov eax, ebx`:

- **Bytes -** `89 D8`
- `89` means `MOV r/m32, r32`.
- `D8` is a  ModR/M.

$$ \text{Mod = 11 (register)} $$
$$ \text{Reg = 3 (EBX)} $$
$$ \text{R/M = 0 (EAX)} $$

#### `mov eax, [ebx]`:

- **Bytes -** `8B 03`
- `8B` means `MOV r32, r/m32`.
- `03` is a ModR/M.

$$ \text{Mod = 00 (memory)} $$
$$ \text{Reg = 0 (EAX)} $$
$$ \text{R/M = 3 (EBX)} $$

#### `mov [ebx+4], eax`:

- **Bytes -** `89 43 04`
- `89` means `MOV r/m32, r32`.
- `43` is a ModR/M.

$$ \text{Mod = 01 (disp8)} $$
$$ \text{Reg = 0 (EAX)} $$
$$ \text{R/M = 3 (EBX)} $$
$$ \fbox{EAX+4}\;\leftarrow\;\text{EAX}  $$

#### `add eax, 5`:

- **Bytes -** `83 C0 05`
- `83` means `ADD r/m32, imm8`.
- `C0` means ModR/M with EAX.
- `05` is immediate `5`.

---