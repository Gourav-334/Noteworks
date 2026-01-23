# $\fbox{DIGITAL ELECTRONICS}$





## **Chapter - 1: Boolean Logic**

- $\downarrow\text{Noise margin} \propto \;\uparrow\text{Reliability}$
- **Idempotent law:** Repeating a condition changes nothing.
- **Complement law:** A condition and its negation can not co-exist.
- **De Morgan's law:** Constraints can be re-written, not changed.
- Transistors act as switches here.



## **Chapter - 2: Combinational Logic**

- **Combinational circuit:** Circuit where output depends only on inputs. ($Y=f(X_1,X_2,...,X_N)$)
- **Sum of products (SOP):** OR of AND terms
- **Product of sums (POS):** AND of OR terms
- **Karnaugh's map (K-map):** Visual tool for compressing Boolean expression.
- **Don't care conditions ($X$):** Input conditions that will never occur.



## **Chapter - 3: Arithmetic Logic**

- **Half adder:** Adder with inputs as $A$ & $B$, and outputs as sum & carry.
- **Full adder:** Inputs as $A$, $B$, $Cin$, and outputs sum & $Cout$.
- **Cin / Cout:** Carry-in / Carry-out
- **Ripple carry adder:** Multiple full adders chained to provide a large binary sum.
- **Unsigned overflow:** Overflow from the MSB in unsigned numbers.
- **Signed overflow:** When sign bit at MSB changes unexpectedly in signed numbers.
- **2's complement:** Subtraction using addition. ($A-B=A+(\overline{B}+1)$)
- **Comparator:** A circuit logic that tells how two inputs compare to each other.



## **Chapter - 4: Sequential Logic**

- **Sequential logic:** Circuit logic where output depends on current input & past state.
- **Latches:** Level-sensitive memory, used when speed matters more than precision.
- **Flip-flops:** Edge-triggered memory, changing state only on clock edge.
- **Clock edge:** Moment when state of clock changes ($0 \rightarrow 1$ or $1 \rightarrow 0$).
- **Flip-flop types:** D, JK, T



## **Chapter - 5: Flip-Flops & Latches**

- **SR latch:** Built using cross-coupled gates & invalid states might exist.
- **D latch:** Eliminates invalid states, data could pass only when enable is $1$.
- **JK flip-flop:** No invalid state & can toggle states.
- **T flip-flop:** Toggles when $T=1$.



## **Chapter - 6: Finite State Machines**

- FSMs are stored encoded in flip-flops.
- **Moore machine:** Output depends on state only.
- **Mealy machine:** Output depends on both state and input.
- There must be a reset setting in FSMs.



## **Chapter - 7: Timing & Hazards**

- **Static hazard:** Temporary output glitch.
- **Dynamic hazard:** Output oscillates before finally settling.
- **Metastability:** A state where output is neither $0$ or $1$ temporarily.
- **Synchronizers:** Solution to metastability by using flip-flops in series.



## **Chapter - 8: Interfacing & Abstraction**

- **Noise margin:** Range for each circuit element to decide their operability.
- **Schmitt trigger:** Circuit that converts noisy signal into clean output using hysteresis.
- **Fan-in:** Number of inputs a gate can accept.
- **Fan-out:** Number of inputs a gate can drive.
- **Clock skew:** Difference in clock edge signal arrival in different parts of circuit.
- **Abstraction layers:** Boolean logic $\rightarrow$ Gates $\rightarrow$ Registers $\rightarrow$ FSMs $\rightarrow$ Systems
- Most errors/failures occur at interfaces.

---
