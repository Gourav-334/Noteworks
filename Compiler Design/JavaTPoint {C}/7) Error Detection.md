# $\fbox{Chapter 7: ERROR DETECTION}$





## **Topic - 1: Lexical Error**

### <u>Introduction</u>

- **<u>Lexical error</u>:** Unmatching pattern in a token.
- It is caught during execution of the program.


### <u>Types Of Lexical Errors</u>

- Spelling error
- Exceeding identifier length
- Exceeding number size
- Illegal character used


### <u>Example</u>

```c
int a = 1xab
```

- `1xab` is neither a number nor identifier.



## **Topic - 2: Syntax Error**

### <u>Types Of Syntax Error</u>

- Error in structure
- Missing operators
- Unbalanced parenthesis


### <u>Examples</u>

- Writing `=` instead of `==`.
- Missing semicolon (`;`).



## **Topic - 3: Semantic Error**

### <u>Introduction</u>

- Semantic error is detected at compile time.
- This includes scope & declaration error.


### <u>Example</u>

- Multiple identifiers with same name declared.
- A function's declaration & definition has mismatch in parameter's type.
- Using wrong operators among two operand (`str1 % 2`).
- Mentioning an undeclared variable.

---
