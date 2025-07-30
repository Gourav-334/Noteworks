# $\fbox{Chapter 3: OBJECT-ORIENTED TESTING}$





## **Topic - 1: Applicability of Conventional Test Case Design**

### <u>Introduction</u>

- OO testing is strategically similar but tactically different from traditional testing.
- OO models are more aligned with real-world software behavior.
- Testing starts from interpretation of analysis/design models.
- Initial emphasis on class-level unit testing.
- Tests often involve collaborating object interactions.


### <u>Evolutionary OO Development</u>

- Models evolve from informal specs to formal class/object structures.

#### Contributors to development:

- Class relationships
- Object behavior design
- Allocation & system structure

>**<u>NOTE</u>:**
> **<u>Goal</u>:** Catch errors early in the model phase, before they propagate to implementation.


### <u>Testing Class Descriptions</u>

- Incorrect attribute/method specification can cause deep, latent bugs.
- Late-discovered modeling errors incur higher maintenance costs.



## **Topic - 2: Boundary Value Analysis (BVA)**

### <u>Introduction</u>

- Focuses on boundary inputs where errors are most probable.


### <u>Types Of BVA</u>

- Minimum-maximum
- Just above and just below limits
- Nominal and error values


### <u>BVA Guidelines</u>

- For input range $[x,y]$, test at:

$$ x-1,\;x,\;x+1 $$
$$ y-1,\;y,\;y+1 $$

- Ensure performance under edge conditions is validated.



## **Topic - 3: Equivalence Class Partitioning**

### <u>Introduction</u>

- Partitions input domain into **equivalence classes**.
- Only one test per class needed to represent its behavior.


### <u>Example</u>

- Valid ranges are $1$–$10$ & $20$–$30$.
- So, suggested test cases would be $5$ (valid), $15$ (invalid), $25$ (valid), etc.



## **Topic - 4: Decision Table Based Testing**

### <u>Introduction</u>

- Also known as **Cause-Effect Mapping**.
- Used when output is based on combinations of inputs.


### <u>Steps</u>

1. Identify functional output dependent on multiple inputs.
2. Divide inputs into manageable subsets.
3. Construct decision table with input-output mapping.


### <u>Example</u>

- Submit button is enabled only if all required fields are filled.



## **Topic - 5: Issues in Object-Oriented Testing**

### <u>Encapsulation</u>

- Method behavior depends on object’s internal state.
- Testing requires constructing appropriate internal states.


### <u>Inheritance</u>

- Derived class cannot be fully tested using base class test cases.
- Overridden behavior may alter functionality.


### <u>Polymorphism</u>

- A method may have multiple bindings.
- Requires different test cases for each possible binding.


### <u>Research Process Impact</u>

#### Demands of OO Paradigm:

- Dynamic binding handling
- State-aware testing strategies
- Consideration of collaboration patterns



## **Topic - 6: Fault-Based Testing**

### <u>Introduction</u>

- Intentionally triggers **potential faults** in design or code.
- Best when tester has insight into probable errors.


### <u>Steps</u>

1. Identify likely fault scenarios.
2. Build tests to activate and expose them.


### <u>Limitations</u>

- Can't detect incorrect logic or conditions.
- Can't detect faulty object interactions.



## **Topic - 7: Scenario-Based Testing**

### <u>Introduction</u>

- Focuses on **user-driven flows** rather than object-internal behavior.
- Detects workflow errors & gaps in real-world usability.


### <u>Example – Print Document</u>

1. Open document  
2. Print document  
3. Close editor  

>**<u>NOTE</u>:**
>**<u>Edge case</u>:** User expects 100 copies but only 1 prints $\rightarrow$ spec issue.



## **Topic - 8: Random Testing**

### <u>Introduction</u>

- Also known as **monkey testing**.
- Useful under strict deadlines.
- Generates random operation sequences within allowed input space.
- Helps simulate unpredictable, real-world usage.


### <u>Example - Account Class</u>

#### Valid operations:

- Open
- Setup
- Deposit
- Withdraw
- Balance
- Overview


### <u>Test Cases Examples</u>

- **Test $r_1$ -** Open $\rightarrow$ Config $\rightarrow$ Deposit $\rightarrow$ Deposit $\rightarrow$ Balance $\rightarrow$ Overview $\rightarrow$ Withdraw $\rightarrow$ Close
- **Test $r_2$ -** Open $\rightarrow$ Config $\rightarrow$ Deposit $\rightarrow$ Withdraw $\rightarrow$ Deposit $\rightarrow$ Balance $\rightarrow$ Credit cap $\rightarrow$ Withdraw $\rightarrow$ Close



## **Topic - 9: Partition Testing for Classes**

### <u>Introduction</u>

- Reduces test cases by grouping similar operations.


### <u>State-Based Partitioning</u>

#### State-modifying operations:

- Deposit
- Withdraw

#### Not state modifying:

- Balance
- Summary
- Credit limit


### <u>Example</u>

- **Test $p_1$ -** Open $\rightarrow$ Setup $\rightarrow$ Deposit $\rightarrow$ Withdraw $\rightarrow$ Close
- **Test $p_2$ -** Open $\rightarrow$ Config $\rightarrow$ Balance $\rightarrow$ Summary $\rightarrow$ Credit cap $\rightarrow$ Close



## **Topic - 10: Interclass Test Case Design**

### <u>Introduction</u>

- As systems grow, class collaborations dominate testing scope.


### <u>Approach</u>

- Partition testing  
- Random testing  
- Scenario-based testing  


### <u>Visual Techniques</u>

- Use UML/message sequence diagrams to show class interactions.

$$ \text{Arrows = Message direction} $$
$$ \text{Dots = Triggered operations} $$

---
