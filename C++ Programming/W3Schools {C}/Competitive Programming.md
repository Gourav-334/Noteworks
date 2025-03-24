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

>**<u>NOTE</u>:**
>All the containers are part of the `std` namespace.

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



## **Topic - 3: Stack & Queue**

### <u>Introduction</u>

- Both stack & queue are part of the `queue.h` header in C++.


### <u>Stack</u>

#### Methods:

- `push(x)`
- `pop()`
- `top()`
- `size()`
- `empty()`


### <u>Queue</u>

#### Methods:

- `push(x)`
- `pop()`
- `front()`
- `back()`
- `size()`
- `empty()` - Returns `true` is the queue is empty.



## **Topic - 4: Ordered Containers**

### <u>Introduction</u>

- Ordered maps are part of the `<map>` header.
- These are often used for implementing red-black trees.


### <u>Map</u>

```cpp
map<int,string> mp;

/* mp[key] = value; */
mp[1] = "One";
mp[2] = "Two";

/* Map operations */
mp.insert({3,"Three"});        // Alternatively to method above.
mp.erase(2);

/* Access elements */
cout << mp[2];            // Creates an entry if not existing.
cout << mp.at(2);         // Throws error for not existing.
```


### <u>Multimap</u>

- Similar to maps, but allows multiple values for same key.

```cpp
multimap<int,string> mm;

mm.insert({1,"Good"});
mm.insert({2,"Neglected"});
mm.insert({3,"Child"});        // Notice duplicacy.
```

#### Methods:

- `insert({key,value})`
- `erase(key)`
- `find(key)`
- `count(key)`
- `equal_range(key)`


### <u>Set</u>

#### Methods:

- `insert(x)`
- `erase(x)`
- `find(x)`
- `count(x)` - Returns `1` if exists, else `0`.
- `lower_bound(x)` - Returns iterator to the first element $\ge$ `x`
- `upper_bound(x)` - Returns iterator to the first element $\gt$ `x`



## **Topic - 5: Unordered Containers**

### <u>Introduction</u>

- Unordered containers are often used in hash mapping.


### <u>Containers</u>

- `unordered_map` - Unordered map
- `unordered_multimap` - Unordered multimap
- `unordered_set` - Unordered set
- `unordered_multiset` - Unordered multiset



## **Topic - 6: Algorithms**

### <u>Introduction</u>

- STL algorithms use header `algorithm` & `numeric`.


### <u>Sorting Algorithms</u>

- Has a complexity of $O(nlog(n))$.
