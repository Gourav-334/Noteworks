# TCS IPA Java Cheat Sheet

> Focus: Core Java, OOP, Collections, Exceptions, Strings, Arrays, and basic language syntax.

---

# 1. Java Basics

- Platform Independent (JVM)
- Object-Oriented
- Strongly Typed
- Compiled to Bytecode

#### Flow:

```
.java
↓
javac
↓
.class (Bytecode)
↓
JVM
↓
Execution
```

---

# 2. JDK vs JRE vs JVM

| Component | Purpose |
|-----------|---------|
| JVM | Executes bytecode |
| JRE | JVM + Libraries |
| JDK | JRE + Compiler + Tools |

---

# 3. Java Program

```java
class Main {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

---

# 4. Variables

```java
int age = 20;
double pi = 3.14;
char grade = 'A';
boolean flag = true;
String name = "John";
```

---

# 5. Primitive Data Types

| Type | Size |
|------|------|
| byte | 1 byte |
| short | 2 bytes |
| int | 4 bytes |
| long | 8 bytes |
| float | 4 bytes |
| double | 8 bytes |
| char | 2 bytes |
| boolean | JVM dependent |

---

# 6. Operators

Arithmetic

```
+
-
*
/
%
```

Comparison

```
==
!=
<
>
<=
>=
```

Logical

```
&&
||
!
```

---

# 7. Control Statements

If

```java
if(x>0){}
```

Switch

```java
switch(choice){}
```

Loops

```java
for
while
do-while
```

---

# 8. Arrays

```java
int[] a = new int[5];
```

Enhanced loop

```java
for(int x : a)
```

Length

```java
a.length
```

---

# 9. Methods

```java
int add(int a,int b) {
    return a+b;
}
```

---

# 10. Classes & Objects

```java
class Car {
    String model;
}

Car c = new Car();
```

---

# 11. Constructor

Default

```java
Car(){}
```

Parameterized

```java
Car(String name){}
```

Constructor has **no return type**.

---

# 12. this Keyword

Refers to current object.

```java
this.name = name;
```

---

# 13. OOP Pillars

### Encapsulation

Hide data.

```java
private int age;
```

---

### Inheritance

```java
class Dog extends Animal
```

---

### Polymorphism

Method Overloading

```java
add(int)
add(double)
```

Method Overriding

```java
@Override
```

---

### Abstraction

```java
abstract class Animal
```

Interface

```java
interface Shape
```

---

# 14. Access Modifiers

| Modifier | Same Class | Package | Subclass | Other |
|-----------|------------|----------|-----------|-------|
| private | ✓ | ✗ | ✗ | ✗ |
| default | ✓ | ✓ | ✗ | ✗ |
| protected | ✓ | ✓ | ✓ | ✗ |
| public | ✓ | ✓ | ✓ | ✓ |

---

# 15. Static

Belongs to class.

```java
static int count;
```

Call

```java
ClassName.method();
```

---

# 16. final

- Variable cannot change.
- Method nannot override.
- Class cannot inherit.

---

# 17. String

- Immutable.

#### Create:

```java
String s = "Hello";
```

#### Methods:

```java
length()

charAt()

substring()

equals()

equalsIgnoreCase()

contains()

replace()

trim()

toUpperCase()

toLowerCase()
```

---

# 18. StringBuilder

- Mutable string.

```java
StringBuilder sb = new StringBuilder();
```

#### Methods:

```
append()
insert()
delete()
reverse()
```

---

# 19. Exception Handling

```java
try {
}

catch(Exception e) {
}

finally {
}
```

Throw

```java
throw new Exception();
```

---

# 20. Checked vs Unchecked

#### Checked:

- Compile time

Examples

```
IOException
SQLException
```

#### Unchecked:

- Runtime

Examples

```
ArithmeticException
NullPointerException
ArrayIndexOutOfBoundsException
```

---

# 21. Collections

List

```
ArrayList
LinkedList
```

Set

```
HashSet
TreeSet
```

Map

```
HashMap
TreeMap
```

Queue

```
PriorityQueue
```

---

# 22. ArrayList

```java
ArrayList<Integer> list = new ArrayList<>();
```

Methods

```
add()
remove()
get()
set()
size()
contains()
```

---

# 23. HashMap

```java
HashMap<Integer,String> map = new HashMap<>();
```

Methods

```
put()
get()
remove()
containsKey()
keySet()
```

---

# 24. Inheritance Keywords

```
extends
implements
```

---

# 25. Interface

```
Multiple inheritance supported.
```

Example

```java
interface Animal {
}
```

---

# 26. Abstract Class

#### Can contain:

- Abstract methods
- Concrete methods

Cannot instantiate.

---

# 27. Wrapper Classes

```
int → Integer
double → Double
char → Character
boolean → Boolean
```

---

# 28. File Handling

```java
File
FileReader
FileWriter
BufferedReader
Scanner
```

---

# 29. Packages

Import

```java
import java.util.*;
```

---

# 30. Common java.lang Classes

```
Object
String
Math
System
Integer
Double
```

---

# 31. Scanner

```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
String s = sc.nextLine();
```

---

# 32. Common Exceptions

```
NullPointerException
ArithmeticException
ClassCastException
IOException
NumberFormatException
ArrayIndexOutOfBoundsException
```

---

# 33. Common MCQ Topics

✓ OOP
✓ Constructor
✓ this
✓ static
✓ final
✓ String
✓ StringBuilder
✓ Arrays
✓ Loops
✓ Access modifiers
✓ Inheritance
✓ Interface
✓ Abstract class
✓ Exception handling
✓ Collections
✓ ArrayList
✓ HashMap
✓ Scanner
✓ Packages
✓ Wrapper classes

---

# Frequently Asked MCQs

**Which method starts a Java program?**

```java
main()
```

---

**Which keyword creates an object?**

```java
new
```

---

**Which class stores dynamic arrays?**

```
ArrayList
```

---

**Which collection stores unique elements?**

```
HashSet
```

---

**Which collection stores key-value pairs?**

```
HashMap
```

---

**Is String mutable?**

```
No
```

---

**Is StringBuilder mutable?**

```
Yes
```

---

**Can constructors have return types?**

```
No
```

---

**Can interfaces have constructors?**

```
No
```

---

**Can Java inherit multiple classes?**

```
No
```

---

**Can Java implement multiple interfaces?**

```
Yes
```

---

# Last-Minute Revision

✓ JVM executes bytecode
✓ JDK = JRE + Compiler
✓ Java is object-oriented
✓ String is immutable
✓ StringBuilder is mutable
✓ ArrayList → Dynamic array
✓ HashSet → Unique values
✓ HashMap → Key-value pairs
✓ extends → Inheritance
✓ implements → Interface
✓ static → Class member
✓ final → Cannot modify/override/inherit
✓ private → Same class only
✓ public → Everywhere
✓ try-catch-finally → Exception handling
✓ Constructor name = Class name
✓ Constructor has no return type
✓ new creates objects
✓ Scanner reads input
✓ Collections are in `java.util`
