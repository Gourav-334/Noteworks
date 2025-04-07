# $\fbox{CMAKE}$





## **Topic - 1: Basic Concepts**

- CMake is used for making cross-platform build files.
- It can do the same through user's tool chain, like specific compiler or code editor.
- It supports C, C++, Python & even some other languages.



## **Topic - 2: Stages**

### <u>Configuration</u>

1. Reads build script.
2. Executes build script.
3. Outputs variable cache.


### <u>Generation</u>

4. Runs toolchain specific generator.
5. Reads configuration.
6. Generates build script for target toolchain.


### <u>Build</u>

7. Toolchain or build-system does actual build.



## **Topic - 3: Setup**

- Install package `build-essesntial` which are used in build purposes.
- Also install a code editor, supposedly Visual Studio Code.

```sh
sudo apt install build-essential cmake
```

- Already installed tools will be skipped & only required will be installed.



## **Topic - 4: Using CMake**

### <u>Introduction</u>

- Create a $CMakeLists.txt$ file in project's root directory.
- We write comments in this file like that in Python (`#`).


### <u>Joining External Libraries</u>

- This step is optional, only when we are linking external libraries.
- For example, someone installs **GNU's Readline** library, then its path has to be added.

```txt
include_directories(/usr/include)
link_directories(/usr/lib)
```


### <u>Contents In File</u>

```txt
# Minimum accepted CMake version
cmake_minimum_required(VERSION 3.10)

# Project's name & language
project(myProject C)

# Specify language standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)

# Add the executable
add_executable(program main.c)
```

- For C++, `set()` line will be `set(CMAKE_CXX_STANDARD 17)`, for example.
- For having multiple executable files, we can also write the `add_executable()` line as following.

```txt
add_executable(program
	main.c
	src/utils.c
	src/mathlib.c
	src/file.c
)
```

- Here, `src/` is the path which is not always required to be added.
- Ensure that header files for the used libraries are there.


### <u>Linking External Libraries</u>

```txt
target_link_libraries(myExecutable PRIVATE api1 api2)
```

- This step must be done only if we added path for external libraries that we are using.
- We will later see what `PRIVATE` does, but this is how we link a particular library.
- As per the example given above, expect the libraries to be named `libapi1.a` or `libapi1.so` & `libapi2.a` or `libapi2.so`.
- `myExecutable` is the executable we are creating.
- This process must be done after the ``


### <u>Make Process</u>

```sh
mkdir build
cd build
cmake ..
make
```

- After the `cmake` command, CMake checks what toolchain is used there.
- And as per that, downloads its own files right there.
- `make` command now creates the executable in the $build$ directory.


### <u>Linking Libraries</u>

- Add the following line for linkage of library.

```txt
# Create static library (SHARED for shared)
add_library(utils STATIC utils.c)

# Link libraries mentioned
target_link_libraries(program PRIVATE m utils)
```

- Here in particular, we are linking our program to `-lm` i.e. `math` library.
- And `utils` is `libutils.a` or `libutils.so` (library name), a custom library unlike `math`.
- `PRIVATE` is the scope of linking, where it is not passed to dependents.
- `PUBLIC` passes the linking to dependents.
- `INTERFERE` makes only targets link to it.
- Targets here are other files that depend on that library.



## **Topic - 5: Why CMake?**

- We can use batch or bash files for automation, but CMake files are portable across platforms.
- Same patch can be pulled in another OS & made using CMake in its native environment.
- Moreover, CMake integrates well with many code editors.
- CMake targets specific binaries which has to be changed instead of recompiling every single thing, saving time in big projects.

---
