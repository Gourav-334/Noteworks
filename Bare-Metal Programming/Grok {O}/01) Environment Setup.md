# $\fbox{Chapter 1: ENVIRONMENT SETUP}$





## **Topic - 1: Bare-Metal In Industries**

### <u>Definition</u>

- **<u>Good definition</u>:** Software executing directly on hardware without OS.
- **<u>Bad definition</u>:** Writing assembly without any library.


### <u>Hardware Contract</u>

| Component            | What You Are Guaranteed                     |
| -------------------- | ------------------------------------------- |
| CPU                  | Reset state + architecture rules            |
| Firmware (BIOS/UEFI) | Optional, limited services                  |
| RAM                  | Physically present, not logically organized |
| Devices              | Exist, but uninitialized                    |

- This minimal state is called **platform bring-up**.



## **Topic - 2: x86 Boot Process**

