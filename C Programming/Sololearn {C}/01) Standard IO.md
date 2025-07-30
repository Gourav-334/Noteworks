# $\fbox{Chapter 1: STANDARD IO}$





## **Topic – 1: Special I/O Functions**

### <u>For Characters</u>

```c
char c = getchar();
putchar(c);
```


### <u>For Strings (Unsafe)</u>

```c
gets(str);
puts(str);
```

- These are unsafe because they might overwrite memory across its limit if a string is passed larger than its actual size.


### <u>For Strings (Safe)</u>

```c
char str[20];

fgets(str, 20, stdin);
fputs(str, stdout);
```



## **Topic – 2: Format Specifiers**

### <u>Multiple Inputs</u>

```c
scanf("%d %f %s", &num, &fl, text);
```

- Putting a space between two won’t affect, but putting anything else will.
- `%e` – scientific notation (exponent)


### <u>Rounding Off Floats</u>

```c
printf("PI = %3.2f", 3.14159);    // PI = 3.14
```

- `%3.2` is same as `%-3.2`.
- In `%3.2`, `2` is number of digits after decimal point.



## **Topic – 3: Boolean Expressions**

- Are evaluated from left to right.

>**<u>NOTE</u>:**
>Remember expressions like: `if(!(m=='x'||n=='x'))`.

---
