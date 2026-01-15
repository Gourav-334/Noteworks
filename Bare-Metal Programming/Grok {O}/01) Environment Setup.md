# $\fbox{Chapter 1: ENVIRONMENT SETUP}$





## **Topic - 1: Bare-Metal In Industries**

### <u>Definition</u>

- **<u>Good definition</u>:** Software executing directly on hardware without OS.
- **<u>Bad definition</u>:** Writing assembly without any library.


### <u>Hardware Contract</u>

| Component            | What You Are Guaranteed                     |
| -------------------- | ------------------------------------------- |
| CPU                  | Reset state + architecture rules            |
| Firmware (BIOS/UEFI) | Optional, limited services                  |
| RAM                  | Physically present, not logically organized |
| Devices              | Exist, but uninitialized                    |

- This minimal state is called **platform bring-up**.



## **Topic - 2: x86 Boot Process**

### <u>Power-On Reset</u>

#### When CPU powers/resets:

- CPU enters real-mode
- Interrupts are disabled
- Paging is disabled
- Caches are undefined
- Segment registers are in reset state

#### Reset vector/ CPU execution point:

| What             | Where                      |
| :--------------- | :------------------------- |
| CS:IP            | `0xF000:0xFFF0`            |
| Physical address | `0xFFFFFFF0` (modern CPUs) |

- This mapping is not to the RAM.
- Instead it maps to firmware ROM, where the CPU starts.


### <u>Firmware's BIOS Model</u>

1. CPU sanity check
2. POST (Power-On Self Test)
3. Hardware enumeration & detection
4. Boot device selection
5. Bootstrapping first sector

>**<u>NOTE</u>:**
>Firmware disappears after temporary services.


### <u>BIOS Services</u>

- BIOS interacts with hardware using software interrupts.

| Interrupt  | Purpose      |
| :--------: | :----------- |
| `INT 0x10` | Video output |
| `INT 0x13` | Disk I/O     |
| `INT 0x16` | Keyboard     |
| `INT 0x15` | System info  |

#### Interrupt constraints:

- Usable in real-mode only
- Often buggy & inconsistent

>**<u>NOTE</u>:**
>As per industrial standards, it is advised to only use BIOS for bootstrapping, not fully depend.


### <u>Boot Device & Sector Load</u>

1. BIOS selects a boot device.
2. Reads sector `0`.
3. Loads 512 bytes to memory address.
```sh
0x0000:0x7C00
```
4. Checks last two bytes.
```sh
0x55 0xAA
```
5. Jumps to `0x7C00`.
6. Now our code executes here.


### <u>Boot Sector Constraints</u>

- Fit in 512 bytes
- End with signature `0xAA55`
- Executes in real mode
- No memory stack
- No memory map


### <u>Usual Boot Sectors</u>

1. Sets up minimal stack
2. Uses BIOS disk
3. Loads more sectors
4. Transfers control


### <u>OS Handover Models</u>

- Raw bootloader $\rightarrow$ Kernel
- Multiboot loader $\rightarrow$ Kernel
- Firmware $\rightarrow$ OS (UEFI)


### <u>After Entering Kernel</u>

|Aspect|State|
|---|---|
|Mode|32-bit protected mode|
|Paging|Disabled|
|Interrupts|Disabled|
|Stack|Undefined unless set|
|Memory map|Provided (if Multiboot)|
|Devices|Mostly uninitialized|


### <u>Common Failure Points</u>

- Wrong segment assumptions
- Stack misuse
- Overwriting boot code
- Invalid GDT entries
- Jumping without flushing pipeline
- Long dependency on BIOS


### <u>Timeline</u>

$$ \framebox[7cm]{Power On} $$
$$ \downarrow $$
$$ \framebox[7cm]{CPU Reset Vector (ROM)} $$
$$ \downarrow $$
$$ \framebox[7cm]{Firmware (BIOS)} $$
$$ \downarrow $$
$$ \framebox[7cm]{Boot Device Selection} $$
$$ \downarrow $$
$$ \framebox[7cm]{Boot Sector @ 0x7C00} $$
$$ \downarrow $$
$$ \framebox[7cm]{Bootloader} $$
$$ \downarrow $$
$$ \framebox[7cm]{Protected Mode} $$
$$ \downarrow $$
$$ \framebox[7cm]{Kernel Entry} $$



## **Topic - 3: Cross-Compilation Setup**

### <u>Introduction</u>

- **<u>Hosted compiler</u>:** Compilers which produces programs to run on OS.
- **<u>Freestanding compiler</u>:** Compilers which produce programs to run without OS.


### <u>Hosted Environment Assumptions</u>

- OS exists
- C's runtime library `crt0` is present
- Syscalls are available
- Stack, heap & TLS exist


### <u>Freestanding Environment Assumptions</u>

- No OS
- No startup files
- No runtime support


### <u>Target Triples</u>

- **<u>Target triple</u>:** Encodes system expectation in `<architecture>-<vendor>-<system>` format.

| Triple             | Meaning           |
| ------------------ | ----------------- |
| `x86_64-linux-gnu` | Hosted Linux      |
| `i686-elf`         | 32-bit x86, no OS |
| `x86_64-elf`       | 64-bit x86, no OS |


### <u>Required Toolchains</u>

|Tool|Purpose|
|---|---|
|`gcc`|Code generation|
|`as`|Assembly|
|`ld`|Linking & layout|
|`objdump`|Disassembly|
|`readelf`|ELF inspection|
|`nm`|Symbol inspection|


### <u>Flags</u>

#### Compiler flags:

```sh
-ffreestanding              # Assumes there is no host
-fno-builtin                # Prevents libc injection
-fno-stack-protector        # Removes protections
-nostdlib
-nostartfiles
-nodefaultlibs
```

#### Architecture control:

- These control ABI-specific behavior.

```sh
-m32                   # For 32-bit kernel
-mno-red-zone          # Mandatory for x86_64 kernels
-mcmodel=kernel        # Later, for 64-bit
```


### <u>Linker Script</u>

- **<u>Linker script</u>:** A script which defines which files have to be linked.
- Programmer has to explicitly define load address, section placement, entry symbol, and memory regions.

#### Example pseudocode:

```asm
ENTRY(_start)

SECTIONS {
  . = 1M;
  .text : { *(.text*) }
  .rodata : { *(.rodata*) }
  .data : { *(.data*) }
  .bss : { *(.bss*) }
}
```



### <u>Build Steps</u>

1. Build `binutils` for `i686-elf`.
2. Build `gcc` for `i686-elf`.
3. Install into isolated prefix.
4. Add to `PATH`.


### <u>Setting Environment</u>

1. Install pre-requisites.

```sh
sudo apt update
sudo apt install -y \
  build-essential \
  bison \              # Parser generator
  flex \               # Lexer generator
  libgmp3-dev \        # GNU multiple-precision arithmetic lib
  libmpc-dev \         # GNU complex number arithmetic lib
  libmpfr-dev \        # GNU multiple-precision floating point lib
  texinfo \            # Documentation tool for vendor validation
  wget
```

2. Create an isolated toolchain prefix.

```sh
export PREFIX="$HOME/opt/cross"        # Setting new dir "cross" for installation.
export TARGET=i686-elf                 # Setting prefix to control this dir.
export PATH="$PREFIX/bin:$PATH"        # Setting default lookup path at "/bin".
```

3. Build `binutils`

```sh
mkdir -p ~/src && cd ~/src          # Creating dir to work within.
wget https://ftp.gnu.org/gnu/binutils/binutils-2.42.tar.xz
tar -xf binutils-2.42.tar.xz        # Downloading source code (not binary).

mkdir binutils-build && cd binutils-build    # Separating build artifacts.
../binutils-2.42/configure \        # Audits system & creates makefile per that.
  --target=$TARGET \        # Tying target as i686-elf
  --prefix=$PREFIX \        # Tying path as $HOME/opt/cross
  --with-sysroot \          # Enables support for system root dir.
  --disable-nls \           # Disables native language support.
  --disable-werror

make -j$(nproc)        # Parallel build with all CPU cores.
make install           # Copies tools to PATH.
```

4. Build GCC

```sh
cd ~/src
wget https://ftp.gnu.org/gnu/gcc/gcc-13.2.0/gcc-13.2.0.tar.xz
tar -xf gcc-13.2.0.tar.xz        # Downloading GNU source code.

mkdir gcc-build && cd gcc-build
../gcc-13.2.0/configure \
  --target=$TARGET \
  --prefix=$PREFIX \
  --disable-nls \
  --enable-languages=c \
  --without-headers

make -j$(nproc) all-gcc                  # Using just code generator.
make -j$(nproc) all-target-libgcc        # Helping processes
make install-gcc
make install-target-libgcc
```



## **Topic - 4: QEMU, GDB, Makefile**

### <u>QEMU Emulation</u>

- A full system emulator.
- **Emulates -** CPU, RAM, chipset, BIOS, peripherals, etc.
- It doesn't emulate Linux.

```sh
qemu-system-i386 \        # Emulating 32-bit x86 machine.
  -drive file=disk.img,format=raw \
  -boot order=c \         # Boot from disk (not network/CD)
  -no-reboot \            # Don't reboot, just stop on crash
  -no-shutdown
```


### <u>Bare-Metal Debugging</u>

- GDB doesn't debug OS, just the CPU state.
- QEMU has a remote debugging port to connect with GDB.

```sh
-s \        # Freeze CPU at rest.
-S          # Start GDB server on TCP port 1234.
```

- After this, GDB can see registers, memory, and control execution.
- GDB reads symbols from `.elf` files, `.img` file is for booting purpose.


### <u>Minimal Makefile</u>

#### Format:

```make
target: dependencies
	command
```

#### Example:

```sh
all: disk.img        # First target to build on command "make"

boot.o: boot.s
	$(AS) boot.s -o boot.o

kernel.elf: boot.o
	$(LD) -T linker.ld boot.o -o kernel.elf

disk.img: kernel.elf
	dd if=kernel.elf of=disk.img conv=notrunc        # Executable to disk.
```

- `$(AS)` expands to `i686-elf-as`.
- `$(LD)` expands to `i686-elf-ld`.



## **Topic - 5: Empty Bootable Image**

### <u>Required Directory Layout</u>

```sh
baremetal/
├── boot.s           # 16-bit real-mode boot sector
├── linker.ld        # Controls where bytes land
├── Makefile         # Deterministic build
└── build/           # Artifacts (optional, but clean)
```


### <u>Boot Sector</u>

- Code must be in real mode, loaded at `0x7C00`, end with signature `0x55AA`.

```asm
/* boot.s — Minimal boot sector */
.code16
.global _start


_start:
    cli                 // No interrupts yet.

.hang:
    hlt                 // Stop the CPU.
    jmp .hang           // Loop forever


/* Pad to 512 bytes and add boot signature. */
.org 510            // 510 bytes
.word 0xAA55        // Next 2 bytes
```

- `.org` tells assembler that code is starting from address `0x0`.
- **`cli` -** Clear interrupt flag


### <u>Linker Script</u>

```ld
/* linker.ld — absolute control */
ENTRY(_start)

SECTIONS
{
  . = 0x7C00;                # . means current location counter
  .text : { *(.text*) }      # Place everything with '.text' pattern
}
```


### <u>Makefile</u>

```make
AS      := i686-elf-as
LD      := i686-elf-ld

all: disk.img

boot.o: boot.s
	$(AS) boot.s -o boot.o

kernel.elf: boot.o
	$(LD) -T linker.ld boot.o -o kernel.elf

disk.img: kernel.elf
	i686-elf-objcopy -O binary kernel.elf disk.img

clean:
	rm -f boot.o kernel.elf disk.img
```

- `bs=512` & `count=1` means exactly one boot sector with `512` bytes of space.
- `conv=notrunc` avoids accidental truncation to code.
- Now we can `make` and `hexdump` to verify boot signature.


### <u>Running In QEMU</u>

```sh
qemu-system-i386 \
  -drive file=disk.img,format=raw \
  -boot order=c \
  -no-reboot \
  -no-shutdown
```


### <u>Trying Debugging</u>

#### Attaching GDB to QEMU:

```sh
qemu-system-i386 -s -S -drive file=disk.img,format=raw
```

#### GDB commands:

```sh
gdb kernel.elf
```

```gdb
target remote :1234
info registers
```

---
