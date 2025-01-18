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


### <u>Object Files</u>

#### Compilation:

```sh
gcc -c example.c -o example.o
```

- To be done for each file separately.
- Insert `-g` for debugging if required.

#### Linking:

```sh
gcc -o file file1.o file2.o file3.o
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



## **Topic - 5: Archive Files**

### <u>Static Compilation</u>

- Just add the `-static` flag during it.

```sh
gcc -c file.c -o file.o
```


### <u>Compiling Archives</u>

```sh
ar rcs libfile.a file1.o file2.o
```

- In `rcs`, each letter tells different thing.
- `r` - Insert/replace files in archive.
- `c` - Create the archive if it doesn't exist.
- `s` - Add index to archive.
- The name `libfile.a` has prefix `lib` because it is used during linking.
- The same thing goes on with shared object files.


### <u>Linking Archives</u>

```sh
gcc -o program main.c -L. -static -lmath
```

- `program` - Name of the executable we are creating after linking.
- `main.c` - The user file with the `main()` function.
- `-L.` - Tells compiler to search for library to link in same directory.
- `-lmath` - It searches for the file `libmath.a`, omitting `lib`.
- We can write path after `-L` too.



## **Topic - 6: Shared Objects**

### <u>Dynamic Compilation</u>

```sh
gcc -fPIC -c program.c -o program.o
```


### <u>Compiling Shared Objects</u>

```sh
gcc -shared -o libprogram.so program.o
```


### <u>Linking Shared Objects</u>

```sh
gcc -o program main.c -L. -lprogram
```

- We can also link object files to the `program` library.



## **Topic - 7: Conclusion**

### <u>Linking External Library</u>

#### Making library:

$$ \framebox[4cm][c]{Library Source}\xrightarrow{(.a)\;Compilation}\framebox[4cm][c]{Library Objects}\xrightarrow{(.a/.so)\;Compilation}\framebox[4cm][c]{Archive/ Shared} $$

#### Making program:

$$ \framebox[4cm][c]{User Source}\xrightarrow{(.o)\;Compilation}\framebox[4cm][c]{User Objects} $$

#### Linking:

$$ \{\;\framebox[4cm][c]{Archive/ Shared}\xrightarrow{Linking}\framebox[4cm][c]{User Objects}\;\} $$
$$ \downarrow $$
$$ \framebox[4cm][c]{Executable} $$


### <u>Making Huge Application</u>

$$ \framebox[4cm][c]{User Lib Source}\xrightarrow{(.a)\;Compilation}\framebox[4cm][c]{User Lib Objects}\xrightarrow{(.out/.)\;Compilation}\framebox[4cm][c]{Executable} $$

- Its not necessary to produce archive ($.a$) or shared objects ($.so$) when making libraries only for your own program.


### <u>Common Doubts</u>

- Source files ($.c$) can be directly linked, but creating intermediate objects ($.o$) is considered a good practice to avoid complete linking from starting.
- Tools like CMake provide even further selective linking.
- Its best to follow standards to avoid facing any kind of problems.

---
