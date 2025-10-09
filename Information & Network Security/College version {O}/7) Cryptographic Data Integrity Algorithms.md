# $\fbox{Chapter 7: CRYPTOGRAPHIC DATA INTEGRITY ALGORITHMS}$





## **Topic - 1: Hash Functions**

### <u>Definition</u>

- Function $H(M)$ maps variable-length message fixed-length hash $h$.


### <u>Property</u>

- Small change in $M \rightarrow$ large change in $h$ (avalanche effect).


### <u>Applications</u>

1. Message authentication
2. Digital signatures
3. One-way password storage



## **Topic - 2: Security Requirements for Hash Functions**

- **Disclosure -**  Prevent release of message contents.
- **Traffic analysis -** Prevent pattern inference.
- **Masquerade -** Prevent fake sources inserting messages.
- **Content modification -** Detect tampering.
- **Sequence modification -** Prevent reordering.
- **Timing modification -** Prevent delay / replay.
- **Source repudiation -** Stop sender denial.
- **Destination repudiation -** Stop receiver denial.



## **Topic - 3: Hash Functions via Cipher Block Chaining (CBC)**

### <u>Introduction</u>

- Uses block cipher in CBC mode.


### <u>CBC-MAC Process</u>

1. Split message into blocks.
2. XOR each block with previous ciphertext.
3. Encrypt with symmetric cipher.
4. Final block $\rightarrow$ MAC.


### <u>Properties</u>

- **Advantages -** Simple, efficient for fixed-length.
- **Limitations -** Insecure for variable-length without fixes, requires key management.



## **Topic - 4: Secure Hash Algorithm (SHA)**

### <u>Requirements</u>

1. Input arbitrary length
2. Output fixed-length digest
3. Easy to compute $H(M)$
4. One-way property $\rightarrow$ infeasible to invert
5. Weak collision resistance $\rightarrow$ hard to find $y \neq x$ with $H(y)=H(x)$
6. Strong collision resistance $\rightarrow$ hard to find $m_1 \neq m_2$ with $H(m_1)=H(m_2)$


### <u>Variants</u>

| SHA Variant | Digest Size | Message Size | Block Size | Word Size | Steps |
|-------------|-------------|--------------|------------|-----------|-------|
| SHA-1       | 160         | < $2^{64}$   | 512        | 32        | 80    |
| SHA-224     | 224         | < $2^{64}$   | 512        | 32        | 64    |
| SHA-256     | 256         | < $2^{64}$   | 512        | 32        | 64    |
| SHA-384     | 384         | < $2^{128}$  | 1024       | 64        | 80    |
| SHA-512     | 512         | < $2^{128}$  | 1024       | 64        | 80    |


### <u>SHA-512 Steps</u>

1. Append padding bits
2. Append 128-bit length field
3. Initialize hash buffer (512-bit)
4. Process message in 1024-bit blocks over 80 rounds
5. Final digest = 512 bits



## **Topic - 5: Message Authentication Codes (MAC)**

### <u>Definition</u>

- Provides authenticity & integrity.


### <u>Requirements</u>

- Same as hash security goals (disclosure, masquerade, etc.)


### <u>Functions</u>

- Encrypt full message + hash → confidentiality + integrity
- Encrypt only hash → lighter
- Use hash + secret value $S$ → no encryption, integrity only



## **Topic - 6: Security of MACs**

### <u>Goals</u>

- Unforgeability (attacker cannot generate valid MAC).
- Integrity (detect modifications).


### <u>Attack types</u>

- Existential forgery
- Selective forgery
- Replay attacks
- Length-extension attacks


### <u>Constructions</u>

- **CBC-MAC -** Secure for fixed-length
- **HMAC (SHA-based) -** Secure, resists extension
- **CMAC (AES-based)**
- **Poly1305** (fast, with ChaCha20)


### <u>Best Practices</u>

- Use secure primitives (e.g., HMAC-SHA256).
- Don’t reuse keys.
- Use nonces / timestamps to prevent replay.
- Prefer authenticate-then-encrypt or AEAD (e.g., AES-GCM).



## **Topic - 7: HMAC**

### <u>Motives</u>

- Use existing hash functions (MD5, SHA, etc.)
- Allow replacing underlying hash.
- Retain performance, simplicity, and strong analysis.


### <u>Steps</u>

1. Pad key $K \rightarrow b$ bits
2. XOR with ipad $\rightarrow$ $S_i$
3. Append message $M \rightarrow$ compute $H(S_i||M)$
4. XOR $K$ with opad $\rightarrow$ $S_o$
5. Append previous hash $\rightarrow$ compute final HMAC



## **Topic - 8: Digital Signatures**  


### <u>Definition</u>

- Authenticates message origin & integrity using asymmetric keys.
- **Process -** $Hash(M)$ $\rightarrow$ encrypt with private key $\rightarrow$ signature.
- Verified with public key.
- Provides non-repudiation (unlike MACs).


### <u>Attacks</u>

- Key-only attack
- Known-message attack
- Chosen-message (generic, directed, adaptive)


### <u>Forgeries</u>

- Total break
- Universal
- Selective
- Existential


### <u>Requirements</u>

- Signature depends on message & sender’s unique info.
- Easy to produce & verify.
- Infeasible to forge.
- Practical to store.



## **Topic - 9: Digital Signature Standard (DSS)**

### <u>Introduction</u>

- NIST standard using SHA.
- Signature only (not encryption / key exchange).


### <u>Approaches</u>

- **RSA -** Encrypt hash with private key, verify with public key.
- **DSA -** Signature = $(r,s)$ using per-message random $K$.
- **ElGamal -** Modular arithmetic with inverses.
- **Schnorr -** Efficient, based on discrete logs.

---
