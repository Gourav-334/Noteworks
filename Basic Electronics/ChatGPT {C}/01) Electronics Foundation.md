# $\fbox{Module 1: ELECTRONICS FOUNDATION}$

> **Purpose**  
> Establish unambiguous physical and conceptual foundations before introducing components or semiconductors.  
> This module exists to eliminate confusion that later appears in circuit theory and electronics.

---

## 1.1 What Is Electricity? (Physical View)

Electricity is **not a substance**.  
It is the **collective behavior of electric charges** under the influence of electric fields.

#### Key points:

- Electric charge is an intrinsic property of matter
- Charges exist even when nothing is “happening” electrically
- Electrical effects arise due to **charge imbalance** and **energy gradients**

#### In solid conductors:

- Protons are fixed in the lattice
- **Electrons are the mobile charge carriers**

#### Electricity manifests as:

- Charge accumulation
- Charge motion
- Energy transfer through fields

> ⚠️ Common misconception: Electricity does **not** flow like water. The analogy is useful but physically false.

---

## 1.2 Electric Charge (Q)

**Electric charge** is a fundamental property of particles that causes them to experience electric forces.

- Symbol: **Q**    
- Unit: **Coulomb (C)**

#### Properties:

- Exists in discrete packets (quantized)
- Conserved quantity (cannot be created or destroyed)
- Two types: positive and negative

#### Elementary charge:

- Charge of one electron = −1.602 × 10⁻¹⁹ C

#### Macroscopic charge:

- Practical circuits deal with **huge collections of charges**, not individual electrons

---

## 1.3 Electric Current (I)

**Electric current** is the **rate of flow of electric charge**.

$$ I = \frac{dQ}{dt} $$

- Symbol: **I**
- Unit: **Ampere (A)**

#### Interpretation:

- Current measures how fast charge is moving past a point
- Direction of conventional current is **opposite to electron flow** (historical choice)

#### Important distinction:

- Current does **not** mean energy is flowing
- Current only describes charge motion

---

## 1.4 Electric Potential & Voltage (V)

**Electric potential** is **energy per unit charge** at a point.
**Voltage** is the **difference in electric potential between two points**.

$$ V = \frac{W}{Q} $$

- Symbol: **V**
- Unit: **Volt (V)**

#### Interpretation:

- Voltage represents the _cause_ of current
- It exists even if no current flows
- It is analogous to height difference, not flow

#### Key idea:

> Voltage is a **field property**, not a moving entity.

---

## 1.5 Electrical Energy & Power

### Electrical Energy

Energy is transferred when charges move through a potential difference.

$$ W = QV $$

### Electrical Power

Power is the **rate of energy transfer**.

$$ P = VI $$

- Unit: **Watt (W)**

#### Alternate forms (from Ohm’s Law):

- $P = I^2R$
- $P = \frac{V^2}{R}$

#### Practical meaning:

- Power determines heating
- Power ratings define component safety

---

## 1.6 Ideal vs Practical Elements

### Ideal Elements

- Perfect behavior
- No losses
- Used for analysis and theory

#### Examples:

- Ideal wire: zero resistance
- Ideal source: constant voltage/current

### Practical Elements

- Have limits and losses
- Temperature dependent
- Age and degrade

> Engineering is the art of managing non‑ideal behavior.

---

## 1.7 Ohm’s Law (With Boundaries)

Ohm’s Law relates voltage, current, and resistance:

$$ V = IR $$

- Valid only for **ohmic materials**
- Assumes constant temperature

#### Resistance:

- Symbol: **R**
- Unit: **Ohm (Ω)**

#### Important limits:

- Not valid for diodes, transistors, lamps
- Not a universal law of electricity

---

## 1.8 Kirchhoff’s Laws (Why They Work)

### Kirchhoff’s Current Law (KCL)

> The algebraic sum of currents at a node is zero.

#### Physical basis:

- Conservation of charge

### Kirchhoff’s Voltage Law (KVL)

> The algebraic sum of voltages around a closed loop is zero.

#### Physical basis:

- Conservation of energy

---

## 1.9 DC vs AC (Conceptual View)

### Direct Current (DC)

- Constant direction
- Constant magnitude
- Batteries, DC supplies

### Alternating Current (AC)

- Direction reverses periodically
- Enables efficient power transmission

#### Key difference:

- DC is static in time
- AC is time‑varying

---

## 1.10 Electrical Sources

### Voltage Sources

- Maintain fixed potential difference
- Supply energy

### Current Sources

- Maintain fixed current
- Adjust voltage as needed

### Independent vs Dependent Sources

- Independent: fixed value
- Dependent: controlled by circuit variables

---

## 1.11 Summary (Invariants of Module 1)

- Charge is conserved
- Energy is conserved
- Voltage causes current
- Current alone does not imply power
- Models have limits

> These invariants remain true across **all of electronics**, analog or digital.

---

**End of Module 1**