# $\fbox{Chapter 1: AN INTRODUCTION}$





## **Topic - 1: Getting Started**

### <u>General Steps In Programming</u>

- **Write program text**
- **<u>Compile</u>:** Create an executable.
- **<u>Load</u>:** Load required data to memory.
- **Run**
- **Check output**

> **<u>NOTE</u>:**
> Functions in C is like subroutines in Fortran & procedures in Pascal.


### <u>Basic Program Anatomy</u>

```c
#include <stdio.h>

main()
{
	printf("Hello, World\n");
}
```

- Notice that older C compiler accepted `main` function without any return type mentioned.
- Modern C compilers like GCC and Clang however expect a return type to be explicitly mentioned.
- **<u>Character string/ string constant</u>:** Any string between double quotes `" "`.


### <u>Newline Character</u>

- Broken statements like the one given below can generate errors.

```c
printf("Hello, World!
");
```



## **Topic - 2: Variables & Arithmetic Expressions**

### <u>Thermometer Program</u>

- Formula for temperature conversion is as given below.

$$ C = (5/9)(F-32) $$

- **<u>Declaration</u>:** Mentioning name with data type of a variable.

```c
float celc, fahr;
```

- The range of both all data types depends on the particular machine architecture.
- For example, an integer can hold value up to $2^{64}$ in 64-bit architecture computer.


### <u>Format Specification</u>

- Float format specifier `%3.0f` says that the floating point number to be printed must be at least `3` characters wide & `0` fraction digits after decimal point.
- `%6f` just tells to print floating point number in at least `6` digits.
- `%.2f` just tells to print it with `2` fraction digits after decimal point.
- Similarly, we can apply the same to decimals too.
- `%6d` tells a decimal number to print at least `6` characters long.
- We use `%o` for octal & `%%` to print `%` itself.


## **Topic - 3: The `for` Statement**

- The 3rd argument in a `for` statement can be any operation to perform when the loop has to start.



## **Topic - 4: Symbolic Constants**

- Constants defined using `#define` macro are also known as **symbolic constants**.



## **Topic - 5: Character Input & Output**

### <u>Text Stream</u>

- **<u>Text stream</u>:** A stream of characters divided into multiple lines.
- Each line has zero or more characters first, then a newline character at last.


### <u>Single Character Functions</u>

#### `getchar()` function:

```c
c = getchar();
```

- Inputs are taken using either keyboard or files.

#### `putchar()` function:

```c
putchar(c);
```

- Output can be on multiple type of devices, but mostly monitor screens.

---
