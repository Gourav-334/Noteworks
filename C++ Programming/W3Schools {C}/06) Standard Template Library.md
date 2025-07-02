# $\fbox{Chapter 6: STANDARD TEMPLATE LIBRARY}$





## **Topic - 1: Introduction To STL**

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

- Defined in `<vector>`.
- Also uses `bits/stdc++.h`.
- $O(1)$ in operations.

#### Scalable vector:

```cpp
vector<int> v;
```

- Vectors can also be a perimeter type.

#### Fixed size vector:

```cpp
vector<int> v[5];        // All elements initialized to 0.
```

#### Functions:

```cpp
vector<int> &v2 = v;        // Copying - Takes O(n).

v.push_back(7);        // Pushing 7 to vector 'v'.
v.pop_back();
v.size();              // Size of vector 'v'.
v.clear();
v1.swap(v2);
v.front();             // Referring to first element.
v.back();
v.at(4);
v.empty();             // Tells if empty or not.
v.capacity();
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


### <u>Unordered Map</u>

- Uses `<unordered_map>` library.
- Values are hashed to keys & keys are hashed to indices.

#### Putting values:

```cpp
map1["Name"] = "Gourav Kumar Mallick";
map1["Age"] = "19";
map1["Branch"] = "Computer Science & Engineering";
```

$$ \text{OR} $$

```cpp
unordered_map<char,int> umap = {
	{'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
	{'4', 4}, {'5', 5}, {'6', 6}, {'7', 7}
}
```

#### Traversal/iteration:

```cpp
for (auto x: map1) {
	cout << x.first << ": " << x.second << endl;
}
```

$$ \text{OR} $$

```cpp
unordered_map<string,string>::iterator it;

for (int = map1.begin(); it != map1.end(); it++)
{
	cout << it->first << ": " << it->second << endl;
}
```

- `begin()` and `end()` are used with an iterator only as shown above.
- `end()` is place after crossing the last pair in memory.
- It traverses in reverse.
- Address operations don’t work on unordered maps.
- Time complexity of unordered map is $O(1)$, contrary to map with $O(log(n))$.

#### Function with no return type:

```cpp
map1.erase("Name");
```

#### Functions with return type:

```cpp
cout << map1.bucket("Age");    // Returns bucket number of key.
cout << map1.empty();          // Returns with 1 or 0.
cout << map1.count("Age");     // Counts total values for a key.
```

#### For control statements:

```cpp
if (map1.find("Any key")==map1.end())
	cout << "Element not present\n";
```



## **Topic - 6: Algorithms**

### <u>Introduction</u>

- STL algorithms use header `algorithm` & `numeric`.


### <u>Sorting Algorithms</u>

- Both have a complexity of $O(nlog(n))$.
- Again, they can be included through `std`.

#### Simple sorting:

```cpp
sort(v.begin(), v.end());        // Sorting in ascending order.
sort(v.begin(), v.end(), greater<int>());    // Descending
```

#### Stable sorting:

- This is when duplicate elements retain their original order.

```cpp
stable_sort(v.begin(), v.end());
```


### <u>Searching Algorithm</u>

#### Binary sort:

- Both give a complexity of $O(log(n))$.
- `binary_search` returns `true` when original document is found.
- Returns `true` if `5` is in array.

```cpp
binary_search(v.begin(), v.end(), 5);
```

- In C++, conditional statement expressions evaluate to Booleans, not integers as in C.


### <u>Minimum & Maximum</u>

- Again, these are too part of `std` namespace.

#### Among two elements:

```cpp
cout << min(10,20);    // Output: 10
cout << max(10,20);    // Output: 20
```

#### More than two elements:

```cpp
cout << min({3,1,5,2});    // Output: 1
```

#### In a container:

```cpp
min_element(v.start(), v.end());
max_element(v.start(), v.end());
```


### <u>Modification</u>

- Again, these are too part of `std` namespace.

#### Reversing:

```cpp
reverse(v.begin(), v.end());
```

#### Rotating elements:

```cpp
rotate(v.begin(), v.begin()+2, v.end());    // Rotates left by 2.
```

#### Removing duplicates:

```cpp
auto it = unique(v.begin(), v.end());
v.resize(distance(v.begin(), it));        // Trim extra space.
```


### <u>Numeric Algorithms</u>

- Are included in `<numeric>` header.

#### Accumulate:

```cpp
accumulate(v.begin(), v.end(), 0);    // Sums all elements in 'v'.
```

#### Filling containers:

- Fills a range in container with a particular order.

```cpp
vector<int> v(5);    // 'v = {0,0,0,0,0}' by default.

/* Ordering in increasing order of 1 */
itoa(v.begin(), v.end(), 1);    // v = {1,2,3,4,5};
```


### <u>Set Algorithms</u>

#### Set union:

```cpp
vector<int> a = {1,3,5};
vector<int> b = {3,4,6};
vector<int> res(10);

auto it = set_union(
	a.begin(), a.end(),
	b.begin(), b.end().
	res.begin()
);

res.resize(it - res.begin());
```

#### Set intersection:

- Similar to previous function, just name the function as `set_intersection()`.


### <u>Randomization</u>

- Also part of the `std` namespace.
- Uses `<random>` header.

```cpp
random_device rd;
mt19937 g(rd());
shuffle(v.begin(), v.end(), g);
```

---
