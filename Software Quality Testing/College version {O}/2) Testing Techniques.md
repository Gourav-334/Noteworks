# $\fbox{Chapter 2: TESTING TECHNIQUES}$





## **Topic - 1: Basic Testing Process**

- Execute program with desired input(s), observe actual output(s)  
- Compare actual output(s) with expected output(s)  
- If they match, program is correct as per specification  
- ***"Testing is the process of executing a program with the intent of finding faults"***



## **Topic - 2: Roles in Testing**

### <u>Introduction</u>

- Developer, tester, customer — each plays a role.


### <u>Involvements In Testing</u>

- Verification & Validation.
- Test, Test Case, Test Suite.
- **<u>Acceptance Testing</u>:** By customer at delivery.
- **<u>Alpha Testing</u>:** Customer at developer site.
- **<u>Beta Testing</u>:** Potential users at their site.



## **Topic - 3: Tester Responsibilities**

- Analyze client requirements.
- Create test plan, scenarios & test cases.
- Track and report defects.
- Suggest quality improvements.
- Communicate with test lead/manager.
- Participate in review meetings.



## **Topic - 4: Software Tester Skills**

### <u>Introduction</u>

- Design test suites, understand usability.
- Knowledge of test design & execution methodologies.
- Strong communication for dev-team interaction.


### <u>Tester Responsibilities</u>

  - Usability scenario design
  - Test execution & result analysis
  - Reporting defects to dev team
  - Interacting with clients for requirements
  - Documentation & walkthrough participation



## **Topic - 5: White Box Testing (WBT)**

### <u>Overview</u>  

- Also known as **glass-box testing**.
- Focuses on internal logic & structure


### <u>Goals Of WBT</u>

- Cover all independent paths
- Test all logical decisions (true/false)
- Execute loops with boundary conditions
- Validate internal data structures


### <u>Types Of WBTs</u>

- Basic Path Testing
- Cyclomatic Complexity
- Control Structure Testing



## **Topic -6: Basis Path Testing**

- Measures logical complexity of procedural design.
- Ensures each statement is executed at least once.
- Derives a basis set of execution paths.



## **Topic - 7: Cyclomatic Complexity**

### <u>Introduction</u>

- Metric for quantitative logical complexity.
- Helps determine the number of independent paths to test.


### <u>Definitions</u>

- $E$ is number of edges.
- $N$ is number of nodes.
- $P$ is number of predicate nodes.

$$ V(G)\;=\;E\;-\;N\;+\;2 $$
$$ V(G)\;=\;P\;+\;1 $$

#### Interpretation:  

- $V(G)$ is number of linearly independent paths.
- Upper bound on number of tests needed for full coverage.



## **Topic - 8: Control Structure Testing**

### <u>Condition Testing</u>

- Tests logical conditions inside modules.
- All possible outcomes of condition evaluated.
- For $n$ boolean variables, $2^{n}$ test cases.


### <u>Data Flow Testing</u>

- Structural test based on variable definition & usage.
- Not related to DFDs.

#### Detects:

- Undefined variable use  
- Defined but unused variables  
- Redefinition before usage  


### <u>Loop Testing</u>

- Focuses on loop construct validity  

#### Types:

- Simple loops ($0$, $1$, $2$, $m<n$, $n$, $n+1$ iterations)
- Nested loops
- Concatenated loops
- Unstructured loops



## **Topic - 9: Black Box Testing**  

### <u>Characteristics</u>  

- Focuses on functional requirements.
- Also known as **behavioral** or **functional testing**.
- Complements white-box testing.


### <u>Detects</u>  

- Missing or incorrect functions
- Interface errors
- Data structure or database issues
- Performance or behavior faults
- Initialization & termination problems



## **Topic - 10: Graph Concepts in Testing**  

### <u>Nodes & Edges</u>  

- **<u>Node</u>:** Statement, state, method, basic block.
- **<u>Edge</u>:** Branch, transition, method call.


### <u>Test Paths</u>  

- Execution paths exercised by test cases.
- Some test paths may be feasible or infeasible & covered by multiple cases.
- **Goal -** Identify minimal test paths for full coverage.



## **Topic - 11: Black Box Techniques**  

### <u>Equivalence Partitioning</u>  

- Divides input domain into valid or invalid equivalence classes.
- Test one representative from each class.


### <u>Example</u>

- Let's say that valid input length is $6$ to $12$ characters.

#### Classes:

- $<6$ $\rightarrow$ Invalid
- $6–12$ $\rightarrow$ Valid
- $>12$ $\rightarrow$ Invalid


### <u>Boundary Value Analysis (BVA)</u>  

- Focus on edges of input ranges.
- Complements equivalence partitioning.

#### Example:

- Let's say the system supports 5000 users.
- Now test for $4999$, $5000$, $5001$ users.
 
---
