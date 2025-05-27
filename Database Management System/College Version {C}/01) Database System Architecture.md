# $\fbox{Chapter 1: DATABASE SYSTEM ARCHITECTURE}$





## **Topic – 1: Introductory Concepts**

### <u>Introductory Terms</u>

- **<u>Knowledge</u>:** Proper collection of information.


### <u>File Processing System (FPS)</u>

#### Advantages:

- Cost friendly, being free or inbuilt.
- Can be easily learned and used, being basic.
- High scalability.

#### Disadvantages:

- Different file formats cause problem accessing.
- Duplication of data.
- Difficult to accessing data.
- Adding new features requires changes in program, and making this change is difficult.
- Failure during database update leads to inconsistent state.
- Concurrent access by multiple users.
- Limited data sharing.


### <u>Purpose Of DBMS</u>

- No need of paper work (compactness).


### <u>Benefits Of DB Approach</u>

- Less redundancy
- Restriction of unauthorized ID
- Backup & recovery service
- Multiple user access
- Defined integrity constraints
- Data isolation is not an issue
- Guaranteed atomicity
- More secured
- Less program maintenance required
- Better backup facility


### <u>Basic DBMS Terms</u>

- **<u>Data dictionary</u>:** Information repository containing metadata.
- **<u>Data Warehouse</u>:** Information repository containing data (not metadata).



## **Topic – 2: ANSI SPARC Standards**

### <u>Three Levels Of ANSI SPARC Database System</u>

- **<u>Schema</u>:** Anything that describes logical structure of something.


### <u>Internal level (Physical Schema)</u>

- This complex data is called abstraction.
- Contains internal schema.


### <u>Conceptual level (logical view)</u>

- It also describes what data must be stored, and also sets the relationships among those data.
- But here the internal information like internal structure and abstraction are hidden.
- Programmers and data administrators work at this level.


### <u>External Level (View Level)</u>

- Contains external schema and other schemas too, collectively called subschema.
- **<u>Mapping</u>:** Communication in between these levels (receiving & transmitting).
- **<u>Data independence</u>:** Feature that allows someone to modify the schema definition in one level, without affecting the higher level.


### <u>Physical Data independence</u>

- Modifying physical schema without affecting logical (conceptual) schema.
- Changes at internal levels are generally done to improve performance of program.


### <u>Modifications At Internal Level</u>

- File structures
- Compression techniques
- Hashing algorithm
- Storage devices
- **<u>Hashing algorithm</u>:** It is an algorithm used for making data unreadable using mathematical functions.



## **Topic – 3: DBMS Users**

### <u>Types Of Database Users</u>

1. **<u>Naïve users</u>:** End users.
2. Application programmers
3. **<u>Sophisticated users</u>:** Users who interact with database without using any program, but by tools like SQL.
4. **<u>Specialized users</u>:** User who uses administrative tools.


### <u>Role Of Database Administrator (DBA)</u>

- Defines logical schema.
- Decides way to represent data.
- Decides how the data will be accessed.
- Takes steps for security of DB.
- Controls authorization over data.
- Provides the required data to the user.
- Assists the application programmer.
- Maintains good performance by making changes at different schemas.
- Responsible for proper backup of the databases.

---
