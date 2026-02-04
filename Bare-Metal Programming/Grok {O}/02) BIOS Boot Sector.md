# $\fbox{Chapter 2: BIOS BOOT SECTOR}$





## **Topic - 1: x86 Memory Model & Segmentation**

### <u>CPU At Code Start</u>

- When BIOS jumps to boot sector, it starts using real-mode.
- Maximum addressable memory is of $1\;MiB$.
- There is still no paging, memory safety, or virtual memory.
- Addresses are computed on physical address instead.


### <u>Segmented Addressing Rule</u>

$$ \text{Physical address = (Segment << 4) + Offset} $$

- This rule is compulsory in real-mode computation.
- **Segment registers (16-bit):** `CS`, `DS`, `ES`, `SS`
- **Offset value (16-bit):** `IP`, `SP`, `BP`, `SI`, `DI`, etc


### <u>History Of Segmentation</u>

- Original 8086 had 16-bit registers, required to address more than $64\;KiB$.
- It had a 20-bit long address, where 16-bit is left shifted to 20-bits and then summed with 16-bit offset.
- So yes there is an overlap in addresses, where same address could be produced with different `CS`:`IP` values.


### <u>Usage Of Registers</u>

- `CS`:`IP` combine to tell from where the codes are fetched from.
- BIOS uses this combination to jumping into code.
- Typical boot state has: `CS`=`0x0000` and `IP`= `0x7C00`


### <u>Other Segment Registers</u>

| Segment Register | Name             | Usage                                    |
| :--------------: | :--------------- | :--------------------------------------- |
|       `DS`       | Data segment     | Stores data address.                     |
|       `ES`       | Extended segment | Often used for string operations.        |
|       `SS`       | Stack segment    | Combined with `SP`/`BP` to access stack. |


### <u>Segment Selection Rule</u>

| Instruction          |      Segment Used       |
| :------------------- | :---------------------: |
| Instruction fetching |          `CS`           |
| `mov al, [addr]`     |          `DS`           |
| `mov al, [bx]`       |          `DS`           |
| `mov al, [bp]`       |          `SS`           |
| Stack push/pop       |          `SS`           |
| String ops (`movsb`) | `DS` $\rightarrow$ `ES` |


### <u>Overlapping Segments</u>

#### Example:

- `CS`:`IP` = `0000`:`7C00`
- `IP`:`CS` = `7C00`:`0000`

#### Boot code:

```asm
mov ax, 0x7c00
mov ds, ax
```

- Now `DS` will contain the boot sector code address as offset.
- Everything else accessed will be relative to this address.
- `0x7C00` isn't directly moved to `AX` because earlier 8086 chips had no wire to transfer immediate to segment register directly.


### <u>Real-Mode Address Space</u>

- Starts from `0x00000` & ends at `0xFFFFF` which is equivalent to $1\;MiB$.
- But this address space is divided into 6 key regions.

| Address Range          | Purpose                         |
| ---------------------- | ------------------------------- |
| `0x00000` to `0x003FF` | Interrupt Vector Table (IVT)    |
| `0x00400` to `0x004FF` | BIOS Data Area (BDA)            |
| `0x00500` to `0x07BFF` | Free / scratch                  |
| `0x07C00` to `0x07DFF` | Boot sector                     |
| `0x07E00` to `0x9FFFF` | Free (typical loaders use this) |
| `0xA0000` to `0xFFFFF` | Video ROM, BIOS ROM, devices    |

- These are not strict enforcement, but industrial standards for division, used by hardware.
- Vendors like **Intel** just hardcoded the offset (`0x00000`) and base (`0xFFFFF`).
- It is not advised to overwrite IVT and BDA to avoid undefined machine behavior.


### <u>Boot Code Initialization Rules</u>

1. Disable interrupts (`cli`)
2. Set known segment values (`DS`, `ES`, `SS`)
3. Set a valid stack (`SS`:`SP`)
4. Then proceed with the objective.
