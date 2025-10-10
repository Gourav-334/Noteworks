# $\fbox{Chapter 8: KEY MANAGEMENT \& DISTRIBUTION}$





## **Topic - 1: Symmetric Key Distribution Using Symmetric Encryption**

### <u>Introduction</u>

- Purpose is to deliver secret keys securely between parties.

#### Types Of Keys:

- **Master key -** Long-term, rarely used.
- **Session key -** Temporary, used for single session.

### Objectives:

- Entities share same secret key.
- Change keys frequently.


### <u>Key Distribution Methods</u>

1. A selects key $\rightarrow$ physically delivers to B.
2. Third party selects key $\rightarrow$ physically delivers to A & B.
3. A or B transmits new key encrypted with old key.
4. Trusted third party (KDC) distributes session key.


### <u>Key Distribution Center (KDC)</u>

- Trusted third-party managing session key distribution.

#### Process:

1. A $\rightarrow$ KDC: request session key (includes IDA, IDB, N1).
2. KDC $\rightarrow$ A: E(Ka, \[Ks||IDA||IDB||N1\]) || E(Kb, \[Ks||IDA\]).
3. A $\rightarrow$ B: E(Kb, \[Ks||IDA\]).
4. B $\rightarrow$ A: E(Ks, N2).
5. A $\rightarrow$ B: E(Ks, f(N2)).
- Nonce (N1, N2): timestamp/random value ensuring uniqueness.
- Ensures both parties share valid session key Ks and prevents replay.


### <u>Without KDC</u>

- Each system maintains $(n−1)$ master keys with peers.

#### Process:

  1. A $\rightarrow$ B: IDA || N1.
  2. B $\rightarrow$ A: E(Km, \[Ks||IDA||IDB||f(N1)||N2\]).
  3. A $\rightarrow$ B: E(Ks, f(N2)).



## **Topic - 2: Symmetric Key Distribution Using Asymmetric Encryption**

### <u>Simple Secret Key</u>

1. A generates {PUa, PRa} $\rightarrow$ sends PUa || IDA to B.
2. B generates Ks $\rightarrow$ sends E(PUa, Ks) to A.
3. A decrypts using D(PRa, E(PUa, Ks)).
4. Both discard temporary keys.


### <u>With Confidentiality & Authentication</u>

1. A $\rightarrow$ B: E(PUb, [N1||IDA]).
2. B $\rightarrow$ A: E(PUa, [N1||N2]).
3. A $\rightarrow$ B: E(PUb, N2).
4. A $\rightarrow$ B: E(PUb, E(PRa, Ks)).
5. B decrypts $\rightarrow$ D(PUa, D(PRb, M)).



## **Topic - 3: Distribution of Public Keys**

### <u>Introduction</u>

- **Goal -** Ensure key authenticity.
- **Problem -** Prevent impersonation or key spoofing.


### <u>Methods</u>

1. **Public announcement:**
   - Openly distribute key (email, website, etc.).
   - Problem: identity spoofing.

2. **Public directory:**
   - Maintained by authority.
   - {Name, Public Key} entries.
   - Secure authenticated communication required.

3. **Public-key authority:**
   - Centralized entity verifying and distributing keys securely.
   - **Process**:
     1. A $\rightarrow$ Authority: Request || T1.
     2. Authority $\rightarrow$ A: E(PRauth, \[PUb||Request||T1\]).
     3. A $\rightarrow$ B: E(PUb, \[IDA, N1\]).
     4. B $\rightarrow$ Authority: Request || T2.
     5. Authority $\rightarrow$ B: E(PRauth, \[PUa||Request||T2\]).
     6. B $\rightarrow$ A: E(PUa, \[N1||N2\]).
     7. A $\rightarrow$ B: E(PUb, N2).

4. **Public-key certificates:**
   - Issued by Certificate Authority (CA).
   - Any participant can read certificate to obtain public key, verify origin (signed by CA), and confirm validity & expiration.



## **Topic - 4: X.509 Certificates**

### <u>Introduction</u>

- **<u>X.509</u>:** Standard for digital certificates (Public Key Infrastructure – PKI).
- Ensures public key authenticity of user, device, or service.
- Each certificate signed by trusted CA’s private key.


### <u>Structure</u>

| Field | Description |
|--------|--------------|
| Version | Certificate format version (1, 2, or 3). |
| Serial Number | Unique ID assigned by issuing authority. |
| Signature Algorithm | Algorithm used for signing. |
| Issuer Name | Entity issuing the certificate (CA). |
| Validity Period | Not Before – Not After dates. |
| Subject Name | Entity whose key is being certified. |
| Subject Public Key Info | Public key + algorithm ID. |
| Unique Identifiers | Optional fields for CA and subject. |
| Extensions | Extra attributes (in version 3). |
| Signature | Signed hash verifying authenticity. |



## **Topic - 5: Public Key Infrastructure (PKI)**

### <u>Introduction</u>

- **<u>PKI</u>:** Set of hardware, software, people, and procedures managing digital certificates.


### <u>Functions</u>

- Create, manage, store, distribute, revoke certificates.
- Enable secure acquisition & verification of public keys.


### <u>PKI Entities</u>

- **End Entity -** User, device, or system.
- **Certification Authority (CA) -** Issues certificates & CRLs.
- **Registration Authority (RA) -** Verifies identity before issuing certificates.
- **CRL Issuer -** Publishes certificate revocation lists.


### <u>PKI Operations</u>

- Registration, Initialization, Certification.
- Key pair recovery & update.
- Revocation & publication.

```css
/* Diagram Placeholder: PKI Structure */
/* Diagram Placeholder: X.509 Certificate Fields */
```



## **Topic - 6: Advanced Topics**

### <u>Firewall</u>

- Security system filtering incoming/outgoing network traffic.
- Acts as barrier between trusted and untrusted networks.

#### Types:

- Hardware or software.
- Packet filtering, stateful inspection, proxy firewall.


### <u>Intruders</u>

- Unauthorized users attempting system/data access.

#### Types:

- External $\rightarrow$ outsiders.
- Internal $\rightarrow$ insiders or employees.
- **Methods -** Phishing, password cracking.


### <u>Virus</u>

- Malicious code attaching to legitimate files/programs.
- Replicates during execution.
- **Effects -** Corruption, slowdown, data loss.
- **Prevention -** Antivirus, avoid suspicious downloads.


### <u>Trojan</u>

- Disguised as legitimate software.
- Provides attackers remote access.
- **Effects -** Data theft, spyware installation.
- **Spread -** Email attachments, fake apps.


### <u>Malware</u>

- Collective term for malicious software: virus, worm, Trojan, spyware, adware, ransomware.
- **Impact -** Crashes, theft, financial loss.
- **Defense -** Firewall, antivirus, safe browsing.


### <u>Ransomware</u>

- Encrypts victim’s data, demands payment.
- **Examples -** WannaCry, Petya.
- **Protection -** Backups, updates, awareness.

---
