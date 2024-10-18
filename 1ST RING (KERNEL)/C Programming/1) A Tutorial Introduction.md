# A TUTORIAL INTRODUCTION





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

```
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

```
printf("Hello, World!
");
```



## <u>Variables & Arithmetic Expressions</u>

- Formula for temperature conversion is as given below.

$$ C = (5/9)(F-32) $$

- **<u>Declaration</u>:** Mentioning name with data type of a variable.

```
float celc, fahr;
```

- The range of both `int` and `float` depends on the particular machine architecture.
- Means an integer can hold value up to $2^{64}$ in 64-bit architecture computer.
