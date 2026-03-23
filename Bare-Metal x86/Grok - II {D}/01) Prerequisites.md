# $\fbox{Chapter 1: PREREQUISITES}$





## **Topic - 1: Digital Operations**

- `<<` and `>>` are also considered as bitwise operations.
- 2's complement gives negative value.

$$ -(3)_{10} = \neg(00000011)_{2} + 1 = (2^{8}-3)_{10} \; \text{[MSB = 1]} $$



## **Topic - 2: Processor & ISA**

- x86 is little-endian, meaning lower bytes first.
- `volatile` is used with inline assembly.
- **Registers:** RAX-R15 (16 GPR), RSP, RIP, RFLAGS
- **Segments:** CS, DS, ES, FS, GS (ignored by long mode)

| RFLAGS Flag Name | Purpose  |
| :--------------: | :------- |
|        CF        | Carry    |
|        ZF        | Zero     |
|        SF        | Sign     |
|        OF        | Overflow |



## **Topic - 3: Tools & Environments**

### <u>GCC</u>

```sh
GCC -ffreestanding -mno-red-zone -mcmodel=kernel
```

- **`ffreestanding` -** Without OS services.
- **`mno-red-zone` -** Disables access to red zone ($128\;bytes$ below RSP).
- **`mcmodel=kernel` -** Memory code model set in kernel space (higher-half memory).


### <u>QEMU</u>

```sh
qemu-system-x86_64 -kernel kernel.bin
qemu-system-x86_64 -fda floppy.img
qemu-system-x86_64 -bios OVMF.fd
```

- **`kernel` -** Load kernel directly.
- **`fda` -** BIOS boots from floppy disk image.
- **`bios OVMF.fd` -** Emulate UEFI system using OVMF
- **`OVMF` -** Open Virtual Machine Firmware


### <u>Debugging</u>

```sh
qemu -s -S
```

- **`s` -** Start GDB server in QEMU.
- **`S` -** Stops CPU immediately after startup.

---
