# $\fbox{Module 4: DIODES \& RECTIFIER CIRCUITS}$

> **Purpose**  
> Introduce the first practical nonlinear device and show how semiconductor physics collapses into one-way conduction, rectification, and basic regulation.

---

## 4.1 From Semiconductor to Device

A **diode** is formed by joining:

- One **P-type** region
- One **N-type** region

This creates a **PN junction**, the foundation of nearly all semiconductor devices.

Key idea:

> The diode does not _create_ directionality; the junction physics enforces it.

---

## 4.2 PN Junction Formation

When P-type and N-type materials are joined:

- Electrons diffuse from N → P
- Holes diffuse from P → N

This leads to:

- Recombination near the junction
- Formation of a **depletion region**
- Built-in electric field opposing further diffusion

---

## 4.3 Biasing the PN Junction

### Forward Bias

- P-side connected to positive terminal
- Depletion region narrows
- Current flows easily

### Reverse Bias

- P-side connected to negative terminal
- Depletion region widens
- Only small leakage current flows

> Biasing determines whether diffusion or field dominance wins.

---

## 4.4 Diode I–V Characteristics

The diode is a **nonlinear device**.

#### Key regions:

- Cutoff (reverse bias)
- Knee region
- Conduction region

#### Practical diode drops:

- Silicon ≈ 0.7 V
- Germanium ≈ 0.3 V

> Voltage drop is not a flaw; it is a physical consequence.

---

## 4.5 Diode Models (For Circuit Analysis)

### Ideal Model

- Zero voltage drop
- Infinite reverse resistance

### Practical Model

- Constant forward voltage drop

### Piecewise Linear Model

- Threshold + small resistance

> Models are chosen for usefulness, not truth.

---

## 4.6 Rectification — Converting AC to DC

Rectification uses diodes to:

- Block negative cycles
- Allow positive cycles

### Half-Wave Rectifier

- One diode
- Uses only half the AC waveform
- High ripple

### Full-Wave Rectifier

- Two or four diodes
- Uses entire waveform
- Better efficiency

---

## 4.7 Bridge Rectifier

A **bridge rectifier** uses four diodes to:

- Eliminate center-tapped transformers
- Improve practical usability

Trade-off:

- Two diode drops in conduction path

---

## 4.8 Filtering the Rectified Output

Rectified output is **pulsating DC**.

#### Capacitor filter:

- Charges at peaks
- Discharges between peaks
- Reduces ripple

Ripple depends on:

- Load current
- Capacitance
- Frequency

---

## 4.9 Zener Diode & Voltage Regulation

A **Zener diode** operates in controlled breakdown.

#### Key properties:

- Fixed breakdown voltage
- Used for regulation and protection

#### Zener regulator:

- Series resistor + Zener diode
- Maintains constant output voltage

> Breakdown is engineered behavior, not failure.

---

## 4.10 Practical Limitations

#### Real diodes exhibit:

- Reverse leakage current
- Temperature dependence
- Power dissipation limits
- Switching speed limits

#### These matter in:

- High-frequency circuits
- Power electronics

---

## 4.11 Summary (Invariants of Module 4)

- PN junction creates directionality
- Biasing controls conduction
- Diodes are nonlinear elements
- Rectification enables DC power
- Regulation exploits controlled breakdown

> This module is the bridge from physics to circuits.

---

**End of Module 4**