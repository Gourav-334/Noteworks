# $\fbox{Chapter 9: CODE OPTIMIZATION}$





## **Topic - 1: Machine-Independent Optimization**

### <u>Introduction</u>

- In machine-independent optimization, we optimize the intermediate code to get a naturally optimized target code.
- But we optimize only those codes here which doesn't involve memory locations or CPU registers.
- These changes might make it difficult to track back how the program was actually written.

#### Improvable bottlenecks:

- Using constants instead of variables
- Replacing copies of variables with constants (if unchanged).
- Replacing repeated expressions with their evaluated values.


### <u>Ways To Optimize Code</u>

1. Compile-time evaluation
2. Variable propagation
3. Dead code elimination
4. Code motion
5. Induction variable
6. Strength reduction


### <u>Variable Propagation</u>

- Some expression might have different variables among each other, but they might have same value.
- We replace them with one of those variable name.

#### Unoptimized:

```c
c = a*b;
x = a;

d = x*b+4;
e = a+6;
f = x/9;
g = a-3*x;
```

#### Optimized:

```c
c = a*b;
x = a;

d = a*b+4;
e = a+6;
f = a/9;
g = a-3*a;
```


### <u>Code Motion</u>

- Code motion optimization is used for bringing loop-irrelevant statements out of the loop to avoid multiple same evaluation.

#### Unoptimized:

```c
j = 10;

while (i<j) {value = 7; j++;}
```

#### Optimized:

```c
j = 10;
value = 7;

while (i<j) {j++;}
```


#### <u>Induction Variable</u>

- **<u>Induction variable</u>:** A variable whose value in loop changes in predictable manner.

```c
/* Unpredictable */

while (i<5)
{
	arr[i] = i*2;
}


/* Predictable */

while (i<5)
{
	arr[i] = i*2;
	i++;
}
```


### <u>Strength Reduction</u>

- In strength reduction, we replace expensive operations with cheaper ones.
- Expensive operations like multiplication & division cost more computation cost than addition & subtraction.

#### Unoptimized:

```c
for (int i=0; i<10; i++)
{
	int x = i*5;    // Multiplication on each iteration.
	arr[i] = x;
}
```

#### Optimized:

```c
int x = 0;

for (int i=0; i<10; i++)
{
	arr[i] = x;
	x += 5;        // Cheaper alternative.
}
```
