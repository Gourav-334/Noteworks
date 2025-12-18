# $\fbox{Chapter 2: ENTERING KERNEL SPACE}$





## **Topic - 1: Objectives**

- Loading custom driver code to Linux kernel.
- Exiting kernel by unloading the code back.



## **Topic - 2: Legal Kernel Modules**

### <u>Conditions For Legal Modules</u>

- Kernel entry point
- Kernel exit point


### <u>Kernel Module Lifecycle</u>

$$ \framebox[6cm]{Kernel loads module} $$
$$ \downarrow $$
$$ \framebox[6cm]{module\_init() runs} $$
$$ \downarrow $$
$$ \framebox[6cm]{Module resides in kernel} $$
$$ \downarrow $$
$$ \framebox[6cm]{module\_exit() runs} $$
$$ \downarrow $$
$$ \framebox[6cm]{Kernel forgets module} $$



## **Topic - 3: Kernel Space Privileges**

- There is no `stdio` or `libc` which are are present in **user space**.
- So we can't use `printf`, `scanf`, etc.
- Thus we use `printk` to write on kernel ring buffer.
- And we use `dmesg` to read from the kernel ring.



## **Topic - 4: Directory Setup**

### <u>Shell Code</u>

```sh
mkdir -p ~/kernel-lab/module1
cd ~/kernel-lab/module1
```


### <u>Directory Requirements</u>

- One `.c` file
- One `Makefile` file



## **Topic - 5: Minimal Legal Module Code**

```c
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>



MODULE_LICENSE("GPL");
MODULE_AUTHOR("Gourav");
MODULE_DESCRIPTION("My first kernel module");


static int __init my_init(void)
{
    printk(KERN_INFO "Hello from kernel space\n");
    return 0;
}


static void __exit my_exit(void)
{
    printk(KERN_INFO "Goodbye from kernel space\n");
}


module_init(my_init);
module_exit(my_exit);
```

- `__init` frees built-in memory (if any).
- `printk()` runs in kernel ring buffer & not on terminal.
- It could run without a screen/monitor, but could be configured to communicate with the screen.
- To communicate with user-space applications, `dmesg` is used.



## **Topic - 6: Module Unloading**

### <u>Dangers Of Unloading</u>

- After a module is unloaded, the code is removed from the memory & data structures are removed.
- But function pointers still exist there.
- And if the unloaded modules are called, a reference to unmapped memory is made, which leads to kernel panic.


### <u>Sources Of Crashes</u>

- Registered interrupt handlers
- Armed timers
- Scheduled work queues
- Open device files
- Wrong references


### <u>Production Safety</u>

- Many kernels disable module unloading.
- It is encouraged to add reference counting into driver code.
- Kernel counts how many times `struct module` is used.



## **Topic - 7: Logging, Tainting, Survival**

### <u>Kernel Log Levels</u>

- Type of log affects console visibility, rate limiting, and crash diagnostics.
- Following are the log types supported by `printk()`.

```c
KERN_EMERG
KERN_ALERT
KERN_CRIT
KERN_ERR
KERN_WARNING
KERN_NOTICE
KERN_INFO
KERN_DEBUG
```


### <u>Kernel Tainting</u>

- **<u>Taint flags</u>:** Flags set to drivers by kernel when proprietary, forced, or out-of-tree drivers are loaded to kernel.
- And if a driver is flagged tainted, upstream developers may refuse to debug it.



## **Topic - 8: Testing Sample Module**

### <u>Writing Makefile</u>

```
obj-m += mydriver.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

- `obj-m` - Builds a loadable object module.
- `-C .../build` - Accessing kernel's build system.
- `M=$(PWD)` - Compile our code as external module.


### <u>Using Makefile Properly</u>

```sh
make              # Make/compile the file.
make clear        # To revert the make process.
```


### <u>Loading Module</u>

```sh
sudo insmod module1.ko        # Load module
sudo rmmod module1            # Unload module
sudo dmesg | tail -10         # Show kernel logs (10 recent)
```

---
