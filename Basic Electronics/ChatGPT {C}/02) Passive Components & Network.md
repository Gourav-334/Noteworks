# $\fbox{Module 2: PASSIVE COMPONENTS \& NETWORK}$

> **Purpose**  
> Introduce passive electrical components and establish how real circuits store, dissipate, and exchange energy over time.

---

## 2.1 Passive Components — Definition

A **passive component** is an element that:

- Does not generate energy
- Can only **dissipate**, **store**, or **return** energy

Three fundamental passive elements:

1. Resistor (R)
2. Capacitor (C)
3. Inductor (L)

These form the **basis of all analog circuits**.

---

## 2.2 Resistors

### Physical Meaning

A resistor opposes the flow of electric current by converting electrical energy into heat.

- Symbol: **R**
- Unit: **Ohm (Ω)**

Microscopic view:

- Electron collisions with lattice atoms
- Energy lost as thermal vibration

### Key Properties

- Approximately linear
- Temperature dependent
- Power limited

$$ V = IR $$
$$ P = I^2R $$

---

## 2.3 Capacitors

### Physical Meaning

A **capacitor stores energy in an electric field**.

- Two conductive plates
- Separated by a dielectric
- Symbol: **C**
- Unit: **Farad (F)**

$$ Q = CV $$

Energy stored:

$$ W = \frac{1}{2}CV^2 $$

### Key Behavior

- Blocks DC after charging
- Allows AC
- Voltage cannot change instantaneously

---

## 2.4 Inductors

### Physical Meaning

An **inductor stores energy in a magnetic field** when current flows.

- Coil of wire
- Magnetic flux linkage
- Symbol: **L**
- Unit: **Henry (H)**

$$ V = L \frac{dI}{dt} $$

Energy stored:

$$ W = \frac{1}{2}LI^2 $$

### Key Behavior

- Opposes change in current
- Current cannot change instantaneously

---

## 2.5 Series and Parallel Networks

### Series Connection

- Same current through all elements
- Voltages add

$$ R_{eq} = R_1 + R_2 + ... $$

### Parallel Connection

- Same voltage across all branches
- Currents add

$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + ... $$

---

## 2.6 Time-Domain Behavior (RC & RL)

### RC Circuit

- Capacitor charging and discharging
- Time constant:

$$ \tau = RC $$

### RL Circuit

- Inductor current rise and decay
- Time constant:

$$ \tau = \frac{L}{R} $$

Interpretation:

- Time constant defines response speed

---

## 2.7 Frequency Response (Intuitive)

- Capacitors favor high-frequency signals
- Inductors favor low-frequency signals

#### Enables:

- Filters
- Signal shaping
- Noise suppression

---

## 2.8 Power Dissipation & Ratings

All passive components have limits:

- Maximum voltage
- Maximum current
- Maximum power

Ignoring ratings leads to:

- Overheating
- Component failure
- Safety hazards

> Ratings are engineering constraints, not suggestions.

---

## 2.9 Summary (Invariants of Module 2)

- Resistors dissipate energy
- Capacitors store electric-field energy
- Inductors store magnetic-field energy
- Energy storage elements resist instantaneous change

> These rules govern how real circuits evolve over time.

---

**End of Module 2**