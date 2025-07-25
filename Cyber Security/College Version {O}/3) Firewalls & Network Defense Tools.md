# $\fbox{Chapter 3: FIREWALLS \& NETWORK DEFENSE TOOLS}$





## **Topic - 1: Firewall Basics**

### <u>Introduction</u>

- **<u>Definition</u>:** A firewall is a security device placed between internal and external networks to regulate traffic.
- **<u>Purpose</u>:** Secure internal systems from external threats (mainly internet).
- **<u>Working Principle</u>:** Allows or blocks data packets based on pre-configured rule sets.


### <u>Example Scenario</u>

- **Setup -** LAN (e.g., campus network) $\leftrightarrow$ WAN (Internet)  

#### Firewall role:

- Evaluates source/destination IP, ports.
- Applies rule set to allow or deny traffic.


### <u>Traffic Filtering Methods</u>  

#### Allow-All-Except:

   - Permits all traffic unless explicitly restricted.
   - Depends on type of firewall, source/destination, ports.

#### Deny-All-Unless:

   - Blocks all traffic unless it meets specific criteria.
   - Operates at the network layer.



## **Topic - 2: Types Of Firewalls**

### <u>Packet Filtering Firewall</u>

 - Oldest type; inspects headers only (IP, port, protocol)  
 - Lightweight; no deep inspection  
 - Easy to bypass  


### <u>Circuit Level Gateway</u>

 - Verifies TCP handshake only  
 - Doesn’t inspect packet content  
 - Lightweight, but vulnerable  


### <u>Stateful Inspection Firewall</u>

 - Combines packet header check & TCP handshake validation
 - Stronger than previous types
 - Resource-intensive


### <u>Proxy Firewall (Application Layer Gateway)</u>

 - Intercepts traffic at application layer  
 - Performs deep inspection  
 - Adds anonymity; causes latency  


### <u>Application Level Firewall</u>

 - Filters traffic specific to services/applications  
 - For example, web application firewall  


### <u>Next Generation Firewall (NGFW)</u>

 - Includes DPI, TCP checks, IPS  
 - No fixed definition; capabilities vary  


### <u>Software Firewall</u>

 - Installed on endpoint devices  
 - Good for internal segmentation  
 - Difficult to manage at scale  


### <u>Hardware Firewall</u>

 - Dedicated appliance (acts like router)  
 - Handles perimeter security  
 - Performance varies by vendor  


### <u>Cloud Firewall (FaaS)</u>

 - Delivered via cloud infrastructure  
 - Easily scalable  
 - Often proxy-based  



## **Topic - 3: Firewall v/s Packet Filter**

### <u>Firewall</u>

- Acts as a proxy; filters based on protocol & services  
- No direct exposure between networks  


### <u>Packet Filter</u>

- Applies rule-set per packet  
- Usually configured on routers  
- Stateless unless combined with a firewall  



## **Topic - 4: Packet Filter Characteristics**

### <u>Common Filtering Parameters</u>

- **Protocol type -** IP, TCP, UDP, ICMP, IPsec
- Source & destination IP and Port
- ICMP Type
- TCP Flags (ACK, FIN, SYN)
- Network interface


### <u>Examples</u>

```sh
deny proto icmp type 8:0 from any to 192.168.1.0/24        # Block ping
allow proto tcp from any to 192.168.1.50:80                # Allow HTTP
deny proto all from any to 192.168.1.0/24                  # Block all
```



## **Topic - 5: Stateless v/s Stateful Filtering**

### <u>Stateless Firewall</u>

- No memory of previous packets.
- Easier to bypass (especially UDP).  
- Acts per-packet  


### <u>Stateful Firewall</u>

- Maintains session info.
- Smarter; allows dynamic decisions.
- Known as dynamic packet filtering.



## **Topic - 6: Network Address Translation (NAT)**

### <u>Introduction</u>

- **<u>Purpose</u>:** IP address conservation and translation.

#### Function:

- Maps private IP $\leftrightarrow$ Public IP
- Allows private networks to access internet.
- Common in routers/firewalls.


### <u>Reserved Private IP Ranges</u>

  - `10.0.0.0/8`
  - `172.16.0.0/12`
  - `192.168.0.0/16`



## **Topic - 7: Port Forwarding**

### <u>Introduction</u>

- **<u>Port forwarding</u>:** Redirects traffic from one `IP:port` combo to another using NAT.


### <u>Usage</u>

- Allows external users to access services inside LAN (e.g., SSH, FTP).
- Opens specific ports in firewall.



## **Topic - 8: TCP/IP Ports & Sockets**

- **<u>IP Address</u>:** Identifies host
- **<u>Port</u>:** Identifies service on the host

$$ \text{Socket = IP Address + Port} $$

- Used for establishing connections between devices.



## **Topic - 9: Virtual Private Network (VPN)**

### <u>Introduction</u>

- **Purpose -** Secure communication over public networks.


### <u>Benefits</u>

- Security
- Reduced cost (vs. leased lines)
- Remote access flexibility


### <u>Mechanisms</u>

  - Uses tunneling over insecure networks.
  - Point-to-point virtual connection


### <u>Types</u>

- Remote-Access VPN  
- Site-to-Site (intranet/extranet-based)



## **Topic - 10: Linux Firewalls (Netfilter + iptables)**

### <u>Introduction</u>

- **<u>Netfilter</u>:** Kernel-level packet filtering system.
- **<u>iptables</u>:** User-space tool to configure Netfilter.


### <u>iptables Tables</u>

| Table      | Use Case                      |
| ---------- | ----------------------------- |
| `filter`   | Basic packet filtering        |
| `nat`      | Address translation           |
| `mangle`   | Modify headers, DSCP, ToS     |
| `raw`      | Low-level configuration       |
| `security` | Works with SELinux, MAC rules |


### <u>iptables Chains</u>

- **INPUT -** Inbound to local system  
- **OUTPUT -** Outbound from local system  
- **FORWARD -** Passing through the system  



## **Topic - 11: Windows Firewall**

### <u>Introduction</u>

- Built-in host-based firewall (on by default).

#### Rules based on:

- IP addresses, protocols, services
- Port numbers, application names


### <u>Advanced Features</u>

- IPsec support  
- Dynamic profiles via **Network Location Awareness (NLA)**.
- Encryption, authentication for trusted devices.



## **Topic - 12: Firewall Rules**

### <u>Required Conditions</u>

- App/service name  
- Source/Destination IP  
- Protocol, port  
- Interface type  
- ICMP type/code  
- Dynamic references (DNS, DHCP, gateway)  



## **Topic - 13: Snort — Intrusion Prevention System (IPS)**

### <u>Introduction</u>

- **<u>Snort</u>:** Open-source IPS/IDS for real-time traffic analysis.


### <u>Capabilities</u>

- Logs packets
- Detects intrusions
- Protocol analysis
- Content matching
- Detects buffer overflows
- Detects OS fingerprinting
- Detects port scans


### <u>Modes</u>

- **Sniffer mode -** Displays packets  
- **Packet logger mode -** Logs to disk  
- **NIDS mode -** Detects intrusions using rule-set
 
---
