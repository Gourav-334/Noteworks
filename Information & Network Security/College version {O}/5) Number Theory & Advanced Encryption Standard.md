# $\fbox{Chapter 5: NUMBER THEORY \& ADVANCED ENCRYPTION STANDARD}$ 





## **Topic - 1: Euclidean Algorithm**  

### <u>Introduction</u>

- Computes GCD (Greatest Common Divisor) of two integers.


### <u>Steps</u>

1. Let $a > b$
2. Divide $a$ by $b$, remainder = $r$
3. Replace $a = b$, $b = r$
4. Repeat until $r = 0$
5. Last non-zero remainder means its a GCD.


### <u>Example</u>

$$ 56\;=\;15\times3\;+\;11 $$
$$ 15\;=\;11\times1\;+\;4 $$
$$ 11\;=\;4\times2\;+\;3 $$
$$ 4\;=\;3\times1\;+\;1 $$
$$ 3\;=\;1\times3\;+\;0 $$
$$ =>\;GCD\;=\;1 $$



## **Topic - 2: Modular Arithmetic**  

### <u>Introduction</u>

- Arithmetic under modulo $n$.


### <u>Operations</u>

- Addition: $(a + b) \bmod n$  
- Subtraction: $(a - b) \bmod n$  
- Multiplication: $(a \times b) \bmod n$  
- Exponentiation: $(a ^ b) \bmod n$  


### <u>Properties</u>

- Congruences  
- Inverses  
- Residue Classes  


### <u>Examples</u>

$$ 7 \bmod 5 = 2 $$
$$ 18 \bmod 7 = 4 $$


### <u>Applications</u>

- RSA (public-key cryptography)
- Diffie–Hellman (key exchange)
- Hashing, Random number generation
- **Fermat’s theorem**, **Chinese Remainder Theorem**



## **Topic - 3: Finite Fields GF(p)**  

### <u>Introduction</u>

- Also called **Galois Fields**.
- **<u>GF(p)</u>:** finite field with prime $p$ elements $\{0,1,2,…,p−1\}$.
- **Operations -** Addition & multiplication mod $p$.


### <u>Examples</u>

$$ GF(2)\;=\;\{0,1\}  $$
$$ GF(5)\;=\;\{0,1,2,3,4\} $$



## **Topic - 4: Polynomial Arithmetic**  

### <u>Introduction</u>

- Operations on polynomials can be to **add**, **subtract**, **multiply** & **divide**.
- **<u>Degree</u>:** Highest power of variable.


### <u>Finite Fields</u>

- Operate under $GF(p)$.
- Use **irreducible polynomials** (cannot be factored further).


### <u>Applications</u>

- Error-correcting codes (Reed-Solomon).
- AES (encryption transformations).
- Elliptic curve cryptography (ECC).



## **Topic - 5: Advanced Encryption Standard (AES)**  

### <u>Introduction</u>

- Rijndael algorithm, symmetric block cipher, etc.
- Block size is of 128-bits & key size of 128-bits, 192-bits or 256-bits.
- **Rounds -** 10 (128-bit key), 12 (192-bit key), 14 (256-bit key)  


### <u>AES Process</u>

1. `AddRoundKey` (initial XOR with key)  
2. `SubBytes` (S-box substitution)  
3. `ShiftRows` (row-wise permutation)  
4. `MixColumns` (column transformation)  
5. `AddRoundKey` (XOR with round key)  

>**<u>NOTE</u>:**
>Final round omits `MixColumns`.


### <u>Example Transformations</u>

- **`SubBytes`:** Nonlinear byte substitution via **S-box**.
- **`ShiftRows`:** Cyclic left shifts
	- Row 0 = no shift  
	- Row 1 = 1-byte shift  
	- Row 2 = 2-byte shift  
	- Row 3 = 3-byte shift  
- **`MixColumns`:** Multiply each column with fixed polynomial matrix in $GF(2^8)$.
- **`AddRoundKey`:** XOR state with round key.



## **Topic - 6: AES Key Expansion**  

### <u>Introduction</u>

- Input key expanded into multiple round keys.
- For **128-bit** key → **44 words** (**176 bytes**).
- Each new word depends on previous ones.


### <u>Uses</u>

- `RotWord`
- `SubWord`
- `Rcon` (round constants)


### <u>Rcon Table</u>

```
1, 2, 4, 8, 16, 32, 64, 128, 27, 54 ...
```


### <u>Structure</u>

- Round 0 $\rightarrow$ W0...W3
- Round 1 $\rightarrow$ W4...W7
- Round N $\rightarrow$ W40...W43

---
