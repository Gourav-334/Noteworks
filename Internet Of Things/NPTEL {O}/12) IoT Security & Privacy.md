# $\fbox{Chapter 12: IoT SECURITY \& PRIVACY}$





## **Topic - 1: Introduction**

### <u>Overview</u>

- IoT security ensures **confidentiality, integrity, and availability (CIA)** of interconnected devices.
- Due to heterogeneity and limited device resources, IoT faces unique security challenges.

```css
/* Diagram Placeholder: IoT Security Overview */
```



## **Topic - 2: Need for IoT Security**

### <u>Factors</u>

- Massive device interconnectivity.
- Weak authentication and outdated firmware.
- Sensitive data transmission (health, energy, home data).
- **Objective:** Ensure end-to-end trust and secure communication.

```css
/* Diagram Placeholder: IoT Threat Surface */
```



## **Topic - 3: Security Goals**

| Goal                | Description                             |
| ------------------- | --------------------------------------- |
| **Confidentiality** | Protect data from unauthorized access.  |
| **Integrity**       | Prevent unauthorized data modification. |
| **Availability**    | Ensure system uptime and reliability.   |
| **Authentication**  | Verify entity identities.               |
| **Authorization**   | Control device and data access.         |
| **Non-repudiation** | Ensure accountability of transactions.  |



## **Topic - 4: IoT Security Architecture**

### <u>Layers and Protection Mechanisms</u>

| Layer | Components | Security Mechanisms |
|--------|-------------|----------------------|
| **Perception Layer** | Sensors, RFID, nodes | Encryption, authentication, tamper detection |
| **Network Layer** | Routers, gateways | TLS/SSL, VPN, secure routing |
| **Application Layer** | Cloud, APIs | Access control, data integrity, patch management |

```css
/* Diagram Placeholder: Layered IoT Security Model */
```



## **Topic - 5: Threats and Vulnerabilities**

### <u>Common IoT Threats</u>

| Category                 | Example                              |
| ------------------------ | ------------------------------------ |
| **Physical Attacks**     | Tampering, node capture              |
| **Network Attacks**      | DoS, spoofing, man-in-the-middle     |
| **Software Attacks**     | Malware injection, buffer overflow   |
| **Data Attacks**         | Unauthorized access, privacy leakage |
| **Configuration Issues** | Default passwords, insecure APIs     |

```css
/* Diagram Placeholder: IoT Threat Taxonomy */
```



## **Topic - 6: Major IoT Attacks**

### <u>Denial of Service (DoS / DDoS)</u>

- Overloads IoT devices or servers, making them unavailable.
- **Example:** Mirai Botnet (2016).


### <u>Spoofing & Identity Theft</u>

- Fake identities or cloned devices to manipulate systems.


### <u>Man-in-the-Middle (MITM)</u>

- Intercepts communication between devices.


### <u>Eavesdropping & Data Leakage</u>

- Passive data interception due to weak encryption.


### <u>Firmware Exploitation</u>

- Compromising devices via outdated firmware.

```css
/* Diagram Placeholder: Common IoT Attack Scenarios */
```



## **Topic - 7: IoT Security Mechanisms**

### <u>Cryptographic Protection</u>

| Mechanism                    | Example         | Layer                 |
| ---------------------------- | --------------- | --------------------- |
| **Symmetric Encryption**     | AES, DES        | Device / Network      |
| **Asymmetric Encryption**    | RSA, ECC        | Network / Application |
| **Hashing**                  | SHA-256, SHA-3  | Application           |
| **Authentication Protocols** | OAuth, EAP, TLS | Cross-layer           |

```css
/* Diagram Placeholder: IoT Cryptography Flow */
```



## **Topic - 8: Lightweight Cryptography**

### <u>Motivation</u>

- IoT devices have limited **CPU, memory, and power**.


### <u>Lightweight Algorithms</u>

| Algorithm | Type | Description |
|------------|------|-------------|
| **PRESENT** | Block Cipher | Hardware-efficient design. |
| **SPECK / SIMON** | Block Cipher | Designed by NSA for embedded systems. |
| **ChaCha20** | Stream Cipher | High-speed and low overhead. |
| **HIGHT** | Block Cipher | Low-resource 64-bit cipher. |

```css
/* Diagram Placeholder: Lightweight Cryptography Comparison */
```



## **Topic - 9: Authentication Mechanisms**

### <u>Device Authentication</u>

- Mutual authentication between devices using digital certificates or shared secrets.


### <u>Multi-Factor Authentication (MFA)</u>

- Combines passwords, biometrics, and tokens.


### <u>Secure Boot</u>

- Verifies firmware integrity before system startup.

```css
/* Diagram Placeholder: IoT Authentication Workflow */
```



## **Topic - 10: Access Control in IoT**

### <u>Models</u>

| Type     | Description                                                                               |
| -------- | ----------------------------------------------------------------------------------------- |
| **RBAC** | Role-Based Access Control – users get permissions based on roles.                         |
| **ABAC** | Attribute-Based Access Control – policies depend on attributes (e.g., device type, time). |
| **CBAC** | Context-Based Access Control – considers environment or location.                         |

```css
/* Diagram Placeholder: IoT Access Control Models */
```



## **Topic - 11: Secure Communication Protocols**

| Protocol                 | Description                            |
| ------------------------ | -------------------------------------- |
| **DTLS (Datagram TLS)**  | TLS variant for UDP-based IoT.         |
| **CoAP over DTLS**       | Secure IoT messaging (UDP-based).      |
| **MQTT over TLS**        | Ensures broker-client confidentiality. |
| **HTTPS / RESTful APIs** | Secure web-based IoT communication.    |

```css
/* Diagram Placeholder: Secure IoT Communication Stack */
```



## **Topic - 12: Privacy Issues in IoT**

| Concern                     | Example                                    |
| --------------------------- | ------------------------------------------ |
| **Data Profiling**          | Tracking user behavior from smart devices. |
| **Location Tracking**       | GPS-based privacy invasion.                |
| **Unauthorized Sharing**    | Cloud services selling user data.          |
| **Weak Consent Management** | Poor control over collected data.          |

- **Solution:** Data anonymization, differential privacy, and legal frameworks (GDPR, HIPAA).

```css
/* Diagram Placeholder: IoT Privacy Threat Map */
```



## **Topic - 13: Security Frameworks and Standards**

| Standard             | Issued By | Focus                                  |
| -------------------- | --------- | -------------------------------------- |
| **ISO/IEC 27001**    | ISO       | Information Security Management System |
| **NISTIR 8259**      | NIST      | IoT device security baseline           |
| **OWASP IoT Top 10** | OWASP     | IoT vulnerability classification       |
| **IEEE 2413**        | IEEE      | IoT architecture framework             |
| **ETSI EN 303 645**  | ETSI      | Cybersecurity for consumer IoT         |

```css
/* Diagram Placeholder: Global IoT Security Framework Landscape */
```



## **Topic - 14: Blockchain for IoT Security**

### <u>Role of Blockchain</u>

- Provides **decentralized authentication and auditability**.
- Ensures **tamper-proof transaction logs**.

#### Applications:

- Device identity management.
- Secure firmware updates.
- Data integrity and provenance.

```css
/* Diagram Placeholder: Blockchain-Enabled IoT Security */
```



## **Topic - 15: Artificial Intelligence in IoT Security**

### <u>Role</u>

- Detect anomalies and intrusions in real-time.

#### Techniques:

- Machine learning for intrusion detection.
- Deep learning for malware classification.

#### Challenges:

- Dataset imbalance, explainability, and computational overhead.

```css
/* Diagram Placeholder: AI-based IoT Security Architecture */
```



## **Topic - 16: Case Study – Smart Home Security**

### <u>Scenario</u>

- Smart home system with IoT sensors and cloud APIs.


### <u>Threats</u>

- Weak Wi-Fi passwords, unsecured mobile apps, outdated firmware.


### <u>Mitigation</u>

- Use of WPA3, OTA updates, and TLS-based communication.

```css
/* Diagram Placeholder: Smart Home Security Framework */
```



## **Topic - 17: IoT Forensics**

### <u>Definition</u>

- Process of **detecting, preserving, and analyzing** digital evidence from IoT environments.


### <u>Challenges</u>

- Volatile memory, distributed data, and encryption.

#### Approaches:

- Cloud-assisted forensics.
- Blockchain-based evidence logging.

```css
/* Diagram Placeholder: IoT Forensic Workflow */
```



## **Topic - 18: Future Research Directions**

- Quantum-safe IoT cryptography.
- Zero-trust IoT network design.
- Privacy-preserving AI models.
- Federated learning for distributed IoT intelligence.

```css
/* Diagram Placeholder: Future IoT Security Research Areas */
```



## **Topic - 19: Summary**

- IoT systems require layered security from devices to cloud.
- Lightweight cryptography and blockchain enhance resilience.
- Privacy, interoperability, and AI-driven defense define future security models.

```css
/* Diagram Placeholder: Summary of IoT Security and Privacy */
```

---
