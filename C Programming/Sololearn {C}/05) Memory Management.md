# $\fbox{Chapter 5: MEMORY MANAGEMENT}$





## **Topic – 1: Three Basic Functions**

### <u>Contagious Allocation</u>

```c
m = calloc(7, sizeof(int));
```

- The code above allocates `7` contagious memories of `4` bytes.
- `calloc()` can only allocate memory as per a particular data type, not manually input number of byte or equation.


### <u>Reallocation</u>

```c
realloc(m, 16);    // Expands pointer coverage by 16 bytes.
```

---
