# <u>Chapter 4</u>: SOFTWARE METRICS





## **Topic - 1: Fundamentals Of Software Metrics**

### <u>Introduction</u>

- **<u>Software metrics</u>:** Measurable software characteristics.
- Metric includes measurement of software performance, resources, productivity etc.
- Often based on historical data/record.


### <u>Classification Of Software Metrics</u>

1. **<u>Product metrics</u>:** Measures size, complexity, quality & reliability etc of software.
2. **<u>Process metrics</u>:** Measures efficiency of methods, techniques & tools being used in development.

![Software Metrics Classification](./media/image17.png)


### <u>Types Of Metrics</u>

- **<u>Internal metrics</u>:** Used to measure properties which are meaningful to the programmer. For example, LOCs.
- **<u>External metrics</u>:** Used to measure properties which are meaningful to the user. For example, portability.
- **<u>Hybrid metrics</u>:** Used to measure properties which are hybrid of product, process & resource metrics. For example, cost per LOC.
- **<u>Project metrics</u>:** Used to measure properties which are important to the project manager. Like cost, time & effort.


### <u>Advantages</u>

- Proper study and analysis of various programming languages & software tools used.
- Verification of tools being standard enough for being used.
- System optimization.
- Various kinds of cost savings.


### <u>Disadvantages</u>

- Applying software metrics might itself be very costly.
- Time consuming & difficult to apply.
- Can't evaluate employee performance.
- Measurements might not be precise.



## **Topic - 2: Size Oriented Metrics**

### <u>LOC Metrics</u>

- This metrics aims to measure productivity of programmers as per LOCs.
- However, this method is old & was used when Fortran and COBOL used to be very popular.
- **<u>Effort</u>:** Measured in units of **person-months**.

$$ Productivity = \frac{KLOC}{Effort} $$

- Measuring productivity through KLOCs is flawed as we know.
- LOC metric can't be used where GUI programming (code blocks) are used.
- Many units can be measure per & using KLOC.


### <u>Advantages</u>

- Simple to measure.


### <u>Disadvantages</u>

- Assembly code would make productivity too high.
- Empty/skipped lines in programs.
- It doesn't judge quality of comments written in programs.
- LOC is about length of program, not their quality.



## **Topic - 3: Halstead's Software Metrics**

### <u>Introduction</u>

***"All computer programs can be broken down into two types of tokens, operators & operands."*** *- Halstead*


### <u>Token Count</u>

#### Token type symbols:

$$ n1 = Total \; unique \; operators $$
$$ n2 = Total \; unique \; operands $$
$$ N1 = Total \; operators $$
$$ N2 = Total \; operands $$

#### Size of program:

$$ N \; = \; N1 \; + \; N2 $$


### <u>Halstead Metrics</u>

- 