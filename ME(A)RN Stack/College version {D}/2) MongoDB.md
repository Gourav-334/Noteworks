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

#### `db.collection_name.insertOne()`:

- Inserts single document to collection.

```json
db.user.insertOne({
	sno: 1,
	name: "Gourav",
	age: 21
})
```

#### `db.collection_name.insertMany()`:

- Inserts multiple documents to collection.

```json
db.user.insertMany([
	{
		name: "Gourav",
		special: "System programming",
		religion: "Hindu"
	},

	{
		name: "Wong De Piht",
		special: "Game development",
		religion: "Buddhist"
	}
])
```

- MongoDB generates `_id` itself if not provided.


### <u>Read Operation</u>

#### Get all documents:

- We use `db.collection_name.find()` to get all documents from collection.

```json
db.Office.find()
```

#### Get limited documents:

```json
db.Office.find().limit(5);
```

#### Skip documents:

```json
db.Office.find().skip(7);
```

- This command skips first 7 documents.

>**<u>NOTE</u>:**
>We can also chain multiple commands like `limit()` & `skip()`.

#### Count documents:

```json
db.Office.find().count();
```

#### Get specific field:

```json
db.Office.find({},{"age":20, "special":"embedded"})
```

#### Filtering documents:

```json
db.Office.find({"age":20, "special":"embedded"})
```

#### Logical operators:

```json
db.Office.find({$or:[{name:"Aarav", age:9}]});
```

#### Comparison operators:

```json
db.user.find({age:{$gt:20}});
```

>**<u>NOTE</u>:**
>Adding `;` is optional but advised for cleaner code.


### <u>Update Operations</u>

#### Updating single document:

- `updateOne` just updates first encountered document.

```json
db.Office.updateOne(
	{name:"Aayush"},
	{$set:{age:21, branch:"CSE"}}
);
```

#### Updating many documents:

- `updateMany()` command updates all the documents matching entered field.


### <u>Delete Operation</u>

#### Delete single document:

```json
db.Office.deleteOne({name:"Ankit"});
```

- Similarly, there is another command called `deleteMany()`.



## **Topic - 4: Indexing**

### <u>Introduction</u>

- **<u>Index</u>:** A data structure implemented to cut data retrieval time.
- It is similar to paging in RDBMS like SQL.


### <u>Types Of Index</u>

- Single field index
- Compound index
- Text index
- Geospatial index


### <u>Creating Index</u>

```json
db.Office.createIndex({name:1});
```

- This command creates index based on field `name`.
- `1` means ascending order, while `-1` means descending order.


### <u>Verifying Index</u>

```json
db.Office.getIndexes();
```

- Shows set indexes.



## **Topic - 5: Aggregation Framework**

### <u>Introduction</u>

- These are actually text indexing commands.
- Compound indexing is all about grouped indexing.


### <u>Matching Values</u>

```json
db.Office.aggregate([
	{$match:{field:value}}
]);
```


### <u>Grouping</u>

```json
db.Office.aggregate([
	{$group:{_id:"$category", total:{$sum:"$quantity"}}}
]);
```


### <u>Chaining Aggregate Functions</u>

```json
db.Office.aggregate([
	{$match:{field:value}},
	{$group:{_id:"$category", total:{$sum:"$quantity"}}}
]);
```



## **Topic - 6: Schema Design & Data Modeling**

### <u>Introduction</u>

- For making a efficient & scalable application, a schema must be maintained in MongoDB databases, though it has no fixed schema.
- MongoDB stored data in BSON format.


### <u>Steps For Data Modeling</u>

1. Know about data & thus required schema.
2. Perform less normalizations as they reduce performance in MongoDB.
3. For less complex relation among data, embed them.
4. For more complex relation among data, reference them.
5. Perform frequent indexing to improve read performance, but be aware as it also reduces write speed.
6. Choose an appropriate shard key, which defines how your data is spread.
7. Chain multiple commands for more atomic & secured operations.
8. Use MongoDB version 3.6 or later which has feature for defining & validating schema.
9. Avoid pushing or modifying large arrays, as they slow down the performance.

---
