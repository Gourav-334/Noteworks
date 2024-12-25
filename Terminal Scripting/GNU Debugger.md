# $\fbox{GNU Debugger}$





## **Topic - 1: Steps In Brief**

1. Compile the C program into an object file with `-g` flag.
2. Open GDB.
3. Load the target object file into GDB.
4. Set breakpoints.
5. Run required commands.



## **Topic - 2: Basic Commands**

### <u>Source To Object Compilation</u>

```sh
gcc example.c -o example
```

- But GDB can't detect it for debugging as it lacks the debugging flag.


### <u>Debugging Flag</u>

- GDB expects us to put a flag to the compiled object program in order to detect it & being allowed to debug.

```sh
gcc -g example.c -o example
```


### <u>Running GDB</u>

```sh
gdb
```


### <u>Loading Target Object File</u>

```gdb
file ./example
```


### <u>Running</u>

```gdb
run
```

- It is used for running the program (simple execution of program).


### <u>Start & Breakpoint</u>

```gdb
start
```

- It starts our program & may show some breakpoints to us.
- **<u>Breakpoint</u>:** A point in program up to which we can analyze flow of program.


### <u>Listing All Code Lines</u>

```gdb
list
```


### <u>Next</u>

- `next` or `n` command selects the next non-blank line of code.

```gdb
next
```

- This also executes that particular line of code.


### <u>GDB Text Editor Mode</u>

- Press `CTRL + X + 1` to start GDB in text editor mode for the chosen file.
- Its just more visual mode of GDB with same set of commands.
- Also we can refresh it using `CTRL + L`.


### <u>Seeing Assembly Beneath</u>

#### Whole function:

```gdb
disassemble myFunc
```

#### Within A Range:

```gdb
disassemble 0x400600, 0x400620
```



## **Topic - 3: Debugging**

### <u>Example Code</u>

```c
#include <stdio.h>

int *ptr = NULL;

void foo() {*ptr = 7;}

int main()
{
	foo();
	
	return 0;
}
```

- Consider the program above for the upcoming commands.


### <u>Variables Value Check</u>

- We can check value of a variable or macro at a particular line.

```gdb
print my_var
```

- Also we can check information about the arguments of current function via the following command.

```gdb
info args
```


### <u>Setting Values</u>

- We can set the value of a variable as shown below.

```gdb
set var1=var2
```


### <u>Step</u>

- `step` command jumps us into the source of current line of code.
- For example, if the line is a function call like `foo();`, then we jump to the part where they were declared.


### <u>Finding Bug Source</u>

- For the example we did, we find that the problem in the 5th line.

```c
*ptr = 7;
```

- And we can trace where else it is spread using `bt` command.

```gdb
bt
```



## **Topic - 4: Breakpoints**

### <u>Setting Breakpoints</u>

#### At a particular line:

```gdb
br 8
```

- This sets breakpoint at line 8.

#### For a particular token:

```gdb
br foo
```

- This sets breakpoint for say a function named `foo()`.


### <u>Removing Breakpoints</u>

```gdb
delete 8
```


### <u>Getting Info</u>

```gdb
info breakpoints
```

- This commands gets us information about all the breakpoints set.


### <u>Continuing To Next Breakpoint</u>

```gdb
continue
```



## **Topic - 5: Bonus Facts**

### <u>Enabling Warnings</u>

- We can allow all warnings to show up with `-Wall`.
- And we can also allow all warnings to be treated as errors with `-Werror`, as a good programming practice.

```sh
gcc -Wall -Werror example.c -o example
```


### <u>Object Dump</u>

- GNU Object Dump is a default system software in UNIX & UNIX-like OSes for analyzing object files.
- One can type the following command to read its manual on terminal.

```sh
man objdump
```


### <u>Symbol Table</u>

- We can see the whole symbol table for an object code with following command.

```sh
objdump -t ./example
```

---
