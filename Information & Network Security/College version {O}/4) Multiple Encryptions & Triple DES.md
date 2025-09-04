# $\fbox{Chapter 4: MULTIPLE ENCRYPTIONS \& TRIPLE DES}$





## **Topic - 1: Multiple Encryption**

### <u>Introduction</u>

- DES vulnerable to brute-force (needs $2^{56} \approx 72$ quadrillion operations).


### <u>Alternatives</u>

- New algorithms (AES)
- Multiple encryptions with DES with multiple keys.
- Preserves legacy systems while improving security.



## **Topic - 2: Double DES**

### <u>Introduction</u>

#### Encryption:

$$ C = E(K_2, E(K_1, P)) $$

#### Decryption:

$$ P = D(K_1, D(K_2, C)) $$


### <u>Meet-In-The-Middle Attack</u>

- Attacker knows $(P, C)$ pair.

#### Steps:

1. For all $2^{56}$ $K_1$ $\rightarrow$ Compute $E(K_1, P)$ $\rightarrow$ Store in table
2. For all $2^{56}$ $K_2$ $\rightarrow$ Compute $D(K_2, C)$ $\rightarrow$ Compare with table
3. Matches are candidate keys.

>**<u>NOTE</u>:**
>Complexity $\approx 2^{57}$ (not $2^{112}$)  



## **Topic - 3: Triple DES (3DES)**

### <u>Introduction</u>

- Strengthens DES by 3 rounds of encryption.


### <u>Forms</u>

#### Two-Key 3DES:

$$ C = E(K_1, D(K_2, E(K_1, P))) $$

- Effective key is of 112-bit.

#### Three-Key 3DES:

$$ C = E(K_3, D(K_2, E(K_1, P))) $$

- Effective key is of 168-bits.
- More secure, widely used in finance (but AES replacing it).



## **Topic - 4: Block Cipher Modes of Operation**

### <u>Electronic Code Book (ECB)</u>

- **Formula -** $C_j = E(K, P_j)$
- **Pros -** Simple, parallelizable, tolerant to lost blocks.
- **Cons -** Identical plaintext $\rightarrow$ Identical ciphertext (pattern leakage)
- **Use -** Secure short data (keys, randoms)


### <u>Cipher Block Chaining (CBC)</u>

- **Input -** $P_j \oplus C_{j-1}$, first block uses IV
- **Pros -** Different ciphertext even for identical plaintext
- **Cons -** Sequential (no parallelization in encryption)
- **Use -** General-purpose encryption, authentication


### <u>Cipher Feedback (CFB)</u>

- Block cipher $\rightarrow$ Stream cipher
- **Input -** Shift register with IV.
- Output bits XORed with plaintext.
- **Pros -** Avoids padding & stream-like.
- **Use -** Data streams


### <u>Output Feedback (OFB)</u>

- Feedback from encryption output (not XOR).
- Keystream can be precomputed.
- **Pros -** No error propagation.
- **Use -** Real-time communications & error-sensitive systems.


### <u>Counter Mode (CTR)</u>

- Uses counter instead of feedback.
- **Formula -** $C_j = P_j \oplus E(K, \text{Counter}+j)$
- **Pros -** Parallelizable, fast, random access, etc.
- **Use -** Network security (IPSec, ATM)



## **Topic - 5: Comparison of Modes**

| Mode |  Type  | Description                       | Use                     |
| :--: | :----: | --------------------------------- | ----------------------- |
| ECB  | Block  | Independent block encryption      | Small data              |
| CBC  | Block  | XOR with previous ciphertext      | General purpose         |
| CFB  | Stream | XOR with part of prev. ciphertext | Streams                 |
| OFB  | Stream | Feedback from encryption output   | Error-sensitive systems |
| CTR  | Stream | Counter-based keystream           | High-speed, parallel    |

---
