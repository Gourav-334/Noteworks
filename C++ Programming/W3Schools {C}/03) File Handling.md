# $\fbox{Chapter 3: FILE HANDLING}$





## **Topic - 1: File Handling**

### <u>Introduction</u>

```cpp
#include <fstream>
```

```cpp
fstream obj_name;             // Both read & write mode.
ifstream obj_name;            // Read mode
ofstream obj_name;            // Write mode
```

- `obj_name` in C++ is similar to `fptr` in C.

```cpp
obj_name.open("corpus.txt");    // By default in read & write mode.

/* Manully opening with read & write mode. */
obj_name.open("corpus.txt", ios::in | ios::out | ios::trunc);
```

- `ios::trunc` overwrites a file if it exists & creates if it doesn’t exist.
- Not using it won’t create a file.
- `ios::app` is used for append.
- One of the both (`ios::trunc` or `ios::app`) must be selected.

```cpp
if (obj_name.is_open())       {cout << "Opened successfully!";}
else if (!obj_name.is_open()) {cerr << "Can't open the file";}
```

```cpp
obj_name.close();
```

### <u>Writing To File</u>

```cpp
file << "I am Gourav Kumar Mallick." << endl;
file << "I enjoy C++";
```


### <u>Reading From File</u>

```cpp
ifstream file("sample.txt");    // Both defining 'obj' & opening.

string line;
getline(file, line);    // getline(fetch_location, paste_location)
```


### <u>Getting All The Lines</u>

```cpp
while (file.good())        // good() tells if EOF has reached.
{
	getline(file, line);
	cout << line;
}
```


### <u>Moving Cursor Somewhere</u>

```cpp
file.seekg(0);        // Beginning of the file.
```

```cpp
file.seekg(5, ios::beg);    // Means how many bytes from cursor.
file.seekg(1, ios::cur);    // 1 byte after current position.
file.seekg(0, ios::end);
```


### <u>Check Cursor Positions</u>

- Read & write are done using separate cursors.

```cpp
cout << file.tellg() << endl;    // g stands for 'get' (read cursor)
cout << file.tellp();            // p stands for 'put' (write cursor)
```


### <u>Binary Mode</u>

```cpp
fstream file;
file.open("sample.bin", ios::binary | ios::in | ios::out | ios::trunc);
```

- Notice the `ios::binary` written.

---
