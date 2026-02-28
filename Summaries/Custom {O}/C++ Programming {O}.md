# $\fbox{C++ PROGRAMMING}$





## **Chapter - 1: Comparison With C**

- `main()` function must always be of `int` type.
- **`f`:** Separates a `float` from `double`, like `5.13f`.

```cpp
/* Reading whole string */
getline(cin, str);

/* Appending string method - 2 */
str3 = str1.append(str2);

/* Math functions */
min(a,b)
abs(x)
cbrt(x)         // Cube root
ceil(x)
cos(x)          // In radians
exp(x)          // e^x
fabs(x)         // Floating point absolute
floor(x)
pow(x,y)        // Returns 'nan' if numbers not whole.
```

- **`nan`:** String returned by not-defined answers.
- Its possible to pass whole array as argument in C++.



## **Chapter - 2: Object-Oriented Programming**

- `;` is added at the end of each C++ class block.

```cpp
/* Method defined outside class */
int Cars::speed(int max_speed) {        // Needs to be declared inside class.
	return max_speed;
}

/* Constructor example */
Cars(int x, int y) {                    // Special method, nothing returned.
	this -> x = x;
	this -> y = y;
}

/* Inheritence */
class Cars: protected Vehicle {};      // Public in Vehicle protected in Vehicles.

/* Multi-inheritence (common attributes derived) */
class Mutation: public Dinosaurs, public Rats {};

/* Polymorphism */
class Parent {
	public:
		virtual string meth() { return "Papa"; }
};
class Child: public Parent {
	public:
		string meth() override { return "Beta"; }
};
```



## **Chapter - 3: File Handling**

```cpp
/* File handling library */
#include <fstream>

/* File object types */
fstream file;                       // Read + write
ifstream file;                      // Read
ofstream file;                      // Write
ifstream file("sample.txt");        // Defining & opening file

/* Opening and closing file */
file.open("corpus.txt", ios::in | ios::out | ios::truc);
if (!file.is_open()) { cerr << "Error opening!"; }
file.close();

/* Read and write operations */
file << "I enjoy C++" << endl;            // Writing to file.
getline(file, str);                       // Reading a line from file.
while (file.good()) { /* Code */ }        // Until EOF not reached.

/* Cursor position manipulation */
file.seekg(0);                  // Set to beginning of file.
file.seekg(5, ios::beg);
file.seekg(1, ios::cur);
file.seekg(0, ios::end);

/* Cursor position checking */
cout << file.tellg();        // 'g' = Get (read)
cout << file.tellp();        // 'p' = Put (write)

/* Binary mode file */
file.open("sample.img", ios::binary | ios::in | ios::out | ios::trunc);
```



## **Chapter - 4: Exception Handling**

```cpp
/* Try-catch blocks */
try {
	if (age>=18) { cout << "Welcome"; }
	else         { throw age; }
}
catch (int num) {        // num = Caught integer
	/* Code */
}

/* Generic catch block */
catch (...) {            // Handles all exceptions
	/* Code */
}
```



## **Chapter - 5: Memory Management**

```cpp
/* Memory management header */
#include <new>

/* Memory allocation & deallocation */
ptr = new int(10);        // Allocate for an 'int', fill with 10.
ptr = new int[n];
delete[] ptr;

/* Dynamic class objects */
Tree *my_tree = new Tree();        // Allocated via pointer
my_tree -> insert(89);             // Running operations via pointer
delete my_tree;
```



## **Chapter - 6: Standard Template Library**

- STL contains *containers*, *iterators*, *algorithms*, and *functors*.
- **Containers:** *Sequential* (vectors, stack, queue, pair), *ordered* (maps, multimap, set, multiset), and *unordered* (unordered map, unordered set).
- **Iterators:** Pointer to memory addresses of containers (`begin()` & `end()`).
- **Algorithms:** Upper bound, lower bound, sort/comparator, max-element, min-element, accumulate, reverse, count, find, next permutation, and previous permutation.
- **Functors:** Classes with ability to act as functions.

```cpp
/* Pairs (expandable size) */
pair<int,string> p;
p = make_pair(1, "abc");
p = {2, "def"};                     // Alternative way
cout << p.first << p.second;        // Accessing pair elements

/* Pair (fixed size) */
pair<int,string> p[5];
pair[0] = {1, "abc"};
swap(p[0], p[1]);                   // Swapping pairs

/* Vectors */
vector<int> &v2 = v;                // Copying takes O(n)
v.push_back();
v.pop_back();
v.size();
v.clear();
v.swap(v2);
v.front();
v.back();
v.at(4);
v.empty();                          // Tells if empty or not
v.capacity();

/* Stack */
push(x);
pop();
top();
size();
empty();

/* Queue */
push(x);
pop();
front();
back();
size();
empty();

/* Ordered maps */
map<int,string> mp;
mp[1] = "One";
mp.insert({1,"One"});        // Same as above
mp.erase(1);
cout << mp[1];
cout << mp.at(2);            // Same as above
```

- **Multimap:** Same as map, but allows inserting multiple values for same key.

```cpp
/* Ordered multimaps */
multimap<int,string> mm;
mm.insert({1,"Neglected"});
mm.erase(1);
mm.find(1);
mm.count(1);
mm.equal_range(1);                 // ???

/* Ordered set */
set<int> st;
st.insert(x);
st.erase(x);
st.find(x);
st.count(x);
st.lower_bound(x);        // Returns iterator to next greater or equal element.
st.upper_bound(x);        // Returns iterator to next greater element.
```

- Other containers - `unordered_map`, `unordered_multiset`, and `unordered_set`, `unordered_multiset`.

```cpp
/* Unordered maps */
unordered_map umap = {
	{'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
	{'4', 4}, {'5', 5}, {'6', 6}, {'7', 7}
};
umap.bucket("abc");        // Returns bucket number

/* Map traversal */
for (auto x: mp) {
	cout << x.first << ": " << x.second;
}

/* Alternative traversal method */
unordered_map<int,string>::iterator it;
for (it=mp.begin(); it!=mp.end(); it++) {
	cout << it->first << ": " << it->second;
}
```

- Time complexity for insertion in ordered map is of $O(log(n))$, and of $O(1)$ in unordered map.
- Sorting algorithms require including `std`.

```cpp
/* Algorithm headers */
#include <algorithm>
#include <numeric>

/* Sorting in container */
sort(v.begin(), v.end());                        // Ascending order
sort(v.begin(), v.end(), greater<int>());        // Descending order
stable_sort(v.begin(), v.end());                 // Duplicates retain position

/* Searching in container */
binary_search(v.begin(), v.end(), x);        // Searches for 'x'
min_element(v.begin(), v.end());
max_element(v.begin(), v.end());

/* Positional modification */
reverse(v.begin(), v.end());
rotate(v.begin(), v.begin()+2, v.end());        // Rotates left by 2

/* Duplicate removal */
auto it = unique(v.begin(), v.end());
v.resize(distance(v.begin(), it));           // Trim extra space

/* Numerical operations */
accumulate(v.begin(), v.end(), 0);        // Sum all elements
itoa(v.begin(), v.end(), 1);              // Initiating container in inc order

/* Containers union into another container */
auto it = set_union(
	v1.begin(), v1.end(),        // Containers could be of any type,
	v2.begin(), v2.end(),        // not just sets.
	v3.begin()
);
```

- For set operations on container, there is also `set_intersection()`.

```cpp
/* Randomization */
random_device rd;
mt19937 g(rd());
shuffle(v.begin(), v.end(), g);
```



## **Chapter - 7: Generic**

- **Generic:** Class of function defined as a template.

```cpp
/* Alternative for functions */
template <typename T>
T add(T x, T y) {
	return x+y;
}

/* Template for classes */
template <class T>
class Class_name {
	// Class definition
	// T used inside as a type
}

/* Example */
cout << add<int>(3,5);
cout << add(3,5);             // Same as above
```

- We can't use `auto` in generic.
- Templates could be used on object methods, and be overloaded.



## **Chapter - 8: Making Libraries**

- **Dependency walker:** A tool used to solve compatibility issues with shared object files.
- For using anything that comes from `std` library, we need to use resolution operator (`::`) instead of `using namespace` to avoid bloated binary & name collision.

```cpp
/* Static header file */
#ifndef MYLIB_HPP
	#define MYLIB_HPP

#ifdef __cplusplus               // Ensuring C & C++ compatibility
extern "C" {void func();}        // For shared C features (like functions)

#endif
#endif
```

- G++ dynamic header files in Linux preserve same structure as in GCC.

```cpp
/* Dynamic header file */
#ifndef EXAMPLE_HPP
	#define EXAMPLE_HPP

#ifdef __GNUC__
	#define EXAMPLE_API __attribute__((visibility("default")))
#else
	#define EXAMPLE_API

#endif

extern EXAMPLE_API int num;

#endif
```

- Compiling process in G++ is same as in GCC.

```sh
# Linking libraries
g++ -o example example.c -lm

# Optimizing code
g++ -O3 -o example example.c        # Vectorization (using SIMD/SISD)

# Static compilation
g++ -c file.c -o file.o
ar rcs libfile.a file1.o file2.o
g++ -o main main.c -L. -static -lm

# Dynamic compilation
g++ -fPIC -c program.c -o program.o
g++ -shared -o libprogram.so program.o
g++ -o program main.c -L. -lprogram

# Example linking in order
g++ myfile.c \
-I/usr/include -I/usr/include/readline -I../../include \
-L/usr/lib/x86_64-linux-gnu -L../../lib \
-ltosbitAPI-lreadline-lhistory-lncurses \
-o myfile
```
