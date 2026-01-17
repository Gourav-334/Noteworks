# $\fbox{Chapter 4: BASICS OF HADOOP}$





## **Topic - 1: Introduction**

### <u>Definition</u>

- **Apache Hadoop**: Open-source framework for **distributed storage and processing** of large datasets across clusters of commodity hardware.
- Developed by **Doug Cutting** and **Mike Carafella (2005)**.
- Named after Cutting’s son’s **toy elephant**.


### <u>Objective</u>

- Efficient handling of **big data** (structured, semi-structured, unstructured).
- Fault-tolerant, scalable, and high-throughput system.

![Hadoop Ecosystem Overview](Big%20Data%20Analytics/College%20Collab%20{C}/media/image4.png)



## **Topic - 2: Distributed File System (DFS)**

### <u>Concept</u>

- Classical file system distributed across multiple machines.
- Hidden distribution layer — clients experience a unified system view.
- Provides **high throughput** and **fault tolerance**.


### <u>Example Use Case (India)</u>

- **Aadhaar Database**: Requires matching 10 fingerprints, 2 irises, and demographics for each record.
- Handles 600 trillion comparisons daily using Hadoop.

![Distributed File System Concept](Big%20Data%20Analytics/College%20Collab%20{C}/media/image6.png)



## **Topic - 3: Scalability**

### <u>Introduction</u>

| Type                       | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| **Vertical (Scale-up)**    | Increase resources (RAM/CPU) of a single node. Requires downtime. |
| **Horizontal (Scale-out)** | Add nodes dynamically without downtime.                           |


### <u>Fault Tolerance</u>

- Data replication across nodes ensures no single point of failure.

![Vertical vs Horizontal Scaling](Big%20Data%20Analytics/College%20Collab%20{C}/media/image5.png)



## **Topic - 4: Hadoop Characteristics**

- **High Scalability & Availability**
- **Fault-tolerance**
- Uses **commodity hardware**
- Moves **computation to data**, reducing network overhead.



## **Topic - 5: RDBMS vs Hadoop**

| Feature               | RDBMS                               | Hadoop                                    |
| --------------------- | ----------------------------------- | ----------------------------------------- |
| **Data Format**       | Structured only                     | Structured, semi-structured, unstructured |
| **Volume**            | GB-level                            | TB–PB level                               |
| **Processing Type**   | OLTP (real-time)                    | OLAP (batch)                              |
| **Transaction Model** | ACID                                | BASE                                      |
| **Storage**           | Table-based                         | File/block-based                          |
| **Scalability**       | Vertical                            | Horizontal                                |
| **Performance**       | Low throughput                      | High throughput                           |
| **Consistency Model** | Strong (Consistency > Availability) | Eventual (Availability > Consistency)     |



## **Topic - 6: Hadoop Components (1.x)**

### <u>Introduction</u>

- **HDFS (Storage Layer)**
- **MapReduce (Processing Layer)**


### <u>Hadoop 2.x Enhancements</u>

- Added **YARN (Yet Another Resource Negotiator)** for better resource management.
- Enhanced scalability and multi-application support.

![Hadoop 1.x vs Hadoop 2.x Architecture](Big%20Data%20Analytics/College%20Collab%20{C}/media/image7.png)



## **Topic - 7: Hadoop Distributed File System (HDFS)**

### <u>Key Features</u>

- **Fault-tolerant** and **high-throughput**
- Master–slave architecture
- Master: **NameNode**, Slaves: **DataNodes**


### <u>Block Storage</u>

- Default block size (Hadoop 2.x) is **128 MB** (configurable via `hdfs-site.xml`)
- Files split into blocks; each block replicated (default 3 copies).
- **Example:** 514 MB file → 5 blocks (4 × 128 MB + 1 × 2 MB); replicated thrice = 15 total blocks.

![HDFS Block Replication](Big%20Data%20Analytics/College%20Collab%20{C}/media/image8.png)



## **Topic - 8: Rack Awareness**

### <u>Concept</u>

- DataNodes grouped into **racks**; NameNode knows rack locations.
- Ensures **fault tolerance** and **network efficiency**.

#### Replication Policy:

- No two replicas on same node.
- Max two replicas on same rack.

![Hadoop Rack Awareness](Big%20Data%20Analytics/College%20Collab%20{C}/media/image9.png)



## **Topic - 9: HDFS Components**

### <u>NameNode</u>

- Master daemon maintaining metadata (file paths, block locations).
- Receives **heartbeats** and **block reports** from DataNodes.
- Single point of failure → mitigated via **Secondary NameNode** or backups.

#### Stores metadata in:

- **FsImage:** File system snapshot.
- **EditLog:** Tracks changes since last FsImage.


### <u>Secondary NameNode</u>

- Periodically merges **FsImage** + **EditLog**.
- Backup mechanism for recovery.


### <u>DataNode</u>

- Slave daemon storing actual data blocks.
- Handles **read/write requests** and **block replication**.

![HDFS Master–Slave Architecture](Big%20Data%20Analytics/College%20Collab%20{C}/media/image10.png)



## **Topic - 10: HDFS Operations**

### <u>Write Mechanism</u>

1. Client requests NameNode to create file.
2. NameNode allocates blocks & DataNodes.
3. Data written via pipeline — DataNode1 → DataNode2 → DataNode3.
4. Each node sends acknowledgment back.


### <u>Read Mechanism</u>

1. Client queries NameNode for block location.
2. Reads blocks directly from nearest DataNodes.



## **Topic - 11: MapReduce Overview**

### <u>Concept</u>

- Parallel processing framework for distributed data.

#### Two main phases:

- **Map:** Process and filter input data.
- **Reduce:** Aggregate or summarize results.


### <u>Limitations</u>

- Batch-oriented (no real-time processing).
- Non-trivial for interdependent tasks (e.g., TSP).

![MapReduce Flow](Big%20Data%20Analytics/College%20Collab%20{C}/media/image11.png)



## **Topic - 12: Hadoop 2.x Components (YARN)

### <u>Architecture</u>

| Component              | Type      | Role                         |
| ---------------------- | --------- | ---------------------------- |
| **Resource Manager**   | Master    | Schedules resources & jobs   |
| **Node Manager**       | Slave     | Monitors containers & health |
| **Application Master** | Job-level | Manages job execution        |


### <u>YARN Functions</u>

- Centralized resource management.
- Enables multi-engine processing (batch, interactive, real-time).

![Hadoop YARN Architecture](Big%20Data%20Analytics/College%20Collab%20{C}/media/image12.png)



## **Topic - 13: Hadoop YARN vs MapReduce**

| Criteria                  | MapReduce             | YARN                             |
| ------------------------- | --------------------- | -------------------------------- |
| **Processing Type**       | Batch only            | Batch + Real-time                |
| **Resource Optimization** | Average (fixed slots) | Excellent (dynamic allocation)   |
| **Supported Frameworks**  | Only MapReduce        | MapReduce + Spark + Tez + Others |



## **Topic - 14: Hadoop Ecosystem**

### <u>Definition</u>

- Collection of tools supporting Big Data storage, processing, and analysis.


### <u>Common Components</u>

| Category | Tools |
|-----------|-------|
| **Data Storage** | HDFS, HBase |
| **Data Processing** | MapReduce, Spark, Pig, Hive |
| **Data Ingestion** | Sqoop, Flume, Kafka |
| **Resource Management** | YARN, ZooKeeper |
| **Data Analysis** | Mahout, Oozie |

![Hadoop Ecosystem Stack](Big%20Data%20Analytics/College%20Collab%20{C}/media/image13.png)



## **Topic - 15: Hadoop 2.x vs Hadoop 3.x**

| Feature              | Hadoop 2.x             | Hadoop 3.x                       |
| -------------------- | ---------------------- | -------------------------------- |
| **Fault Tolerance**  | Replication (3 copies) | Erasure Coding (parity blocks)   |
| **Storage Overhead** | High (3× data)         | Reduced (extra parity only)      |
| **Port Conflict**    | Common                 | Fixed via custom port allocation |



## **Topic - 16: Summary**

- Hadoop provides **scalable**, **fault-tolerant**, and **distributed** data processing.
- HDFS and YARN form its backbone.
- Erasure Coding and YARN improve efficiency and flexibility.
- Key for modern Big Data infrastructure.

![Hadoop Architecture Summary](Big%20Data%20Analytics/College%20Collab%20{C}/media/image14.png)

---
