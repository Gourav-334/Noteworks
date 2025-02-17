




## **Topic - 1: Process Control Functions**



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
