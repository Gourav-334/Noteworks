# $\fbox{BARE-METAL PROGRAMMING}$





## **Chapter - 1: Domain Documents**

- **Problem domain:** Non-technical knowledge required to work on particular technical project.
- **Software-exclusive domains:** Domain including software used by other software.
- **Software requirement document:** Contains information related to *problem domain*.
- **Software specification:** Specifies what output the software must produce for given inputs.
- **Required documents -** *Intel® 64 and IA-32 Architecture Software Developer's Manual (Volume 1, 2, 3)*, *Intel® 3 Series Express Chipset Family Datasheet*, System V ABI.
- **Functional description:** Intel's software requirement document.


## **Chapter - 2: Layers Of Abstraction**

- **Transistor:** Electrical device that can switch automatically as per threshold voltage.
- Threshold is between $+3.5v$ to $+5.0v$, below which the transistor doesn't allow flow of current.
- Earlier, instead of transistors, vacuum tubes (manually switched) represented individual bits.
- **MOSFET:** Low switching delay, stable, low power consumption, easy manufacturing, etc.
- **Functionally complete:** Boolean functions sufficient to create other functions (NAND, NOR).
- **Inverters:** NOT gate (upper part PMOS, lower part NMOS)
- **CMOS:** Contains a NMOS and a PMOS.
- **PMOS:** Conducts if input is LOW, blocks if input is HIGH.
- **NMOS:** Blocks if input is LOW, conducts if input is HIGH.
- For each input in a circuit, there is present one NMOS and one PMOS each.
- **7HC00:** A chip with 14 pins (8 input, 4 output, 1 voltage, 1 ground), including 4 NAND gates.
- **Notch:** A circle on chip's one corner which tells where *pin 1* is.
- **Don't care value:** No fixed value
- **Opcode:** Operation code
- **Decoder:** Electrical device that decides which device to select next.



## **Topic - 3: Computer Architecture**

- **Computer:** A hardware device consisting at least one processor, one memory device, and I/O interfaces.
- **Single-purpose computers:** Hard wired at hardware level to perform specific tasks.
- **General-purpose computers:** Programmable computer
- **Blade server:** A server with modular size.
- **Embedded computer:** Single chip, single board computer.
- **Microcontroller:** Embedded computer that controls other hardware devices.
- **System-on-chip:** Very powerful computer packed in a single chip.
- **PCB:** Printed Circuit Board
- **FPGA:** A hardware device containing re-configurable gates or reprogrammable circuits.
- **Logic blocks:** Re-configurable Boolean logic blocks.
- **Netlist:** Compiled code from HDLs which defines how circuit will be like.
- **ASIC:** Application-Specific Integrated Circuit

$$ \text{Computer Architecture = ISA (Computer Organization (Hardware))} $$

- **Computer organization:** Design of how computer's hardware components are interconnected.
- Two computers may have same ISA but difference organization (like Intel & AMD).
- [Refer to Von Neuman's architecture](https://github.com/Gourav-334/Noteworks/blob/main/Bare-Metal%20x86/Hoang%20%7BO%7D/media/image12.png)
- **Bus:** Electrical wires that transfer raw bits.
- Modern processors come with pre-implemented OS features like paging or switching.
- **Registers:** High-speed data access containers.
- **Ports:** Specialized registers used to exchange data with other devices.
- **Memory controller:** Inbuilt in modern CPUs, while older ones used *MCH (Memory Controller Hub)*.
- RAM contains transistors and capacitors connected to each of the transistor.
- **Bus-width:** Number of wires in bus to carry bits parallelly.
- Processors belonging to same family or series differ in hardware implementation, each made to suit different requirements.
- **Chipset:** Set of chips which enable computer with different services.
- **Motherboard slots -** 1 CPU slot, 1 northbridge chipset slot, 1 southbridge chipset slot, memory stick slots, at least 1 graphic card slot, generic slots, and I/O ports.
- **Northbridge slot:** Used for high-performance communication (CPU / GPU / memory).
- **Southbridge slot:** Used for other communications (I/O ports, etc).
- **Graphic card:** GPU chip, VRAM, VRM, cooling system, BIOS/firmware, display output, PCIe, etc.
- **VRM:** Video Regulation Circuitry
