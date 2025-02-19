# $\fbox{Chapter 2: UNIX STANDARD CALLS}$





## **Topic - 1: Process Control Functions**

### <u>Creating Child Process</u>

#### Declaration:

```c
pid_t fork(void);
```

#### About:

- Its a must to import `<sys/types.h>` to use special data types.
- By default its the parent process in control (our running program).
- `fork()` creates an exact copy of our currently running process (program).
- Return value more than `0` means its a parent process.
- `0` - Child process
- `-1` - Error

#### Example:

```c
if (fork()==0) {
	printf("Child process ID: %d", getpid());
}
```


### <u>Replace Process Image</u>

#### Declaration:

```c
int execl(const char *path, const char *arg, ..., NULL);
int execv(const char *path, char *const argv[]);
```

- `path` - Path to executable
- `arg` - Arguments to process

#### About:

- `exec` is used for replacing parent process with another one at same memory space.
- There can be any number of arguments passed to both `execl` & `execv`.
- `execl` must compulsorily end with `NULL`.

#### Example:

```c
#include <unistd.h>

int main()
{
    execl("/bin/ls", "ls", "-l", NULL);
    return 0; // Will not execute if exec succeeds
}

```


### <u>Process IDs</u>

#### Declaration:

```c
pid_t getpid(void);
pid_t getppid(void);
```

#### About:

- `getppid()` is to get parent process's ID.


### <u>Waiting For Process</u>

#### Declaration:

```c
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
```

- `status` - Exit status for a process

#### About:

- Part of `<sys/wait.h>` header.


### <u>Set User & Group ID</u>

#### Declaration:

```c
int setuid(uid_t uid);
int setgid(gid_t gid);
```

#### Example:

```c
setuid(0);        // 0 means requiring 'root permission'
return 0;
```


### <u>Terminate Process</u>

#### Declaration:

```c
void _exit(int status);
```

#### Example:

```c
#include <unistd.h>

int main() {
    _exit(0);
}
```

- This code exits from the current child process immediately.



## **Topic - 2: File I/O Operations**

### <u>File Flags</u>

- `O_RDONLY`
- `O_WRONLY`
- `O_RDWR` - Read & write
- `O_CREAT` - Create file
- `O_EXECL` - Fail if file already exists (used with `O_CREAT`)
- `O_TRUNC` - Erase contents if file exists
- `O_APPEND`
- `O_NONBLOCK` - Non-blocking mode (devices & pipes)
- `O_SYNC` - Write both data & metadata immediately to disk
- `O_SYNC` - Write only data to disk immediately
- `O_RSYNC` - Sync read & write operations


### <u>Creating & Opening File</u>

#### Declaration:

```c
int open(const char *pathname, int flags, mode_t mode);
```

- `mode` (Optional) - Defines file permission when creating new file.
- `flag` - Operation mode

#### About:

- Belongs to `<fcntl.h>`.

#### Example:

```c
int fd = open("filename.txt", O_CREAT | O_WRONLY, 0644);
if (fd==-1) {perror("Opening problem"); return 1;}
```

- `fd` returns `-1` when faced with problem opening file.


### <u>Writing To File</u>

#### Declaration:

```c
ssize_t write(int fd, const void *buf, size_t count);
```

- `buf` - Pointer to data to be written.
- `count` - Number of bytes to write.

#### About:

- Belongs to `<unistd.h>`.

#### Example:

```c
ssize_t bytes_written = write(fd, msg, sizeof(msg)-1);
if (fd==-1) {perror("Writing problem"); return 1;}
```


### <u>Reading From File</u>

#### Declaration:

```c
ssize_t read(int fd, const void *buf, size_t count);
```

#### About:

- Belongs to `<unistd.h>`.


### <u>Closing File</u>

#### Declaration:

```c
int close(int fd);
```

#### Example:

```c
close(fd);
if (fd==-1) {perror("Closing problem"); return 1;}
```


### <u>Moving Content Pointer</u>

#### Declaration:

```c
off_t lseek(int fd, off_t offset, int whence);
```

- `offset` - Number of bytes to move.
- `whence` - Reference point (`SEEK_SET`, `SEEK_CUR` & `SEEK_END`).

#### About:

- Belongs to `<unistd.h>`.


### <u>Deleting File</u>

#### Declaration:

```c
int unlink(const char *pathname);
```

#### About:

- Belongs to `<unistd.h>`.

#### Example:

```c
if (unlink("filename.txt")!=0) {perror("Deleting problem");}
```


### <u>Renaming File</u>

#### Declaration:

```c
int rename(const char *oldpath, const char *newpath);
```

#### About:

- Belongs to `<stdio.h>`.

#### Example:

```c
if (rename("file.txt","new_file.txt")!=0)
{
	perror("Renaming problem");
}
```


### <u>Getting File Information</u>

#### Declaration:

```c
int stat(const char *pathname, struct stat *statbuf);
```

#### About:

- Belongs to `<sys/stat.h>`.

#### Example:

```c
struct stat fileStat;

if (stat("new_file.txt", &fileStat)==0)
{
	printf("File Size: %ld bytes", fileStat.st_size);
	printf("Permissions: %o", fileStat.st_mode & 0777);
}
```


### <u>File Permissions</u>

#### Declaration:

```c
int chmod(const char *pathname, mode_t mode);
```

- `mode` - New permission mode

#### About:

- Belongs to `<sys/stat.h>`.


### <u>File Ownership</u>

#### Declaration:

```c
int chown(const char *pathname, uid_t owner, gid_t group);
```

- `owner` - New owner's UNIX ID.
- `group` - New group's UNIX ID.

#### About:

- Belongs to `<unistd.h>`.

#### Example:

```c
if (chown("new_file.txt", 1000, 1000) == 0)
{
	printf("Ownership changed\n");
}
```



## **Topic - 3: File Descriptor Manipulation**

### <u>Duplicate Descriptor</u>

#### Declaration:

```c
int dup(int oldfd);
int dup2(int oldfd, int newfd);
```

#### Example:

```c
/* dup() */
int new_fd = dup(old_fd);

/* dup2() */
dup2(old_fd, new_fd);
dup2(old_fd, STDOUT_FILENO)    // Output streams will be written to file

printf("This will be written to file!");    // STDOUT redirected
```


### <u>File Synchronization</u>

#### Declaration:

```c
fsync(fd);
```



## **Topic - 4: Working Directory Functions**

### <u>Change Directory</u>

#### Declaration:

```c
int chdir(const char *path);
```

#### About:

- `0` - Success
- `-1` - Failure (with `errno`)
- Affects the calling process (current program) & its children.


### <u>Get Current Working Directory</u>

#### Declaration:

```c
char *getcwd(char *buf, size_t size);
```

#### About:

- Points to `buf` on success, otherwise to `NULL`.



## **Topic - 5: System Config**

### <u>Get Host Name</u>

#### Declaration:

```c
int gethostname(char *name, size_t len);
```

- `name` - Buffer to store host's name.

#### About:

- Returns `0` on success & `-1` on failure.
- Hostname is usually set in `etc/hostname` or `etc/hosts`.


### <u>System Configuration</u>

#### Declaration:

```c
long sysconfig(int name);
```

#### About:

- `name` can either be `_SC_NPROCESSORS_ONLN`, `_SC_CLK_TCK`, `_SC_PAGE_SIZE` or `_SC_OPEN_MAX`.
- `_SC_PAGE_SIZE` - Memory page size
- `_SC_OPEN_MAX` - Max file descriptors that can be opened.
- Returns system configuration value on success, `-1` on error.


### <u>Get User & Group IDs</u>

#### Declaration:

```c
uid_t getuid(void);
gid_t getgid(void);

uid_t geteuid(void);
gid_t getegid(void);
```

#### About:

- `e` in last two lines above stands for "effective".
- Effective user or group ID tells us the permissions that a user or group has.



## **Topic - 7: Miscellaneous**

### <u>Sleep In Seconds</u>

#### Declaration:

```c
unsigned int sleep(unsigned int seconds);
```


### <u>Sleep In Microseconds</u>

```c
int usleep(useconds_t usec);
```


### <u>Terminal Type File Descriptor</u>

#### Declaration:

```c
int isatty(int fd);
```

#### About:

- `isatty()` checks if a file descriptor points to terminal.

---
