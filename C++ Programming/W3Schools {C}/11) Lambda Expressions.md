# $\fbox{Chapter 11: LAMBDA EXPRESSIONS}$





## **Topic - 1: Lambda Expressions**

### <u>Introduction</u>

- Lambda expressions are used for defining functions which will be used shortly & very less.
- Though its advised to write the return type as a good practice, that's not a necessity here.
- And lambda expressions are used with vectors.
- We use the `vector.h` header for this purpose.


### <u>Code Structure</u>

```cpp
[capture_clause] (parameters) -> return_type
{
	// Codes to execute
}
```


### <u>Example Code</u>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numbers = {1, 2, 3, 4, 5};
	
    for_each(numbers.begin(), numbers.end(), [](int n)
    {
        cout << n << " ";
    });
    
    return 0;
}
```

- Here, `for_each` is indeed a function, part of `algorithm.h` header.
- Also, there is another function `sort` with very obvious effect.
- Whatever variable is written inside `[]` is considered a copied local variable for the expression, than changing it outside too.

---
