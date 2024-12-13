# $\fbox{Chapter 1: ESSENTIAL CONCEPTS}$





## **Topic - 1: Opening Monologue**

- Text editors, servers, databases are also system software.
- These are system software even though not communicating with the kernel.


## **Topic - 2: System Programming**

### <u>Introduction</u>

- UNIX was a system-level program.
- How much low-level or high-level an application is, depends on which stack it was written at.


### <u>Why Learn It?</u>

- Even though application level software like web apps & high-level language usage is high, someone is required to maintain the low-level compiler they use.


### <u>System Calls</u>

- System programming uses system calls throughout the program.
- Even games use system calls to communicate with hardware.
- Linux uses comparatively less system calls than other kernels.
- All machine architectures have their own system calls.
- But most of them are common among them.
- ***x86-64*** architecture has around 300 system calls.

### <u>Invoking System Calls</u>

- User space applications (not application software) aren't allowed to directly manipulate the kernel code for safety reasons.
- Thus, system calls act as signals to kernel for executing something.
- ***i386*** uses `0x80` interrupt to access kernel space.
- And `0x80` interrupt is handled by the system call handler itself.
- Registers are used to stuff system calls in them as parameters.
- For example, `5` (`open()`) is stuffed in `eax` for opening operation.
- Parameters are passed to `ebx`, `ecx`, `edx`, `esi` & `edi` in order.
- One of these register is used to point at addresses where these parameters have to be kept.


### <u>GNU Compiler Collection</u>

- Modern Linux systems use ***glibc*** (***GNU libc***), a C library.
- GNU's C++ library is ***libstdc++***



## **Topic - 3: APIs & ABIs**

### <u>APIs</u>

- **<u>API</u>:** Any software program that provides a higher-level functionality to another software by abstracting its own code.
