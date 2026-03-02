# $\fbox{Chapter 3: ENTERING PROTECTED MODE}$





## **Topic - 1: Benefits Of Protected-Mode**

### <u>Limitations Of Real-Mode</u>

- Real-mode gives $20\;bit$ of address i.e. $1\;MiB$ of address space.
- While modern systems have multiple $GBs$ of RAM and memory-mapped devices.
- Real-mode has unsafe memory, no privilege hierarchy, no multi-tasking, no rings, etc.
- CPU clips size and treats a 32-bit register as 16-bit in real-mode.
- Also, BIOS is slow & varies across vendors.


### <u>Additions In Protected-Mode</u>

- Protected-mode supports $4\;GiB$ address space.
- Is faster than real-mode.
- It has segment descriptors, limit addressing, and access control.
- This solves problems like illegal access & stack overflow.


### <u>Privilege Rings</u>

| Ring | Purpose        |
| ---- | -------------- |
| 0    | Kernel         |
| 3    | User processes |

- Now this enables ring transitions, stack switching, and instruction restrictions.
- **Innovations enabled -** OS design, paging, multitasking, security, etc.
- Also segments are entered to GDT in protected mode.


### <u>Switching Steps</u>

1. Create a GDT
2. Load GDT with `lgdt`
3. Set protection enable (PE) bit in `CR0`
4. Perform a far jump
5. Reload segment registers



## **Topic - 2: A20 Gate Enabling**

### <u>Introduction</u>

- 8086 has $20\;bits$ address bus line which could address $1\;MiB$.
- 80286 and newer processors introduced wider address buses, addressing over $1\;Mib$.
- But to keep newer version compatible, IBM disabled address line 20.
- Now this mechanism is called **A20 gate**.


### <u>A20 Disabling Aftermath</u>

- Disabling A20 gate results in address wrapping around $1\;MiB$.
- **<u>Wrapping</u>:** Starting all over after crossing memory limit.

$$ \text{Physical address = 0xFFFF0 + 0x20 = 0x100010} $$
$$ \text{But wrapping = 0xFFFF0 + 0x20 = 0x00010} $$


### <u>A20 Enabling</u>

- Enabling A20 address line provides access to larger memory.
- Disabled A20 means no page table, incorrect kernel loading, and corrupt memory.


### <u>A20 History</u>

- Earlier A20 have used **keyboard controller (8042)** historically.
- This is not the best way to use A20 gate, but still some modern systems use it.
- But most modern systems provide fast A20 access via I/O port `0x92`.


### <u>A20 Enabling Methods</u>

#### Method 1 - BIOS call:

```nasm
int 15h
mov ax, 2501h
```

- Simple but not reliable.

#### Method 2 - Keyboard controller (8042):

- Communicate with empty buffer of keyboard controller using enabled A20.
- Send command `0xD1` and wait for it.
- Method is slow and works on legacy hardware, but still valid by emulators like QEMU.

#### Method 3 - Fast A20 (port `0x92`):

- When 2nd bit is `0`, read from the port `0x92`.
- After reading, set it to `1` and write it back.
- Faster and simpler, even used in modern QEMU.


### <u>Industrial Standards</u>

- Modern bootloaders are made using fast A20 port.
- But if A20 is not found, 8042 is used.
- Enabling A20 without checking its presence is very hazardous.


### <u>Checking Enabled Status</u>

- If disabled, address `0x000000` and `0x100000` will refer to same address.
- Its critical to check if A20 is enabled at port before using it.


### <u>Minimal Fast A20 Enabling</u>

```nasm
enable_a20:
    inb $0x92, %al         # Read system control port
    orb $0x02, %al         # Set 2nd bit to 1 (A20 enable)
    outb %al, $0x92        # Write back
    ret
```

- Again, this doesn't guarantee successful activation.


### <u>Legacy Justification</u>

- Modern UEFI systems handle A20 automatically.



## **Topic - 3: Global Descriptor Table (GDT)**

### <u>Importance Of GDT</u>

$$ \text{Linear address = Segment base + Offset} $$

- Segment base again tells which set of addresses to focus on.
- And it acts as an index instead, telling which GDT entry to choose.
- GDT entry contains the base, limit, and permissions.


### <u>Conceptual Model</u>

- CPU enforces segment size, access permissions, and privilege levels.
- These are enforced as hardware policy.


### <u>Structure Of GDT Entry</u>

- Each GDT descriptor is of $8\;bytes$.
- We will see each field in GDT on bit-size level.

#### Base (total 32-bits):

- Split into 3 parts: Base 15-0, base 23-16, base 31-24
- Defines base address for linear segment (starting point for entry).
