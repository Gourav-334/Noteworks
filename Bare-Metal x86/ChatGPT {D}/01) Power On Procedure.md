# $\fbox{Chapter 1: POWER ON PROCEDURE}$





## **Topic - 1: The CPU Reset State**

### <u>On Reset State</u>

1. CPU starts from a fixed configuration.
2. It fetches first instruction from a fixed address.
3. Avoids undefined behavior.


### <u>Point Of Execution</u>

- After reset, the instruction pointer is set to `CS` and `IP`.
- At start, `CS` is `0xF000` and `IP` is `0xFFF0`, which together form `0xFFFF0`.
- This starting address is called **reset vector**.
- And the reset vector lies in our firmware ROM space, not RAM or disk.


### <u>Top Of Memory</u>

![x86 Memory Map](Bare-Metal%20x86/ChatGPT%20{D}/media/image1.png)

- In the shown diagram, the base of whole region is `0x000FFFF`, while offset for reset vector is at `0x00FFFF0`.
- So, the reset vector is just $16\;bytes$ below the base of real-mode memory.


### <u>About This State</u>

- This is real-mode where only $16-bit$ instructions are valid.
- And interrupts & caches are disabled.
- This compatibility mode was created in 1978.



## **Topic - 2: Firmware BIOS vs UEFI**

### <u>BIOS</u>

![x86 BIOS](Bare-Metal%20x86/ChatGPT%20{D}/media/image2.png)

- **Legacy BIOS** has historically owned the reset vector.
- It runs on 16-bit instructions only, uses software interrupts, loads first $512\;bytes$ from disk, and jumps there.


### <u>UEFI</u>

![UEFI BIOS](image3.jpg)

- UEFI can run in protected or long mode.
- It understands filesystems (FAT), could load executables, and more secured.
- Unlike BIOS which loaded raw sectors, UEFI loads structured programs.



## **Topic - 3: Memory Layout At Boot**

- There are specific memory regions reserved for various programs.
- Like for firmware, MMIO, ACPI table, framebuffer, usable RAM, etc.
- UEFI provides this via `GetMemoryMap()`.



## **Topic - 4: Hands-On Experiment**

### <u>Experiment To Perform</u>

1. Launch QEMU with monitor enabled
2. Break at reset
3. Inspect registers
4. Disassemble at `0xFFFF0`
5. Look for `CS` and `IP` value
6. Then look for mode and first instruction


### <u>Step 1: Install QEMU</u>

```sh
qemu-system-x86_64 --version            # Check if downloaded or not
sudo apt install qemu-system-x86        # Download QEMU for x86
```


### <u>Step 2: Start QEMU In Debug Mode</u>

```sh
qemu-system-x86_64 \
-monitor stdio \            # Monitor console / interactive debugger
-S                          # Stops CPU before 1st instruction executes
```


### <u>Step 3: Inspecting Registers</u>

```sh
info registers        # Shows all register values
```

- `CS` would be `F000` & `RIP` be `FFF0`.

$$ \text{Physical address = CS << 4 + IP} $$
$$ \text{F000 << 4 + FFF0 = F0000 + FFF0 = FFFF0} $$


### <u>Step 4: Inspecting Memory</u>

```sh
xp /10bx 0xffff0        # Shows the memory data at reset vector
```

- `xp` - Examine physical memory
- `10` - Show $10\;bytes$ from chosen address
- `bx` - Display memory as hex bytes


### <u>Step 5: Disassembling Instructions</u>

```sh
xp /10i 0xffff0        # Shows: ljmp $0xf000,$0xe05b
```

- `i` - Instruction
- But this command often fails because QEMU is architecture sensitive.
- This instruction performs a jump somewhere in that firmware.
- Its because `0xffff0` otherwise has just $16\;bytes$ after it, not enough for code to fit.


### <u>Step 6: Continuing Execution</u>

```sh
c           # Letting QEMU continue booting the system
help        # For seeing help/manual
```


### <u>Mental Map</u>

$$ \framebox[6cm]{Power On} $$
$$ \downarrow $$
$$ \framebox[6cm]{CPU Reset} $$
$$ \downarrow $$
$$ \framebox[6cm]{Executes at 0xFFFF0} $$
$$ \downarrow $$
$$ \framebox[6cm]{Firmware Jumps} $$
$$ \downarrow $$
$$ \framebox[6cm]{Firmware Initialization} $$
$$ \downarrow $$
$$ \framebox[6cm]{Bootloader / UEFI} $$
$$ \downarrow $$
$$ \framebox[6cm]{Kernel} $$

---
