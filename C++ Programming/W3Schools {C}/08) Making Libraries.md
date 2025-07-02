# $\fbox{Chapter 8: MAKING LIBRARIES}$





## **Topic - 1: C/C++ Libraries**

- The object files work as intermediate between a program and library.
- **<u>Dependency walker</u>:** A tool used for troubleshooting incompatibleness of `.so` files.
- Generally, static files create larger binary files & thus occupies more space.
- In whole library process, `gcc` is used for C files & `g++` is used for C++ files.
- Windows uses `.o` extension for object files.
- Linking is done for running an executable which uses library(s).
- We can remove the including statement importing the library at final stage of project.

>**<u>NOTE</u>:**
>Windows equivalents to `.o`, `.a`, `.so` in Linux are `.obj`, `.lib`, `.dll` respectively.



## **Topic - 2: Static Library Linking**

### <u>Creating</u>

1. Create a source file containing implementations of the library, we can create such multiple files

```cpp
#ifndef MYLIB_CPP_
	#define MYLIB_CPP_

#include <iostream>
#include "mylib.hpp"

void func() {
	std::cout << "func() running!";
}
```

2. Create a header file with only function definitions.

```cpp
#ifdef MYLIB_HPP_
	#define MYLIB_HPP_

#ifdef __cplusplus

extern "C" {void func();}

#endif

#endif
```

3. Compile library file(s) into object files, gotta do this one by one for each `.c` file.

```sh
g++ -c -o mylib.o mylib.cpp
```

4. Create static libraries, for multiple `.obj` files, add all file names in the command in line.

```sh
ar rcs mylib.a mylib.o
```


### <u>Linking</u>

1. Create a user program importing our library.

```cpp
/* user.cpp */

void main() {
	func();
}
```

2. Compile the user program into an object file.

```sh
g++ -c -o user.o user.cpp
```

3. Linking user program to static library, this creates an executable of user program which can be run.

```sh
g++ -o user user.o -L. mylib.a
```


### <u>Things To Consider</u>

- It’s a good practice to add this to ensure compatibility of user’s C/C++ version.

```cpp
#ifdef __cplusplus
```

- Use `extern "C"` for functions and variables (in header files only).
- But don’t use them for class or its members.


### <u>Project Specific</u>

- During testing phase, include with `.cpp` file.
- Then after completing the project, before linking make them `.hpp`.



## **Topic - 3: Linking Shared Files**

### <u>Creating</u>

1. Create a C/C++ file that contains implementations of the library, we can create such multiple files.

```cpp
#ifndef MYLIB_CPP_
	#define MYLIB_CPP_

#include <iostream>
#include "mylib.hpp"

void func() {
	std::cout << "func() running!";
}
```

2. Create a header file with only function definitions.

#### Linux:

```cpp
#ifndef EXAMPLE_HPP
	#define EXAMPLE_HPP

#include <iostream>

#ifdef __GNUC__
	#define EXAMPLE_API __attribute__((visibility("default")))
#else
	#define EXAMPLE_API

#endif

extern int num;
extern EXAMPLE_API void hello();

#endif
```

#### Windows:

```cpp
#ifndef MYLIB_HPP_
	#define MYLIB_HPP_

#ifdef __cplusplus

#ifdef DYNAMIC
	#define LINK __declspec(dllexport)
#else
	#define LINK __declspec(dllimport)
#endif

extern "C" LINK {void func();}

#endif

#endif
```

3. Compile library file(s) into object files, gotta do this one by one for each `.cpp` file.

```sh
g++ -c -o dsa.o dsa.cpp -DSHARED
```

4. Create dynamic/shared libraries, for multiple `.obj` files, add all file names in the command in line.

```sh
g++ -shared -o mylib.so mylib.o
```

### <u>Linking</u>

1. Create a user program importing our library.

```cpp
/* user.cpp */

#include "mylib.hpp"

void main() {
	func();
}
```

2. Compile the user program into an object file.

```sh
g++ -c -o main.o main.cpp
```

3. Linking user program to dynamic library, this creates an executable of user program which can be run.

```sh
g++ -o user user.o -L. -lmylib
```


## **Topic - 4: Library Structure**

### <u>Header File</u>

- Guard macro
- `__cplusplus`
- `__declspec(dllexport/dllimport)` (if dynamic)
- Required standard header files
- Namespaces
- `extern` keyword
- Declaration of functions, structures and global variables (if any)
- Declaration of class’s public members
- Declaration & definition of class’s private members


### <u>Source File</u>

- Guard macro
- Inclusion of header file
- Implementation of declarations in header file
- Scope resolution operator (`::`) for namespace references


### <u>User Program</u>

- Inclusion of source file.

---
