# TCS IPA UNIX Cheat Sheet

> Focus: Basic UNIX/Linux commands, file system, permissions, shell, and process management.

---

# 1. What is UNIX?

UNIX is a multiuser, multitasking operating system.

Linux is UNIX-like.

Examples:
- Ubuntu
- Debian
- Red Hat
- CentOS

---

# 2. Directory Structure

```
/

├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── tmp
├── usr
└── var
```

Important

```
/home   → User files

/etc    → Configuration

/bin    → Basic commands

/usr    → User programs

/root   → Root user's home

/tmp    → Temporary files
```

---

# 3. Current Directory

Show current path

```bash
pwd
```

---

# 4. List Files

```bash
ls
```

Useful options

```bash
ls -l
```

Long listing

```bash
ls -a
```

Hidden files

```bash
ls -lh
```

Human-readable sizes

---

# 5. Change Directory

```bash
cd folder
```

Go home

```bash
cd
```

Go previous directory

```bash
cd ..
```

Go root

```bash
cd /
```

---

# 6. Create Directory

```bash
mkdir project
```

Nested

```bash
mkdir -p a/b/c
```

---

# 7. Remove Directory

```bash
rmdir folder
```

Delete recursively

```bash
rm -r folder
```

---

# 8. Create File

```bash
touch file.txt
```

---

# 9. Remove File

```bash
rm file.txt
```

Force delete

```bash
rm -f file.txt
```

---

# 10. Copy

File

```bash
cp a.txt b.txt
```

Directory

```bash
cp -r dir1 dir2
```

---

# 11. Move / Rename

```bash
mv old.txt new.txt
```

Move file

```bash
mv file.txt folder/
```

---

# 12. Display File

```bash
cat file.txt
```

Beginning

```bash
head file.txt
```

End

```bash
tail file.txt
```

---

# 13. Search

Find file

```bash
find . -name "*.txt"
```

Search text

```bash
grep hello file.txt
```

Ignore case

```bash
grep -i hello file.txt
```

---

# 14. Count

Lines

```bash
wc -l file.txt
```

Words

```bash
wc -w file.txt
```

Characters

```bash
wc -c file.txt
```

---

# 15. File Permissions

```
r = Read = 4
w = Write = 2
x = Execute = 1
```

Example

```
755

Owner
7 = rwx

Group
5 = r-x

Others
5 = r-x
```

Common

```
777
755
644
600
```

---

# 16. Change Permission

```bash
chmod 755 file
```

Symbolic

```bash
chmod +x file
```

---

# 17. Ownership

```bash
chown user file
```

Group

```bash
chgrp group file
```

---

# 18. Process Commands

Show running

```bash
ps
```

Detailed

```bash
ps -ef
```

Real-time

```bash
top
```

Kill

```bash
kill PID
```

Force

```bash
kill -9 PID
```

---

# 19. Disk Usage

Current folder

```bash
du
```

Human-readable

```bash
du -sh
```

Filesystem

```bash
df -h
```

---

# 20. Archive

Create

```bash
tar -cvf files.tar folder
```

Extract

```bash
tar -xvf files.tar
```

Compressed

```bash
tar -czvf archive.tar.gz folder
```

---

# 21. Compression

```bash
gzip file
```

Extract

```bash
gunzip file.gz
```

---

# 22. Redirection

Overwrite

```bash
>
```

Append

```bash
>>
```

Input

```bash
<
```

Pipe

```bash
|
```

Example

```bash
cat file | grep hello
```

---

# 23. Wildcards

```
*
Any characters
```

```
?
One character
```

Example

```bash
*.txt
```

---

# 24. Environment Variables

Display

```bash
echo $HOME
```

PATH

```bash
echo $PATH
```

Create

```bash
export VAR=value
```

---

# 25. Editors

```
vi

vim

nano
```

---

# 26. Networking

Hostname

```bash
hostname
```

IP

```bash
ip addr
```

Ping

```bash
ping google.com
```

---

# 27. Users

Current user

```bash
whoami
```

Logged users

```bash
who
```

---

# 28. Shell

Common shells

```
sh
bash
zsh
ksh
```

Current shell

```bash
echo $SHELL
```

---

# 29. File Types

```
-  Regular file
d  Directory
l  Symbolic link
c  Character device
b  Block device
```

Seen in

```bash
ls -l
```

---

# 30. Common MCQ Topics

✓ pwd
✓ ls
✓ cd
✓ mkdir
✓ rm
✓ cp
✓ mv
✓ cat
✓ head
✓ tail
✓ grep
✓ find
✓ chmod
✓ chown
✓ ps
✓ top
✓ kill
✓ df
✓ du
✓ tar
✓ gzip
✓ Pipes
✓ Redirection
✓ Wildcards
✓ Environment variables
✓ Shell
✓ File permissions

---

# Frequently Asked MCQs

**Which command shows the current directory?**

```
pwd
```

---

**Which command lists hidden files?**

```bash
ls -a
```

---

**Which command copies files?**

```bash
cp
```

---

**Which command moves or renames files?**

```bash
mv
```

---

**Which command changes permissions?**

```bash
chmod
```

---

**Which command searches text inside a file?**

```bash
grep
```

---

**Which command searches for files?**

```bash
find
```

---

**Which command shows running processes?**

```bash
ps
```

---

**Which command terminates a process?**

```bash
kill
```

---

**Permission 755 means**

```
Owner : rwx
Group : r-x
Others : r-x
```

---

**Permission 644 means**

```
Owner : rw-
Group : r--
Others : r--
```

---

# Last-Minute Revision

✓ pwd → current directory
✓ ls → list files
✓ cd → change directory
✓ mkdir → create directory
✓ touch → create file
✓ rm → delete file
✓ cp → copy
✓ mv → move/rename
✓ cat → display file
✓ grep → search text
✓ find → search files
✓ chmod → permissions
✓ chown → ownership
✓ ps/top → processes
✓ kill → terminate process
✓ df → disk space
✓ du → directory size
✓ tar → archive
✓ gzip → compress
✓ > overwrite output
✓ >> append output
✓ | pipe output
✓ * wildcard
✓ $HOME → home directory
✓ bash is the most common UNIX shell
