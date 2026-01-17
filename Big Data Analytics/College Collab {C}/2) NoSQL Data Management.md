# $\fbox{Chapter 2: NOSQL DATA MANAGEMENT}$  





## **Topic - 1: Introduction to NoSQL**

### <u>Introduction</u>

- NoSQL stands for ***"Not Only SQL"***.
- A non-relational DBMS that does not use tables for storing data.


### <u>Offerings Of NoSQL</u>

- Horizontal scaling
- High availability
- Efficient data access for large-scale applications.
- Common data formats: Key-Value, Document, Column-Family, Graph
- Big data & real-time applications
- Cloud environments
- Unstructured / semi-structured data



## **Topic - 2 Why NoSQL?**

### <u>Drawbacks In RDBMS</u>

- Cannot handle large-scale distributed data.
- Inefficient with non-tabular data (e.g., social networks, sensor data).


### <u>Need For NoSQL</u>

- Need for flexible schema
- High write throughput
- Support for horizontal scaling, i.e. distributed systems
- Reduced latency



## **Topic - 3: CAP Theorem (Eric Brewer)**

### <u>Introduction</u>

- **<u>States</u>:** In a distributed system, only **2 out of 3** properties can be achieved of **CAP**.
- **Consistency (C)**: All nodes see the same data at the same time.
- **Availability (A)**: Every request gets a (non-error) response.
- **Partition Tolerance (P)**: System continues to operate despite network partitions.


### <u>Scenarios</u>

- **CA (no partition tolerance) -** Single node systems, not fault-tolerant.
- **CP (no availability) -** Systems give up availability to preserve consistency during partition.
- **AP (no consistency) -** Systems favor availability, allow eventual consistency.



## **Topic - 4: BASE Model (alternative to ACID)**

### <u>Introduction</u>

| Property                 | BASE Model                      | Description                            |
| ------------------------ | ------------------------------- | -------------------------------------- |
| **Basically Available**  | System guarantees availability  | Even during partial failures           |
| **Soft State**           | State may change over time      | No immediate consistency needed        |
| **Eventual Consistency** | System reaches consistent state | After some time, all replicas converge |


### <u>ACID v/s BASE</u>

- **ACID** prioritizes consistency, integrity $\rightarrow$ good for banking.
- **BASE** prioritizes availability and partition tolerance $\rightarrow$ better for social networks, streaming apps.



## **Topic - 5: Types of NoSQL Databases**

### <u>Key-Value Store</u>

$$ \text{Data = Key + Associated value} $$

- Very fast read/write
- Schema-less
- **For example -** Redis, DynamoDB, Riak, etc


### <u>Document Store</u>

- Stores documents (JSON, BSON, XML)
- Supports nested values, semi-structured data
- Indexable fields
- **For examples -** MongoDB, CouchDB, etc.


### <u>Column-Family Store</u>

- Stores data in column groups (column families)
- Optimized for queries on large data sets
- Each row can have different columns
- **For examples -** Cassandra, HBase, etc.


### <u>Graph DB</u>

$$ \text{Graph = Nodes (entities) + Edges (relationships)} $$

- Ideal for social networks & recommendation engines.
- Queries traverse graph paths,
- **For examples -** Neo4j, ArangoDB, etc.



## **Topic - 6: Pros & Cons of NoSQL**

### <u>Advantages</u>

- Scalability (horizontal)
- Flexibility in schema design
- High throughput and performance
- Better suited for big data workloads
- Supports distributed architecture


### <u>Disadvantages</u>

- Lacks standardization
- Weaker consistency guarantees
- Complex querying (compared to SQL)
- Not ideal for relational data with strict constraints
- Difficult transaction support (ACID not guaranteed)



## **Topic - 8: Use Cases of NoSQL**

- Real-time analytics
- Social networks
- Internet of Things (IoT)
- Recommendation engines
- Mobile & gaming apps
- Content management systems



## **Topic - 9: Conclusion**

- NoSQL provides flexible, scalable alternatives to RDBMS.
- Choice depends on nature of data, consistency v/s availability needs, scalability requirements, etc.

---
