# $\fbox{SYSTEM PROGRAMMING ROADMAP}$

  
  

  

## I. STATUS ABBREVIATIONS

  

- **C** - Complete
- **I** - Incomplete
- **O** - Ongoing
- **S** - Soon

  
  
  

## II. SUMMARY

  

| Sno. |          Study Area          | Status | Requirement                 |
| :--: | :--------------------------: | :----: | --------------------------- |
|  1   |        C Programming         | **C**  | Making software             |
|  2   |       C++ Programming        | **C**  | Standby skill               |
|  3   | Data Structures & Algorithms | **C**  | Optimization                |
|  4   |       Operating System       | **C**  | Kernel architecture         |
|  5   |        Bash Scripting        | **C**  | Automation                  |
|  6   |       Computer Network       | **C**  | TCP/IP stack                |
|  7   |     Software Engineering     | **C**  | Project management          |
|  8   |       Compiler Design        | **O**  | Command-line projects       |
|  9   |         x86 Assembly         | **I**  | Optimization & hardware     |
|  10  |       Tools/Platforms        | **C**  | Smoother development        |
|  11  |      System-Level Calls      | **O**  | Kernel system calls         |
|  12  |        Device Drivers        | **S**  | Hardware device interaction |
|  13  |    Bare Metal Programming    | **S**  | Vendor specific projects    |

  
  
  
  

## III. STUDY AREAS

  
  

### 1. C Programming (C):

  

| Sno. |      Topic/Chapter      | Status |
| :--: | :---------------------: | :----: |
| 1.1  |    Memory management    |   C    |
| 1.2  |        Pointers         |   C    |
| 1.3  |    String operations    |   C    |
| 1.4  |   Structures & Unions   |   C    |
| 1.5  |     Data structures     |   C    |
| 1.6  |      File handling      |   C    |
| 1.7  | Preprocessor directives |   C    |
| 1.8  |   Linking & Libraries   |   C    |

  
  

### 2. C++ Programming (I):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|2.1|Classes & objects|C|
|2.2|Memory management|C|
|2.3|File handling|C|
|2.4|Vectors|C|
|2.5|Unordered maps|C|
|2.6|Generic|C|
|2.7|Multithreading|C|
|2.8|Smart pointers|C|
|2.9|Lambda expressions|C|

  
  

### 3. Data Structures & Algorithms (C):

  

| Sno. |    Topic/Chapter     | Status |
| :--: | :------------------: | :----: |
| 3.1  | Asymptotic notations |   C    |
| 3.2  | Abstract data types  |   C    |
| 3.3  |  Sorting algorithms  |   C    |
| 3.4  |     Linked lists     |   C    |
| 3.5  |        Trees         |   C    |
| 3.6  |        Graphs        |   C    |
| 3.7  |       Hashing        |   C    |
| 3.8  |    Turing machine    |   C    |

  
  

### 4. Operating System (C):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|4.1|Kernel|C|
|4.2|Process management|C|
|4.3|Threading|C|
|4.4|CPU scheduling|C|
|4.5|Deadlocks|C|
|4.6|Memory management|C|
|4.7|Virtualization|C|
|4.8|I/O systems|C|
|4.9|Disk management|C|

  
  

### 5. Bash Scripting (C):

  

| Sno. |   Topic/Chapter    | Status |
| :--: | :----------------: | :----: |
| 5.1  | Arguments & arrays |   C    |
| 5.2  |     Functions      |   C    |
| 5.3  |       Traps        |   C    |
| 5.4  | Scripting elements |   C    |
| 5.5  |  Base conversions  |   C    |

  
  

### 6. Computer Network (C):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|6.1|Network topologies|C|
|6.2|Networking devices|C|
|6.3|Data link layer|C|
|6.4|Network layer|C|
|6.5|Transport layer|C|
|6.6|Application layer|C|

  
  

### 7. Software Engineering (C):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|7.1|Software development lifecycle|C|
|7.2|COCOMO model|C|
|7.3|Software metrics|C|
|7.4|Project planning|C|
|7.5|Testing & validation|C|

  
  

### 8. Compiler Design (O):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|8.1|Deterministic finite automata|C|
|8.2|Regular expressions|C|
|8.3|Context free grammar|C|
|8.4|Parsing|C|
|8.5|Syntax Directed Translation|C|
|8.6|Code Case Studies||
|8.7|Symbol tables||
|8.8|Storage||
|8.9|Error detection||
|8.10|Code generation||
|8.11|Code optimization||

  
  

### 9. x86 Assembly (O):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|9.1|Family of x86 chips|C|
|9.2|Assembly syntax comparisons||
|9.3|Inline assembly||
|9.4|Bootloading||
|9.5|x86 CPU architecture||

  
  

### 10. Tools/Platforms (I):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|10.1|GCC|C|
|10.2|G++|C|
|10.3|Git|C|
|10.4|GDB/Valgrind|C|
|10.5|Linux|C|
|10.6|CMake|C|

  
  

### 11. System-Level Calls (O):

  

| Sno. |   Topic/Chapter    |      Header       | Status |
| :--: | :----------------: | :---------------: | :----: |
| 1.1  |  Standard library  |   `<stdlib.h>`    |        |
| 1.2  |   UNIX standards   |   `<unistd.h>`    |        |
| 1.3  |    File control    |    `<fcntl.h>`    |        |
| 1.4  |  Singal handling   |   `<signal.h>`    |        |
| 1.5  |   Multithreading   |   `<pthread.h>`   |   C    |
| 1.6  | Socket Programming |    *Multiple*     |   C    |
| 1.7  |   Memory mapping   |  `<sys/mman.h>`   |        |
| 1.8  | Direct system call | `<sys/syscall.h>` |        |



  
  

### 12. Device Drivers (S):

  

|Sno.|Topic/Chapter|Status|
|:---:|:---:|:---:|
|12.1|Running modules||
|12.2|Character drivers||
|12.3|Concurrency & race conditions||
|12.4|Time & delays||
|12.5|Memory allocation||
|12.6|Hardware bridging||
|12.7|Interrupt handling||
|12.8|PCI drivers||
|12.9|USB drivers||
|12.10|Block drivers||
|12.11|Network drivers||
|12.12|TTY drivers||

  
  

### 13. Bare Metal Programming (S):

  

| Sno. |      Topic/Chapter      | Status |
| :--: | :---------------------: | :----: |
| 13.1 | Development environment |        |
| 13.2 |     x86 Bare metal      |        |
| 13.3 |     Booting & setup     |        |
| 13.4 |   Testing & debugging   |        |
| 13.5 |    Shell development    |        |

  
  
  

## IV. Statistics

  
  

### 1. Subject statistics:

  

$$ Subjects\;comepleted\;=\;\frac{8}{13}\;=\;61\% $$

$$ Subjects\;incomeplete\;=\;\frac{1}{13}\;=\;8\% $$

$$ Subjects\;ongoing\;=\;\frac{2}{13}\;=\;15\% $$

$$ Subjects\;coming\;=\;\frac{2}{13}\;=\;15\% $$

  
  

### 2. Topic statistics:

  

$$ Topics\;comepleted\;=\;\frac{64}{98}\;=\;65\% $$

$$ Topics\;incomeplete\;=\;\frac{34}{98}\;=\;34\% $$