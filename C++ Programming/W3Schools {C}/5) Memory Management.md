# $\fbox{Chapter 5: MEMORY MANAGEMENT}$





### <u>Memory Management</u>

- We use `<cstdlib>` to include C’s standard library into C++.

```cpp
ptr = new int;           // ptr = malloc(sizeof(int));
delete ptr;              // free(ptr);

ptr = new int[n];        // ptr = malloc(n*sizeof(int));
delete[] ptr;            // "Bhai ye to thaa hi nahi"
```


### <u>Passing Array Argument</u>

#### With reference:

```cpp
void func(int arr[]) {
	cout << arr[i];            // 'i' is some index number.
}

int main()
{
	int arr[5] = {0,1,2,3,4};
	func(arr);                 // 'arr' is base address of array.
}
```

- `arr[]` is same as `*arr`.

#### Without reference:

- Pass as an element or just use your brain buddy!

---
