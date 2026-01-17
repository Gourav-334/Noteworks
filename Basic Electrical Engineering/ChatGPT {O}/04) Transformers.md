# $\fbox{Module 4: TRANSFORMERS}$

> **Purpose**  
> Explain how AC power is transferred efficiently between circuits using magnetic coupling, and how voltage/current levels are changed without changing frequency.

---

## 4.1 Why Transformers Exist

#### Transformers enable:

- **Voltage level change** (step-up / step-down)
- **Efficient long-distance power transmission**
- **Electrical isolation** between circuits

#### Key constraint:

> Transformers work with **AC**, not steady DC.

---

## 4.2 Basic Construction

#### A transformer consists of:

- **Primary winding** (input)
- **Secondary winding** (output)
- **Magnetic core** (low-reluctance flux path)

No electrical connection between windings — only magnetic coupling.

---

## 4.3 Principle of Operation (Mutual Induction)

- AC in primary → alternating current
- Alternating current → **alternating magnetic flux** in core
- Changing flux → **induced EMF** in secondary (Faraday’s law)

> Energy transfer occurs via the **magnetic field**, not electron flow between windings.

---

## 4.4 EMF Equation (Conceptual)

Induced EMF is proportional to:

- Number of turns
- Rate of change of flux

#### Result:

$$ \frac{V_s}{V_p} = \frac{N_s}{N_p} $$

#### Where:

- $V$ = RMS voltage
- $N$ = number of turns

---

## 4.5 Voltage and Current Relationship

For an ideal transformer:

$$ V_p I_p = V_s I_s $$

#### So:

$$ \frac{I_s}{I_p} = \frac{N_p}{N_s} $$

#### Meaning:

- Step-up voltage → step-down current
- Step-down voltage → step-up current

Power is conserved (ideally).

---

## 4.6 Ideal vs Practical Transformer

### Ideal Transformer

- No losses
- No leakage flux
- Infinite core permeability

### Practical Transformer Losses

- **Copper loss** ($I^2R$ in windings)
- **Core loss** (hysteresis + eddy currents)
- **Leakage flux**

---

## 4.7 Transformer Efficiency

#### Efficiency:

$$ \eta = \frac{\text{Output Power}}{\text{Input Power}} \times 100\% $$

Power transformers achieve **very high efficiency** (>95%).

---

## 4.8 Voltage Regulation

Voltage regulation measures output voltage drop from no-load to full-load.

#### Caused by:

- Winding resistance
- Leakage reactance

Lower regulation → better performance.

---

## 4.9 Transformer Types

- Step-up / Step-down
- Power transformer
- Distribution transformer
- Isolation transformer

All follow the same basic principle.

---

## 4.10 Why DC Does Not Work

#### With DC:

- Flux becomes constant
- No changing flux → no induced EMF
- Core saturates → overheating

> Transformers require **changing magnetic flux**.

---

## 4.11 Summary (Module 4)

- Transformers transfer AC power magnetically
- Voltage ratio equals turns ratio
- Power is conserved (ideally)
- Losses limit real performance

---

**End of Module 4**