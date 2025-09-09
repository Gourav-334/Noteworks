# $\fbox{Chapter 5: INTRODUCTION TO CYBER CRIME INVESTIGATION}$  





## **Topic - 1: Firewalls and Packet Filters**

### <u>Introduction</u>

- **<u>Firewall</u>:** Security device monitoring inbound/outbound traffic per policy.
- Acts as barrier between private network & Internet.
- **Goal -** Allow safe traffic, block dangerous traffic, etc.


### <u>Types</u>

- Hardware firewall (router, appliance).
- Software firewall (installed program/host firewall).


### <u>Techniques Used</u>

- Packet-filtering
- Circuit-level gateways
- Cloud firewalls
- Unified Threat Management (UTM)



## **Topic - 2: Packet Filtering Firewall**

### <u>Introduction</u>

- Examines packets via rule sets (protocols, ports, addresses).


### <u>Filtering Criteria</u>

- **Source IP**
- **Destination IP**
- **Protocols** (TCP, UDP, ICMP)
- **Ports** (source/destination)
- **Flags** (TCP header)
- **Network interface**


### <u>Types</u>

1. Dynamic packet filtering  
2. Static packet filtering  
3. Stateless filtering  
4. Stateful filtering  



## **Topic - 3: Password Cracking**

### <u>Introduction</u>

- Process of recovering or stealing passwords from hashes or scrambled forms.
- **Uses -** User recovery, unauthorized access, admin audit, etc.


### <u>Methods</u>

- Brute-force (all combinations)
- Dictionary attack (common words)
- Rainbow tables (precomputed hashes)
- Phishing (trick user)
- Malware-based (stealing from apps)


### <u>Tools Used</u>

- John The Ripper
- Hashcat
- Hydra
- Medusa



## **Topic - 4: Keyloggers**

### <u>Introduction</u>

- Log every keystroke (passwords, credit cards, sites).


### <u>Types</u>

- Software (installed via Trojans/viruses).
- Hardware (physical device on keyboard/PC).


### <u>Popular Tools (2020)</u>

- Kidlogger
- Best Free Keylogger
- Refog Monitor
- All-in-One Keylogger


### <u>Countermeasures</u>

- Anti-keylogger tools.
- Avoid public PCs for sensitive logins.
- Use on-screen keyboard.
- Updated antivirus (limited effectiveness).



## **Topic - 5: Spyware**

### <u>Introduction</u>

- Malware collecting user info secretly.
- Installed via infected apps, sites, attachments, etc.
- Can be avoided with anti-spyware software.


### <u>Steps</u>

1. Infiltrate
2. Monitor & capture (credentials, logins)
3. Send/sell data



## **Topic - 6: Viruses and Worms**

### <u>Introduction</u>

- **<u>Virus</u>:** Attaches to host files, replicates via execution, etc.
- **<u>Worm</u>:** Self-replicating, spreads via networks, no host needed, etc.


### <u>Virus Types</u>

- Stealth
- Polymorphic
- Metamorphic
- Encrypted


### <u>Worm Types</u>

- Email
- IM
- File-sharing



## **Topic - 7: Trojan Horse**

- Malicious code disguised in harmless software.
- Does not self-replicate.
- Creates backdoors for spying, file access, remote control, etc.



## **Topic - 8: Backdoor**

- Hidden entry point bypassing security.
- Added by developers for maintenance/debugging.
- Exploitable if not removed.



## **Topic - 9: Steganography**

### <u>Introduction</u>

- Hides existence of message/data in cover media.


### <u>Types</u>

- Text
- Image
- Audio
- Video
- Network


### <u>Tools</u>

- Stegosuite
- Steghide
- Xiao
- OpenPuff
- SSuite Picsel



## **Topic - 10: DoS & DDoS Attacks**  

### <u>Introduction</u>

- **<u>DoS</u>:** Flood victim server/network to deny service.
- **<u>DDoS</u>:** Coordinated DoS via many compromised systems (zombies/botnets).


### <u>Types</u>

- Volume-based (traffic floods).
- Protocol attacks (Smurf, ICMP abuse).
- Application-layer (Slowloris).


### <u>Impacts</u>

- Revenue loss
- Reputation damage
- Cost increase


### <u>Methods</u>

- **Reflector** (DNS reflection)
- **Amplification** (UDP frag)
- **HTTP floods**



## **Topic - 11: SQL Injection**  

### <u>Introduction</u>

- Exploits poor input validation in database layer.
- Attacker injects SQL via forms/inputs.


### <u>Types</u>

- **In-band** (direct response).
- **Out-of-band** (other server).
- **Blind SQLi** (inferential).



## **Topic - 12: Buffer Overflow**  

- Data exceeds buffer capacity & thus overwrites adjacent memory.
- Results in crashes, execution hijacking, etc.
- Major threat to integrity and reliability.



## **Topic - 13: Attacks on Wireless Networks**  

### <u>Introduction</u>

- Breaks standard AP-client communication.


### <u>Forms</u>

- **DoS attacks** (garbage data floods)
- **Man-in-the-middle** (interception, modification)
- **Wardriving** (mapping WAPs from vehicles)
- **Spoofing, sniffing, encryption cracking**


### <u>Protections</u>

- Firewalls
- Avoid risky Wi-Fi hotspots
- Disable wireless when unused
- Prefer HTTPS/SSL
- Avoid “evil twin” access points
- Strong encryption (WPA2/3)
- Stay vigilant in public networks

---
