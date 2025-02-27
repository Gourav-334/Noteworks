# $\fbox{Chapter 3: DATA TYPES}$





## **Topic – 1: Strings**

### <u>General Information</u>

- Null character can also be represented with `\0`.
- A string pointer is constant and thus can’t be changed.


### <u>Functions</u>

```c
strcat(str1, str2);
strcpy(str1, str2);
strlwr(str);
strupr(str);
strrev(str);
strncat(str1, str2, n);
strncpy(str1, str2, n);
strncmp(str1, str2, n);
strchr(str, c);            // Returns a pointer when found, else NULL.
strrchr(str, c);           // Same as previous but searched in reverse.
strstr(str1, str2);        // Returns a pointer if 'str1' is found in 'str2'.
```

- Function `strcmp()` returns `0` when strings match.



## **Topic – 2: Integers & Floats**

### <u>ASCII Based Conversions</u>

```c
int atoi(str);
int atof(str);

long int atol(str);
long int strtol(str);    // Safer alternative to 'atoi()'.
```

- `strtol()` wasn’t working when I tried it.

---
