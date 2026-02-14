# $\fbox{Chapter 3: ENTERING PROTECTED MODE}$





## **Topic - 1: Benefits Of Protected-Mode**

### <u>Limitations Of Real-Mode</u>

- Real-mode gives $20\;bit$ of address i.e. $1\;MiB$ of address space.
- While modern systems have multiple $GBs$ of RAM and memory-mapped devices.
- Real-mode has unsafe memory, no privilege hierarchy, no multi-tasking, no rings, etc.
- CPU clips size and treats a 32-bit register as 16-bit in real-mode.
- Also, BIOS is slow & varies across vendors.


### <u>Additions In Protected-Mode</u>

- Protected-mode supports $4\;GiB$ address space.
- Is faster than real-mode.
- It has segment descriptors, limit addressing, and access control.
- This solves problems like illegal access & stack overflow.


### <u>Privilege Rings</u>

| Ring | Purpose        |
| ---- | -------------- |
| 0    | Kernel         |
| 3    | User processes |

- Now this enables ring transitions, stack switching, and instruction restrictions.
- **Innovations enabled -** OS design, paging, multitasking, security, etc.
- Also segments are entered to GDT in protected mode.


### <u>Switching Steps</u>

1. Create a GDT
2. Load GDT with `lgdt`
3. Set protection enable (PE) bit in `CR0`
4. Perform a far jump
5. Reload segment registers
