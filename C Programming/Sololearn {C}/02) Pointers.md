# $\fbox{Chapter 2: POINTERS}$





## **Topic – 1: General Information**

- Memory addresses are stored as hexadecimal values.
- `*` is called **indirection/dereference** operator.
- **<u>Dereferencing</u>:** Process of checking what a pointer is pointing to.
- We use parentheses around `(*ptr)++` during unary operations.



## **Topic – 2: Function Pointers**

### <u>Introduction</u>

```c
void func(int x) {printf("%d", x);}
void (*ptr)(int) = NULL;    // Pointer to a void type function (int argument).
ptr = func;                 // Pointer assignment to function.
ptr(3);                     // Performing function
```

- A function with use of its pointer, can only be performed but not printed.


### <u>Using Pointers As Conditional Statements</u>

```c
int add(int x, int y);
int sub(int x, int y);
int mult(int x, int y);
int div(int x, int y);

int (*op[4])(int, int) = {NULL};

op[1] = &add;     // Can also be 'op[1] = add;'
op[2] = &sub;     // Same as 'op[1] = sub;'
op[3] = &mult;    // Same as 'op[1] = mult;'
op[4] = &div;     // Same as 'op[1] = div;'

int choice;
scanf("%d", &choice);
printf("%d", op[choice](a,b));
```

---
