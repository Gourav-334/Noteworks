**<u>Chapter 8:</u> PREPROCESSOR DIRECTIVES**

**Topic – 1: Commonly Used PD**

**<u>Definition Based PD</u>**

***\#undef PI***

- For **macros** defined through ***\#define***, their data types are
  decided by **compiler**.

**<u>Defining Function Using PD</u>**

***// \#define FUNCTION_NAME (parameter) (return)***

***\#define AREA (r) (PI\*(r)\*(r))***

**<u>Extending Number To Next Line</u>**

***\#define MY_FLOAT \\***

***4.5652389***

**Topic – 2: In Code PDs**

- ***\_\_DATE\_\_*** current date in **mm dd yyy**

- ***\_\_TIME\_\_*** current time in **hh:mm:ss**

- ***\_\_FILE\_\_*** current filename as **string**

- ***\_\_LINE\_\_*** current line number as **integer**

**Topic – 3: Operational PDs**

**<u>Conditional Compilation Directives</u>**

***\#if !defined(PI)***

***/\* Statements \*/***

***\#endif***

- We can even write statements like **int x = 5;** in **macro
  conditional blocks**!

**<u>Preprocessor Operators</u>**

- **Stringification/ stringizing** operator converts parameter to string
  constant.

***// We can name TO_SSTR() function as something else too***

***\#define TO_STR(x) \#x***

***int main()***

***{***

***printf("%s", TO_STR(123/@\$@12));***

***return 0;***

***}***

**<u>String Concatenation</u>**

***// STICK is again a custom function name***

***\#define STICK(name, surname) name##surname***
