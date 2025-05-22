# $\fbox{Chapter 1: COMPLEXITIES}$





### <u>Introduction</u>

- **<u>Data Structure</u>:** Systematic way of organizing and accessing of data.


### <u>Non-Primitive Data Type</u>

- Non-primitive data type is focused on structuring homogeneous & heterogeneous data.
- **<u>Graph</u>:** It is a collection of nodes, and connecting edges between them.


### <u>Types Of Graphs</u>

- Same as in discrete mathematics.


### <u>Operations On Data Structures</u>

- There are total 12 types of operation in data structures.
- For example, look at the code below.

```c
for (int i=0; i<n; i++)
{
	for (int j=0; j<n; j++)
	{
		count++;
	}
}
```

|  Element  | Number Of Times Used |
| :-------: | :------------------: |
|   `i=0`   |         $1$          |
|   `i<n`   |        $n+1$         |
|   `i++`   |         $n$          |
|   `j=0`   |         $n$          |
|   `j<n`   |       $n(n+1)$       |
|   `j++`   |        $n*n$         |
| `count++` |        $n*n$         |

- Summing up the number of times used gives the time complexity.

$$ 1\;+\;n\;+\;1\;+\;n\;+\;n\;+\;n(n+1)\;+\;n*n\;+\;n*n $$
$$ = 3n^{2}\;+\;4n\;+\;2 $$
$$ =\;O(n^{2}) $$


### <u>Order of Growth of Algorithm</u>

- It means how the computation time increases as the input size increases.
- Large input size make significant change to computation time.
- For example, refer to the table below.

| Time Complexity |        Name        | Example                                         |
| :-------------: | :----------------: | :---------------------------------------------- |
|       $1$       |      Constant      | Adding an element to the font of a linked list. |
|    $log(n)$     |    Logarithmic     | Finding an element in a sorted array.           |
|       $n$       |       Linear       | Finding an element in an unsorted array.        |
|   $n\;log(n)$   | Linear logarithmic | Sorting n items by merge sort.                  |
|     $n^{2}$     |     Quadratic      | Shortest path between two nodes in a graph.     |
|     $n^{3}$     |       Cubic        | Matrix multiplication.                          |
|     $2^{n}$     |    Exponential     | The towers of Hanoi problem.                    |


### <u>Searching Problems</u>

- There are two types of searches:
- Linear search
- Binary search


### <u>Linear Search Complexity Analysis</u>

#### Case time:

- Worst case - $O(n)$
- Average case - $O(n)$
- Best case - $O(1)$

#### Space complexity:

- $O(1)$


### <u>Binary Search Complexity Analysis</u>

#### Case time:

- Worst case - $O(log(n))$
- Average case - $O(log(n))$
- Best case - $O(1)$
- Space complexity - $O(1)$


### <u>Binary Search: Calculating Time Complexity</u>

- Let the length of array to be $n$.
- At 1st iteration, length of array is $n$.
- At 2nd iteration, length of array is $\frac{n}{2}$.
- At 3rd iteration, length of array is $\frac{n}{2^{2}}$.
- At kth iteration, length of array is $\frac{n}{2^{k}}$.
- $k$ is the last iteration, after which length of array becomes $1$.

#### Applying $log_{2}$:

$$ \frac{n}{2^{k}}\;=\;1 $$
$$ n\;=\;2^{k} $$
$$ log_{2}(n)\;=\;k\;log_{2}(2) $$
$$ log_{2}(n)\;=\;k\;log_{2}(2) $$
$$ log_{2}(n)\;=\;k $$
$$ k\;=\;log_{2}(n) $$

---
