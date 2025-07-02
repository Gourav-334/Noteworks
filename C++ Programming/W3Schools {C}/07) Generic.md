# $\fbox{Chapter 7: GENERIC}$





### <u>Introduction</u>

- **<u>Generic</u>:** Class or function that is defined as a template.


### <u>Template Declaration</u>

```cpp
template <class T>

T add(T x, T y) {
	return x+y;
}
```

$$ \text{OR} $$

```cpp
template <typename T>

T add(T x, T y) {
	return x+y;
}
```

- Both lines must be written together like this.
- Must be written after headers & using namespaces (if any).


### <u>Calling Function</u>

```cpp
cout << add<int>(3,5);
```

$$ \text{OR} $$

```cpp
cout << add(3,5);
```

- In this one, compiler decides the data type by itself.
- `auto` keyword can’t be used.
- Same template data type (`T` here) can be used in multiple generics.
- Template overloading is possible.


### <u>Passing Object Arguments</u>

```cpp
template <typename T>

T printDataofBase(T &obj)
{
	obj.toString();
}
```


### <u>Templates For Classes</u>

```cpp
template <class T>

class className
{
	/*
	 * Class Definition 
	 * We can use T as a type inside this class. 
	 */
}
```

---
