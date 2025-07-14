# $\fbox{UBUNTU}$





## **Topic - 1: Maintenance**

### <u>Upgrading Package Manager</u>

- Once or twice a week, make sure your packages are up to date.

```sh
sudo apt update && sudo apt upgrade
```


### <u>Clean Unrequired Packages</u>

```sh
sudo apt autoremove && sudo apt autoclean
```



## **Topic - 2: Shell Fundamentals**

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


### <u>Error Code</u>

- If a command doesn't run, we can use `$?` to know what went wrong.

```sh
# Say a file doesn't exist.
ls sample.txt
echo $?

# Output: 2
```

#### Scripting example:

```sh
cp source.txt backup.txt

if [ $? -eq 0 ]; then
	echo "Copy successful"
else
	echo "Copy failed"
fi

```



## **Topic - 3: Special Operators**

### <u>Execute Arguments</u>

- `xargs` is used to convert `stdin` of previous command(s) into arguments.
- It uses a pipe (`|`) which is used for passing output of one command as input of next.

#### Example 1:

- We can find some files with particular extension & then remove them.

```sh
find . -name "*.txt" | xargs rm
```

#### Example 2:

- Or we can split string into arguments from whitespace.

```sh
echo "file1 file2" | xargs -n 1 echo
```

- `-n 1 echo` means run `echo` on each argument of previous command for once (`1`).
- `-n` - For each
- `1` - Once
- `echo` - Output

#### Example 3:

- Let's say a file `names.txt` contains:

```txt
Alice
Bob
Charlie
```

- Each of these name separated by newline (`\n`) is treated as separate argument, as whitespace was previously.
- Same goes with tabs (`\t`).
- We can greet each of the name by the following command.

```sh
cat names.txt | xargs -I{} echo "Hello {}"
```

- `-I{}` is used for containing input from previous command, fit at `{}`.


### <u>Cut</u>

- `cut` command is used for extracting specific columns or characters.
- `-d` is used to define the separation **delimiter** & `-f` for **field**/column number.
- `-c` is used for extracting **character** from a position.

#### Extracting fields:

- Fields can be extracted from files which are delimiter-separated.
- Let's say we have a file `file.csv` as follows.

```sh
Name,Age,City
Alice,30,Berlin
Bob,25,Paris
```

- We want to extract 2nd & 3rd column from this file.
- So, we would write the command as follows.

```sh
# cut -d{DELIMITER} -f{FIELD_NUMS} {FILENAME}
cut -d',' -f2,3 file.csv
```

- Means print 2nd & 3rd column (`-f`) from `file.csv` where cells are separated by `,`.

>**<u>NOTE</u>:**
>Indexing for arguments to `-f` & `-c` start from `1`.

#### Extracting characters:

- We can also extract characters by defining range.
- Let's say we have a file `filename.txt`.

```sh
Gourav
System
Linux
```

- We are extracting 1st to 5th character from each line.

```sh
cut -c1-5 filename.txt

# Goura
# Syste
# Linux
```

#### Example (level-up):

- Let's say we want to extract `2025` from `Gourav 2025 Final`.
- The command for that would be as follows.

```sh
echo "Gourav 2025 Final" | cut -d' ' -f2
```


### <u>Action Scanner & Text Processor</u>

- `awk` is used for matching a pattern & taking action as per that.

```sh
awk 'pattern { action }' filename
```

#### Printing:

```sh
# Printing 1st column from each line (whitespace separated).
awk '{ print $1 }' file.txt

# Printing 1st & 3rd column from each line with ',' as delimiter.
awk -F',' '{ print $1, $3 }' data.csv
```

- Notice that the flag used for delimiter here is `-F`.

#### Filter by condition:

```sh
# Print column 2nd & 3rd where column 1st > 100.
awk '$1 > 100 { print $2, $3 }' file.txt

# Printing whole line if equal in value.
awk '$2 == "Gourav"' names.txt
```

#### Aggregate values:

```sh
# Add all 2nd column values & print it.
awk '{ sum += $2 } END { print sum }' salaries.txt

# Average of 2nd column
awk '{ sum += $2; count++ } END { print sum/count }' salaries.txt
```

- `sum` & `count` are user defined variables, not reserved ones.

#### Pattern matching:

```sh
awk '/error/' logfile.json
```

- This code prints all the lines that contain string `"error"`.


### <u>Stream Editor</u>

- `sed` is used for editing, filtering or transforming text in one line.
- We can do so by either patterns or line numbers.

```sh
# Syntax
sed 's/pattern/replacement/flags' file
```

#### Text substitution:

- `s` means substitution.

```sh
# Replacing 1st occurrence of 'foo' with 'bar'.
sed 's/foo/bar/' file.txt

# Replacing all occurrence of 'foo' with 'bar'.
sed 's/foo/bar/g' file.txt
```

- Flag `g` stands for **global**.

#### Deletion of lines:

```sh
# Delete lines that contain 'debug'
sed '/debug/d' file.txt

# Deletes empty lines
sed '/^$/d' file.txt
```

- `^` means start & `$` alone means end.
- So `^$` means character index where start & end are same.

#### Printing lines in range:

```sh
# Prints from line 5 to 10.
sed -n '5,10p' file.txt
```

- `-n` means the output is modified & not default.
- And for manual usage, `p` is used.

#### Replace on specific lines:

```sh
# On single line (2nd line), only for first occurrence.
sed '2s/foo/bar/'

# On multiple lines, for all occurrences.
sed '1,3s/foo/bar/g'
```

#### Delete specific lines:

```sh
# Single line
sed '3d' file.txt

# Multiple line
sed '5,7d' file.txt
```

#### Inline edit with backup:

```sh
sed -i.bak 's/foo/bar/g' file.txt
```

- Changes are made on `file.txt` & backup is stored as `file.txt.bak`.
- `-i` (inline) means that only changes are made to file, nothing is printed on `stdout` (terminal).

---
