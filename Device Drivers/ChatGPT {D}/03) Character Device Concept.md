# $\fbox{Chapter 3: CHARACTER DEVICE CONCEPT}$





## **Topic - 1: Driver Abstraction**

- Linux treats hardware as files in terms of code.
- It does so by using functions like `open()`, `read()`, `write()`, `ioctl()`, etc.
- This is purely for developer's convenience with application-layer calls like `read(fd)`.



## **Topic - 2: Dev Directory**

### <u>Introduction</u>

- `/dev` is not an ordinary directory on disk.
- It contains details for kernel-registered device numbers.


### <u>Entries</u>

- Each entry contains a **major number** and **minor number**.
- **<u>Major number</u>:** Driver identifier
- **<u>Minor number</u>:** Instance number
- Absence of driver but presence of file means the file is meaningless.


### <u>Example</u>

```sh
crw-rw---- 1 root dialout 188, 0 ttyUSB0
```

- `c` - Character device
- `188` - Driver identifier
- `0` - Instance number



## **Topic - 3: Role Of Character Driver**

### <u>Features</u>

- **<u>Character driver</u>:** A driver which translates file operations into hardware or kernel logic.
- It doesn't interpret user's intent.


### <u>File Operations Translated</u>

- `open()`
- `read()`
- `write()`
- `release()`



## **Topic - 4: File Operations Structure**

### <u>Driver Access Representation</u>

$$ \framebox[6cm]{User calls read()} $$
$$ \downarrow $$
$$ \framebox[6cm]{VFS layer} $$
$$ \downarrow $$
$$ \framebox[6cm]{Driver's function pointer} $$



## **Topic - 5: Powers & Dangers**

### <u>Powers</u>

- Any hardware can be controlled.
- Any behavior can be emulated.
- No need to change user-space.


### <u>Danger</u>

- Fake & malicious devices
- Input interception hack
- Data leakage
- Corrupt communication with user-space



## **Topic - 6: Character Device Skeleton Overview**

### <u>Minimum Requirements</u>

- Major number
- Minor number
- `struct file_operations`
- Initialization & exit routes
- Registration with kernel


### <u>Registration Methods</u>

#### Static major:

- Legacy method
- Simple but dangerous

```c
register_chrdev(240, "mydev", &fops);
```

#### Dynamic major:

- Modern method
- Safe & scalable

```c
alloc_chrdev_region(&dev, 0, 1, "mydev");
cdev_init(&my_cdev, &fops);
cdev_add(&my_cdev, dev, 1);
```


### <u>Open Call Working</u>

$$ \framebox[6cm]{open("/dev/mydev")} $$
$$ \downarrow $$
$$ \framebox[6cm]{VFS resolves inode} $$
$$ \downarrow $$
$$ \framebox[6cm]{Major \& minor fix} $$
$$ \downarrow $$
$$ \framebox[6cm]{file\_operations.open()} $$



## **Topic - 7: Writing Character Device**

### <u>Driver Code File</u>

```c
/* Including required libraries. */

#include <linux/module.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>



/* Useful macro definitions. */

#define DEVICE_NAME "mychardev"
#define BUF_LEN 32





/* Global definitions/declarations */

static dev_t dev_num;
static struct cdev my_cdev;
static char kbuf[BUF_LEN] = "Hello from kernel\n";





/* Driver code for "open" operation. */

static int my_open(struct inode *inode, struct file *file)
{
    pr_info("mychardev: opened\n");
    return 0;
}



/* Driver code for "read" operation. */

static ssize_t my_read(struct file *file, char __user *buf, size_t len, loff_t *offset)
{
    size_t to_copy;

    if (*offset >= BUF_LEN) return 0;
    to_copy = min(len, (size_t)(BUF_LEN - *offset));

    if (copy_to_user(buf, kbuf + *offset, to_copy)) return -EFAULT;
    *offset += to_copy;
    
    return to_copy;
}





/* File operations structure. */

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open  = my_open,
    .read  = my_read,
};





/* Driver code for "initialization". */

static int __init my_init(void)
{
    int ret;

    ret = alloc_chrdev_region(&dev_num, 0, 1, DEVICE_NAME);
    if (ret)
        return ret;

    cdev_init(&my_cdev, &fops);

    ret = cdev_add(&my_cdev, dev_num, 1);
    if (ret)
        unregister_chrdev_region(dev_num, 1);

    pr_info("mychardev: registered (%d:%d)\n",
            MAJOR(dev_num), MINOR(dev_num));
    return ret;
}



/* Driver code for "exiting". */

static void __exit my_exit(void)
{
    cdev_del(&my_cdev);
    unregister_chrdev_region(dev_num, 1);
    pr_info("mychardev: unregistered\n");
}





/* Linking init & exit module + license */

module_init(my_init);
module_exit(my_exit);

MODULE_LICENSE("GPL");

```


### <u>Makefile</u>

```makefile
obj-m += chardev.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```


### <u>Build & Load</u>

```sh
make
sudo insmod chardev.ko
sudo dmesg | grep mychardev    # Will display major & minor number.
```


### <u>Creating Device Node</u>

```sh
sudo mknod /dev/mychardev c <major> <minor>
sudo chmod 666 /dev/mychardev
cat /dev/mychardev
```
