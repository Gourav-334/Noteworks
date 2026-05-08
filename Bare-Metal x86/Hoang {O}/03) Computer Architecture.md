# $\fbox{Chapter 3: COMPUTER ARCHITECTURE}$





## **Topic - 1: Computer**

### <u>Introduction</u>

- **<u>Computer</u>:** A hardware device consisting at least one processor, one memory device, and I/O interfaces.


### <u>Types Of Computers</u>

- **<u>Single-purpose computers</u>:** Built at hardware level for specific tasks.
- **<u>General-purpose computers</u>:** Programmable computer without modifying underlying hardware.


### <u>Servers</u>

- **<u>Blade Server</u>:** A server having modular size, made by keeping physical space in mind.
- **<u>Chassis</u>:** Enclosing physical framework of a *blade server*.


### <u>General-Purpose Computers</u>

#### Desktop:

- Generally includes a mouse, a keyboard, and a monitor.
- Chassis encloses components like processor, motherboard, power supply, and hard drive.

#### Mobile Computer:

- Similar to desktop computers.
- Fewer resources for easy carrying.
- For example, laptop, tablet, smartphone, etc.

#### Game consoles:

- Highly optimized for gaming purpose.
- Accompanied by *game controller* for input purpose.
- And output device is available television.
- CPU and GPU are similar to desktop's, like *Intel Pentium III*.

![Game Consoles Examples](./media/image8.png)

- Handheld gaming consoles enclose input & output systems within the chassis.

![Handheld Game Consoles](./media/image9.png)

#### Embedded computer:

- **<u>Embedded computer</u>:** Single chip, single board computer.
- **<u>Microcontroller</u>:** Embedded computer designed to control other hardware devices.
- It is still general-purpose even with few performable specialized tasks.
- **<u>System-on-chip</u>:** Whole powerful computer packed within a single chip.
- For example, *Apple A5 SoC*, *Qualcomm Snapdragon*, etc.
- **<u>PCB</u>:** *Printed circuit board*, a place where microcontrollers & system-on-chips are connected to form a larger system.

![Raspberry Pi Model B+](./media/image10.png)

#### Field Programmable Gate Array (FPGA):

- **<u>FPGA</u>:** A hardware with array of re-configurable gates or reprogrammable circuit.
- Similar to 74HC00, FPGA contains complicated and lot more *logic blocks*.
- **<u>Logic blocks</u>:** Used to re-configure Boolean logic functions.

![FPGA Architecture](./media/image11.png)

- **<u>Netlist</u>:** Compiled code from hardware description language, which writes how circuits will be interconnected.
- The program for FPGA is written at the level of logic gates.
- FPGA is used where speed is critical and thus a specialized circuit needs to be reprogrammed for that.


### <u>Application-Specific Integrated Circuit (ASIC)</u>

- ASIC is made to run a decided circuit path using logic gates.
- Before ASIC is produced, it is prototyped using FPGA.
- But its faster than FPGA for being optimized specifically for one job.



## **Topic - 2: Computer Architecture**

### <u>Introduction</u>

$$ \framebox[7cm]{Computer Architecture} $$
$$ = $$
$$ \framebox[7cm]{Instruction Set Architecture} $$
$$ \downarrow $$
$$ \framebox[7cm]{Computer Organization} $$
$$ \downarrow $$
$$ \framebox[7cm]{Hardware} $$
