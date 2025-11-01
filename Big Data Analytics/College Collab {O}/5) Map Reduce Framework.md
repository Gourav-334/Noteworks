# Chapter 3B: MapReduce Framework



## 1. Introduction to MapReduce

### Definition
- **MapReduce** is a **parallel programming framework** to process large volumes of distributed data.
- Processes Big Data stored in **HDFS** through user-defined **Map** and **Reduce** functions.
- Originally developed by **Google (2004)**.

### Key Operations
1. **Map:** Processes input data → emits intermediate key–value pairs.
2. **Reduce:** Aggregates intermediate results → outputs final key–value pairs.

```css
/* Diagram Placeholder: MapReduce Flow Overview */
```

---

## 2. Working of MapReduce

### Architecture
- Operates on a **Master–Slave** model.
- **Master (JobTracker)** coordinates jobs and assigns tasks.
- **Workers (TaskTrackers)** execute Map and Reduce tasks.

### Execution Flow
1. User submits job to **JobTracker**.
2. JobTracker splits input data → assigns to TaskTrackers.
3. Each TaskTracker runs **Mapper** and **Reducer** independently.
4. Results are aggregated and written back to **HDFS**.

```css
/* Diagram Placeholder: Master–Slave Communication in MapReduce */
```

---

## 3. MapReduce Functions

### Functional Model
```text
map(in_key, in_value) → list(out_key, intermediate_value)
reduce(out_key, list(intermediate_value)) → list(out_value)
```

### Programming Influence
- Derived from **functional programming** concepts.
- Abstracts parallelization, fault tolerance, and load balancing.

```css
/* Diagram Placeholder: Map and Reduce Function Structure */
```

---

## 4. Challenges Solved by MapReduce

| Challenge | Description | MapReduce Solution |
|------------|--------------|--------------------|
| **Critical Path Problem** | Delay in one node affects job completion. | Parallel, independent task execution. |
| **Reliability** | Node failure halts progress. | Task re-execution on other nodes. |
| **Equal Split** | Uneven data load on nodes. | Automatic data partitioning. |
| **Single Split Failure** | Failure in one chunk affects entire job. | Fault-tolerant reprocessing. |
| **Aggregation** | Need to merge distributed results. | Automatic shuffling & merging. |

---

## 5. Advantages of MapReduce

- **Parallel Processing:** Divide and Conquer → faster data handling.
- **Data Locality:** Computation moves to data, not vice versa.
- **Scalability:** Processes petabyte-scale datasets efficiently.
- **Fault Tolerance:** Retries failed tasks automatically.

```css
/* Diagram Placeholder: Parallelism and Data Locality */
```

---

## 6. Core MapReduce Terminologies

| Term | Definition |
|------|-------------|
| **Payload** | User-defined Map and Reduce logic. |
| **Mapper** | Transforms input key–value pairs → intermediate pairs. |
| **Reducer** | Aggregates intermediate pairs → final output. |
| **NameNode** | Manages HDFS metadata. |
| **DataNode** | Stores actual data blocks. |
| **JobTracker** | Master that manages jobs and assigns tasks. |
| **TaskTracker** | Executes tasks and reports progress. |
| **Job** | Complete MapReduce program execution. |
| **Task** | Execution instance of Mapper or Reducer. |
| **Task Attempt** | A retry of a failed task on a different node. |

---

## 7. Mapper Function – Workflow

### Steps
1. **Input Split:** Logical unit of work; defines data processed by a single mapper.
2. **RecordReader:** Converts input splits into key–value pairs.
3. **Mapping:** Processes pairs and outputs intermediate key–value results.

### Input Formats
- **TextInputFormat (Default)**
- **KeyValueTextInputFormat**
- **SequenceFileInputFormat**
- **SequenceFileAsTextInputFormat**

```css
/* Diagram Placeholder: Mapper Function Flow */
```

---

## 8. Shuffle and Sort Phase

### Purpose
- Automatically handled by the MapReduce framework.
- Ensures values for the same key reach the same reducer.

### Sub-steps
1. **Merging:** Combines all pairs with identical keys.
2. **Sorting:** Orders pairs by key → <Key, List<\Value>>.

```css
/* Diagram Placeholder: Shuffle and Sort Mechanism */
```

---

## 9. Reducer Function – Workflow

### Function
- Executes once per **unique key**.
- Aggregates all intermediate values for that key.

### Output
- Zero or more final key–value pairs.
- Final results stored in **HDFS output directory**.

```css
/* Diagram Placeholder: Reducer Function Flow */
```

---

## 10. End-to-End MapReduce Process

1. Input split into chunks.
2. Mappers process each chunk → emit intermediate results.
3. Shuffle–sort groups results by key.
4. Reducers aggregate grouped values.
5. Final output written to HDFS.

```css
/* Diagram Placeholder: Complete MapReduce Pipeline */
```

---

## 11. MapReduce Applications

| Category | Example |
|-----------|----------|
| **Summarization** | Counting, statistics aggregation |
| **Classification** | Top-N records, sorting |
| **Recommendation** | Predict user preferences |
| **Analytics** | Join, selection, filtering |

---

## 12. Example – Inverted Index

### Problem
Build a list of unique words or hashtags and their document occurrences.

### Example Input (Tweets)
```
"It’s not too late to vote. #ElectionDay"
"Happy #PrimaryDay"
```

### Map Function
```text
map(tweet) → (hashtag, tweet)
```

### Reduce Function
```text
reduce(hashtag, list(tweets)) → (hashtag, [list of tweets])
```

### Example Output
```
(ElectionDay, [“It’s not too late to vote...”, “Say NO to corruption...”])
(PrimaryDay, [“Midtown polling office...”, “Happy #PrimaryDay”])
```

```css
/* Diagram Placeholder: Inverted Index via MapReduce */
```

---

## 13. MapReduce on YARN

### MRv2 (MapReduce v2)
- Integrated with **YARN** in Hadoop 2.x.
- **JobTracker** and **TaskTracker** replaced by:
  - **ResourceManager**
  - **ApplicationMaster**
  - **NodeManager**

### Advantages
- Enhanced scalability and multi-job execution.
- Supports real-time and interactive applications.

```css
/* Diagram Placeholder: MapReduce on YARN Architecture */
```

---

## 14. Summary

- MapReduce simplifies large-scale data processing using **parallelism**.
- Fault tolerance and scalability are built-in.
- MRv2 with YARN provides improved flexibility.
- Commonly used for analytics, indexing, and recommendation systems.

```css
/* Diagram Placeholder: Summary of MapReduce Workflow */
```

---
