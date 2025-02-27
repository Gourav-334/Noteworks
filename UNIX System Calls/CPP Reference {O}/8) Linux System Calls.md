# $\fbox{Chapter 8: LINUX SYSTEM CALLS}$





## **Topic - 1: System Call Functions**

### <u>Introduction</u>

- This chapter is regarding functionalities provided in `<sys/syscall.h>` header.


### <u>System Calls</u>

#### Declaration:

```c
long syscall(long number, ...);
```

- `number` - System call number
- `...` - Rest of the arguments to system call (if any)

#### About:

- Used for gaining even lower of access to operating system, even below **glibc**.
- Often used in sandboxing & security.
- `number` is found in `/usr/include/asm/unistd_64.h` or in `/usr/include/x86_64-linux-gnu/asm/unistd_64.h`.

#### Example:

```c
/* Getting process ID using 'syscall()' */

pid_t pid = syscall(SYS_getpid);    // Instead of 'getpid()'.


/* Printing 'Hello, World!' without 'write()' */

const char msg[] = "Hello, World!\n";
syscall(SYS_write, STDOUT_FILENO, msg, sizeof(msg)-1);
```



## **Topic - 2: Frequently Asked Questions**

### <u>Why Use This Instead Normal Functions?</u>

- It is useful in environment where **glibc** isn't available.
- Avoids overhead that **libc** wrappers carry.
- Access to special system calls like `gettid()` & `clone()`.
- Used in **seccomp** filters, which restricts the set of system calls that can be used by processes.


### <u>When glibc Might Not Be Available?</u>

- Bootloaders that require minimalist compilers.
- Compilation of small binaries that don't require **glibc**.
- Embedded systems & minimalist environments which are scarce of resources.
- Unikernels which require high performance with full POSIX support.
- Security sandboxing & isolation
- Writing system software which can run on **0th ring**.


### <u>When To Avoid glibc?</u>

- When having size constraints, use ***musl*** or ***uClibc*** instead.
- When having strong security requirements, use ***seccomp*** instead.
- When having high performance requirements, use `syscall()` instead.
- When programming or maintaining a kernel, **glibc** isn't available in kernel space.

---
