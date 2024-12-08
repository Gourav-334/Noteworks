# $\fbox{Chapter 1: BINARY SYSTEM}$





## **Topic - 1: Number Base Conversion**

### <u>Octal To Other Systems</u>

#### Octal to hexadecimal:

1. Convert octal to binary.
2. Now convert that binary to hexadecimal.

> **<u>NOTE</u>:**
> Similar approach when converting hexadecimal to octal.



## **Topic - 2: Gray Code**

### <u>Introduction</u>

- Gray code is used for solving sequential errors in digits.
- Also known as **reflected binary code** & **cyclic variable code**.
- Basic idea behind gray code is making change to only one bit when proceeding to next number.


### <u>Steps Involved</u>

1. Write the first digit of the number as it is.

$$ b_{1} \; b_{2} \; b_{3} \; b_{4} \; ... \; b_{n} \; \rightarrow \; b_{1} $$

2. From next digits onward keep XORing the previous & current digit until all are done.

$$ (b_{1}) \; (b_{1} \oplus b_{2}) \; (b_{2} \oplus b_{3}) \; (b_{3} \oplus b_{4}) \; ... \; (b_{n-1} \oplus b_{n}) $$
$$ (g_{1}) \; (g_{2}) \; (g_{3}) \; (g_{4}) \; ... \; (g_{n}) $$
$$ g_{1} \; g_{2} \; g_{3} \; g_{4} \; ... \; g_{n} $$


### <u>Gray Code Table</u>

| Decimal | Binary | Gray |
| :-----: | :----: | :--: |
|    0    |  000   | 000  |
|    1    |  001   | 001  |
|    2    |  010   | 011  |
|    3    |  011   | 010  |
|    4    |  100   | 110  |
|    5    |  101   | 111  |

>**<u>NOTICE</u>**
>Notice how the change is made at only one digit while our series of numbers proceed.
