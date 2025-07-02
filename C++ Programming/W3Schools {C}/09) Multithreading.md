# $\fbox{Chapter 9: MULTITHREADING}$





## **Topic - 1: Multithreading**

### <u>Creating & Joining</u>

```cpp
void func() {
	cout << "Hello from thread!";
}

int main()
{
	thread th(func);        // Assigning function to act as thread.
	th.join();              // Wait for the thread to finish executing.
	
	return 0;
}
```


### <u>Thread IDs</u>

```cpp
thread::id ID = this_thread::get_id();        // 'this_thread' is a namespace
```

---
