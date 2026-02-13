# $\fbox{BARE-METAL PROGRAMMING}$





## **Chapter - 1: Environment Setup**

- **Bare-metal software:** Software executing directly on hardware without OS.
- **Firmware:** Bare-metal software which initializes system & provides basic functions.
- **BIOS:** Legacy firmware that boots OS using real mode code, uses interrupts.
- **UEFI:** Modern firmware that boots OS using protected & long mode.
- **Platform bring-up:** Raw hardware without any software on it.
- When CPU resets, interrupts are disabled and caches are undefined.
- **Reset vector:** CPU execution point (`cs:ip` at `0xf000:0xfff0`)
- **Reset address:** `0xfffffff0` (modern CPUs)
- **POST:** Power-On Self Test
- **BIOS steps:** CPU check $\rightarrow$ POST $\rightarrow$ Hardware detection $\rightarrow$ Boot device selection $\rightarrow$ Bootstrapping first section (512 bytes at `0`)
- **Boot signature bytes:** `0x55` & `0xaa` (ending bytes `.word 0xAA55`)
- **Post-boot execution point:** `0x7c00`
- **Kernel entry:** Occurs in protected mode with disabled interrupts.
- **Bootloader:** Program loaded by firmware to initialize kernel into memory.
- **`crt0`:** C library to support runtime execution.
- **Target triplet:** `<arch>-<vendor>-<system>` format
- **Linker script:** Script listing files to be linked.
- **Setup steps:** Install separate `gcc` and `binutils` $\rightarrow$ Edit configuration files in them $\rightarrow$ Add shortcut prefix to path $\rightarrow$ Join toolchain copy dirs with prefix
- **QEMU:** Emulates hardware (not OS).
- **QEMU debug port:** `1234` for GDB (debugs `.elf` files).
- **Bare-metal project structure:** `boot.s`, `linker.ld`, `Makefile`, `build/`
- **`.org`:** Assembler macro to request storing data from `0x0` in order.



## **Chapter - 2: BIOS Boot Sector**

- At boot sector, BIOS uses real-mode with max $1\;MiB$ memory. [1]
- $\text{Physical address = (Segment << 4) + Offset = (CS x 16) + IP}$ [1]
- `CS` = Offset of considered frame of $64\;KiB$ [1]
- `IP` = Address from that $64\;KiB$ frame [1]
- For example, $\text{Address = CS:IP = 0x0000 + 0x7C00 = 0x00007C00}$ [1]
- Earlier 8086 had no wire to transfer immediate value to segment register. [2]
- **Real-mode address space:** $1\;MiB$ (6 regions in `0x00000`-`0xFFFFF`) [2]
- **IVT:** Interrupt Vector Table (`0x00000`-`0x003FF`) [2]
- **BDA:** BIOS Data Area (`0x00400`-`0x004FF`) [2]
- **Booting steps:** Disable interrupts $\rightarrow$ Set segments $\rightarrow$ Set stack $\rightarrow$ Re-enable interrupts $\rightarrow$ Proceed with work [3]
- **BIOS service:** Software interrupt letting firmware take control, returned using `IRET`. [3]
- IVT has 256 entries of $4\;bytes$ each (`{IP_low, IP_high, CS_low, CS_high}`). [3]
- BIOS services fill `CS`:`IP` with IVT entries to use interrupts. [3]
- Every interrupt request must include function number, parameters, and return status. [3]
- **Video services:** Interrupt = `0x10`, Function number = `0x0E` [4]
- Disk is read using function number `0x02`. [4]
- Disks are legacy, nowadays separate drivers are required instead of code. [4]
- BIOS isn't called from protected mode. [5]
- If booting one device fails, BIOS moves to next one. [5]
- **CHS:** Cylinder Head Sector (legacy disk with moving parts) [6]
- CHS code remained same for legacy when SSDs came.
- Boot sector's 4 parts - Boot code (most), disk signature, partition table, and boot signature. [6]
