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
5. Induction-variable elimination
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
- This technique is used specifically for loops.

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


#### <u>Induction-Variable Elimination</u>

- **<u>Induction variable</u>:** A variable whose value in loop changes in predictable manner.
- This technique too is used specifically for loops.

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

- Again, for loops only.
- In strength reduction, we replace expensive operations with cheaper ones.
- Expensive operations like multiplication & division cost more computation cost than addition & subtraction.
- And exponentiation is even more expensive than multiplication & division.

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



## **Topic - 2: DAG Representation**

### <u>Introduction</u>

- **<u>DAG</u>:** Directed Acyclic Graph
- DAG data structure is used for breaking an expression into sub-expressions.
- So, it represents a clear picture of how expressions are computed dynamically.
- These are optimized as they use minimal required nodes.

#### Structure grouping:

1. **Leaf nodes -** Identifiers like variables or constants etc.
2. **Interior nodes -** At non-leaf nodes, we get operator symbols & the expression identifier(s).


### <u>Example</u>

#### Expression set:

```c
S1 = 4 * i;          // (a)
S2 = a[S1];          // (b)
S3 = 4 * i;          // (c)
S4 = b[S3];          // (d)
S5 = s2 * S4;        // (e)
S6 = prod + S5;      // (f)
prod = S6;
S7 = i + 1;          // (g)
i = S7;

if (i<=20) {goto(i);}    // (h)
```

#### Step-by-step construction:

1. `S1 = 4 * i;`

![a](./media/image33.png)

2. `S2 = a[S1];`

![b](./media/image34.png)

3. `S3 = 4 * i;`

![c](./media/image35.png)

4. `S4 = b[S3];`

![d](./media/image36.png)

5. `S5 = s2 * S4;`

![a](./media/image37.png)

6. `S6 = prod + S5;`

![f](./media/image38.png)

7. `S7 = i + 1;`

![g](./media/image39.png)

8. `if (i<=20) {goto(i);}`

![a](./media/image40.png)

>**<u>NOTE</u>:**
>1. Operands on left & right are written on left & right respectively.
>2. Expressions involving only `=` operator doesn't affect the DAG.
>3. Other than `=` operator, all other operators must be in DAG.
