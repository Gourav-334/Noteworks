
# Plain:

```
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# Smalltalk (s):

```s
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# General Assembly (asm):

```asm
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# GNU Assembler (gas):

```gas
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# Big S (S):

```S
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```


# GNU:

```gnu
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# Literal assembly (assembly):

```assembly
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```

# NASM:

```nasm
    .section .data

msg:
    .rept 9                # Repeat next given for 9 times
    .byte '*'              # The character
    .endr                  # End repetition

    .section .text
    .globl _start

_start:
    movl    $9, %edx       # Number of bytes to write
    movl    $msg, %ecx     # Address of the message
    movl    %ebx, %eax     # Copy EBX to EAX
    int     $0x80          # Interrupt to terminate (syscall)
```
