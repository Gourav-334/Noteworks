# $\fbox{Chapter 2: LINUX FUNDAMENTALS}$





## **Topic - 1: Linux Fundamentals Part I**

### <u>Usage Of Linux</u>

>**<u>NOTE</u>:**
>Ubuntu servers might take space as less as 512 MB.


### <u>Command Line</u>

#### Printing text:

- The `echo` command runs even without double inverted commas (`"`).

```sh
echo Gourav Mallick        # Output: Gourav Mallick
```

#### Getting username:

```sh
whoami
```


### <u>File System Navigation</u>

#### Expanding abbreviations:

- `ls` - Listing
- `cd` - Change directory
- `cat` - Concatenate
- `pwd` - Print working directory


### <u>Outputting Contents</u>

- We can output contents of a file using `cat`.
- It is handy as it doesn't require a code editor to view contents inside.

```sh
cat header.h
```


### <u>Finding Files</u>

- We can search for files using `find` command as follows.

```sh
find -name passwords.txt    # Particular file
find -name *.txt            # Particular extension
```


### <u>Using Grep</u>

- `grep` command allows us to search regarding contents of file.

#### Count words in file:

```sh
wc -l access.log
```

#### Grep:

- `grep` command shows us the content in which a pattern in contained.
- To understand this better, look at the example below.

```sh
grep "Hello" hello.c        # Output: printf("Hello, World!");
```

- This command looks for where the word `Hello` is in file `hello.c`.


### <u>Operators</u>

#### `&`:

- `&` is used for running commands in background.
- This is used in some tasks where a task might take too long.

```sh
cp largeFile.mp4 direc/largeFile.mp4 &
```

#### `>`:

- Used for redirecting output to a file.

```sh
echo "Hello" > smallFile.txt
```

- This command writes `Hello` to file `smallFile.txt`.
- If `smallFile.txt` already exists, it will be overwritten.

#### `>>`:

- Same as before, but the message is appended instead of being overwritten.
