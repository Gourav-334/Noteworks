# $\fbox{Chapter 2: BOOT PROCESS}$





## **Topic - 1: The Boot Process**

- OS could be booted from any storage device attached to the computer.
- **<u>BIOS</u>:** Collection of software routines loaded from a chip to memory when computer is powered ON.
- It provides auto-detection & basic control over essential computer devices.
- And it conducts some tests on these hardware, specially on memory regarding its working.
- BIOS has no idea about what a file-system is, so instead of loading OS as a file, it reads a specific sector ($512\;bytes$) of memory.
- On disk services this location is - Cylinder 2, Head 3, Sector 5
- **<u>Boot sector</u>:** Cylinder 0, Head 0, Sector 0