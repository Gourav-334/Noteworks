# $\fbox{Module 6: FIELD EFFECT TRANSISTORS}$

> **Purpose**  
> Introduce voltage-controlled devices and explain why MOSFETs dominate modern electronics, from logic to power systems.

---

## 6.1 Why Field-Effect Devices

Bipolar transistors are current-controlled.

#### Field Effect Transistors (FETs) are:

- **Voltage-controlled**
- High input impedance
- Easier to scale and integrate

> Modern electronics exists because charge can be controlled by _fields_, not currents.

---

## 6.2 FET vs BJT (Conceptual Contrast)

| Aspect          | BJT      | FET       |
| --------------- | -------- | --------- |
| Control         | Current  | Voltage   |
| Input impedance | Low      | Very high |
| Speed           | Moderate | High      |
| Power           | Higher   | Lower     |

This shift enables dense integration.

---

## 6.3 MOSFET Structure

$$MOSFET = \text{Metal Oxide Semiconductor Field Effect Transistor}$$

#### Terminals:

- **Gate (G)**
- **Source (S)**
- **Drain (D)**
- **Body/Substrate (B)**

#### Key feature:

- Gate is insulated by a thin oxide layer

---

## 6.4 NMOS and PMOS

### NMOS

- Majority carriers: electrons
- Faster
- Lower resistance

### PMOS

- Majority carriers: holes
- Slower
- Higher resistance

They are complementary devices.

---

## 6.5 Channel Formation & Threshold Voltage

Applying gate voltage creates an **inversion layer**.

- Below threshold: no channel
- Above threshold: conductive channel forms

#### Threshold voltage (Vₜ):

- Minimum gate voltage required for conduction

> MOSFETs are normally OFF devices.

---

## 6.6 Regions of Operation

### Cutoff

- $V_GS < Vₜ$
- Device OFF

### Triode (Linear)

- Acts like voltage-controlled resistor

### Saturation

- Current controlled by gate voltage
- Used in amplification

---

## 6.7 MOSFET as a Switch

#### Key advantages:

- Near-zero gate current
- Low ON resistance
- Fast switching

#### Used in:

- Digital logic
- Power converters
- Motor drivers

> Switching, not amplification, is the MOSFET’s primary strength.

---

## 6.8 CMOS Logic (Intuition)

$$CMOS = \text{Complementary MOS}$$

- NMOS pulls output LOW
- PMOS pulls output HIGH

#### Benefits:

- Near-zero static power consumption
- High noise immunity

---

## 6.9 Scaling & Modern Relevance

#### Why MOSFETs scale well:

- Field-based control
- Minimal gate current
- Compatible with lithography

#### This enables:

- Integrated circuits
- Microprocessors
- Memory devices

---

## 6.10 Practical Limitations

#### Real MOSFET issues:

- Gate oxide breakdown
- Leakage currents
- Short-channel effects
- Heat dissipation

---

## 6.11 Summary (Invariants of Module 6)

- MOSFETs are voltage-controlled
- Gate controls channel via electric field
- NMOS and PMOS are complementary
- CMOS enables modern digital systems

> This module completes the transition to modern electronics.

---

**End of Module 6**