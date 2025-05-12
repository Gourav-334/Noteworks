# $\fbox{Chapter 4: SIGNAL HANDLING}$





## **Topic - 1: Portable Functions**

### <u>Signals In UNIX</u>

| Signal    | Default Action | About                         |
| --------- | -------------- | ----------------------------- |
| `SIGINT`  | Terminate      | Keyboard interrupt            |
| `SIGABRT` | Core dump      | Aborts signal using `abort()` |
| `SIGFPE`  | Core dump      | Floating-point exception      |
| `SIGKILL` | Terminate      | Kill the signal               |
| `SIGSEGV` | Core dumped    | Segmentation fault            |
| `SIGPIPE` | Terminate      | Writing to a closed pipe      |
| `SIGALRM` | Terminate      | Alarm clock                   |
| `SIGTERM` | Termination    | Gracefully terminating signal |

- There are even more signals used for even more niche purposes.


### <u>Signal</u>

#### Declaration:

```c
void (*signal(int signum, void (*handler)(int)))(int);
```

- `signum` - Signal number
- `handler` - Pointer to function which runs when signal is received

#### About:

- `signum` as `SIGINT` means receiving $CTRL\;+\;C$ interrupt.
- While `SIGUSR1` is for resetting global flag.
- `signal()` is used to register a signal with a function.

#### Example:

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_signal(int signum) {
    printf("Caught signal %d!\n", signum);
}

int main()
{
    signal(SIGINT, handle_signal);    // Handle Ctrl+C
    
    while (1) {
        printf("Running...\n");
        sleep(2);
    }
    
    return 0;
}
```

- Press $Ctrl+Z$ to exit the process, as it $Ctrl+C$ will just execute `handle_signal()` code.
- When we called the `signal()` function, it registered $Ctrl+C$ with function `handle_signal()`.
- Whatever function we make & register with `signal()`, it can have at max one argument which works as signal number.
- That function can have more than two arguments, but other than first one all would be unnecessary.


### <u>Raise</u>

#### Declaration:

```c
int raise(int sig);
```

- `sig` - The signal send to process.

#### About:

- We use `raise` for raising a signal.
- For example, if we raise `SIGINT` signal & if it is registered with a function using `signal()`, then that signal would be called when raised.

#### Example:

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_signal(int signum) {
    printf("Caught signal %d!\n", signum);
}

int main()
{
    signal(SIGINT, handle_signal);    // Handle Ctrl+C
    raise(SIGINT);
    
    return 0;
}
```



## **Topic - 2: Purely POSIX Functions**

### <u>Kill</u>

#### Declaration:

```c
int kill(pid_t pid, int sig);
```

- `sig` - Signal to send

#### About:

- Used generally to kill a process, but can execute other signals too.
- Use `SIGKILL` to kill a process.

#### Example:

```c
pid_t pid = getpid();

printf("Killing process %d\n", pid);
kill(pid, SIGKILL);
```


### <u>Signal Action</u>

#### Declaration:

```c
int sigaction(
	int signum,
	const struct sigaction *act,
	struct sigaction *oldact
);
```

- `act` - Pointer to a constant structure which defines new handler.
- `oldact` - Can also be passed as `NULL`, defines older handle if not `NULL`.

#### Example:

```c
void handle_sigint(int sig) {
    printf("Received SIGINT\n");
}


int main()
{
    struct sigaction sa;
    sa.sa_handler = handle_sigint;
    sigemptyset(&sa.sa_mask);        // Empties 'sa_mask'
    sa.sa_flags = 0;
	
    sigaction(SIGINT, &sa, NULL);
    
    while (1) {
        printf("Running...\n");
        sleep(2);
    }
    
    return 0;
}
```


### <u>Signal Process Masking</u>

#### Declaration:

```c
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

- `how` - Operation to perform
- `set` - New signal to set
- `oldset` - If not `NULL`, stores the older mask

#### About:

- Blocking signals at certain sections of the program.
- `how` can be `SIG_BLOCK`, `SIG_UNBLOCK` & `SIG_SETMASK`.

#### Example:

```c
/* Defining 'set' & emptying it. */

sigset_t set;
sigemptyset(&set);


/* Registering 'set' with SIGINT signal. */

sigaddset(&set, SIGINT);


/* Masking 'set' by blocking it. */

sigprocmask(SIG_BLOCK, &set, NULL);
printf("SIGINT is now blocked\n");


/* SIGINT won't interrupt during these 5 sec. */

sleep(5);


/* Unblocking 'set' assigned signal. */

sigprocmask(SIG_UNBLOCK, &set, NULL);
printf("SIGINT is now unblocked\n");
fflush(stdout);    // Forces OS to write last printf()
```

- The program stops right when the `SIGINT` is unblocked, if user requests termination during the `5` seconds sleep.
- This is because the signal requests are queued, not ignored completely.


### <u>Signal Wait</u>

#### Declaration:

```c
int sigwait(const sigset_t *set, int *sig);
```

- `set` - Set of signals to wait for
- `sig` - Stores the received signal

#### About:

- Often used for pausing a thread until a signal is received.
- For example, in managing daemons.
- **<u>Daemon</u>:** A background process that doesn't require direct user interaction.

#### Example:

```c
sigset_t set;
int sig;

sigemptyset(&set);
sigaddset(&set, SIGINT);


/* Waits until SIGUSR1 - 'kill' signal is received. */

printf("Waiting for SIGUSR1...\n");
sigwait(&set, &sig);
printf("Received signal %d\n", sig);
```


### <u>Signal Suspend</u>

#### Declaration:

```c
int sigsuspend(const sigset_t *mask);
```

#### About:

- Used for pausing a process until signal is received without polling.
- **<u>Poll</u>:** Repetitively checking a condition to be true.

#### Example:

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>


void handle_signal(int sig) {
    printf("Received signal %d, exiting...\n", sig);
}


int main()
{
    signal(SIGTERM, handle_signal);
	
	
	/* Creating a mask to block signals. */
	
    sigset_t mask;
    sigfillset(&mask);            // By default masks all signals
    sigdelset(&mask, SIGTERM);    // SIGTERM is made an exception
	
    printf("Waiting for SIGTERM...\n");
    sigsuspend(&mask);            // Waits for unsuspended signal
	
    return 0;
}
```

---
