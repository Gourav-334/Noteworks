### <u>Performance Testing</u>

- Load testing
- Stress testing
- Regression testing
- Compatibility testing
	- Device compatibility
	- Browser compatibility
	- Platform compatibility
- Endurance testing
- User acceptance testing
- Beta testing
- Black-box testing


### <u>Black-Box Testing Techniques</u>

1. Boundary-value analysis
2. Equivalent-class partition
3. Decision table
4. Error guessing
5. Error handling
6. Cause-effect
7. State-transition
8. Use case testing

#### Tools:

- Selenium
- Jmeter
- QTP


### <u>White-Box Testing</u>

#### Advantages:

- Expert feedback
- Risk avoidance
- Quality improvement

#### Disadvantages:

- Cost (to human resources)

#### Types:

1. Penetration testing
2. Path testing
3. Mutation testing
4. Loop testing
5. Unit testing
6. Integration testing


### <u>Cyclomatic Complexity</u>

| Cyclomatic Complexity | Level                       |
| :-------------------: | :-------------------------- |
|         1-10          | Low (effort, cost, time)    |
|         11-20         | Medium (effort, cost, time) |
|         21-30         | High (effort, cost, time)   |
|       31-ABOVE        | Highest                     |

- Independent path
- Nodes
- Edges
- Region (bounded)

$$ CC(m)\;\text{OR}\;V(G) $$
$$ M\;=\;E\;-\;N\;+\;2 $$
$$ M\;=\;R\;+\;1 $$


### <u>BBT v/s WBT</u>

| BBT                                         | WBT                                                  |
| :------------------------------------------ | :--------------------------------------------------- |
| Beta testing                                | Alpha testing                                        |
| User, client, stakeholder, businessmen      | Tester, developer, export, project manager, SQA, SQC |
| Externally                                  | Internally                                           |
| Domain knowledge experience is not required | Required (domain, project, code)                     |
| Closed-box testing                          | Glass-box, clear-box, code-based test                |
| Get feedback from user & client             | Tester, developer, expert (feedback)                 |


### <u>Object-Oriented Testing</u>

- **<u>OOT</u>:** A method in which we can check all concepts of OOP.
- It is done after completion of conventional testing.
- Mainly applicable on large scale projects.

#### Disadvantages:

- Complex issues
- Can't perform automation testing

#### Levels:

1. Algorithmic level
2. Class-level testing
3. Interclass-level testing
4. Cluster-level testing
5. System-level testing
6. Regression testing

>**<u>QUESTIONS</u>:**
>1. Disadvantages of conventional testing.
>2. Disadvantages of OOT.


### <u>OOT Techniques</u>

1. Random testing (monkey testing / fuzzy testing)
2. Partition testing
3. State-based testing
4. Scenario-based testing
5. Use-based testing
6. Attribute-based testing
7. Class testing
8. Integration testing
9. Inheritance testing
10. Polymorphism testing

>**<u>TOOLS</u>:**
>1. Quick check
>2. Test sigma
>3. Randoop
>4. Test grain

### <u>Random testing</u>

- We can use random values for testing.
- Similar to black-box testing.
- Can be performed by user.
- Used in large scale projects.
- Doesn't require formal training.
- No boundary set for testing values.
- Can perform random testing on it.


### <u>Partition Testing</u>

- Very similar to equivalence class testing.
- Three types - State-based, attribute-based & category-based.


### <u>Scenario-Based Testing</u>

- We can test based on different scenarios.


### <u>Question Set - 2</u>

#### Differentiate between OOT & conventional testing:

| Aspect         | Object-Oriented Testing                                                                      | Conventional Testing                                  |
| :------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Type**       | Manual testing                                                                               | Both manual & automation testing                      |
| **Levels**     | It includes algorithmic, class, system, regression level.                                    | It includes unit & integration level.                 |
| **Techniques** | Class, inheritance, polymorphism, fault-based, scenario-based, state-based, partition-based. | Boundary value, decision table, white box, black box. |



### <u>Client-Server & Web-Based Testing</u>

| Client-Server Testing                                                                                                             | Web Application Testing                                                                                                                                   |
| :-------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client-server testing involves testing interactions between client and server over the intranet in a more controlled environment. | Web application testing involves testing interactions between the web browser and web server over the internet is more diverse than the intranet network. |
| Client-server testing is usually two-tier architecture testing. This consists of a client system and a server system.             | Web application testing is usually three-tier architecture testing. This consists of a web server, browser, and DB server.                                |
| Testing over the intranet. An intranet is a private computer network within an organization                                       |                                                                                                                                                           |
| Security and performance are not a concern in this testing.                                                                       | Security and performance are big concern in this testing.                                                                                                 |
| Testing efforts and types of testing are less.                                                                                    | Testing efforts and types of testing are more.                                                                                                            |
| The client-server testing  types performed are as follows -                                                                       |                                                                                                                                                           |


### <u>Software Testing Lifecycle (STLC)</u>

1. Requirement analysis
2. Test planning
3. Test case development
4. Test environment setup
5. Test execution
6. Test closure/exit

#### Advantages:

- We can use Agile while using STLC.
- We can easily find out the bugs when using STLC.