# $\fbox{Chapter 1: CYBER SECURITY BASICS}$





## **Topic - 1: Offensive Security Intro**

### <u>Introduction</u>

- Hacking into systems to understand hacker mind.


### <u>Hacking First Machine</u>

- **<u>Gobuster</u>:** CLI application used for finding hidden pages in websites (if any).

```sh
gobuster -u "http://fakebank.thm" -w wordlist.txt dir
```

- `-u` tells what website we're scanning.
- `-w` takes a list of words to find in website.

<img src="./media/image1.png"
style="width:5in;height:4in" />

- Status `200` means, that name in list was found on website.
- We found a page called `/bank-transfer`.
- This can be accessed by just appending `/bank-transfer` to end of URL.

>**<u>NOTE</u>:**
>1. Consistency is the key.
>2. Daily practice at TryHackMe.


### <u>Careers In Cyber Security</u>

- **Penetration tester**
- **<u>Red teamer</u>:** Tries attacking an organization & gives feedback from enemy's perspective.
- **Security engineer**
- **Malware analyst**
