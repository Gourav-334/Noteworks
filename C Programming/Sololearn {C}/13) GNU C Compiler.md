# $\fbox{Chapter 13: GNU C Compiler}$





## **Topic - 1: Making Libraries**

### <u>Header Files (Static)</u>

- Header file includes variable declarations, function declarations & macro declarations.
- We import all required header files here too.
- It is compulsory to add `extern` keyword before names of variables & good practice to do the same before functions too.

```c
/* example.h */

#ifndef EXAMPLE_H
	#define EXAMPLE_H

#define <stdio.h>

#define MAX_SIZE 256

extern int num;
extern void hello();

#endif
```


### <u>Header Files (Dynamic)</u>

#### Windows:

```c
#ifndef EXAMPLE_H
	#define EXAMPLE_H

#include <stdio.h>


#ifdef _WIN32

	#ifdef EXAMPLE_EXPORT
		#define EXAMPLE_API __declspec(dllexport)
	#else
		#define EXAMPLE_API __declspec(dllimport)
	#endif

#else
	#define EXAMPLE_API

#endif


extern int num;
extern EXAMPLE_API void hello();

#endif
```

#### Linux:

```c
#ifndef EXAMPLE_H
	#define EXAMPLE_H

#include <stdio.h>


#ifdef __GNUC__
	#define EXAMPLE_API __attribute__((visibility("default")))
#else
	#define EXAMPLE_API

#endif


extern int num;
extern EXAMPLE_API void hello();

#endif
```


### <u>Source Files</u>

- Source file imports its corresponding header file.
- All variables must be redeclared in it & assigned value too.

```c
/* example.c */

#include "example.h"

int num = 0;

void hello() {
	printf("Hello, World!");
}
```



## **Topic - 2: Compilation & Linking**

### <u>Compiling Executables Directly</u>

```sh
gcc -o example example.c example2.c example3.c
```


### <u>Compiling Without Linking</u>

```sh
gcc -c example.c
```

- `-c` must always be added when files mentioned don't have main function.


### <u>Object Files (Compilation)</u>

```sh
gcc -c example.c -o example.o
```

- To be done for each file separately.
- Insert `-g` for debugging if required.


### <u>Object Files (Linking)</u>

```sh
gcc -c file1.o file2.o file3.o -o file
```


### <u>Standard Libraries Linking</u>

- Here, `-lm` is for linking standard mathematic library.
- It is compulsory to add some standard libraries like this one.

```sh
gcc -o example example.c -lm
```



## **Topic - 3: Optimization Levels**

- `-O0` means no optimization, which is the default level.
- `-O1` introduces basic optimizations.
- `-O2` makes even more optimizations.
- `-O3` optimizes aggressively with inlining & vectorization.

```sh
gcc -O2 -o example example.c
```


## **Topic - 4: Warnings & Errors**

- We can add `-Werror` & `-Wall` flags during compilation.
- `-Werror` treats all warnings as errors.
- `-Wall` displays all warnings on the terminal screen.

```sh
gcc -Wall -Werror -g -o example example.c
```
