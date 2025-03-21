# $\fbox{COMPETITIVE PROGRAMMING}$





## **Topic - 1: Standard Library Template**

### <u>STL Features</u>

1. Containers
2. Iterators
3. Algorithms
4. Functors


### <u>Containers</u>

- Sequential (vectors, stack, queue, pair)
- Ordered (maps, multimap, set, multiset)
- Unordered (unordered map, unordered set)

#### Nested Containers:

```cpp
vector<vector<int>>
map<int,vector<int>>
set<pair<int,string>>
vector<map<int,set<int>>>
```


### <u>Iterators</u>

- Iterators point to memory addresses of containers.
- For example, `begin()` & `end()`.


### <u>Algorithms</u>

- Upper bound
- Lower bound
- Sort (comparator)
- Max-element
- Min-element
- Accumulate
- Reverse
- Count
- Find
- Next permutations
- Prev permutations


### <u>Functors</u>

- **<u>Functors</u>:** Classes which can act as functions.



## **Topic - 2: Pairs & Vectors**

### <u>Pairs</u>

#### General code:

```cpp
#include <bits/stdc++.h>

using namespace std;

int main()
{
	pair<int,string> p;

	p = make_pair(2, "abc");
	// p = {2, "abcd"};			// Alternative

	cout << p.first << p.second << endl;

	return 0;
}
```

#### Pair array:

```cpp
pair<int,string> p_arr[3];

p_arr[0] = {0, "Gourav"};
p_arr[1] = {0, "Rikhish"};
p_arr[2] = {0, "Deepanjan"};

swap(p_arr[0], p_arr[2])
```


### <u>Vectors</u>

- Also uses `bits/stdc++.h`.
- $O(1)$ in operations.

#### Scalable vector:

```cpp
vector<int> v;

v.push_back(7);        // Pushing 7 to vector 'v'.
v.size();              // Size of vector 'v'.
```

- Vectors can also be a perimeter type.

#### Fixed size vector:

```cpp
vector<int> v[5];        // All elements initialized to 0.
```

#### Copying vectors:

```cpp
vector<int> &v2 = v;        // Takes O(n).
```

- Not adding `&` won't have future changes in `v2`.


### <u>Vector Of Pairs</u>

```cpp
vector<pair<int,int>> v = {{1,2}, {3,4}, {5,6}};
```


### <u>Nested Vectors</u>

```cpp
vector<vector<int>> v;

v[0].push_back(4);        // Pushing 4 to first vector.
```
