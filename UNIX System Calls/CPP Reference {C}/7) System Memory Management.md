# $\fbox{Chapter 7: SYSTEM MEMORY MANAGEMENT}$





## **Topic - 1: Memory Mapping**

### <u>Introduction</u>

- This whole chapter covers the functionalities in header file `sys/mman.h`.


### <u>Map Memory</u>

#### Declaration:

```c
void *mmap(
	void *addr,
	size_t length,
	int prot,
	int flags,
	int fd,
	off_t offset
);
```

- `addr` - User's preferred address (`NULL` means OS will decide)
- `length` - Length of mapped region
- `prot` - Memory protection flag
- `flags` - Mapping flags
- `fd` - `-1` for anonymous mapping
- `offset` - File offset (page-aligned)

#### About:

- `prot` can be `PROT_READ`, `PROT_WRITE` & `PROT_EXEC`.
- `flag` can be `MAP_SHARED` or `MAP_PRIVATE`.
- `mmap()` can access files through memory address, without `read()/write()`.
- Controlling memory sharing.
- Creating isolated dynamic memory regions.

#### Example:

```c
int fd = open("example.txt", O_RDONLY);
if (fd == -1) {perror("open"); return 1;}


/* Mapping memory occupied by the FD 'fd'. */

void *map = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE, fd, 0);
if (map == MAP_FAILED) {perror("mmap"); return 1;}
```


### <u>Unmap Memory</u>

#### Declaration:

```c
int munmap(void *addr, size_t length);
```

#### About:

- Frees/detaches mapped memory.

#### Example:

```c
void *mem = mmap(
	NULL,
	4096,
	PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE,
	-1,
	0
);

if (mem == MAP_FAILED) {return 1;}

munmap(mem, 4096);

return 0;
```



## **Topic - 2: Memory Control**

### <u>Memory Protection</u>

#### Declaration:

```c
int mprotect(void *addr, size_t len, int prot);
```

#### About:

- Used for modifying/changing the protection flag of an existing memory map.


### <u>Memory Synchronization</u>

#### Declaration:

```c
int msync(void *addr, size_t length, int flags);
```

#### About:

- Used to ensure that file memory maps are written to disk properly (atomicity).
- Also prevents data loss during power failure (durability).
- Similar to `fflush()` & `fsync()`.
- `flags` can be `MS_SYNC`, `MS_ASYNC` & `MS_INVALIDATE`.
- `MS_SYNC` - Blocks until changes are written
- `MS_ASYNC` - Doesn't block (writes asynchronously)
- `MS_INVALIDATE` - Discards cached pages

#### Example:

```c
msync(map, 4096, MS_SYNC); // Ensure changes are written to disk
munmap(map, 4096);
```


### <u>Memory Advise</u>

#### Declaration:

```c
int madvise(void *addr, size_t length, int advice);
```

- `advice` - Provides advise for memory usage

#### About:

- Used for receiving hint about memory optimization.
- Reduces page faults.
- `advice` can be `MADV_NORMAL`, `MADV_SEQUENTIAL` & `MADV_RANDOM`.

#### Example:

```c
void *mem = mmap(
	NULL,
	4096,
	PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE,
	-1,
	0
);


/* Inform kernel that access will be random. */

madvise(mem, 4096, MADV_RANDOM);
munmap(mem, 4096);
```


### <u>Memory Lock/Unlock</u>

#### Declaration:

```c
int mlock(const void *addr, size_t len);
int munlock(const void *addr, size_t len);
```

#### About:

- Sometimes, the free space in RAM might be low.
- So an OS might detect it & load entire memory page to disk.
- If there is something very sensitive in it like password, we can lock swapping with disk using `mlock()` & unlock with `munlock()`.

---
