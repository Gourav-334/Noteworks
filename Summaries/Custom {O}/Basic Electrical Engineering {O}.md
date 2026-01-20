# $\fbox{BASIC ELECTRICAL ENGINEERING}$





## **Chapter - 1: AC Fundamentals & Phasors**

- **AC advantages:** Efficient voltage transformation, low transmission loss over distances, produced simply by rotating electrical machines.
- **Angular frequency ($\omega$):** Rate of change of sinusoidal phase/angle ($\phi$) in circle. ($\omega = 2 \pi r$)
- **Peak value ($V_m$):** Peak value of AC voltage.
- **AC standard form:** $v(t)=V_msin(\omega t + \phi)$
- **One cycle:** One complete sinusoidal journey for a waveform.
- **Root mean square (RMS):** DC value producing same heat as per given AC values. ($V_{rms}=\frac{V_m}{\sqrt{2}}$)
- RMS is applicable to both $V$ and $I$, which depend on same sinusoidal AC curve.
- **Inductive circuits:** Circuits $I$ lags in phase angle from $V$.
- **Capacitive circuits:** Circuits $I$ leads in phase angle from $V$.
- **Phasor:** Rotating vector diagram (sinusoidal circle) independent of time.
- **Radius ($r$):** Represents the peak amplitude of $V$ or $I$ in a circuit.
- **Instantaneous analysis:** Time-domain & uses differential equations.
- **Steady state AC analysis:** Phasor-domain & uses algebraic equations.



## **Chapter - 2: AC Circuit Analysis**

- **j:** $\sqrt{-1}$
- **Reactance ($X$):** Assumed temporary energy buffer.
- **Impedance ($Z$):** Opposition to flow of current. ($Z=R+jX$)
- **Impedance magnitude:** $|Z|=\sqrt{R^2+X^2}$
- **Pure resistive circuit:** Circuit that doesn't store energy & dissipates everything as heat. ($X_R=0$)
- **Purely inductive circuit:** Circuit where inductor resists change in current. ($X_L=\omega L$), ($Z_L=jX_L$)
- Current lags voltage by $90 \degree$ in purely inductive circuit.
- **Purely capacitive circuit:** Circuit where capacitor resists change in voltage. ($X_C=\frac{1}{\omega C}$), ($Z_C=-jX_C$)
- Current leads voltage by $90\degree$ in purely capacitive circuit.
- **Series RLC circuit:** $Z=R+j(X_L-X_C)$
- **RLC phase angle:** $tan \phi = \frac{X_L-X_C}{R}$
- **AC value:** $I=\frac{V}{Z}$
- **AC real power:** Power that is actually consumed. ($P=VI\;cos\phi$)
- **AC reactive power:** Power that keeps moving between source and reactive elements, but never consumed. ($Q=VI\;sin \phi$)
- **AC apparent power:** Total power that appears to be used in circuit, both of previous. ($S=VI$)
- **Power factor ($cos \phi$):** Ratio of useful power to the supplied power.
- **Power triangle:** Relationship between real and reactive power. ($S^2=P^2+Q^2$)



## **Chapter - 3: Magnetic Circuits**

- **Energy conversion:** Electrical $\leftrightarrow$ Magnetic $\leftrightarrow$ Mechanical
- **Magnetic flux ($\Phi$):** Total magnetic field passing through an area. Measured in Weber ($Wb$).
- **Magnetomotive force ($MMF$):** Force causing magnetic flux. ($MMF=NI$)
- **Number of turns ($N$):** Total coil turns, measured in Turns ($T$).
- **Magnetic field intensity ($H$):** Strength of field produced by MMF, measured in $A/m$.
- **Magnetic flux density ($B$):** Flux per unit area, measured in Tesla ($T$).
- **Permeability ($\mu$):** Property of material supporting flux flow, higher $\mu$ meaning easier flow. ($\mu=\mu_0\mu_r$)
- **Permeability of free space:** $\mu_0$
- **Relative permeability:** $\mu_r$
- **Reluctance ($\mathcal{R}$):** Opposition to magnetic flux. ($\mathcal{R}=\frac{l}{\mu A}$)
- **Magnetic circuit law:** Also known as Hopkinson's law. ($\Phi=\frac{MMF}{R}$)
- **Series magnetic circuit:** Same flux across, active MMF add up.
- **Parallel magnetic circuit:** Same MMF across, flux splits from nodes.
- **Magnetic energy storage ($W$):** Energy is stored and returned in ideal circuits. ($W=\frac{1}{2}LI^2$)
- **Hysteresis:** Energy loss per cycle in practical circuits.
- **Eddy's current:** Current induced in magnetic field from change in flux, also producing heat.