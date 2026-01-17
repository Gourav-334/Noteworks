# $\fbox{Module 2: AC CIRCUIT ANALYSIS}$

> **Purpose**  
> Analyze how resistors, inductors, and capacitors behave in AC circuits using phasors, and understand real power, reactive power, and power factor.

---

## 2.1 Impedance in AC Circuits

In AC, opposition to current is **impedance (Z)**.

$$ Z = R + jX $$

#### Where:

- **R** → resistance (real, dissipates energy)
- **X** → reactance (imaginary, stores energy)

#### Magnitude:
$$ |Z| = \sqrt{R^2 + X^2} $$

---

## 2.2 Pure Resistive Circuit (R)

- Voltage and current are **in phase**
- No energy storage
- All power is dissipated as heat

$$ Z_R = R $$

---

## 2.3 Pure Inductive Circuit (L)

- Inductor resists **change in current**
- Current **lags** voltage by 90°

#### Inductive reactance:
$$ X_L = \omega L $$

#### Impedance:

$$ Z_L = jX_L $$

Energy stored temporarily in magnetic field.

---

## 2.4 Pure Capacitive Circuit (C)

- Capacitor resists **change in voltage**
- Current **leads** voltage by 90°

#### Capacitive reactance:

$$ X_C = \frac{1}{\omega C} $$

#### Impedance:
$$ Z_C = -jX_C $$

Energy stored temporarily in electric field.

---

## 2.5 Series RLC Circuit

#### Total impedance:

$$ Z = R + j(X_L - X_C) $$

#### Phase angle:

$$ \tan\phi = \frac{X_L - X_C}{R} $$

- Net inductive if (X_L > X_C)
- Net capacitive if (X_C > X_L)

---

## 2.6 Current in AC Circuit

$$ I = \frac{V}{Z} $$

- Magnitude depends on $|Z|$
- Phase depends on angle of $Z$

---

## 2.7 AC Power Components

### Real (Active) Power

$$ P = VI\cos\phi $$

- Unit: watt ($W$)
- Actually consumed

### Reactive Power

$$ Q = VI\sin\phi $$

- Unit: $VAR$
- Oscillates between source and reactive elements

### Apparent Power

$$ S = VI $$

- Unit: $VA$

---

## 2.8 Power Factor

$$ \text{Power Factor} = \cos\phi $$

#### Indicates:

- Efficiency of power usage
- Ratio of useful power to supplied power

Low power factor → higher current → higher losses.

---

## 2.9 Power Triangle

#### Relationship:

$$ S^2 = P^2 + Q^2 $$

Visual tool to understand real vs reactive power.

---

## 2.10 Practical Significance

- Power factor affects transmission losses
- Industries use **power factor correction**
- AC machines depend on phase behavior

---

## 2.11 Summary (Module 2)

- Impedance generalizes resistance for AC
- Inductors and capacitors introduce phase shift
- Power splits into real and reactive components
- Power factor measures effectiveness of power use

---

**End of Module 2**