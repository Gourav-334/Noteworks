# $\fbox{Chapter 1: ENVIRONMENT SETUP}$





## **Topic - 1: Clarifying Misconception**

- Linux kernel is not a library.
- If kernel crashes, the machine suffers damage.



## **Topic - 2: User Space v/s Kernel Space**

### <u>User Space</u>

- Doesn't have access to all CPU features.
- Crashing doesn't harm the system.
- Uses ***syscalls*** to send requests to the kernel.


### <u>Kernel Space</u>

- Kernel runs in 0th ring.
- It has direct access to memory, CPU, and hardware.
- Here, device driver acts as a trusted code.



## **Topic - 3: Device Drivers In Linux**

### <u>Definition</u>

- **<u>Linux device driver</u>:** A kernel component that translates generic kernel requests into hardware-specific action.
- A kernel doesn't know or need to know how the device works.
- It is job of a driver to translate them into hardware-specific action.


### <u>Functions Of Kernel</u>

- `read()`
- `write()`
- `interrupt()`
- Power state
- Configuration



## **Topic - 4: Kernel Architecture (Top-View)**

### <u>Layers</u>

```
+---------------------+
| User Applications   |
+---------------------+
| System Calls        |
+---------------------+
| Kernel Core         |
| (MM, Scheduler)     |
+---------------------+
| Device Drivers      |
+---------------------+
| Hardware            |
+---------------------+
```


### <u>Key Idea</u>

- Drivers live within the kernel, and also work from there only.
- They aren't independent of kernel, they depend on it to work.
- The drivers even make use of many of the kernel's frameworks.



## **Topic - 5: Code Entering Kernel**

### <u>Legal Entry Points</u>

- System calls (from user space)
- Interrupts (from hardware)
- Kernel threads
- Module load/unload


### <u>Driver Entry Points</u>

- System call path (read/write/ioctl)
- Interrupt path



## **Topic - 6: Loadable Kernel Modules (LKM)**

### <u>Introduction</u>

- Drivers are mostly separate modules, which don't come built-in inside the kernel.
- They are compiled separately from the kernel.
- They are dynamically linked to kernel symbols & thus loaded at runtime.


### <u>Sample Driver Files</u>

```sh
insmod mydriver.ko
rmmod mydriver
```



## **Topic - 7: Challenges In Kernel Programming**

- No standard C library
- No floating point
- Limited stack
- Forbidden sleeping (as per context)
- Global concurrency

>**<u>NOTE</u>:**
>This forces discipline to the engineers.



## **Topic - 8: Setting Up Kernel Lab**

### <u>Objectives</u>

- Compiler kernels fearlessly
- Load/unload Linux modules
- Debug through logs
- Use QEMU within Ubuntu


### <u>Setup Steps</u>

1. Get **Ubuntu 22.04.x LTS (Desktop)** for kernel stability & proper documentation.
2. Then add the downloaded disk image (`ubuntu-22.04.x-desktop-amd64.iso`) to **VirtualBox**.
3. Configure Ubuntu's disk image as per the table below:

| Category                             | Field               | Set To                |
| :----------------------------------- | :------------------ | :-------------------- |
| **System $\rightarrow$ Motherboard** | RAM                 | 4096-8192 MB          |
|                                      | Boot Order          | Hard disk             |
|                                      | Chipset             | PIIX3                 |
|                                      | EFI                 | Disabled              |
| **System $\rightarrow$ Processor**   | CPUs                | 2-4                   |
| **Display**                          | Video Memory        | 128 MB (max)          |
|                                      | Graphics Controller | VMSVGA                |
| **Storage**                          | Controller          | SATA                  |
|                                      | Disk Type           | VDI                   |
|                                      | Allocation          | Dynamically allocated |
|                                      | Size                | 40 GB (minimum)       |
| **Network**                          | Adapter 1           | NAT                   |
| **General**                          | Clipboard           | Bidirectional         |
|                                      | Drag'n'Drop         | Bidirectional         |
4. Install required kernel development toolchains:
```sh
sudo apt update
sudo apt upgrade -y

sudo apt install -y \
build-essential \                  # For compiler toolchain
linux-headers-$(uname -r) \        # For module building
git \
vim \
gcc \
make \
gdb \
pkg-config \
libncurses-dev \
flex \
bison \
bc \
elfutils \                         # For kernel debugging
dwarves \                          # Also for kernel debugging
qemu-system-x86 \                  # For safely testing kernel
```

5. Verify kernel developmental readiness.
```sh
uname -r
ls /lib/modules/$(uname -r)/build
```

6. Take a snapshot of the current state of VM to rollback on crashes.
7. Make a sanity test:
```sh
cat /proc/version
```

---
