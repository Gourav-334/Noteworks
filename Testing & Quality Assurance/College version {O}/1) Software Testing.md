# $\fbox{Chapter 1: SOFTWARE TESTING}$





## **Topic - 1: Testing, Verification & Validation**  

### <u>Testing</u>  

- Practice of executing a program to uncover mistakes.
- Can prove presence of bugs, not their absence.
- **Objective -** Detect faults via test execution.


### <u>Verification</u>  

- **<u>Verification</u>:** Evaluation of software/artifacts to ensure it meets initial phase conditions.
- **<u>Static Testing</u>:** Done before validation.
- **Focus -** Are we building the product right?
- QA (Quality Assurance) falls under this.  


### <u>Validation</u>  

- **<u>Validation</u>:** Execution-based process to check if software meets user needs.
- **Dynamic Testing -** Done after verification.
- **Focus -** Are we building the right product?
- QC (Quality Control) falls under this.


### <u>Difference: Verification vs. Validation</u>  

| Aspect             | Verification            | Validation               |
| ------------------ | ----------------------- | ------------------------ |
| **Type**           | Static testing          | Dynamic testing          |
| **Timing**         | Before development ends | During/after development |
| **Goal**           | Build product right     | Build right product      |
| **Responsibility** | QA                      | QC                       |



## **Topic - 2: Debugging**  

### <u>Debugging Process</u>  

1. Locate fault/flaw  
2. Upgrade the code  
3. Re-test the fix  


### <u>Terminology</u>  

- **<u>Error</u>:** Developer's mistake or misunderstanding.  
- **<u>Fault</u>:** Defect injected due to error.  
- **<u>Failure</u>:** System's inability to meet expected behavior under defined conditions.  



## **Topic - 3: Test Case Design**  

### <u>Test Case Variables</u>

- **Input data -** From hardware/ software/ humans
- **Execution conditions**
- **Expected output**


### <u>Test Suite & Related Terms</u>  

- **<u>Test</u>:** A group of test cases.
- **<u>Test Suite</u>:** Database-related test group, run collectively.
- **<u>Test Oracle</u>:** Source to verify test output correctness.
- **<u>Test Bed</u>:** Environment + tools for testing.



## **Topic - 4: Software Quality & Metrics**  

### <u>Quality</u>  

- Degree to which software meets specified requirements or customer expectations.


### <u>Metric</u>  

- **<u>Definition</u>:** Quantitative measure of a specific software/process attribute.  

#### Types:

- **<u>Service Metric</u>:** For example, LOC (Lines of Code).
- **<u>Process Metric</u>:** For example, time, cost.
- **<u>Quality Metric</u>:** Degree of a quality attribute.



## **Topic - 5: Software Testing Principles**  

1. Testing means Executing selected cases to detect defects & assess consistency.  
2. Good test cases have high defect detection probability (**Defect Clustering**).  
3. Findings should be meticulously verified (**Absence of Error Fallacy**).  
4. Expected output must be predefined.  
5. Include both **valid & invalid** input conditions.  
6. Testing must be done by **independent group**.  
7. Tests should be **reusable & repeatable** (**Pesticide Paradox**).  
8. Test early (**Early Testing**).  
9. Integrate testing in full SDLC.  
10. Testing is context-dependent and creative.  



## **Topic - 6: Test Strategies**  

### <u>For Conventional Software</u>  

#### Types:

- Unit Testing  
- Integration Testing  
- System Testing  
- Validation Testing  

#### Based on:

  - Source code features  
  - Design architecture  
  - Full system behavior  
  - Business spec validation  


### <u>For OO Software</u>  

- Less emphasis on I/O & focus on object behavior & interactions.



## **Topic - 7: Unit Testing**  

### <u>Introduction</u>

- Tests individual modules/functions.
- Performed by developers or peers.
- Isolates small code segments.
- Detects early defects.


### <u>Advantages</u>  

- Reduces defects in early stage.
- Lowers overall testing cost.
- Aids refactoring & design.
- Integrates with build process.
- Increases maintainability confidence.



## **Topic - 8: Integration Testing**  

### <u>Introduction</u>

- Tests interactions among components.
- Comes after unit testing.  
- Checks data flow and interface logic.


### <u>Types</u>  

#### Top-down:

- High-level to low-level.
- Stubs required.
- Interface errors found early.

#### Bottom-up:

  - Low-level to high-level.
  - Drivers required.
  - Detects critical module issues early.


### <u>Stubs & Drivers</u>  

- **<u>Stub</u>:** Simulates called module.
- **<u>Driver</u>:** Simulates calling module.



## **Topic - 9: Validation Testing**  

### <u>Introduction</u>

- Covers functional & non-functional aspects.
- **Includes -** Unit, Integration, System, UAT.
- Done using tools (e.g. Selenium, HP QC).
- **<u>Reports</u>** test plan, results, defect logs, metrics.


### <u>Advantages</u>  

- Aligns with business needs.
- Captures unmet specs.
- Detects missed issues from verification phase.



## **Topic - 10: Alpha Testing**  

### <u>Introduction</u>

- Done by developer team, in lab setting.
- At end of development, before beta.
- Developers simulate user behavior.


### <u>Steps</u>  

1. Review specs  
2. Create plan & test cases  
3. Execute & log defects  
4. Fix & re-test  


### <u>Advantages</u>  

- Speeds delivery  
- Early feedback  
- Reusable test artifacts



## **Topic - 11: Beta Testing**  

### <u>Introduction</u>

- Done by real users, in real environment.
- After alpha, before release.

#### Focus area:

- UI feedback
- Stability in live conditions


### <u>Advantages</u>  

- Reduces product failure risk
- Uncovers issues testers miss
- Builds user confidence


### <u>Disadvantages</u>  

- Uncontrolled environment
- May delay release
- Depends on user input quality



## **Topic - 12: System Testing**  

### <u>Introduction</u>

- End-to-end testing on full integrated product.
- Done by independent QA team.

#### Covers:

- Functional requirements
- Non-functional behavior
- Performance, compliance


### <u>Car Analogy Example</u>

$$ \text{Unit Testing = Check engine, wheels separately} $$
$$ \text{Integration Testing = Assemble \& test subsystems} $$
$$ \text{System Testing = Drive full car on all terrains} $$



## **Topic - 13: System Testing Process**  

1. Setup test environment  
2. Create test cases  
3. Generate test data  
4. Execute tests  
5. Detect & log defects  
6. Retest after fixes  



## **Topic - 14: Recovery Testing**  

### <u>Introduction</u>

- Tests system's ability to recover from failure.
- Ensures fault tolerance.


### <u>Features</u>

  - Power outage
  - Network/server failure
  - Unresponsive peripherals



## **Topic - 15: Security Testing**  

### <u>Introduction</u>

- Detects vulnerabilities, ensures data integrity.

### <u>6 Testing Principles</u>

1. Confidentiality
2. Integrity
3. Authentication
4. Authorization
5. Availability
6. Non-repudiation


### <u>Focus Areas</u>

- Network security
- System software
- Client-side & server-side protection



## **Topic - 16: Stress Testing**  

- Assesses app's robustness under extreme load.
- For example, high user traffic & large data imports.
- Prevents crashes in crunch situations.
- Shows appropriate error messages.



## **Topic - 17: Performance Testing**  

### <u>Introduction</u>

- Reveals performance bottlenecks pre-launch.


### <u>Measures</u>

- Speed
- Scalability
- Stability
- Resource use


### <u>Types</u>  

- **<u>Load Testing</u>:** Expected user traffic  
- **<u>Stress Testing</u>:** Beyond limits  
- **<u>Endurance Testing</u>:** Over time  
- **<u>Spike Testing</u>:** Sudden traffic spikes  
- **<u>Volume Testing</u>:** Massive data  
- **<u>Scalability Testing</u>:** Increase in load handling  



## **Topic - 18: Metrics**  

### <u>Basic Definitions</u>  

- **<u>Measure</u>:** Raw count (e.g., number of failures).
- **<u>Measurement</u>:** Process of obtaining a measure.
- **<u>Metric</u>:** Quantitative attribute of system/process.


### <u>Source Code Metrics</u>  

- LOC
- Comment ratio
- Cyclomatic complexity


### <u>Development Metrics</u>  

- Defect count  
- Time-to-fix  
- Skill/resource mismatch detection  


### <u>Testing Metrics</u>  

- Coverage  
- Defect density  
- Test case effectiveness  
 
---
