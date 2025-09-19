### <u>Key-Value</u>

- Key-value pair.
- Can handle lots of data & heavy load.
- Store data using hash table.
- Values can be JSON, BLOB, String etc.

| Key  | Value |
| :--- | ----- |
| Name | "abc" |
| Age  | 21    |

$$ \fbox{Key}\rightarrow\fbox{Value} $$

>**<u>NOTE</u>:**
>**Value** must be kept in oval.

- Most basic types.
- Collections, dictionaries, associative arrays.
- Works best for shopping cart content.

#### DBS:

- CoucheBase
- DynamoDB
- Riak

#### Advantages:

- Easy to use.
- Fast response time.
- Scalable (vertical as well as horizontal)
- Reliable because of in-built redundancy removal.

#### Disadvantages:

- Query language not present.


### <u>NewSQL</u>

$$ \text{NewSQL = SQL + NoSQL} $$

- Combines scalability of NoSQL with traditional RDBMS.
- High performance & availability $=> \text{NoSQL}$
- ACID properties (consistency) $=> \text{SQL}$

#### Databases:

- VoltDB
- NuoDB

#### RDBMS v/s NoSQL v/s NewSQL:

| Aspect         | RDBMS                                 | NoSQL                             | NewSQL                            |
| :------------- | :------------------------------------ | :-------------------------------- | :-------------------------------- |
| **Schema**     | Has fixed schema                      | Has flexible schema               | Has flexible schema               |
| **Data types** | Uses custom data types                | Utilizes those native to JSON     | Uses custom & JSON data types     |
| **Properties** | Supports ACID theorem                 | Supports CAP theorem              | Supports both ACID & CAP theorems |
| **Use case**   | Security & consistency                | Performance & scalability         | All                               |
| **Technology** | Government information infrastructure | Corporate information information | Big data analytics                |
| **Scaling**    | Vertical scaling                      | Horizontal scaling                | Both                              |
| **Examples**   | MySQL, PostgreSQL etc                 | MongoDB, Redis etc                | CockroachDB, MariaDB etc          |



### <u>Hive</u>

- Data warehouse
- Analysis
- HIVE engine translate into DAG
- HQL
- User/ hive/ warehouse
