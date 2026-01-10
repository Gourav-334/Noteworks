# $\fbox{Chapter 2: LINUX KERNEL ARCHITECTURE}$





## **Topic - 1: Kernel Space vs. Userspace**

### <u>Userspace</u>

- Processes have restriction on privileges (ring 3 in x86).
- Hardware aren't accessed directly, but through kernel interface.


### <u>Kernel Space</u>

- Processes have special privileges (ring 0 in x86).
- Can directly access hardware and memory.


### <u>System Calls</u>

- Mode or services through which userspace requests kernel for action.
- For example, `open`, `read`, `write`, `ioctl`, `mmap`, etc.
- Invoked using `syscall` instruction in x86-64 assembly languages.
- Kernel's job is to validate parameters, perform operation, and return result or error.

>**<u>NOTE</u>:**
>Error is returned using `errno`.



## **Topic - 2: Monolithic Design & Kernel Modules**

### <u>Monolithic Design</u>

- Linux is a monolithic kernel.
- **<u>Monolithic kernel</u>:** A kernel where all core components are compiled into single binary.
- These components include scheduler, memory manager, driver, etc.
- This ensures smaller base kernel.


### <u>Loadable Kernel Modules (LKM)</u>

- LKM is a feature that allows drivers to be compiled separately from kernel, and being loaded/unloaded at runtime.
- This is achieved using `insmod`, `modprobe`, `rmmod`, etc.
- So, development becomes easier with dynamic addition of drivers.


### <u>Kernel Configuration</u>

- Makes use of `make menuconfig` and `.config`.
- Turning `CONFIG_MODULES=y` enables module support.
- 