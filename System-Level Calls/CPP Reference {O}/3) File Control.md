# $\fbox{Chapter 3: FILE CONTROL}$





## **Topic - 1: Descriptor Manipulation**

### <u>File Controller</u>

#### Declaration:

```c
int fcntl(int fd, int cmd, ...);
```

- `cmd` - Command to perform
- Rest of the arguments are arguments to be passed to command.

#### About:

- Used for non-blocking mode, duplicating file descriptor & managing locks.
- Non-blocking mode are the default modes for performing file operations (read/write or return `errno` error).
- `cmd` can be `F_GETFL` & `F_SETFL`.

#### Example:

```c
int flags = fcntl(fd, F_GETFL);

if (flags == -1) {
	perror("Error getting flags");
	return 1;
}

/* Set file to non-blocking mode */

if (fcntl(fd, F_SETFL, flags | O_NONBLOCK) == -1)
{
	perror("Error setting flags");
	return 1;
}
```


### <u>Flock</u>

#### Declaration:

```c
int flock(int fd, int operation);
```

#### About:

- Part of `<sys/file.h>`, but might be sometimes found in `<fcntl.h>`.
- Different types of locks are there like `LOCK_SH`, `LOCK_EX`, `LOCK_UN` & `LOCK_NB`.
- `LOCK_SH` - Shared lock, allowing multiple processes to only read a file.
- `LOCK_EX` - Exclusive lock, allowing only one process to read/write.
- `LOCK_UN` - Unlock the file.
- `LOCK_NB` (Optional) - Non-blocking mode.
- Returns `-1` on error.

---
