# $\fbox{Module 7: AMPLIFIERS \& OPERATIONAL AMPLIFIERS}$

> **Purpose**  
> Abstract discrete devices into functional blocks and introduce operational amplifiers as idealized, high-gain building elements for analog systems.

---

## 7.1 Why Amplifiers Matter

Electronics is not only about switching; it is also about **manipulating signal magnitude**.

#### Amplifiers enable:

- Signal strengthening
- Signal conditioning
- Interfacing between subsystems

> Amplification is controlled energy transfer, not energy creation.

---

## 7.2 What an Amplifier Is

An **amplifier** is a circuit that:

- Takes energy from a power supply
- Uses a small input signal to control a larger output signal

#### Key parameters:

- Gain
- Bandwidth
- Linearity
- Stability

---

## 7.3 Amplifier Gain

Gain is the ratio of output to input.

#### Types:

- Voltage gain: $A_v = \frac{V_o}{V_i}$
- Current gain
- Power gain

Gain is frequency dependent.

---

## 7.4 Input and Output Impedance

### Input Impedance

- Resistance seen by the source
- High input impedance prevents signal loading

### Output Impedance

- Resistance seen by the load
- Low output impedance enables efficient signal delivery

> Good amplifiers isolate source and load.

---

## 7.5 Frequency Response & Bandwidth

Real amplifiers do not amplify all frequencies equally.

#### Key terms:

- Bandwidth
- Cutoff frequencies
- Gain–bandwidth tradeoff

---

## 7.6 Introduction to Operational Amplifiers

An **operational amplifier (op-amp)** is a high-gain differential amplifier.

#### Ideal op-amp assumptions:

- Infinite open-loop gain
- Infinite input impedance
- Zero output impedance
- Infinite bandwidth

> Op-amps are _idealized abstractions_.

---

## 7.7 Op-Amp Terminals

- Non-inverting input (+)
- Inverting input (−)
- Output
- Power supply terminals

---

## 7.8 Negative Feedback (Core Idea)

#### Negative feedback:

- Feeds part of output back to input
- Reduces gain
- Increases stability and predictability

> Feedback trades raw gain for control.

---

## 7.9 Basic Op-Amp Configurations

### Inverting Amplifier

- Gain set by resistor ratio

### Non-Inverting Amplifier

- High input impedance

### Voltage Follower

- Unity gain buffer

---

## 7.10 Practical Op-Amp Limitations

#### Real op-amps have:

- Finite gain
- Finite bandwidth
- Slew rate limitation
- Input offset voltage

These limit high-speed and precision applications.

---

## 7.11 Common Op-Amp Applications

- Signal amplification
- Summing amplifier
- Integrator
- Comparator

> Op-amps enable circuit design by composition.

---

## 7.12 Summary (Invariants of Module 7)

- Amplifiers control energy flow
- Gain is always frequency dependent
- Feedback is essential for stability
- Op-amps abstract complex transistor behavior

> This module elevates electronics from devices to systems.

---

**End of Module 7**