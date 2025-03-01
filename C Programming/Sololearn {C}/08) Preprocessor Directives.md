# $\fbox{Chapter 8: PREPROCESSOR DIRECTIVES}$





## **Topic – 1: Commonly Used PD**

### <u>Definition Based PD</u>

```c
#undef PI
```

- For defined through `#define`, their data types are decided by compiler.


### <u>Defining Function Using PD</u>

```c
#define FUNCTION_NAME (parameter) (return)
#define AREA (r) (PI*(r)*(r))
```


### <u>Extending Number To Next Line</u>

```c
#define MY_FLOAT \
4.5652389
```



## **Topic – 2: In Code PDs**

- `__DATE__` current date in ***mm dd yyy***
- `__TIME__` current time in ***hh:mm:ss***
- `__FILE__` current filename as **string**
- `__LINE__` current line number as **integer**



## **Topic – 3: Operational PDs**

### <u>Conditional Compilation Directives</u>

```c
#if !defined(PI)
	/* Statements */
#endif
```

- We can even write statements like `int x = 5;` in macro conditional blocks!


### <u>Preprocessor Operators</u>

- Stringification/stringizing operator converts parameter to string constant.

```c
/* We can name TO_SSTR() function as something else too. */

#define TO_STR(x) #x

int main()
{
	printf("%s", TO_STR(123/@$@12));
	return 0;
}
```


### <u>String Concatenation</u>

```c
/* STICK is again a custom function name. */

#define STICK(name, surname) name##surname
```

---
