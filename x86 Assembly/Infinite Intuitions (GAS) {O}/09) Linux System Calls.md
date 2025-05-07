# $\fbox{Chapter 9: LINUX SYSTEM CALLS}$





## **Topic – 1: Introduction To System Calls**

### <u>Definition</u>

- System calls are APIs between the user & kernel.


### <u>Steps</u>

1. Put the system call number in RAX register.
2. Store the argument to system call in the appropriate register.
3. Call the interrupt (`0x80` or `80h`), result is returned in RAX register.



## **Topic – 2: Argument Storage**

- Registers storing arguments of system call are RBX, RCX, RDX, RSI, RDI & RBP.
- For more than six arguments, the memory location of first argument is stored in EBX.



## **Topic – 3: System Call Codes**

### <u>System Exit</u>

```gas
xorl %ebx, %ebx
movl $1, %eax        # sys_exit
```


### <u>System Write</u>

```gas
movl $1, %ebx    # File descriptor (stdout)
movl $4, %eax    # sys_write
```


### <u>System Read</u>

```gas
movl $2, %ebx        # Activate error checking (stderr)
movl $3, %eax        # sys_read
```

>**<u>NOTE</u>:**
>All system calls are listed in `/usr/include/asm/unistd.h`.


### <u>System Call Table</u>

| `%eax` |    Name     | `%ebx`           | `%ecx`         | `%edx`   | `%esx` | `%edi` |
| :----: | :---------: | :--------------- | :------------- | :------- | :----- | :----- |
|   1    | `sys_exit`  | `int`            | -              | -        | -      | -      |
|   2    | `sys_fork`  | `struct pt_regs` | -              | -        | -      | -      |
|   3    | `sys_read`  | `unsigned int`   | `char *`       | `size_t` | -      | -      |
|   4    | `sys_write` | `unsigned int`   | `const char *` | `size_t` | -      | -      |
|   5    | `sys_open`  | `const char *`   | `int`          | `int`    | -      | -      |
|   6    | `sys_close` | `unsigned int`   | -              | -        | -      | -      |



## **Topic – 4: Input Read & Display Program**

>**<u>NOTE</u>:**
>1. It doesn’t matter whether we use single or double inverted commas for character or string.
>2. When we calculate the length, the length isn’t stored anywhere but its memory is referred when it is mentioned.


### <u>Bss Segment</u>

#### 32-bit:

```gas
	.segment .bss
.comm num, 5        # Common symbol of 5 bytes (1 for sign).
```

#### 64-bit:

```gas
	.segment .bss
num: .space 5      # Same code as previous.
```


### <u>Taking Input</u>

```gas
movl $5, %edx
movl $num, %ecx
movl $2, %ebx
movl $3, %eax

int 0x80
```



## **Topic - 5: Register Order & Calling**

### <u>Register Roles</u>

#### 32-bit:

| Register | Role Description             | Note                               |
| :------: | :--------------------------- | :--------------------------------- |
|  `%eax`  | Stores the system call code. | `sys_read`, `sys_write` etc.       |
|  `%ebx`  | Stores the operation mode.   | `stdin`, `stdout` or `stderr` etc. |
|  `%ecx`  | Stores the data.             | -                                  |
|  `%edx`  | Stores size of the data.     | Data is either input or output.    |

- Writing in order is necessary to avoid critical errors & panics.
- In order, we `%eax` or `%rax` has role of storing system call code.
- While rest of the following registers are listed as argument 1, argument 2 etc.
- **32-bit** & **64-bit** assembly differ in transfer of data a lot.

#### 64-bit:

| Register | Role Description             | Note                                                   |
| :------: | :--------------------------- | :----------------------------------------------------- |
|  `%rax`  | Stores the system call code. | `sys_read`, `sys_write` etc.                           |
|  `%rdi`  | Stores the operation mode.   | `stdin`, `stdout` or `stderr` etc.                     |
|  `%rsi`  | Point to address of data.    | Takes help of `%rsi` for calculating relative address. |
|  `%rdx`  | Stores size of the data.     | Data is either input or output.                        |

- While **32-bit** assembly allows direct transfer of data through its name, **64-bit** assembly doesn't.
- **64-bit** assembly requires loading data to registers first.
- Uninitialized data are loaded using `%rip`.

$$ a\;\rightarrow\;Symbol $$
$$ \$a\;\rightarrow\;Address\;of\;symbol $$


### <u>Operation & Call Codes</u>

#### System call code:

|                 |                                                     |                  |                  |
| --------------- | --------------------------------------------------- | ---------------- | ---------------- |
| **System Call** | **Description**                                     | **64-bit (rax)** | **32-bit (eax)** |
| `read`          | Read data from a file descriptor                    | 0                | 3                |
| `write`         | Write data to a file descriptor                     | 1                | 4                |
| `open`          | Open a file                                         | 2                | 5                |
| `close`         | Close a file descriptor                             | 3                | 6                |
| `lseek`         | Reposition file offset                              | 8                | 19               |
| `mmap`          | Map or unmap files or devices into memory           | 9                | 90               |
| `munmap`        | Unmap a previously mapped memory region             | 11               | 91               |
| `exit`          | Terminate the calling process                       | 60               | 1                |
| `getpid`        | Get process identification                          | 39               | 20               |
| `getuid`        | Get user identification                             | 102              | 24               |
| `getgid`        | Get group identification                            | 104              | 47               |
| `brk`           | Change program data segment size                    | 12               | 45               |
| `ioctl`         | Control device-specific operations                  | 16               | 54               |
| `stat`          | Get file status                                     | 4                | 106              |
| `fstat`         | Get file status (by file descriptor)                | 5                | 107              |
| `access`        | Check user's permissions for a file                 | 21               | 33               |
| `pipe`          | Create a pipe                                       | 22               | 42               |
| `dup`           | Duplicate a file descriptor                         | 23               | 41               |
| `dup2`          | Duplicate a file descriptor to a specified one      | 32               | 63               |
| `pause`         | Wait for signal                                     | 29               | 29               |
| `unlink`        | Delete a filename                                   | 87               | 10               |
| `execve`        | Execute a program                                   | 59               | 11               |
| `chdir`         | Change current working directory                    | 80               | 12               |
| `time`          | Get time                                            | 13               | 13               |
| `fork`          | Create a child process                              | 57               | 2                |
| `waitpid`       | Wait for process to change state                    | 26               | 114              |
| `kill`          | Send a signal to a process                          | 62               | 37               |
| `uname`         | Get system name and information                     | 63               | 122              |
| `mprotect`      | Set protection on a region of memory                | 10               | 125              |
| `prctl`         | Process control                                     | 157              | 172              |
| `openat`        | Open a file relative to a directory file descriptor | 257              | 322              |
| `getdents`      | Get directory entries                               | 65               | 141              |
| `getdents64`    | Get directory entries                               | 78               | N/A              |

#### Operation code:

| Code | Operation | Description     |
| :--: | --------- | --------------- |
| `0`  | `stdin`   | Standard input  |
| `1`  | `stdout`  | Standard output |

---
