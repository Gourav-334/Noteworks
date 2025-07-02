# $\fbox{Chapter 1: Comparison With C}$





## **Topic - 1: Basic Concepts**

### <u>Structure Of Program</u>

- `<<` is used for concatenation.
- In C++, main function must compulsorily return `int`.


### <u>Floating Points</u>

- Letter `f` after typing value is compulsory to specify `float`, not `double`.

```cpp
float length = 5.31f;
```

- In C++, floats when printed, are shown up to the decimal point necessary, unlike C.


### <u>More On Variables</u>

- `auto` keyword is used to let compiler decide data type of a variable.
- **<u>Pascal case</u>:** `TheBadassEngineer`
- **<u>Camel case</u>:** `theBadassEngineer`


### <u>Taking Input</u>

```cpp
cin >> a >> b;    // Taking multiple inputs.
```

- For reading whole string, write as following.

```cpp
getline(cin, name);
```


### <u>The Switch Statement</u>

- Forgetting to add `break` at case's ending, results in executing all cases despite wrong value.
- `default` case is executed if none of the case matches.


## **Topic - 2: Utility Libraries**

### <u>String</u>

#### Appending:

- We can append strings in two ways.

```cpp
string name = "John";
string surname = "Doe";
string fullName = name + " " + surname;

/* OR */

fullName = name.append(surname);
```

- The append function above appends `surname` to string `name` also.

#### Length:

```cpp
str.length()
```

- Namespace `std` is used for `string` and `cout` functions.


### <u>Math</u>

```cpp
min(a,b)
max(a,b)
abs(x)
cbrt(x)     // Cube root.
ceil(x)     // Returns larger integer.
cos(x)
exp(x)      // e^x
fabs(x)     // Floating point absolute.
floor(x)    // Returns smaller integer.
pow(x,y)
```

- Not-defined answers return a string `nan`.
- The inputs for trigonometric functions must be in radians.
- In `pow()`, if raised power is not a whole number neither float with only zeroes after decimal point, then `nan` is returned.


## **Topic - 3: Storage Elements**

### <u>Structures</u>

```cpp
struct {
	int myNum;
	string myString;
}
myStruct1, myStruct2, myStruct3;
```

- When pointers are defined for structures without `typedef`, then the pointers are blamed by the compiler & debugger.


### <u>Function Parameters</u>

- We can also pass whole array as parameter.

```cpp
void myFunc(int arr[6]) {}

int main()
{
	int nums[6];
	myFunc(nums);
}
```

---
