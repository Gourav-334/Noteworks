# $\fbox{Chapter 6: ASYMMETRIC CIPHERS}$





## **Topic - 1: Prime Numbers**  

### <u>Definition</u>

- Integers $> 1$ with no divisors other than $1$ and themselves  
- Basis for public-key algorithms (e.g., RSA)  


### <u>Key property</u>

- Easy: multiply large primes  
- Hard: factor the product  
- Security relies on the integer factorization problem  



## **Topic - 2: Principles of Public-Key Cryptosystems**

### <u>Symmetric Key Encryption</u>  

- Single secret key $K$ shared by sender & receiver.
- For example, AES.
- Alice encrypts with $K$ $\rightarrow$ Bob decrypts with same $K$.


### <u>Asymmetric Key Encryption</u>  

- Each user has Public Key ($PU$) and Private Key ($PR$).

#### Two primary modes:

  1. Encryption with $PU$ $\rightarrow$ confidentiality
  2. Encryption with $PR$ $\rightarrow$ digital signature (authentication)


### <u>Mailbox Analogy</u>  

- Public key is something open mailbox (anyone can drop message).
- Private key is something only owner can open mailbox.


### <u>Combined Authentication & Confidentiality</u>  

#### Example compostion:
  $$ Z = E(PU_b,\; E(PR_a,\; X)) $$
  $$ X = D(PU_a,\; D(PR_b,\; Z)) $$


### <u>Applications</u>  

1. Encryption / Decryption
2. Digital Signatures
3. Key Exchange



## **Topic - 3: RSA Algorithm**  

### <u>General Steps</u>  

1. Generate keys ($PU$ and $PR$)
2. Encrypt with $PU$
3. Decrypt with $PR$


### <u>Key Generation</u>

- Choose large primes $p, q$  

#### Computation:

  $$ n = p \times q $$  $$ \varphi(n) = (p - 1)(q - 1) $$  
- Select $e$ such that $\gcd(e,\varphi(n)) = 1$
- Compute $d$ where $d \cdot e \equiv 1 \;(\bmod\; \varphi(n))$

#### Keys:

  - Public: $\{e, n\}$
  - Private: $\{d, n\}$


### <u>Encryption/ Decryption</u>  

#### Ciphertext:

$$ C = M^e \bmod n $$

#### Plaintext:

$$ M = C^d \bmod n $$


### <u>Examples</u>  

#### Example 1:

$p=3,\; q=11$ $\rightarrow$ $n=33,\; \varphi(n)=20$; $e=7,\; d=3$; encrypt $M=14$ $\rightarrow$ $C=20$ $\rightarrow$ decrypt $\rightarrow$ $M=14$  

#### Example 2:

$p=7,\; q=17$ $\rightarrow$ $n=119,\; \varphi(n)=96$; $e=5,\; d=77$; encrypt $M=10$ $\rightarrow$ $C=40$  

#### Example 3:

$p=17,\; q=11$ $\rightarrow$ $n=187,\; \varphi(n)=160$; $e=7,\; d=23$; encrypt $M=88$ $\rightarrow$ $C=11$  



## **Topic - 4: Diffie–Hellman Key Exchange**

### <u>Concept</u>  

- Two parties agree on shared secret over insecure channel.
- Security relies on discrete logarithm hardness.


### <u>Primitive Root</u>  

- For prime $p$, integer $a$ is a primitive root if powers $a^k \bmod p$ generate $1..p-1$
- For example, for $p=7$, a primitive root is $3$.


### <u>General Procedure</u>  

1. Public values: $q$ (prime), $\alpha$ (primitive root mod $q$)
2. User A: choose private $X_A < q$, compute $Y_A = \alpha^{X_A} \bmod q$
3. User B: choose private $X_B < q$, compute $Y_B = \alpha^{X_B} \bmod q$
4. Exchange $Y_A, Y_B$
5. Shared secret:
	- A computes $K = Y_B^{X_A} \bmod q$
	- B computes $K = Y_A^{X_B} \bmod q$


### <u>Examples</u>  

#### Example 1:

$q=23,\; \alpha=5$; $X_A=6 \Rightarrow Y_A=8$; $X_B=15 \Rightarrow Y_B=19$; shared $K=2$  

#### Example 2:

$q=19,\; \alpha=10$; $X_A=7 \Rightarrow Y_A=15$; $X_B=8 \Rightarrow Y_B=17$; shared $K=5$  



## **Topic - 5: Man-in-the-Middle Attack**  

### <u>Attack Steps</u>  

1. Alice sends $Y_A$ $\rightarrow$ attacker intercepts, replaces with $Y_{D1}$
2. Bob receives $Y_{D1}$, computes key with attacker’s value.
3. Bob sends $Y_B$ $\rightarrow$ attacker intercepts, replaces with $Y_{D2}$.
4. Alice computes key with $Y_{D2}$.
5. Result: Alice–attacker share one key, Bob–attacker share another; true Alice–Bob secret not established.


### <u>Mitigation</u>  

- Authenticate public values (digital signatures, certificates).
- Use authenticated key-exchange variants (e.g., authenticated Diffie–Hellman).

---
