# $\fbox{Chapter 9: SNINOFF SUMMARIES}$





## **Topic - 1: Standard Library**

### <u>Exit Functions</u>

```c
/* Exit without cleanup. */
void abort(void);

/* Executes 'atexit()' functions when called. */
void exit(int exit_code);

/* Execute 'at_quick_exit()' functions, partial cleanup, call _Exit(). */
void quick_exit(int exit_code);

/* Partial cleanup, no registered exit functions. */
void _Exit(int exit_code);

/* There can be 32 of registered 'atexit()'. */
int atexit(void (*func)(void));

/* There can be 32 of registered 'at_quick_exit()'. */
int at_quick_exit(void (*func)(void));
```


### <u>Environment Variables</u>

```c
/* Get environment variable. */
char *getenv(const char *name);

/* More precise & safe way. */
errno_t getenv_s(
	size_t *restrict len,
	char *restrict value,
	rsize_t valuesz,
	const char *restrict name
);

/* Modifying environment variable. */
int setenv(
	const char *envname,
	const char *envval,
	int overwrite
);

/* Removing an environment variable. */
int unsetenv(const char *name);

/* Modify environment variable by its path. */
int putenv(char *string);
```



## **Topic - 2: UNIX Standard Calls**

### <u>Process Functions</u>

```c
/* Create copy of current parent process. */
pid_t fork(void);

/* Replacing current parent process. */
int execl(const char *path, const char *arg, ..., NULL);
int execv(const char *path, const char *argv[]);

/* Get child's process ID. */
pid_t getpid(void);

/* Get parent's process ID. */
pid_t getppid(void);

/* Put parent process into waiting. */
pid_t wait(int *status);

/* Put child process into waiting. */
pid_t waitpid(pid_t pid, int *status, int options);

/* Set user ID. */
int setuid(uid_t uid);

/* Set group ID. */
int setgid(gid_t gid);

/* Terminate current child process. */
void _exit(int status);
```


### <u>File Operations</u>

```c
/* Creating/opening file. */
int open(const char *pathname, int flags, mode_t mode);

/* Writing to file. */
ssize_t write(int fd, const void *buf, size_t count);

/* Reading from file. */
ssize_t read(int fd, const void *buf, size_t count);

/* Closing file. */
int close(int fd);

/* Moving file pointer. */
off_t lseek(int fd, off_t offset, int whence);

/* Deleting a file. */
int unlink(const char *pathname);

/* Renaming a file. */
int rename(const char *oldpath, const char *newpath);

/* Getting information about the file. */
int stat(const char *pathname, struct stat *statbuf);
```


### <u>File Permissions</u>

```c
/* Assigning permission to a file. */
int chmod(const char *pathname, mode_t mode);

/* File ownership. */
int chown(const char *pathname, uid_t owner, gid_t group);

/* Get user ID. */
uid_t getuid(void);

/* Get group ID. */
gid_t getgid(void);

/* Get effective user ID. */
uid_t geteuid(void);

/* Get effective group ID. */
gid_t getegid(void);
```


### <u>File Descriptor Manipulation</u>

```c
/* Duplicating descriptor. */
int dup(int oldfd);
int dup2(int oldfd, int newfd);

/* Syncing file. */
fsync(fd);

/* Checks if FD points to terminal. */
int isatty(int fd);
```


### <u>Working Directory Functions</u>

```c
/* Change directory. */
int chdir(const char *path);

/* Get current working directory. */
int *getcwd(char *buf, size_t size);
```


### <u>System Configuration</u>

```c
/* Get host name. */
int gethostname(char *name, size_t len);

/* Get a system information as per the passed 'name'. */
long sysconfig(int name);
```


### <u>Sleep</u>

```c
/* Second-precision */
unsigned int sleep(unsigned int seconds);

/* Microsecond-precision */
int usleep(useconds_t usec);
```



## **Topic - 3: File Control**

```c
/* File controller, modifying permissions to descriptor flag. */
int fcntl(int fd, int cmd, ...);

/* Flocker, modifying the type of lock on file behaviour. */
int flock(int fd, int operation);
```



## **Topic - 4: Signal Handling**

### <u>Portable Signal Functions</u>

```c
/* Signal registering & handling. */
void (*signal(int signum, void (*handler)(int)))(int);

/* Raise a signal manually. */
int raise(int sig);
```


### <u>POSIX Signal Functions</u>

```c
/* Generally used to kill a signal, but works elseway too. */
int kill(pid_t pid, int sig);

/* Assigning new signal handling struct for a signal. */
int sigaction(
	int signum,
	const struct sigaction *act,
	struct sigaction *oldact
);

/* Change masking rules for a signal. */
int sigprocmask(int how, const sigset_t  *set, sigset_t *oldset);

/* Waits until a signal is received. */
int sigwait(const sigset_t *set, int *sig);

/* Pausing or suspending a signal (no polling). */
int sigsuspend(const sigset_t *mask);
```



## **Topic - 5: POSIX Multithreading**

### <u>Creation Of Thread</u>

```c
#include <stdio.h>
#include <pthread.h>


/* Exit function for thread. */

void *func(void *arg)
{
	pthread_exit(NULL);
	return NULL;
}


/* Main function */

int main()
{
	/* Creating thread ID storage. */
	
	pthread_t thread;           // Single thread ID
	pthread_t thread_arr[7];    // Array of thread IDs
	
	
	/* Creating the thread itself. */
	
	pthread_create(&thread, NULL, func, NULL);
	
	
	/* Let main() function wait for thread execution. */
	
	pthread_join(thread, NULL);
	
	return 0;
}
```


### <u>Thread Attributes</u>

```c
/* Creating attribute. */
pthread_attr_t attr;

/* Initializing attribute. */
pthread_attr_init(&attr);

/* Joinable state */
pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

/* Detached state */
pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);

/* State size setting. */
pthread_attr_setstacksize(&attr, size);

/* Killing an attribute. */
pthread_attr_destroy(&attr);
```


### <u>Mutex</u>

```c
/* Creating mutex. */
pthread_mutex_t lock;

/* Initializing mutex. */
pthread_mutex_init(&lock, NULL);

/* Actions */
pthread_mutex_lock(&lock);           // Blocks until resource is in use.
pthread_mutex_unlock(&lock);         // Unlocks the thread.
pthread_mutex_trylock(&lock);        // Returns 0 if mutex already lock.

/* Kill a mutex. */
pthread_mutex_destroy(&lock);
```


### <u>Mutex Attributes</u>

```c
/* Creating mutex attribute. */
pthread_mutexattr_t lockAttr;

/* Initializing mutex attribute. */
pthread_mutexattr_init(&lockAttr);

/* Configuring mutex type. */
pthread_mutexattr_settype(&lockAttr, PTHREAD_MUTEX_NORMAL);
```



## **Topic - 6: Socket Programming**

### <u>Server</u>

#### Required headers:

```c
#include <sys/types.h>     // Contains special data types.
#include <sys/socket.h>    // Contains socket-related structures.
#include <netinet/in.h>    // Contains internet domain related stuffs.
```

#### Structures & functions:

```c
/* Socket's address (like server's, clinet's). */
struct sockaddr_in server;
server.sin_family = AF_NET;             // Must always be set to AF_NET.
server.sin_port = htons(port);          // Argument conversion to port number.
server.sin_addr.s_addr = INADDR_ANY;    // IP address of server.

/* Creating a socket. */
sockfd = socket(AF_NET, SOCK_STREAM, 0);

/* Binding a socket. */
bind(sockfd, (struct sockaddr_in*) &server, sizeof(server));

/* Looking for a server. */
listen(sockfd, 5);

/* Accepting connection request. */
newsockfd = accept(sockfd, (struct sockaddr_in*), &client, &clilen);

/* Reading from socket. */
n = read(newsockfd, buffer, 256);

/* Writing to socket. */
n = write(newsockfd, "I got your message!", 19);
```


### <u>Client</u>

#### Required headers:

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>             // Defines structure for 'hostent'.
```

#### Structures & functions:

```c
/* Fethcing port number of host. */
portno = argv[2];

/* Socket address of client. */
struct sockaddr_in client;

/* Pointer to 'hostent' struct, containing host details. */
struct hostent *server;
server.sin_family = AF_INET;        // IP address
server.sin_port = htons(portno);

/* Setting up client socket. */
sockfd = socket(AF_NET, SOCK_STREAM, 0);

/* Fetching hostname from argument. */
hostname = gethostbyname(argv[1]);

/* Connecting to server socket. */
connect(sockfd, &server, sizeof(server));

/* Sending stream to server. */
write(sockfd, buffer, strlen(buffer)*sizeof(char));
```
