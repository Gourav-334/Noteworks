# $\fbox{BASH}$





## **Topic - 1: Basic Information**

### <u>System Privilege Levels</u>

- `#` prompts execution of commands with root privileges, either with default root user or with `sudo`.
- `$` executes commands as a non-privileged user.


### <u>Getting Installed Location</u>

```sh
which bash
```



## **Topic - 2: Getting Started**

### <u>Convention</u>

```sh
#!usr/bin/bash
```

- Though `#` is used for commenting in Bash, this one is not a comment.
- `#!` is called a shebang & thus together are not read as comment.


### <u>First Program</u>

```sh
#!usr/bin/bash

str="Hello, World!"
echo $str
```

>**<u>NOTE</u>:**
>There is no space around assignation operator.



## **Topic - 3: Functions**

### <u>Introduction</u>

```sh
#!usr/bin/bash

function myFunc
{
	var="local"
	echo $var
}

myFunc        # Calling the function
```

- Just like in most programming languages, variables inside a function are treated as local variables.


### <u>Printing Conventions</u>

```sh
#!usr/bin/bash

echo $1 $2 $3        # Not printed
echo '$1 $2 $3'      # Printed
echo "$1 $2 $3"      # Not printed
```


### <u>Arguments</u>

```sh
#!usr/bin/bash

args=("$@")        # Must write to play with arguments.

# Prints argumentss passed when running the bash file
echo ${args[0]} ${args[1]} ${args[2]}

echo $@        # Prints all passed arguments
echo $#        # Prints 
```



## **Topic - 4: Input & Output**

### <u>Uname</u>

```sh
#!usr/bin/bash

echo $(uname -o)        # Tells the OS name
echo uname -o           # Prints literally uname -o
```


### <u>Numerical I/O</u>

```sh
#!usr/bin/bash

echo "Enter your age: "
read age
echo "$age"
```


### <u>String I/O</u>

```sh
#!usr/bin/bash

echo "Enter full name: "
read name sur            # Gourav Kumar Mallick
echo "$name, $sur"       # Gourav, Kumar Mallick
```


### <u>Default Read Variable</u>

- If no variable is mentioned to take input, the input is stored in `REPLY` variable by default.

```sh
#!usr/bin/bash

echo "Say something: "
read
echo "You said: $REPLY"
```


### <u>Error Handling</u>

- `-e` makes the pointer jump to next line if any error.

```sh
#!usr/bin/bash

echo -e "Rise"
read -e word
```



## **Topic - 5: Arrays & Traps**

### <u>Taking Elements</u>

```sh
#!usr/bin/bash

read -a fruits
echo "${fruits[0]}, ${fruits[1]}, ${fruits[2]}"
```

- `-a` tells that `fruits` is name of an array.


### <u>Trap/Interrupt</u>

- We named out trap as `bashtrap` (of type `INT`).
- `;` is used for writing multiple codes of same line.

```sh
#!usr/bin/bash

#trap name TYPE
trap bashtrap INT

clear;

bashtrap()
{
	echo "\"CTRL + C\" is detected!"
}
```


### <u>Shell Commands</u>

```sh
#!usr/bin/bash

ls                  # Fast & structured
echo "$(ls)"        # Introduces little more overhead
```


### <u>Assigning Array</u>

```sh
ARR=('Ubuntu' 'Arch' Mint Fedora)

TOTAL=${#ARR[@]}        # Prints number of elements in ARR
```
