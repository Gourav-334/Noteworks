# $\fbox{Chapter 1: STANDARD LIBRARY}$





## **Topic - 1: Program Termination**

### <u>Introduction</u>

- This whole chapter covers the functionalities in header file `stdlib.h`.


### <u>Abort</u>

#### Declaration:

```c
void abort(void);
```

#### About:

- `abort()` prematurely & abnormally breaks/aborts the program.
- It generates a `SIGABRT` signal which causes the program to terminate.
- Calling `abort()` causes the called resources to not be cleaned up, though modern OSes clean it up, but some boards don't.
- Must be used only in cases of fatal errors like kernel panics.

#### Example:

```c
FILE *fptr = fopen("myDoc.txt", "r");

if (fptr==NULL) {
	fprintf(stderr, "Can't open the file!");
	abort();    // Aborts the program
}

/* This thus won't be executed. */
printf("CPP Reference.");
```


### <u>Exit</u>

#### Declaration:

```c
void exit(int exit_code);
```


#### About:

- Unlike `abort()`, this one conducts normal procedures to exit a process with cleanups.
- Here, functions passed to `atexit()` are called in reverse order when `exit()` is called.
- All streams are flushed & closed.
- Exit code can be `EXIT_SUCCESS`, `EXIT_FAILURE` or custom value.
- `exit()` works just like `abort()` otherwise & instantly terminates the code.

>**<u>NOTE</u>:**
>Using `return` in `main()` or even reaching its end, `exit()` is called to terminate the program.

#### Example:

```c
void func1(void) {printf("Hello");}
void func2(void) {printf("World");}
void func3(void) {printf("Singapore");}

int main(void)
{
	atexit(func1);           // func1 will be second.
	atexit(func2);           // func2 will be first.
	at_quick_exit(func3);    // func3 won't be called.
	
	exit(EXIT_SUCCESS);
	
	return 0;
}
```


### <u>Quick Exit</u>

#### Declaration:

```c
void quick_exit(int exit_code);
```

#### About:

- Function `quick_exit()` causes normal termination of program with partial cleanups.
- Similar to `exit()`, calls functions passed to `at_quick_exit()` in reverse order, but not the ones passed to `atexit()`.
- After calling those registered functions, `_Exit(exit_code)` is called to exit the program.


### <u>Exit - II</u>

#### Declaration:

```c
void _Exit(int exit_code);
```

#### About:

- Similar to `quick_exit()`, not completely cleaning resources, specially the buffer streams.
- Difference is that it doesn't call functions registered to `atexit()` & `at_quick_exit()`.


### <u>At Exit</u>

#### Declaration:

```c
int atexit(void (*func)(void));
```

#### About:

- `atexit()` supports registration of at least 32 functions.

>**<u>NOTE</u>:**
>Never forget to use functions in a smart way to achieve the objectives.


### <u>At Quick Exit</u>

#### Declaration:

```c
int at_quick_exit(void (*func)(void));
```

#### About:

- There is no data race condition when calling `at_quick_exit()` from different thread.
- Like `atexit()`, it supports registration of at least 32 functions.


### <u>Exit Codes</u>

#### Declaration:

```c
#define EXIT_SUCCESS
#define EXIT_FAILURE
```

#### About:

- A success status can be returned using any of `EXIT_SUCCESS` or `0`.
- But that doesn't mean that defined value of `EXIT_SUCCESS` macro is `0`.



## **Topic - 2: Communicating With Environment**

### <u>System</u>

#### Declaration:

```c
int system(const char *command);
```

#### About:

- **<u>Command processor</u>:** A program to process terminal commands.
- Passing a null pointer to `system()` returns error as a non-zero value.
- UNIX terminal command `data +%A` returns day of the week.


### <u>Piping Processes</u>

#### Declaration:

```c
FILE *popen(const char *command, const char *mode);
```

#### About:

- `popen()` is actually part of `stdio.h` header.
- 