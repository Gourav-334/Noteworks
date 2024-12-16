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
- For example, the standard C libraries which are imported through headers.


### <u>ABIs</u>

- **<u>ABI</u>:** Application Binary Interface
- API is about higher level programs, whereas ABI is about lower level binaries.
- APIs on different architectures may have same higher-level code, but different binary results when compiled on them.
- These binaries vary from one architecture to another.
- For example, we use `std::cout` from `<iostream>` in both Intel & ARM architectures, but they are compiled into different binaries.
- Meaning the syntax used in them is same, but not same on the base level.
- They are made differently from scratch on each architecture & OS, to look identical & provide same functionalities.



## **Topic - 4: Standards**

### <u>C Language Standards</u>

- At first, C used ANSI standards but later used standards by ISO.
- C11 came with many features which are available in C++.


### <u>Linux & Standards</u>

- Linux follows POSIX & SUS standards.
- **<u>POSIX</u>:** Portable Operating System Interface
- **<u>SUS</u>:** Single UNIX Specification
- Though it follows POSIX standards, no official certification is gained by it.
- The ***gcc*** and ***g++*** are collectively known as GNU C.
- No matter how old a ***gcc*** version is on a system, it will always comply with newer kernel.
- This is because the syntax of both C & kernel system calls are not changed is newer ***gcc*** versions.
- Linux is registered under using LSB standard.
- **<u>LSB</u>:** Linux Standard Base



## **Topic - 5: Concept Of Linux Programming**

### <u>Files & The Filesystem</u>

- **<u>File descriptor</u>:** A pointer which points to contents of a file.
- This descriptor is unique on each instance of opening a file.
- They are of `int` type & abbreviated as fd.


### <u>Regular Files</u>

- **<u>Regular files</u>:** Data in form of byte stream.
- **<u>Byte stream</u>:** Linear array of data.
- **<u>File position</u>:** Position of fd from file offset (in bytes).
- File position can't be negative & can go beyond the length of file.
- If we go beyond this limit & append bytes somewhere, then the bytes between EOF & append position will be filled with `0`.

#### File size:

- **<u>Length of file</u>:** Number of bytes a file contains.
- **<u>Truncation</u>:** A process to resize a file.
- If truncating decreases a file's size, its bytes are removed from the end.
- Else if it increases its size, then the unassigned bytes are filled with `0`s.
- Maximum file size depends on what data type is used as fd.
- For example, an `int` fd in modern Linux system can of $2^{64}$ bytes max.
- That is, how far a fd can go from file offset at max.

#### Inode:

- Files can be concurrently accessed by multiple processes.
- Files are accessed via their filenames but aren't linked to them in any way.
- Rather, files are referenced by their inode, which is assigned a ino.
- **<u>Inode</u>:** Information Node
- **<u>Ino</u>:** A unique number in the filesystem space.
- Inode stores all file metadata like modification timestamp, owner, file type, file location etc.


### <u>Directories & Links</u>

- Files are mapped with names for user's ease & security purpose.
- By default, we are at the root directory which is denoted by `/`.
- Even directories have inodes.
- When given a directory like `home/myCodes/engine.c`, the kernel goes through each directory one-by-one to access the file.
- The inode contains these hierarchical storage information.

#### Pathnames:

- **<u>Directory resolution</u>:** Accessing a file or directory through a hierarchy of directories.
- It is also known as pathname resolution.
- **<u>Dentry cache</u>:** "Directory entry" cache, used for storing result of recent directory resolution.
- **<u>Absolute pathnames</u>:** Pathname for root directory.
- These are said to be fully qualified.
- **<u>Relative pathnames</u>:** Pathnames other than root directory.
- 