# $\fbox{Chapter 2: CLASSICAL ENCRYPTION TECHNIQUES}$





## **Topic - 1: Symmetric Cipher Model**

- **<u>Plaintext</u>**: Original message (intelligible input to encryption)
- **<u>Ciphertext</u>**: Encrypted message (scrambled, unintelligible)
- **<u>Encryption</u>**: Plaintext $\rightarrow$ Ciphertext
- **<u>Decryption</u>**: Ciphertext $\rightarrow$ Plaintext
- **<u>Key</u>**: Secret input independent of both plaintext & algorithm
- **<u>Algorithm</u>**: Applies substitutions & transformations, are reversible (encryption $\leftrightarrow$ decryption).
- **Assumption -** Cipher is known & key is distributed over secured channel.



## **Topic - 2: Cryptanalysis**

### <u>Introduction</u>

- Study of breaking encryption without key.
- **Objective** - Recover plaintext, key, or both.


### <u>Main Methods</u>

  - **<u>Cryptanalysis</u>**: Exploit algorithm weaknesses
  - **<u>Brute force</u>**: Try all key combinations



## **Topic - 3: Cryptanalysis Attacks**

|       Type        | Known to Attacker                                         |
| :---------------: | --------------------------------------------------------- |
|  Ciphertext Only  | Ciphertext, encryption algorithm                          |
|  Known Plaintext  | Ciphertext, encryption algorithm, one or more (P,C) pairs |
| Chosen Plaintext  | Encryption algorithm, ciphertexts for chosen plaintexts   |
| Chosen Ciphertext | Ciphertexts + their decryptions                           |
|    Chosen Text    | Both chosen plaintext & ciphertext with their mappings    |



## **Topic - 4: Substitution Techniques**

### <u>Introduction</u>

- **<u>Substitution techniques</u>:** Replaces symbols with other symbols or patterns.


### <u>Caesar Cipher</u>

- Formula is as shown below.

#### Encryption:

$$ C\;=\;(P\;+\;K)\;mod\;26 $$

#### Decryption:

$$ P\;=\;(C\;-\;K)\;mod\;26 $$

- **<u>Key</u>**: Shift $K$ positions
- For example, refer to plaintext & cipher below.

$$ \text{Plaintext}\;\rightarrow\;\text{THE QUICK BROWN FOX} $$
$$ \text{Key}\;\rightarrow\;3 $$
$$ \text{Ciphertext}\;\rightarrow\;\text{WKH TXLFN EURZQ IRA} $$

- **Brute Force -** Only 25 keys → Easily breakable


### <u>Monoalphabetic Cipher</u>

- Uses random permutation of alphabets.
- Total keys are $26!$, meaning brute force is infeasible.
- **Attack -** Frequency analysis (letters, diagrams)


### <u>Playfair Cipher</u>

- $5 \times 5$ matrix using key ($I$ & $J$ combined)
- Operates on letter pairs (diagrams).

#### Rules:

- Same row $\rightarrow$ Right letters
- Same column $\rightarrow$ Below letters
- Rectangle $\rightarrow$ Swap corners

#### Example:

$$ Key\;\rightarrow\;\text{OCCURRENCE} $$
$$ Plaintext\;\rightarrow\;\text{TALL TREES} $$
$$ Converted\;\rightarrow\;\text{TA LX LT RE ES} $$
$$ Cipher\;\rightarrow\;\text{PF IZ TZ EO RT} $$


## **Topic - 5: Hill Cipher**

### <u>Introduction</u>

- Based on matrix multiplication in modular arithmetic.


### <u>Formulae</u>

#### Encryption:

$$ C\;=\;P\;\times\;K\;mod\;26 $$

#### Decryption:

$$ P\;=\;C\;\times\;K^{-1}\;mod\;26 $$

- Key Matrix must be invertible ($mod\;26$).


### <u>Steps</u>

  1. Convert text to numbers ($A=0$, ..., $Z=25$).
  2. Use key matrix $K$.
  3. Multiply $P\;\times\;K$, reduce $mod\;26$.


### <u>Inverse Matrix</u>

#### $2\times2$:

$$ K^{-1}\;=\;(\frac{1}{det})\;\times\;[\;\matrix{d&-b\\c&a}\;]\;mod\;26 $$

#### $3\times3$

$$ K^{-1}\;=\;adj(K)\;\times\;det^{-1}\;mod\;26 $$


### <u>Modulo Inverse Example</u>

$$ (3\;\times\;9)\;mod\;26\;=\;1 $$
$$ \fbox{9 is mod inverse of 3} $$



## **Topic - 6: Polyalphabetic Ciphers**

### <u>Introduction</u>

- Uses multiple cipher alphabets to reduce frequency correlation.


### <u>Vigenère Cipher</u>

$$ C_{i}\;=\;(P_{i}\;+\;K_{i})\;mod\;26 $$

- Key repeats if shorter than plaintext.


### <u>Example</u>

$$ Plain\;\rightarrow\;\text{HELLO} $$
$$ Key\;\rightarrow\;\text{GMGMG} $$
$$ Cipher\;\rightarrow\;\text{NQRXU} $$

- Repeated patterns help in attacking.


### <u>Vernam Cipher</u>

- Also known as **stream cipher**.

$$ C_{i}\;=\;P_{i}\;XOR\;K_{i} $$

- Bitwise XOR
- Used in OTP (One Time Pad).



## **Topic - 7: OTP (One-Time Pad)**

### <u>Introduction</u>

- Key is truly random, same length as plaintext.
- Unbreakable due to no frequency correlation.


### <u>Limitations</u>

  - Difficult key generation & distribution.


### <u>Example</u>

  - Same ciphertext may yield multiple plausible plaintexts.



## **Topic - 8: Transposition Techniques**

### <u>Introduction</u>

- Rearranges symbols i.e. no substitution.


### <u>Rail Fence</u>

- Write in diagonal rails, read row-wise.


### <u>Example</u>

```
M . . . E . . . E . . . T
. E . M . T . A . T . E .
. . A . . K . . . E . . .
```

$$ Cipher\;\rightarrow\;\text{MEMATEAKETETHPR} $$


### <u>Row/Column Transposition</u>

- Write in matrix & read columns in order of key.

$$ Key\;\rightarrow\;4\;3\;1\;2\;5\;6\;7 $$
$$ Plain: $$
$$ \text{ATTACKP} $$
$$ \text{POSTPONE} $$
$$ \text{DUNTILT} $$
$$ \text{WOAMXYZ} $$
$$ Cipher\;\rightarrow\;\text{TTNA APTM TSUO AODW COIX KNLYPETZ} $$

- It is stronger as it applies transposition in multiple stages.



## **Topic - 9: Steganography**

### <u>Introduction</u>

- Hides data inside cover media (image/audio/video).
- Goal is to make message invisible, not unreadable.
- We use **Least Significant Bit (LSB) alteration** method.


### <u>Example</u>

$$ \text{Hide "Hi"}\;\rightarrow\;H=01001000,\;i=01101001 $$

- Change LSBs of 16 pixels accordingly


### <u>Tools</u>

- Online LSB tools
- **Python -** Stegano, Pillow

---
