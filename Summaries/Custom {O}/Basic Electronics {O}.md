# $\fbox{BASIC ELECTRONICS}$





## **Chapter - 1: Electronics Foundations**

- **Electricity:** Behavior of electric charges under electric fields.
- Electrical affects arise from charge imbalance & energy gradients.
- **Electric charge ($Q$):** Property of particles causing them to experience electrical force.
- **One electron charge ($e$):** $e = -1.602 \times 10^{-19} C$
- **Electric current ($I$):** Rate of flow of electric charge. ($I = \frac{dQ}{dt}$)
- Direction of current is opposite to electron's flow.
- **Electric potential ($V$):** Energy per unit charge at a point in circuit.
- Electrons carry electric potential ($V$) which they loose when used.
- **Voltage / Potential difference ($V$):** Difference between two electric potentials.
- **Electrical charge ($W$):** Energy transferred when potential difference changes. ($V=\frac{W}{Q}$)
- **Power ($P$):** Rate of energy transfer. ($P=VI$)
- **Ohm's law:** Voltage is directly proportional to current. ($V=IR$)
- **Kirchhoff's current law (KCL):** Sum of currents at a node is $0$ (fast distribution from node).
- **Kirchhoff's voltage law (KVL):** Sum of voltages in a closed loop is $0$.
- **Direct current (DC):** Constant direction & magnitude.
- **Alternating current (AC):** Direction reverses periodically.



## **Chapter - 2: Passive Components & Network**

- **Passive components:** Does not generate energy (register, capacitor, inductor).
- **Register ($R$):** Opposes flow of current by converting electrical energy into heat.
- **Capacitor ($C$):** Stores energy in electric field (two conductive plate + dielectric in mid). ($Q=CV$)
- **Inductor ($L$):** Stores energy in magnetic field (coil of wire). ($V=L \frac{dI}{dt}$)
- **Series connection:** Same current across / voltages add.
- **Parallel connection:** Same voltage across / currents add.
- **Time constant ($\tau$):** Response speed
- **RC circuit:** Capacitor charging and discharging ($C$ resists change in $V$). ($\tau =RC$)
- **RL circuit:** Inductor current rise and decay ($L$ resists change in $I$). ($\tau = \frac{L}{R}$)
- **Frequency response:** Capacitors = $\uparrow$ freq. signals & Inductors = $\downarrow$ freq. signals



## **Chapter - 3: Semiconductor Physics**

- **Charge carriers:** High in conductors, low in insulators, controlled in semiconductors.
- **Band:** Equilibrium energy arising from merging of each atom's energy.
- **Valence band:** Tightly held electrons.
- **Conduction band:** Loosely held electrons.
- **Bandgap ($E_9$):** Region without energy.
- **Hole:** Absence of electrons, considered positive charge (for electrons' behavior to it).
- **Intrinsic semiconductor:** Semiconductor made purely from one element ($n_{electrons}=n_{holes}$).
- **Extrinsic semiconductor:** Making extrinsic semiconductors is also known as doping.
- **N-type semiconductor:** Extrinsic with pentavalent dopant. ($n_{electrons}>n_{holes}$)
- **P-type semiconductor:** Extrinsic with trivalent dopant. ($n_{electrons}<n_{holes}$)
- **Drift:** Electric field induced motion of charges.
- **Diffusion:** Concentrated gradient (charge) induced motion of charges.
- **Recombination:** Electrons filling holes.
- **Generation:** Creation of electron-hole pair (opposite of recombination).
- $\text{Rate of generation = Rate of recombination}$



## **Chapter - 4: Diodes & Rectifier Circuits**

- **Diode:** PN junction (P-type region + N-type region)
- In PN junction, electrons move N to P, and holes move P to N.
- **Depletion region:** Region between P & N junctions.
- **Forward bias:** P-side connected to +ve terminal, depletion region $\downarrow$, easy current flow.
- **Reverse bias:** P-side connected to -ve terminal, depletion region $\uparrow$, difficult current flow.
- **Practical diode drops:** Silicon $\approx 0.7V$, Germanium $\approx 0.3V$
- **Rectification:** Converting AC to DC by blocking -ve clock cycles and allowing +ve ones.
- **Half-wave rectifier:** Uses only +ve waveform in AC, uses 1 diode.
- **Full-wave rectifier:** Uses +ve waveform and converts -ve ones to +ve, uses 2-4 diodes.
- **Bridge rectifier:** Rectifier with 4 diodes in diamond shape, with 2 dropping in each cycle.
- **Capacitor filter:** Filters ripples in rectified AC by charging in peak, and discharging otherwise.
- **Zener diode:** Doesn't break in reverse bias.
- **Zener regulator:** A resistor and Zener diode in series, maintaining constant output voltage.



## **Chapter - 5: Bipolar Junction Transistor**

- **Transistor:** Control element used in amplification and switching.
- **Bipolar junction transistor (BJT):** Transistor with 3 regions - emitter, base, collector.
- **Emitter:** Injects electrons, heavily doped.
- **Base:** Place to recombine, very thin and lightly doped.
- **Collector:** Collects electrons, moderately doped
- **NPN transistor:** Emitter-base junction is forward biased, base-collector is reverse.
- NPN transistor is used for amplification.
- **Transistor current:** $I_E=I_B+I_C$
- **Current gain:** $\beta = \frac{I_C}{I_B}$
- **Cutoff:** BJT switched OFF
- **Saturation:** BJT switched ON