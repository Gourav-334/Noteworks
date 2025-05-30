# $\fbox{Chapter 8: DATABASE SECURITY}$





## **Topic - 1: Data Security**

### <u>Data Security</u>

- Protection from unauthorized access.
- DBA decides who will access what.


### <u>Benefits Data Security Offers</u>

- Keeps your reputation clean.
- Resists potential damage to client accounts.


### <u>Data Integrity</u>

- Stable, non-scattered, as it is data.
- Or in simple language, making sure that data is not corrupt.
- It helps keeping data safer.
- Security is built-in during database designing phase.


### <u>Physical Integrity</u>

- Basic definition of data integrity.
- Can be destroyed in natural disasters, or when electricity goes off.


### <u>Logical Integrity</u>

- Protection from human error and hackers.


### <u>Access Control</u>

- Ensures that clients are who they claim to be.
- Three models: DAC, MAC, RBAC


### <u>Discretionary Access Control (DAC)</u>

- This access is given to creator/owner of the data.
- He controls access control too.
- SQL commands for this are `GRANT`, `REVOKE`.


### <u>Mandatory Access Control (MAC)</u>

- Here one person does not control everything.
- Access permission is bifurcated to various levels.
- Users at each level have different level of control as per their access.
- Users at higher level have more access to data.
- These permissions include read & write operations.


### <u>Role Based Access Control (RBAC)</u>

- Similar to MAC.
- It is the level of access an employee of an organization has.
- User can only access data that is required to perform his job.
- Access is granted on the basis of authority of the employee.


### <u>Intrusion Detection System (IDS)</u>

- A safety application.
- Alarms the authority when any malicious activity is noticed.
- Scans for suspicious patterns in network/system.
- **<u>SIEM</u>:** Security information & event management


### <u>Different IDS</u>

- Network IDS
- Host IDS
- Protocol-based IDS
- Application protocol-based IDS
- Hybrid IDS


### <u>Working of IDS</u>

#### General information chaining order:

- Internet
- Router
- Firewall
- IDS
- System

>**<u>NOTE</u>:**
>After information passed through firewall, IDS immediately checks it.


### <u>Detection Methods by IDS</u>

#### Signature based detection:

- Binary computing pattern formed on network traffic.
- Pre-programmed malicious instruction sequence readings.
- Signature based detection lacks at detecting new malicious patterns.

#### Anomaly based detection:

- Detects unknown malware attacks.
- Uses machine learning.
- These ML models can be trained for particular hardware.


### <u>IDS vs Firewall</u>

- Firewall looks for outward intrusion, IDS looks for inside intrusion.
- Firewall restricts access between networks.


### <u>SQL Injection</u>

- Can alter/manipulate background code.
- May cost revelation of sensitive/unintended data.


### <u>Data Encryption</u>

- Data is made unreadable.
- So that if someone accesses data, it would be useless for him.
- **<u>Cipher text</u>:** Encoded data.
- Readable for authorized users however.


### <u>Data Decryption</u>

- Uses similar algorithm to encryption.
- Conversion of encrypted data is not same as decrypting data.


### <u>Types of Encryptions</u>

#### Symmetric key encryption:

- Also known as private key encryption.
- Encryption and decryption have same keys.
- Sender and receiver must be careful when sharing the key.

#### Asymmetric key encryption:

- Also known as public key encryption.
- Encryption and decryption keys are different.
- The sender keeps the encryption key.
- The receiver keeps the decryption key.
 
---
