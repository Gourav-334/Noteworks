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

/*  */
int sigaction(
	int signum,
	const struct sigaction *act,
	struct sigaction *oldact
);
```
