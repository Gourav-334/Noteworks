# $\fbox{Chapter 1: STANDARD LIBRARY}$





## **Topic - 1: Program Termination**

### <u>Introduction</u>

- This whole chapter covers the functionalities in header file `stdlib.h`.

### <u>Abort</u>

```c
void abort(void);
```

- `abort()` prematurely breaks/aborts the program.
- But it doesn't work if `SIGABRT` is being managed by a signal handler.
- Also, calling `abort()` causes `atexit()` to not execute (if later defined).

```c
FILE *fptr = fopen("myDoc.txt", "r");

if (fptr==NULL) {
	fprintf(stderr, "Can't open the file!");
	abort();    // Aborts the program
}

/* This thus won't be executed. */
printf("CPP Reference.");
```
