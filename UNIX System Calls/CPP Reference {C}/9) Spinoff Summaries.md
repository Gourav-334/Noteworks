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
