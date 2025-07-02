# $\fbox{Chapter 10: SMART POINTERS}$





## **Topic - 1: Smart Pointers**

```cpp
#include <memory>
```

- Pointer is the owner & dynamic variable is owned.



## **Topic - 2: Unique Pointers**

- Only one pointer can own a variable.

```cpp
unique_ptr<int> ptr(new int(7));    // Initialization & assigning

ptr.reset(new int(9));       // Owning different variable
int *raw = ptr.release();    // Transfers ownership to a raw ptr
ptr.get();                   // Accesses address pointer points to
ptr2 = move(ptr);    // Transfers ownership to other unique_ptr
```



## **Topic - 3: Shared Pointers**

- Ownership of a variable is shared among multiple pointers.

```cpp
shared_ptr<int> ptr(new int(7));    // Initialization & assigning
shared_ptr<int> ptr2 = ptr;         // Sharing ownership

ptr.reset(new int(9));    // Owning different variable
ptr.get();                // Accesses address pointer points to
ptr.use_count();    // Returns number of owners owning variable
ptr.unique();       // Checks if the pointer is sole owner
ptr.swap(ptr2);     // Ownership transfer from 'ptr' to 'ptr2'
```



## **Topic - 4: Weak Pointers**

- Share reference to a shared pointer but doesn’t participate in ownership of a variable.
- So, a weak pointer can’t manipulate value of the variable it is referring to through shared pointer.
- Instead, it just watches & tracks the lifetime of an object pointed by shared pointer.

```cpp
shared_ptr<int> shared(new int(42));
weak_ptr<int> weak = shared;

weak.lock();           // Tells address of its 'shared_ptr'
weak.expired();        // Tells if the object still exists
```

---
