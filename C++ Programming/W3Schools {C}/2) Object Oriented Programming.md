# $\fbox{Chapter 2: Object Oriented Programming}$





## **Topic - 1: Objects & Classes**

### **<u>Introduction</u>

- Access specifier in C++ is same as access modifier in C#.
- **<u>Class attribute</u>:** Class members
- Semicolon is necessary after class block.

```cpp
class myClass
{
	public:
		int x;
		string name;
};
```

```cpp
myClass Obj;
```


### <u>Class Methods</u>

```cpp
void myClass::speed(int maxSpeed)
{
	return maxSpeed;
}
```

- To write method the way shown above, it must be first declared in class the regular way.
- Void function can never have a return type, whereas non-void functions may omit return statements if they want to.


### <u>Constructors</u>

- Are always public.
- Can’t have a return value.
- It is a special method!
- Assigning value to object attribute (shortcut).

```cpp
class Cars
{
	public:
		string name;
		string model;
		int year;
		
		Cars(string x, string y, int z) {
			name = x;
			model = y;
			year = z;
		}
};

int main()
{
	Cars car1("Ford", "Mustang", 1969);
}
```

- It is advised to not keep the name of arguments same as attributes.
- There exists a `exist` keyword.


## **Topic - 2: Encapsulation**

### <u>Introduction</u>

- We can use `set()` & `get()` methods to access and modify private attributes.

```cpp
class Employee
{
	public:
		int salary;
	
	private:
		void setSalary(int s) {salary = s;}
		void getSalary() {return salary;}
};
```

- It however is not working at all, I tried.


### <u>Inheritance</u>

- We call it **derived class (child)** and **base class (parent)** in
  C++.

- Done the same way as in C#.

- But you should declare inherited class as **public**, to allow
  operations on it. As shown below:-

- Inheritance **+** providing access specifier to the class:-

<img src="./media/image15.png"
style="width:6.26806in;height:0.26944in" />

**<u>Multiple Inheritance</u>**

- Deriving a child class from multiple parents.

<img src="./media/image16.png"
style="width:6.26806in;height:0.36667in" />

- In this, there **must be no common attribute** among parents.

- Constructors are **not derived**.

- When deriving from multiple parents, it is advised to **not involve**
  any parent attribute in any parent constructor.

**<u>Polymorphism</u>**

- Parameter’s type and quantity **must be same** in each class’s
  overridden methods.

- **virtual** & **override** keywords are used.

<img src="./media/image17.png" style="width:6.26806in;height:1.45in" />

- Never use any **iostream/std** function like **cout** or **cin** for
  **void methods**, else your life will become **hell**!

- Just call **void** methods **directly**.

- And methods with **return type** must use them.

**<u>This Keyword</u>**

- Used to distinguish between **class attribute** & a **method
  variable**.

- Like shown below, value is both an **attribute** & a **local
  variable** in **setValue()**:

<img src="./media/image18.png"
style="width:6.26806in;height:1.88194in" />

**<u>File Handling</u>**

<img src="./media/image19.png"
style="width:6.26806in;height:0.22569in" />

<img src="./media/image20.png"
style="width:6.26806in;height:0.63611in" />

- ***obj_name*** in C++ is similar to ***fptr*** in C.

<img src="./media/image21.png"
style="width:6.26806in;height:0.81111in" />

- ***ios::trunc*** overwrites a file if it **exists** & creates if it
  **doesn’t** exist.

- **Not** using it **won’t** create a file.

- ***ios::app*** is used for append.

- One of the both ***(ios::trunc or ios::app)*** must be selected.

<img src="./media/image22.png"
style="width:6.26806in;height:0.42569in" />

<img src="./media/image23.png"
style="width:6.26806in;height:0.22569in" />

Writing to file using ***ofstream***:-

<img src="./media/image24.png"
style="width:6.26806in;height:0.44375in" />

Reading from file using ***ifstream***:-

<img src="./media/image25.png" style="width:6.26806in;height:0.825in" />

<img src="./media/image26.png"
style="width:6.26806in;height:0.21042in" />

Getting all the lines:-

<img src="./media/image27.png"
style="width:6.26806in;height:0.98056in" />

Moving cursor somewhere:-

<img src="./media/image28.png"
style="width:6.26806in;height:0.23264in" />

<img src="./media/image29.png"
style="width:6.26806in;height:0.62708in" />

Check cursor positions:-

- Read & write are done using separate cursors.

<img src="./media/image30.png"
style="width:6.26806in;height:0.40486in" />

Binary mode:-

<img src="./media/image31.png"
style="width:6.26806in;height:0.41042in" />

- Notice the ***ios::binary*** written.

**<u>Exceptions</u>**

<img src="./media/image32.png"
style="width:6.26806in;height:1.46875in" />

- If our throw is not an identifier, then we can use three dot (…) in
  catch:-

<img src="./media/image33.png"
style="width:6.26806in;height:1.47708in" />

**<u>Memory Management</u>**

- We use **\<cstdlib\>** to include C’s standard library into C++.

<img src="./media/image34.png"
style="width:6.26806in;height:1.00205in" />

**<u>Passing Array Argument</u>**

1.  **With reference:-**

<img src="./media/image35.png"
style="width:6.26806in;height:1.75972in" />

- **arr\[\]** is same as **\*arr**.

2.  **Without reference:-**

- Pass as an element or just use your brain buddy!

**<u>Vectors</u>**

- Declare header file ***\<vector\>***.

- Vector traversal **isn’t** done from beginning, just like **arrays** &
  unlike **linked lists**.

- So vectors are **faster** than linked list.

1.  **Declaration:-**

<img src="./media/image36.png"
style="width:6.26806in;height:0.17639in" />

2.  **Functions with void data types:-**

<img src="./media/image37.png"
style="width:6.26806in;height:0.97014in" />

3.  **Functions with return types:-**

<img src="./media/image38.png"
style="width:6.26806in;height:0.78333in" />

4.  **Iterating/traversing through vectors:-**

<img src="./media/image39.png"
style="width:6.26806in;height:0.62222in" />

**<u>Unordered Map</u>**

- Uses **\<unordered_map\>** library.

- Values are hashed to keys & keys are hashed to indices.

1.  **Declaration:-**

<img src="./media/image40.png"
style="width:3.14656in;height:0.79204in" />

2.  **Putting values:-**

<img src="./media/image41.png"
style="width:6.26806in;height:0.52292in" />

**OR**

<img src="./media/image42.png" style="width:6.26806in;height:0.65in" />

3.  **Traversal/iteration:-**

<img src="./media/image43.png"
style="width:6.26806in;height:0.65069in" />

**OR**

<img src="./media/image44.png"
style="width:6.26806in;height:0.92639in" />

- **begin()** and **end()** are used with an **iterator only** as shown
  above.

- **end()** is place after crossing the last pair in memory.

- It traverses **in reverse**.

- Address operations **don’t** work on unordered maps.

- Time complexity of unordered map is **O(1)**, contrary to **map** with
  **O(log(n))**.

4.  **Function with no return type:-**

<img src="./media/image45.png"
style="width:6.26806in;height:0.18333in" />

5.  **Functions with return type:-**

<img src="./media/image46.png"
style="width:6.26806in;height:0.47639in" />

6.  **Functions to be used in control statements:-**

<img src="./media/image47.png"
style="width:6.26806in;height:0.32222in" />

**<u>Generic</u>**

- **<u>Generic</u>:** Class or function that is defined as a
  **template**.

1.  **Template declaration:-**

<img src="./media/image48.png"
style="width:6.26806in;height:0.34792in" />

**OR**

<img src="./media/image49.png"
style="width:6.26806in;height:0.35417in" />

- Both lines must be written together like this.

- Must be written after **headers** & **using namespaces** (if any).

2.  **Calling function:-**

<img src="./media/image50.png"
style="width:6.26806in;height:0.18333in" />

**OR**

<img src="./media/image51.png"
style="width:6.26806in;height:0.17153in" />

- In this one, compiler decides the data type by itself.

- ***auto*** keyword can’t be used.

- **Same template** data type (**T** here) can be used in multiple
  generics.

- Template **overloading** is possible.

3.  **For passing objects as arguments:-**

<img src="./media/image52.png"
style="width:6.26806in;height:0.79931in" />

4.  **Using templates for classes:-**

<img src="./media/image53.png"
style="width:6.26806in;height:1.11458in" />

**<u>Command Line Arguments in C/C++</u>**

<img src="./media/image54.png"
style="width:6.26806in;height:0.21806in" />

- ***argc*** = Argument count, ***argv*** = Argument values

- ***argc*** is by default ***1***, which is the **file name** itself.

- ***argv\[0\]*** is always the **file’s name**.

- **Code written in command prompt (example):**

<img src="./media/image55.png"
style="width:6.26806in;height:0.46319in" />

- **Linked list program run using *cmd*:**

<img src="./media/image56.png"
style="width:6.26806in;height:1.47059in" />

**<u>Some Newly Observed Keywords</u>**

<img src="./media/image57.png"
style="width:6.26806in;height:0.79444in" />

**<u>C/C++ Libraries</u>**

- The **object files** work as **intermediate** between a program and
  library.

- **<u>Dependency walker</u>:** A tool used for troubleshooting
  incompatibleness of ***.dll*** files.

- Generally, **static files** create **larger** binary files & thus
  occupies **more space**.

- In whole library process, ***gcc*** is used for **C** files &
  ***g++*** is used for **C++** files.

- Windows uses ***.obj*** extension for **object files**.

- Linking is done for running an **executable** which uses library(s).

- We can remove the including statement importing the library at **final
  stage** of project.

**<u>Static Linking & Static Libraries</u>**

Creating (developer’s job):-

- **<u>Step 1</u>:** Create a **source file** containing
  **implementations** of the library:

<img src="./media/image58.png"
style="width:6.26806in;height:2.40417in" />

***\*We can create such multiple files\****

- **<u>Step 2</u>:** Create a **header file** with only **function
  definitions**:

<img src="./media/image59.png"
style="width:6.26806in;height:2.02361in" />

- **<u>Step 3</u>:** **Compile** library file(s) into **object files**:

<img src="./media/image60.png"
style="width:6.26806in;height:0.22847in" />

***\*Gotta do this one by one for each .c file\****

- **<u>Step 4</u>:** Create **static libraries**:

<img src="./media/image61.png"
style="width:6.26806in;height:0.22361in" />

***\*For multiple .obj files, add all file names in the command in
line\****

Linking (user’s job):-

- **<u>Step 1</u>:** Create a **user program** importing our library:

<img src="./media/image62.png"
style="width:6.26806in;height:1.3875in" />

- **<u>Step 2</u>:** **Compile** the user program into an **object
  file**:

<img src="./media/image63.png"
style="width:6.26806in;height:0.24653in" />

- **<u>Step 3</u>:** **Linking** user program to **static library**:

<img src="./media/image64.png"
style="width:6.26806in;height:0.24306in" />

***\*This creates an executable of user program which can be run\****

**<u>Things to Take Under Consideration</u>**

- It’s a good practice to add this to **ensure compatibility** of user’s
  **C/C++ version**.

<img src="./media/image65.png"
style="width:6.26806in;height:0.26667in" />

- Use ***extern "C"*** for **functions** and **variables** (in **header
  files** only).

- But **don’t** use them for **class** or its **members**.

Project specific:-

- During testing phase, include with ***.c/.cpp*** file.

- Then after completing the project, **before linking** make them
  ***.h/.hpp***.

**<u>Dynamic/Shared Files & Linking</u>**

Creating:-

- **<u>Step 1</u>:** Create a **C/C++** file that contains
  **implementations** of the library:

<img src="./media/image66.png"
style="width:6.26806in;height:2.43819in" />

***\*We can create such multiple files\****

- **<u>Step 2</u>:** Create a **header file** with only **function
  definitions**:

<img src="./media/image67.png"
style="width:6.26806in;height:3.24028in" />

- **<u>Step 3</u>:** **Compile** library file(s) into **object files**:

<img src="./media/image68.png"
style="width:6.26806in;height:0.24375in" />

***\*Gotta do this one by one for each .c file\****

- **<u>Step 4</u>:** Create **dynamic/shared** libraries:

<img src="./media/image69.png"
style="width:6.26806in;height:0.22083in" />

***\*For multiple .obj files, add all file names in the command in
line\****

Linking (user’s job):-

- **<u>Step 1</u>:** Create a **user program** importing our library:

<img src="./media/image62.png"
style="width:6.26806in;height:1.3875in" />

- **<u>Step 2</u>:** Compile the **user program** into an **object
  file**:

<img src="./media/image70.png"
style="width:6.26806in;height:0.26597in" />

- **<u>Step 3</u>:** **Linking** **user program** to **dynamic
  library**:

<img src="./media/image71.png"
style="width:6.26806in;height:0.19931in" />

***\*This creates an executable of user program which can be run\****

**<u>Library Structure</u>**

Header file:-

- Guard **macro**.

- ***\_\_cplusplus***

- ***\_\_declspec(dllexport/dllimport)*** \[if **dynamic**\].

- Required standard **header files**.

- Namespaces.

- ***extern*** keyword.

- Declaration of **functions**, **structures** and **global variables**
  (if any).

- Declaration of class’s **public** members.

- Declaration & **definition** of class’s **private** members.

Source file:-

- Guard **macro**.

- Inclusion of **header file**.

- **Implementation** of declarations in header file.

- **Scope resolution operator** (***::***) for namespace references.

User program:-

- Inclusion of **source file**.

**<u>Dynamic Class Objects</u>**

<img src="./media/image72.png"
style="width:6.26806in;height:1.36042in" />

- **Destructors** of ***dynamic class objects*** are **not** called
  automatically when the program ends.

**<u>Multithreading</u>**

Creation & join():-

<img src="./media/image73.png"
style="width:6.26806in;height:2.30486in" />

Thread ID:-

<img src="./media/image74.png"
style="width:6.26806in;height:0.24444in" />

**<u>Smart Pointers</u>**

<img src="./media/image75.png"
style="width:6.26806in;height:0.21111in" />

- ***Pointer*** is the **owner** & ***dynamic variable*** is **owned**.

- **<u>Unique pointers</u>:** Only **one** pointer can own a variable.

<img src="./media/image76.png"
style="width:6.26806in;height:1.16458in" />

- **<u>Shared pointers</u>:** Ownership of a variable is shared among
  **multiple** pointers.

<img src="./media/image77.png"
style="width:6.26806in;height:1.50347in" />

- **<u>Weak pointers</u>:** Share reference to a ***shared pointer***
  but **doesn’t** participate in ownership of a variable.

- So, a ***weak pointer*** **can’t** manipulate value of the variable it
  is referring to through ***shared pointer***.

- Instead, it just **watches & tracks** the lifetime of an object
  pointed by ***shared pointer***.

<img src="./media/image78.png"
style="width:6.26806in;height:0.97292in" />
