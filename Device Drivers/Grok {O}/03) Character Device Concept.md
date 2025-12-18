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

