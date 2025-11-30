# $\fbox{Chapter 2: OBJECT-ORIENTED PROGRAMMING}$





## **Topic - 1: Objects & Classes**

### <u>Objects & Classes</u>

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
			this->name = x;
			this->model = y;
			this->year = z;
		}
};

int main()
{
	Cars car1("Ford", "Mustang", 1969);
}
```

- It is advised to not keep the name of arguments same as attributes if not using `this`.
- There exists an `exist` keyword.


### <u>Encapsulation</u>

- We can use `set()` & `get()` methods to access and modify private attributes.

```cpp
class Employee
{
	private:
		int salary;
	
	public:
		void setSalary(int s) {this->salary = s;}
		int getSalary() {return this->salary;}
};
```


### <u>Inheritance</u>

- We call it derived class (child) and base class (parent) in C++.
- Done the same way as in C#.
- But you should declare inherited class as public, to allow operations on it as shown below.
- Inheritance & providing access specifier to the class.

```cpp
class Job: public Employee {};
```


### <u>Multiple Inheritance</u>

- Deriving a child class from multiple parents.

```cpp
class MyChildClass: public MyClass, public MyOtherClass {
};
```

- In this, there must be no common attribute among parents.
- Constructors are not derived.
- When deriving from multiple parents, it is advised to not involve any parent attribute in any parent constructor.


### <u>Polymorphism</u>

- Parameter’s type and quantity must be same in each class’s overridden methods.
- `virtual` & `override` keywords are used.

```cpp
class Parent {
	public:
		virtual string meth() {return "Papa";}
};

class Child: public Parent {
	public:
		string meth() override {return "Beta";}
}
```


### <u>This Keyword</u>

- Used to distinguish between class attribute & a method variable.
- Like shown below, value is both an attribute & a local variable in `setValue()`.

```cpp
class MyClass
{
	public:
		int value = 10;

		int setValue(int n)
		{
			int value;
			this -> value = n;
			
			return this -> value*2;
		}
}
```

---
