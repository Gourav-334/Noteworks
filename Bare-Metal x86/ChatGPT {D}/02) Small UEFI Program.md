# $\fbox{Chapter 2: SMALL UEFI PROGRAM}$





## **Topic - 1: Analyzing Problem**

- How our code runs on firmware before any OS is loaded during startup?
- Earlier, the legacy BIOS loaded first sector (`512`) from chosen disk.
- Now the UEFI works as a small OS, and runs on PE executables.
- PE executable is same one used by Windows.



## **Topic - 2: Booting Program With UEFI**

$$ \framebox[9cm]{Power On} $$
$$ \downarrow $$
$$ \framebox[9cm]{CPU Reset} $$
$$ \downarrow $$
$$ \framebox[9cm]{Firmware Runs} $$
$$ \downarrow $$
$$ \framebox[9cm]{UEFI Boot Manager} $$
$$ \downarrow $$
$$ \framebox[9cm]{Load Executables From EFI Partition} $$
$$ \downarrow $$
$$ \framebox[9cm]{Call Entry Function} $$

>*This loaded executable is called **UEFI application**.*



## **Topic - 3: UEFI Program**

- UEFI application is a concept mostly common to $64-bit$ x86 systems.
- It has a special entry function, looking similar to given code below.

```c
EFI_STATUS EFIAPI efi_main(
	/* The loaded progra, */
    EFI_HANDLE ImageHandle,
    
    /* Console output, boot services, memory map, firmware interfaces */
    EFI_SYSTEM_TABLE *SystemTable
);
```



## **Topic - 4: Getting EFI Libraries**

### <u>Installing Development Package</u>

```sh
sudo apt install gnu-efi
```


### <u>Confirming Correct Installation</u>

```sh
ls /usr/include/efi

# efi.h
# efilib.h
# eficon.h
# efiapi.h
```



## **Topic - 5: Smallest UEFI Program**

```c
#include <efi.h>
#include <efilib.h>

EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable)
{
    InitializeLib(ImageHandle, SystemTable);
    Print(L"Hello from UEFI!\n");
	
    return EFI_SUCCESS;
}
```

- `InitializeLib()` - Connects the program to firmware services like console access, runtime pointers, library helpers, etc. Enables `Print()` to work.
- We used `L` in `Print()` because UEFI uses wide characters.
- **<u>Wide characters</u>:** UTF-16 characters where each character is of 16-bit.



## **Topic - 6: Building Binary**

### <u>Producing PE</u>

- We have to produce PE executables, not ELF.

```sh
x86_64-w64-mingw32                           # Target to produce PE
sudo apt install gcc-mingw-w64-x86-64        # Cross-compiler install
```


### <u>Minimal Build</u>

```sh
x86_64-w64-mingw32-gcc \
    -ffreestanding \                 # Means no OS, so disables 'libc'.
    -nostdlib \                      # Avoids linking standard runtime C.
    -I/usr/include/efi \
    -I/usr/include/efi/x86_64 \
    -L/usr/lib -lefi -lgnuefi \
    -Wl,--subsystem,10 \             # Subsystem = 10 (EFI application)
    hello.c -o BOOTX64.EFI
```

- `Wl` - Tells the compiler driver to pass configurations written next to itself to linker.
- Only configuration written after `Wl` here is `--subsystem,10`.


### <u>File Location</u>

```sh
EFI/BOOT/BOOTX64.EFI        # For FAT32 EFI Partition System
```

- Firmware runs it automatically after finding it.



## **Topic - 7: Experimenting In QEMU**

- We will attach a virtual disk to QEMU this time.

```sh
qemu-system-x86_64 \
-drive \
format=raw, file=ft:rw:esp        # 'esp' is parent target
```

- `esp` as parent target is `esp/EFI/BOOT/BOOTX64.EFI`.
- Now we can simulate our minimal UEFI application.

---
