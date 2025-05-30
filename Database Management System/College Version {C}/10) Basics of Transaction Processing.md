# $\fbox{Chapter 10: BASICS OF TRANSACTION PROCESSING}$





## **Topic - 1: Transaction**

### <u>Transaction</u>

- Set of instructions and operations.
- It accesses and updates certain data.
- Similar to functions.
- Written in DML or high-level language.


### <u>ACID Properties</u>

- **Atomicity**
- **<u>Consistency</u>:** No parallel/concurrent executions + maintain of data integrity.
- **<u>Isolation</u>:** Multiple transactions done in series, not parallel.
- **<u>Durability</u>:** Changes are saves even if system fails.


### <u>Atomicity Example</u>

<img src="./media/image28.png" style="width:1.77965in;height:2.5396in" />


### <u>Consistency Example</u>

<img src="./media/image29.png" style="width:1.71123in;height:2.93048in" />


### <u>Isolation Example</u>

<img src="./media/image30.png" style="width:1.95666in;height:2.66584in" />

- Can be called as atomicity of each individual statement.


### <u>Durability</u>

- Same example the isolation.


### <u>Transaction State</u>

- Aborted
- Rolled back
- Committed
- **<u>Compensating transaction</u>:** Undo committed transactions.


### <u>Transaction State Diagram</u>

<img src="./media/image31.png" style="width:5.28194in;height:2.80131in" />


### <u>Transaction State In Brief</u>

*/*All states shown in diagram above*


### <u>Transaction Log</u>

- Keeps record of all past transactions.

#### Records include:

- Type of operations done.
- Data affected by it.
- Before and after values of data.
- Commit points of transaction.

### Advantage:

- Ability to search for corrupt point in data.

#### Disadvantage:

- Load and storage of too much information.

---
