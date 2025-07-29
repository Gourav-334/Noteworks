# $\fbox{Chapter 3: BLOCK CIPHER \& DATA ENCRYPTION STANDARD}$





## **Topic - 1: Stream Ciphers & Block Ciphers**  

### <u>Stream Cipher</u>

- Encrypts data one bit or byte at a time.
- **For example -** Autokeyed Vigenère, A5/1, RC4, Vernam cipher, etc.

#### Encryption Flow:

- Plaintext ($p_i$) $\oplus$ Key ($k_i$) $\rightarrow$ Ciphertext ($c_i$)
- Bit-stream generated from key.


### <u>Block Cipher</u>  

- Encrypts blocks of plaintext (e.g., **64** or **128-bits**).
- **For examples -** Feistel Cipher, DES, Triple DES, AES, etc.
- Treats each block as a unit for encryption/decryption.



## **Topic - 2: Block Cipher Principles – Feistel Structure**

### <u>Feistel Process</u>  

1. Split plaintext into halves: $L_i$ and $R_i$
2. $R_i$ → Function F → XOR with $L_i$  
3. Swap halves  


### <u>Design Parameters</u>  

- **Block size -** Common sizes are **64**, **128**, **256-bits**.
- **Key Size -** **128-bit** common; less than **64-bit** considered insecure  
- **Rounds -** Typically 16
- **Round Function F -** Includes substitution and permutation.
- **Subkey Generation -** Uses left circular shift plus permutation per round.



## **Topic - 3: Confusion and Diffusion**  

### <u>Confusion</u>  

- Hides relationship between ciphertext and key.
- Achieved via substitution.
- Small change in key results in large change in ciphertext.

### <u>Diffusion</u>  

- Spreads influence of one plaintext bit across ciphertext.
- Achieved via permutation and mixing operations.



## **Topic - 4: Data Encryption Standard (DES)**  

### <u>Basic Details</u>  

- **Type -** Block cipher
- **Block size -** 64 bits  
- **Key Size -** 64-bits (56-bits effective)  
- **Rounds -** 16


### <u>Encryption Flow</u>  

1. Initial Permutation (IP)
2. 16 Rounds of Feistel Network:
   - Expansion (32 → 48 bits)
   - XOR with round key $K_i$
   - S-box substitution (48 → 32 bits)
   - Permutation (P)
3. Swap $L$ and $R$
4. Final Permutation ($IP^{-1}$)



## **Topic - 5: DES Components**  

### <u>Initial and Final Permutation</u>  

- Reorders bits before first and after last round.
- Final permutation is the inverse of the initial.


### <u>f Function (Per Round)</u>

- **Inputs -** $R_{i-1}$, $K_i$

#### Steps:

1. Expansion E: $R_{i-1}$ (32 $\rightarrow$ 48 bits)  
2. XOR with $K_i$ (**48-bits**)
3. S-box Substitution: 8 S-boxes, **6-bit** input $\rightarrow$ **4-bit** output each  
4. Permutation P (**32-bits**)


### <u>Expansion Table (E)</u>  

- Increases diffusion by duplicating some bits.


### <u>S-Boxes</u>  

- Perform nonlinear substitution.
- Provides resistance to differential cryptanalysis.


### <u>Permutation (P)</u>  

- Rearranges output bits of S-boxes.
- Introduces diffusion.



## **Topic - 6: Avalanche Effect**  

- Small change in input (**1-bit**) causes large change in output (many bits).
- **<u>DES</u>:** Change in 1-bit causes approximately **29-bits** change in ciphertext.



## **Topic - 7: Strength of DES**  

- **56-bit** Key $\rightarrow$ $2^{56}$ combinations — brute-force still hard.
- **Algorithm Design -** Despite attempts, cryptanalysis has not broken DES.



## **Topic - 8: Design Principles of Block Ciphers**  

#### Confusion:

 - Substitution (S-boxes)
 - Hides key-ciphertext relationship

#### Diffusion:

 - Permutation plus mixing
 - Spreads plaintext influence across ciphertext

#### Kerckhoff's principle:

 - Algorithm should be secure even if public
 - Only key must be secret

#### Iterative structure (rounds):

 - Multiple transformation rounds enhance security
 - For example, AES uses $10$/$12$/$14$ rounds

#### Key expansion:

 - Generates unique subkeys per round  
 - Strong expansion improves cryptographic strength  
 
---
