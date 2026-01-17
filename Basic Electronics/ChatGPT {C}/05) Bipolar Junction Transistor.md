# $\fbox{Module 5: BIPOLAR JUNCTION TRANSISTOR}$

> **Purpose**  
> Introduce controlled current amplification and switching by extending PN-junction physics into a three-terminal active device.

---

## 5.1 Why Transistors Exist

Diodes allow **one-way conduction**, but they do not provide **control**.

#### A transistor enables:

- Amplification (small signal controls large signal)
- Switching (logic and power control)

> The transistor is the smallest useful _control element_ in electronics.

---

## 5.2 BJT Structure

A **Bipolar Junction Transistor** consists of three regions:

- **Emitter (E)**
- **Base (B)**
- **Collector (C)**

#### Two types:

- **NPN**
- **PNP**

#### Key construction facts:

- Emitter: heavily doped
- Base: very thin, lightly doped
- Collector: moderately doped

---

## 5.3 Principle of Operation

The BJT works on **carrier injection and collection**.

#### For an NPN transistor:

- Emitter–Base junction: forward biased
- Base–Collector junction: reverse biased

#### Result:

- Electrons injected from emitter
- Few recombine in base
- Majority collected by collector

> A small base current controls a much larger collector current.

---

## 5.4 Transistor Currents

#### Relationships:

$$ I_E = I_B + I_C $$

#### Current gain:

$$ \beta = \frac{I_C}{I_B} $$

#### Key points:

- $\beta$ is not constant
- Device- and temperature-dependent

---

## 5.5 Modes of Operation

### Cutoff

- Both junctions reverse biased
- Transistor OFF

### Active Region

- E–B forward biased
- B–C reverse biased
- Amplification mode

### Saturation

- Both junctions forward biased
- Fully ON (switching)

---

## 5.6 BJT as a Switch

#### Switching behavior:

- Cutoff → OFF
- Saturation → ON

#### Applications:

- Digital logic (historical)
- Relay drivers
- LED drivers

#### Limitations:

- Power loss in saturation
- Slower than MOSFETs

---

## 5.7 BJT as an Amplifier (Conceptual)

#### In active region:

- Small base signal → large collector variation

#### Common configurations:

- **Common Emitter (CE)** – high gain
- **Common Base (CB)** – high bandwidth
- **Common Collector (CC)** – buffer

> Configuration changes _how_ signals are traded, not the physics.

---

## 5.8 Biasing — Why It Is Necessary

#### Biasing ensures:

- Stable operating point
- Operation in desired region

#### Without biasing:

- Distortion
- Thermal runaway
- Unpredictable gain

> A transistor without biasing is unusable.

---

## 5.9 Thermal Effects & Stability

#### Temperature increase causes:

- Increased carrier concentration
- Increased collector current

#### Risk:

- **Thermal runaway**

#### Mitigation:

- Bias stabilization
- Emitter resistors

---

## 5.10 Practical Limitations

#### Real BJTs exhibit:

- Finite gain
- Junction capacitances
- Power dissipation limits
- Storage delay in saturation

These motivate MOSFET dominance in modern systems.

---

## 5.11 Summary (Invariants of Module 5)

- BJT is a current-controlled device
- Small base current controls large collector current
- Biasing defines usability
- Temperature always matters

> The BJT introduces _gain_—the defining leap of electronics.

---

**End of Module 5**