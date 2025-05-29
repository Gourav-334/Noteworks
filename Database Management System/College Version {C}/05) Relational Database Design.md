# $\fbox{Chapter 5: RELATIONAL DATABASE DESIGN}$





## **Topic - 1: Domain & Data Dependency**

### <u>Domain</u>

- **<u>Domain</u>:** Unique set of values, like string can have string values.


### <u>Dependencies</u>

- **<u>Dependencies</u>:** Relation between two or more attributes.
- **<u>Prime attribute</u>:** Dependent on candidate key.
- **<u>Non-prime attribute</u>:** *\*Now you know*
- **<u>Super key</u>:** Group of keys identifying rows in table.


### <u>Types Of Dependencies</u>

- Functional dependency
- Transitive dependency - If $A \rightarrow B$, $B \rightarrow C$ then indirectly $A \rightarrow C$.
- Partial dependency


### <u>Functional Dependency</u>

- Set of constraints between two attributes.
- Let $X$ and $Y$ be subsets of attributes.
- For a tuple, if values of attributes under $X$ determine value of attributes under $Y$ in some way.
- Then $Y$ is functionally dependent on $X$, or $X$ functionally determines $Y$.
- $X \rightarrow Y$ ($X$ at left is determinant, $Y$ on right is dependent).

#### Example:

- As we have discussed, for $X \rightarrow Y$, for each value of X there should one $Y$ value.

| `Sid` | `Sname` |
| :---: | :------ |
| `S1`  | `A`     |
| `S1`  | `A`     |
| `S1`  | `A`     |
| `S2`  | `B`     |
| `S3`  | `B`     |

- As we can see over here for each value of `Sid`, there is only one `Sname` value.
- Hence, $Sid \rightarrow Sname$ is a valid FD.
- For each `Sid`, there exists a unique `Sname` (many-to-one relation).



## **Topic - 2: Normalization**

### <u>Normalization</u>

- Systematic decomposition of tables.
- Process of reducing redundancy of data.
- Improves data integrity.


### <u>Advantages of Normalization</u>

- Eliminates duplicate data.
- Makes transaction faster.


### <u>Different Anomalies</u>

- **<u>Anomalies</u>:** Problem that raises during certain operation.

#### Types of anomalies:

- Data anomaly
- Updation anomaly
- Deletion anomaly


### <u>Types of Normal Form</u>

- 1st normal form (1NF)
- 2nd normal form (2NF)
- 3rd normal form (3NF)
- **Boyce Codd** normal form (BCNF)


### <u>1st Normal Form</u>

- Removes composite and multi-valued attribute cells.
- Creates separate table for related data.
- Identifies separate data by primary keys.


### <u>2nd Normal Form</u>

- It has to be in 1st normal form.
- Table can’t contain partial dependency.
- To solve this, table is split.

#### Example:

- Here, `"Office Location"` is partially dependent on `"Employee ID"`.

| `Employee Id` | `Department Id` | `Office Location` |
| :-----------: | :-------------: | :---------------: |
|   `1EDU001`   |     `ED-T1`     |      `Pune`       |
|   `1EDU002`   |     `ED-S2`     |    `Bengaluru`    |
|   `1EDU003`   |     `ED-M1`     |      `Delhi`      |
|   `1EDU004`   |     `ED-T3`     |     `Mumbai`      |
$$ NORMALIZES\;TO $$

| `Employee Id` | `Department Id` |
| :-----------: | :-------------: |
|   `1EDU001`   |     `ED-T1`     |
|   `1EDU002`   |     `ED-S2`     |
|   `1EDU003`   |     `ED-M1`     |
|   `1EDU004`   |     `ED-T3`     |
$$ + $$

| `Department Id` | `Office Location` |
| :-------------: | :---------------: |
|     `ED-T1`     |      `Pune`       |
|     `ED-S2`     |    `Bengaluru`    |
|     `ED-M1`     |      `Delhi`      |
|     `ED-T3`     |     `Mumbai`      |


### <u>3rd Normal Form</u>

- Must be in 2nd normal form.
- No transitive dependency for non-prime attributes.

#### Example:

- Here, $Student\;Id \rightarrow Subject\;Id\;\&\;Subject\;Id \rightarrow Subject$.

| `Student Id` | `Student Name` | `Subject Id` | `Subject` |  `Address`  |
| :----------: | :------------: | :----------: | :-------: | :---------: |
| `1DT15ENG01` |     `Alex`     |   `15CS11`   |   `SQL`   |    `Goa`    |
| `1DT15ENG02` |    `Barry`     |   `15CS13`   |  `JAVA`   | `Bengaluru` |
| `1DT15ENG03` |    `Clair`     |   `15CS12`   |   `C++`   |   `Delhi`   |
| `1DT15ENG04` |    `David`     |   `15CS13`   |  `JAVA`   |   `Kochi`   |
$$ NORMALIZES\;TO $$

| `Student Id` | `Student Name` | `Subject Id` |  `Address`  |
| :----------: | :------------: | :----------: | :---------: |
| `1DT15ENG01` |     `Alex`     |   `15CS11`   |    `Goa`    |
| `1DT15ENG02` |    `Barry`     |   `15CS13`   | `Bengaluru` |
| `1DT15ENG03` |    `Clair`     |   `15CS12`   |   `Delhi`   |
| `1DT15ENG04` |    `David`     |   `15CS13`   |   `Kochi`   |
$$ + $$

| `Subject Id` | `Subject` |
| :----------: | :-------: |
|   `15CS11`   |   `SQL`   |
|   `15CS13`   |  `JAVA`   |
|   `15CS12`   |   `C++`   |
|   `15CS13`   |  `JAVA`   |


### <u>Boyce Codd Normal Form</u>

- Must be in 3rd normal form.
- For every functional dependency, non-dependent attribute must be super key of the table.
- For example, if $A \rightarrow B$ then $A$ must be super key of the table.
- To solve it, a new column is created which is attached to each split part of the given table.
 
---
