# $\fbox{Chapter 4: EXCEPTION HANDLING}$





### <u>Exceptions</u>

```cpp
try
{
	if (age>=18) {cout << "Welcome!";}
	else         {throw(age);}
}

catch (int num) {        // num = age
	/* Statements */
}
```

- If our throw is not an identifier, then we can use three dot (`...`) in catch.
- See the example given below.

```cpp
try
{
	if (age>=18) {cout << "Welcome!";}
	else         {throw 505;}
}

catch (...) {        /* Handles all exceptions */
	/* Statements */
}
```

---
