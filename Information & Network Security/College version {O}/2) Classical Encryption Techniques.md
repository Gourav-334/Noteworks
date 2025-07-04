# $\fbox{Chapter 2: CLASSICAL ENCRYPTION TECHNIQUES}$





## **Topic - 1: Symmetric Cipher Model (SCM)**

- SCM uses a secret key that is common to both sender & receiver.
- If a strong algorithm is used with a key, it would be difficult for someone to sniff.
- We assume that cipher, algorithm & key is known.


## **Topic - 2: Cryptanalysis & Brute Force Attack**

### <u>Brute Force Attack</u>

- In **brute force attack**, primary objective of attacker is to get key.
- And secondary objective is to directly get message.
- They brute force on ciphertext with various keys until an intelligible message is derived.


### <u>Cryptanalyst Attack</u>

- In **cryptanalyst attack**, the cryptanalysts suggests how to hack traffic & modify texts.
- It can happen at different levels, including when cryptanalysts have knowledge about both ciphertext & key.


### <u>Substitution Technique</u>

- In **substitution technique**, each letter in plaintext is replaced with other characters/ numbers/ symbols.

#### Types:

- Caesar cipher
- Monoalphabetic cipher
- Playfair cipher
- Hill cipher
- Polyalphabetic cipher
- One-time pad



## **Topic - 3: Caesar Cipher**

### <u>Algorithms</u>

#### Encryption:

$$ C\;=\;E(3,P)\;=\;(P+3)\;mod\;26$$

#### Decryption:

$$ P\;=\;D(3,C)\;=\;(C-3)\;mod\;26 $$


### <u>Working</u>

- Alphabets are assigned indexes, starting from $0$ to $25$.
- Basically, alphabets are switched with other alphabets as per the key.
- For negative numbers, subtract the result from $26$.
- During brute force attack on Caesar ciphers, cryptanalyst needs to try just 26 possible keys ($[0,25]$).
