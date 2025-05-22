# $\fbox{Chapter 13: FILE HANDLING}$





## **Topic - 1: Linux System Calls**

### <u>Open</u>

- Opens & creates file if it doesn't exist.
- System call number is `2`.

#### Arguments:

- `%rdi` - Pathname of file (null-terminated)
- `%rsi` - Access mode flag
- `%rdx` - File permission settings (if newly created)

#### Return:

- On success, returns semi-positive file descriptor.
- On failure/error, returns `-1`.
- Error code in stored in `errno`.


### <u>Read</u>

- System call number is `0`.

#### Arguments:

- `%rdi` - Target file descriptor
- `%rsi` - Address of buffer to load streams
- `%rdx` - Number of bytes to read

#### Return:

- Returns `0` if EOF reached.
- Returns `-1` if error is encountered.


### <u>Write</u>

- System call number is `1`.

#### Arguments:

- `%rdi` - Target file descriptor
- `%rsi` - Address of buffer to write from
- `%rdx` - Number of bytes to write

#### Return:

- Returns number of bytes written on success.
- Returns `-1` on failure/error.


### <u>Close</u>

- System call number is `3`.

#### Arguments:

- `%rdi` - Target file descriptor

#### Return:

- Returns `0` on success.
- Returns `-1` on failure/error.



## **Topic - 2: Access Modes Flags**

- In C, these are stored in `<fcntl.h>`.
- But in assembly, we directly use their system call numbers.

|    Flag    |     System Call Number     | Description                              |
| :--------: | :------------------------: | ---------------------------------------- |
| `O_RDONLY` |            `0`             | -                                        |
| `O_WRONLY` |            `1`             | -                                        |
|  `O_RDWR`  |            `2`             | Both read & write.                       |
| `O_CREAT`  |   `64` (`0100` in octal)   | Create if not existing.                  |
| `O_TRUNC`  |  `512` (`01000` in octal)  | Truncate to zero length (if write mode). |
| `O_APPEND` | `1024` (`020001` in octal) | -                                        |

- Multiple flags can be combined with OR (`|`) operator.



## **Topic - 3: File Permissions**

### <u>Introduction</u>

- Octal codes are used for defining file permissions.


### <u>Permission Codes</u>

| Octal Code |       Owner        |    Group     |    Others    |
| :--------: | :----------------: | :----------: | :----------: |
|   `0644`   |     Read/write     |     Read     |     Read     |
|   `0755`   | Read/write/execute | Read/execute | Read/execute |
|   `0600`   |     Read/write     |    $Nil$     |    $Nil$     |



## **Topic - 4: Example**

### <u>Writing To File</u>

```gas
	.section .data
filename: .string "my_file.txt"
message: .string "Hello, file world!\n"
message_len = . - message



	.section .text
	.global _start

_start:
    # Open the file for writing,
    # create if it doesn't exist,
    # truncate if it does.
    
    movq $2, %rax                # 'open' system call number
    movq $filename, %rdi
    movq $(1 | 64 | 512), %rsi   # O_WRONLY | O_CREAT | O_TRUNC
    movq $0644, %rdx             # Permissions
    syscall

	# Checking for errors
    cmp $0, %rax
    jl error_open               # Custom macro

    movq %rax, %r10              # Save the file descriptor


    # Write the message to the file.
    movq $1, %rax                # 'write' system call number
    movq %r10, %rdi              # File descriptor
    movq $message, %rsi          # Buffer address
    movq $message_len, %rdx      # Number of bytes to write
    syscall

	# Check if all bytes were written.
    cmp $message_len, %rax
    jne error_write


    # Close the file.
    movq $3, %rax                # 'close' system call number
    movq %r10, %rdi              # File descriptor
    syscall

	# Checking for errors
    cmp $0, %rax
    jl error_close


    # Exit successfully
    movq $60, %rax               # exit system call number
    movq $0, %rdi                # exit code 0
    syscall



error_open:
    # Handle 'open' error
    movq $1, %rax                # 'write' system call number
    movq $1, %rdi                # File descriptor for 'stderr'
    movq $error_open_msg, %rsi
    movq $error_open_len, %rdx
    syscall

	# Exit system call number
    movq $60, %rax
    movq $1, %rdi                # Exit code 1 (error)
    syscall



error_write:
    # Handle write error
    movq $1, %rax
    movq $1, %rdi
    movq $error_write_msg, %rsi
    movq $error_write_len, %rdx
    syscall

    movq $60, %rax
    movq $1, %rdi
    syscall



error_close:
    # Handle close error
    movq $1, %rax
    movq $1, %rdi
    movq $error_close_msg, %rsi
    movq $error_close_len, %rdx
    syscall

    movq $60, %rax
    movq $1, %rdi
    syscall



	.section .data
error_open_msg: .string "Error opening file!\n"
error_open_len = . - error_open_msg
error_write_msg: .string "Error writing to file!\n"
error_write_len = . - error_write_msg
error_close_msg: .string "Error closing file!\n"
error_close_len = . - error_close_msg
```

---
