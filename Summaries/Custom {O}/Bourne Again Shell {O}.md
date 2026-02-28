# $\fbox{BOURNE AGAIN SHELL}$





## **Chapter - 1: Surface Level Commands**

- `#` = `sudo` user
- `$` = Non-privileged user

```sh
which bash                # Bash's binaries location
uname -o                  # OS name
echo $(uname -o)          # Same as above
echo "$(uname -o)"        # Same as above
echo uname -o             # Prints: uname -o
```

- `#!` = Shebang (not a comment)

```sh
#!usr/bin/bash             # Locating binaries of Bash.

let count=0                # Integer declaration
let count=count-1
str="Hello, World!"        # String declaration
echo $str
```



## **Chapter - 2: Functions**

```sh
# Making & calling function
function my_func {
	var="local"           # A local variable
}
my_func

# Printing problems
echo $1 $2 $3          # Prints variables
echo '$1 $2 $3'        # Prints: $1 $2 $3
echo "$1 $2 $3"        # Prints variables
```



## **Chapter - 3: Input & Output

```sh
# Receiving arguments
args=(" $@ ")        # Receive args
echo ${args[0]} ${args[1]} ${args[2]}
echo $@        # All arguments passed
echo $#        # Total arguments passed

# Input/output format
read name sur                        # Input: Gourav Kumar Mallick
echo "Name: $name, Sur: $sur"        # name="Gourav", sur="Kumar Mallick"

# Default read variable
read
echo "$REPLY"        # Without target, stored here.

# Error skipping
read -e word                 # Jump to next line if any error occurs.
```



## **Chapter - 4: Array & Arguments**

```sh
# Reading args to array
read -a FRUITS
echo "${FRUITS[0]}, ${FRUITS[1]}, ${FRUITS[2]}"

# Custom array
ARR=('Ubuntu' 'Debian' Arch Mint)        # Total 4 args
TOTAL=${#ARR[@]}                         # Returns total number of args.

# For loop
for ((i=0; i<$TOTAL; i++))
do
	echo ${ARR[$i]}
done
```



## **Chapter - 5: Trap Commands**

```sh
trap my_trap INT;        # One of the many traps.
my_trap()
{
	echo "Ctrl+C detected!"
}
```

- **`EXIT`:** Normal exit
- **`ERR`:** Error encountered
- **`TERM`:** Termination request
- **`HUP`:** Hang up/ close terminal
- **`QUIT`:** Exit from keyboard
- **`DEBUG`:** Stores debug info
- **`RETURN`:** Stores return point
- **`SIGINT`:** Trap signal interrupt number



## **Chapter - 6: Conditional Statements**

```sh
if [ $num -le -1 ]
then
	echo "Negative number"
elif [ $num -eq 0 ]
	echo "Neutral number"
else
	echo "Semi-positive number"
fi
```

- **`-n STR`:** True if string isn't empty
- **`-z STR`:** True if string is empty
