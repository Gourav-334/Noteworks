# $\fbox{Chapter 9: MULTITHREADING}$





## **Topic – 1: Creation Of Thread**

### <u>Introduction</u>

- There are two types of multitasking – Process based & thread based.


### <u>Steps Involved</u>

1. Create a function of `void *` type.

```c
void *func(void *arg)        // Atleast one 'void' arg is compulsory
{
	pthread_exit(NULL);        // Exit status = NULL
	return NULL;
}

int main()
{
```

2. Create thread ID storage in `main()` function.

```c
pthread_t thread;           // Thread ID
pthread_t thread[7];        // Array of thread IDs
```

3. Create the thread.

```c
/* pthread_create(thread_ptr, thread_attr, func2call, arg2func); */
pthread_create(&thread, NULL, func, NULL);
```

4. Add a join function which allows thread to finish execution.

```c
/* pthread_join(thread, ret2thread_func) */
pthread_join(thread, NULL);
```



## **Topic – 2: Thread Attributes**

### <u>Monologue</u>

- Attribute’s lifecycle is similar to thread itself, but both are different things.
- Making attribute argument in `pthread_create()` as `NULL` means setting default configuration for our thread.


### <u>Thread Attribute Life Cycle</u>

- Creation
- Initialization
- State definition
- Death


### <u>Creation</u>

```c
pthread_attr_t attribute;
```


### <u>Initialization</u>

```c
pthread_attr_init(&attribute);
```


### <u>State Definition</u>

```c
/* Joinable state */
pthread_attr_setdetachstate(&attribute, PTHREAD_CREATE_JOINABLE);

/* Detached state */
pthread_attr_setdetachstate(&attribute, PTHREAD_CREATE_DETACHED);
```


### <u>Stack Size Setting</u>

```c
size_t size = 2*1024*1024        // 2 MB stack size
pthread_attr_setstacksize(&attribute, size);
```


### <u>Death</u>

```c
pthread_attr_destroy(&attr);
```



## **Topic – 4: Mutex**

### <u>Introduction</u>

- **<u>Mutex</u>:** Stands for mutually exclusive.
- Used for preventive multiple threads from accessing commonly shared resources.


### <u>Mutex Lifecycle</u>

- Creation
- Initialization
- Action
- Destroy


### <u>Creation</u>

```c
pthread_mutex_t m;
```


### <u>Initialization</u>

```c
pthread_mutex_init(&m, NULL); // NULL – Mutex attribute
```


### <u>Action</u>

```c
/* Blocks until critical section is locked by another thread. */
pthread_mutex_lock(&m);

/* Unlocks the thread. */
pthread_mutex_unlock(&m);

/* Returns '0' if mutex is already locked. */
pthread_mutex_trylock(&m);
```


### <u>Death</u>

```c
pthread_mutex_destroy(&m);
```



## **Topic – 5: Mutex Attribute**

### <u>Mutex Attribute Lifecycle</u>

- Creation
- Initialization
- Set type


### <u>Creation</u>

```c
pthread_mutexattr_t myAttr;
```


### <u>Initialization</u>

```c
pthread_mutexattr_init(&myAttr);
```


### <u>Set Type</u>

```c
/*
 * This one is default one.
 * We will discuss more mutex attributes soon.
 */

pthread_mutexattr_settype(&myAttr, PTHREAD_MUTEX_NORMAL);
```

---
