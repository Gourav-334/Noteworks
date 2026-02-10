# $\fbox{C PROGRAMMING}$





## **Topic - 1: Standard I/O**

```c
/* Character I/O */
char c = getchar();
putchar(c);

/* String I/O (unsafe) */
gets(str);
puts(str);

/* String I/O (safe) */
fgets(str, 20, stdin);
fputs(str, stdout);

/* Multiple inputs */
scanf("%d %f %c", &num, &fl, &ch);
```

- Boolean expressions are evaluated left to right.



## **Topic - 2: Pointers**

- **Indirection/dereference operator:** `*`
- **Dereferencing:** Checking what pointer is pointing to.

```c
/* Using pointer as function */
ptr = func;
ptr(3);            // 3 is argument to 'func'.
```



## **Topic - 3: String Functions**

- A string pointer is constant & thus couldn't change.

```c
/* Operations on string */
strcat(str1, str2);
strcpy(str1, str2);
strlwr(str1, str2);
strupr(str1, str2);
strncat(str1, str2, n);
strncpy(str1, str2, n);
strncmp(str1, str2, n);
strchr(str, c);                // Returns pointer to it, else NULL.
strrchr(str, c);               // Same as previous but in reverse.
strstr(str1, str2);            // Returns pointer if 'str1' is found in 'str2'.

/* ASCII-based conversions */
int atoi(str);
int atof(str);
long int atol(str);
long int strtol(str);          // Safer alternative to 'atoi()'.
```



## **Topic - 4: Structures & Unions**

- **Composite data type:** Can contain collection of elements with different data types.
- **Aggregate data type:** Composite data type

```c
/* Structure value transfer */
struct student s3 = s2;

/* Referring struct member */
ptr = (*student).age;
ptr = student -> age;        // Same as previous
```

- In unions, the memory is occupied by its largest member with overwriting possible.

```c
/* Union example */
union accumulator        // Total coverage: 0x0-0x7
{
	uint8_t al;          // Region: 0x0-0x1
	uint16_t ax;         // Region: 0x0-0x2
	uint32_t eax;        // Region: 0x0-0x4
	uint64_t rax;        // Region: 0x0-0x8
};
```
