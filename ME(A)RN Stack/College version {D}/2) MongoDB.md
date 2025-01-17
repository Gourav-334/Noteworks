# $\fbox{Chapter 2: MONGODB}$





## **Topic - 1: Basic Concepts**

### <u>Introduction</u>

- MongoDB is a document-oriented NoSQL database.
- It can store large volumes of unstructured & semi-structured data.
- MongoDB doesn't store data in JSON files, but in files which resemble JSON syntax.


### <u>Key Features</u>

- Document-oriented
- NoSQL
- Scalability
- Indexes
- Aggregation framework
- Data replication
- High-availability
- Ad-Hoc queries
- Open source



## **Topic - 2: NoSQL Database**

### <u>Introduction</u>

- NoSQL is also referred as "Not Only SQL".
- Relational databases store data in tabular manner.
- They also have predefined schema.
- However, NoSQL databases store data in non-tabular format & a defined schema.
- This unstructured hierarchy helps it store rapidly changing data.


### <u>Features Of NoSQL</u>

#### Advantages:

- Flexible schema model
- Scalability
- Complex data types
- Large storage volume
- Fast
- Fault-tolerant
- Real-time data processing
- Horizontal scalability
- Variety styles of documents
- Distributed & highly available
- High-performance

#### Disadvantages:

- Lack of ACID transactions
- Learning curve
- Limited query capabilities
- Poor data consistency
- Non-standard structure


### <u>Types Of NoSQL Databases</u>

- **<u>Document database</u>:** Stores data in semi-structured document formats like JSON, XML etc.
- **<u>Key-value stores</u>:** Stores data as key-value pairs.
- **<u>Column family stores</u>:** Sets of columns which are treated as single unit.
- **<u>Graph databases</u>:** Data are stored as nodes & edges.

>**<u>NOTE</u>:**
>1. NoSQL databases are primarily used to store unstructured data.
>2. Social connection like networks are stored in graph.



## **Topic - 3: CRUD Operation**

### <u>Create Operation</u>

#### Methods:

- `db.collection_name.insertOne()` - Inserts single document to collection.
- `db.collection_name.insertMany()` - Inserts multiple documents to collection.
