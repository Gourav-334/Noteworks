# $\fbox{Chapter 4: STRUCTURES \& UNIONS}$





## **Topic – 1: Structures**

### <u>General Information</u>

- Structures end with a semicolon.
- Structure is also known as composite/aggregate data type.
- **<u>Composite data type</u>:** A data type which can contain collection of multiple elements.


### <u>Ways To Define</u>

```c
struct student s1 = {"Gourav", 20};
struct student s2 = {.age=21, .name="Atharv"};
```


### <u>Structure Value Transfer</u>

```c
struct student s3 = s2;
```


### <u>Pointer To Structure</u>

```c
ptr = &student;
ptr2 = (*student).age;    // Same as 'x = student -> age'.
```


### <u>Array Of Structures</u>

```c
struct cuboid measure[3] = {{1,2,3},{4,5,6},{7,8,9}};
```



## **Topic – 2: Unions**

### <u>General Information</u>

- Its memory location is occupied by only one member at a time.
- Union too uses arrow `->` to refer to its dynamically allocated members.


### <u>Defining Union Inside Structure</u>

```c
union {int id; char name[20];} employee;
```

---
