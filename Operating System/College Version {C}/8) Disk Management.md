# $\fbox{Chapter 8: DISK MANAGEMENT}$





## **Topic - 1: Basic Concepts**

### <u>Introduction</u>

- All data is stored in memory as form of **file**.
- Files can be of many types including text, audio or object files etc.


### <u>File Naming</u>

- File is stored on disk & named for identification.
- Notations for file may vary across OSes.
- File is written in form of `file_name.extension`, where `.` is **period**.
- OS reads extension to know the type of file & type of operations that can be performed on it.


### <u>Types of Files</u>

| File Type  | Extension                       | Work                                                            |
| :--------: | ------------------------------- | --------------------------------------------------------------- |
| Executable | `exe`, `com`, `bin`             | Machine instructions input to loader & executed in main memory. |
|   Object   | `obj`, `o`                      | Compiled machine language.                                      |
|   Source   | `c`, `py`, `java`, `asm`, `177` | Contains sequence of procedures.                                |
|   Batch    | `bat`, `sh`                     | Commands for command interpreter.                               |
|    Text    | `txt`, `doc`                    | Textual data documents.                                         |
|    Word    | `wp`, `nx`, `tef`               | Word processor document.                                        |
|  Archive   | `arc`, `zip`, `tar`             | Compressed files.                                               |



## **Topic - 4: File Type Categorisation**

### <u>Introduction</u>

- Ordinary file
- Directory file
- Special file


### <u>Ordinary File</u>

- Also known as regular file.
- Data in it are just stream of characters.
- It can’t contain another file or directory.
- Can either be a text or binary file.
- High-level source code & binary image files are too ordinary files.
- **<u>Binary file</u>:** Contains unprintable characters like newline terminators unlike text files.
- Can be made & modified through text editors.


### <u>Directory File</u>

- **Directory files** are basically folders.
- They don’t contain data but just references to those data.


### <u>Special File</u>

- Includes - Character device file & block device file
- Also known as device files.
- Files used in communicating with devices.
- Special files contain location, type & access mode for a device.
- **<u>Block device file</u>:** Used to access block device I/O.
- Device files in GNU/Linux are created using mknod command.



## **Topic - 7: File Qualities**

### <u>File Attributes</u>

- **Name**
- **<u>Identifier</u>:** A unique tag number to identify a file.
- **<u>Type</u>:** File type
- **<u>Location</u>:** Pointer to file location.
- **Size**
- **<u>Protection</u>:** Manages user’s access rights.
- **Time, date & user ID**

 >**<u>NOTE</u>:**
 >These information are kept in directory structures.


### <u>File Operations</u>

- Create, delete, open, close, read, write, rename, append, truncate & file seek etc.
- **<u>File seek</u>:** Moving cursor within the file.


### <u>Features of File Structure</u>

- Unstructured sequence of bytes to keep them flexible.
- A custom & fixed length structure within a file.
- Keeps tree of records.



## **Topic - 10: Layered File System**

$$ \framebox[7cm]{Application programs} $$
$$ \downarrow $$
$$ \framebox[7cm]{Logical file system} $$
$$ \downarrow $$
$$ \framebox[7cm]{File organization module} $$
$$ \downarrow $$
$$ \framebox[7cm]{Basic file system} $$
$$ \downarrow $$
$$ \framebox[7cm]{I/O control} $$
$$ \downarrow $$
$$ \framebox[7cm]{Devices} $$

- Just think it from bottom to top regarding how you pressing a keyboard key affects game, an application program.



## **Topic - 11: File Access Methods**

### <u>Introduction</u>

- File organization is done using I/O control system.


### <u>Types of Access Methods</u>

- Sequential access
- Index sequential method
- Direct/ random access


### <u>Sequential Access</u>

- Each file is read one-by-one in sequence, as well as the content in it is read byte-by-byte.
- Read operation advances the file pointer by one byte.
- Write operation appends the material to be added at the end of file.
- Compilers & text editors access files in this order only.
- But one disadvantage of this technique is that it’s an ineffective search technique.

### <u>Index Sequential Method</u>

- In this method, files are given index numbers.
- Index file contains groups of these index numbers.
- When a file is to be found, its index is searched in that index file.
- Then when it is found, the file is accessed with the pointer mapped to that index.
- To find a particular entry, that mapped pointer is moved through the contents of file.
- But disadvantages are that the index files may occupy large portion of memory & the main index file may contain index to smaller index files.


### <u>Direct Access Method</u>

- Also known as random access method.
- Files are accessed after flag is set to read/write before reading or writing.
- And file is treated as a block number, meaning starting from a particular block of memory.
- Can directly access the record, basically how hard disk allows users to do so.
- There is no restriction in order of reading or writing.
- **<u>Relative block number</u>:** Block number provided by the user to OS, which starts from `0` to `1`.
- But disadvantage is that it doesn’t utilizes I/O devices properly & consumes a lot of CPU time.
 


## **Topic - 12: Directory**

### <u>Introduction</u>

- File system maintains directories/folders.
- `.` means current directory & `..` means parent directory.
- While `/` is **root** in GNU/Linux.


### <u>Operations on Directory</u>

- File searching, creation, deletion, renaming & listing of directories.


### <u>Structures of Directory</u>

- Single-level directory
- Two-level directory
- Tree structured directory
- Acyclic graph directory
- General graph directory



## **Topic - 13: Structures of Directory**

### <u>Single-Level Directory</u>

- All files are stored in one directory.
- Files in same directory must have unique name (file name includes the extension).
- File names in ***MS-DOS*** can be at max `11` characters long, while in **UNIX** systems it can be of `255` characters long.


### <u>Two-Level Directory</u>

- It solves the ***unique name only*** problem.
- Each user has their own directory called ***user file directory (UFD)***.
- File is searched as per which user has logged in the system.
- **<u>Master file directory</u>:** Contains entries of user accounts which are mapped to their respective UFD.
- Though files in one UFD must be unique.
- Users can’t share their files to other users within the system.
- However, this structure isn’t ideal when maintaining large number of files.


### <u>Tree Structure Directory</u>

- Users can create their own directories & subdirectories.
- **<u>Absolute path</u>:** Path from root directory to a specific file.
- **<u>Relative path</u>:** Path from current working directory to a specific file.
- If user tries to delete directory or sub-directory which isn’t empty, then it won’t be removed.
- Files & directories can’t be shared.


### <u>Acyclic Graph Structure</u>

- It is similar to tree structure directory but files & directories can be shared here.
- Also, a file or sub-directory maybe linked to multiple directories.
- But one disadvantage is that during deletion, files are linked to multiple directories.


### <u>General Graph Directory</u>

- Unlike acyclic graph structure, it is cyclic.
- Means same file or directory linked in two different sub-directories are linked to another file or sub-directory further.

<img src="./media/image50.png" style="width:6.09806in;height:2.845in" />

- Take the sub-directory book for example.



## **Topic - 14: File Sharing & Protection**

### <u>Introduction</u>

- Owner or creator must be able to provide accessibility to who it wants to.
- Types of access – Read, write & execute.
- Some computers provide backup & hardware safety to avoid physical damage.
- **<u>Access control</u>:** Control on which users can access what in which way.
- Controlled accesses – Rename, repositioning & truncate.


### <u>Access List</u>

- **<u>Access list</u>:** Provides access to files based on their identity.
- Only allowed users can access the file.
- ls `-l` command provides long details about the file.


### <u>Groups</u>

- It’s a protection system.
- Group classification – Owner, group & universe/others.
- **<u>Owner</u>:** User who created the file.
- **<u>Group</u>:** Users who are accessing & sharing the file.
- **<u>Universe/others</u>:** Other users in the system.
- Possible operations – Read-`r`, write-`w` & execute-`x`.
- Value for `r` is `4`, `w` is `2` & `x` is `1`.
- A group is attached to a file so that each member can access that.



## **Topic - 15: File Allocation Method**

### <u>Introduction</u>

- Files are stored in free blocks in disk.
- A block size is `512` bytes.

#### Methods:

- Contiguous allocation method
- Linked allocation method
- Indexed allocation method


### <u>Contiguous Allocation Method</u>

- First block location to store file is allocated randomly from disk.
- Then rest of the blocks (if required) are contiguous to it.
- Contiguous directories contain filename, start block & length.
- It supports both sequential & direct access.
- However, its prone to fragmentation for not being continuously ordered in disk.
- Hence, compaction techniques are used.


### <u>Linked Allocation Method</u>

- Also known as chain allocation.
- Just like linked lists, blocks are allocated randomly & linked with each other.
- Linked directories contain filename, start block & end block.
- So, it’s uses sequential access only.
- Disadvantage is that pointer occupies large part of memory & is hard to maintain.


### <u>Indexed Allocation</u>

- For all part of files, various pointers are present.
- These pointers are kept in a single block.
- Each file has their own index block.
- Index directories contain filename & index block.
- It supports only direct access.



## **Topic - 16: Memory & Free Space Management**

### <u>Methods Used</u>

- <u>Bit map</u>: Free blocks are represented with `0` & busy ones are `1`.
- <u>Linked list</u>: All free blocks are linked with each other.



## **Topic - 17: File System Management**

### <u>Structure Types</u>

- On-disk structure
- In-memory structure


### <u>On-Disk Structure</u>

- Disk contains information about all files, directories, empty blocks & occupied blocks etc.
- Let’s discuss some of these structures there.
- <u>Boot block control</u>: A block containing information about how to boot an OS (only if disk contains the OS).
- <u>Volume control block</u>: Contains details about blocks & the way they are partitioned across the memory.
- <u>File control block (FCB)</u>: Store information related to a file in it.


### <u>In-Memory Structure</u>

- This structure enhances performance of file system via caching.
- <u>Directory structure cache</u>: Holds information about recently accessed directory.



## **Topic - 18: Directory Implementation**

### <u>Methods Used</u>

- Linear list
- Hash map


### <u>Linear List</u>

- Maintains a linear list of filenames in a directory.
- New files are added at the end of the list.
- Uses cache to store recently used files.
- If list is sorted, then binary search can be applied to save time.


### <u>Hash Table</u>

- Same as linear list but hash table is used too.
- Returns a pointer to filename when its created.
- It helps decrease the search time for the user when searching for a file through its name.
- When the filename is searched, the pointer to its name is immediately returned.
- Also, there are mechanisms to avoid collision between files with same name but in different directories.
- This because files with same name may point to same locations as the location in this method is decided as per filename.
- To avoid collision, when hash values point to same location, then a linked list is created at that location instead.


## **Topic - 19: File System Recovery**

### <u>Introduction</u>

- A program called consistency checker checks consistency of files during reboot.
- It compares data in directory structure to data in blocks of disk.
- Not only it finds inconsistencies but also fixes it.


### <u>Signs Of Consistency</u>

- All files, directories & sub-directories etc are arranged the same way without user interference.
- In case the system crashes, a process either completes or is rolled back to initial stage, displaying atomicity.


### <u>Methods To Recover</u>

#### Backup & restore:

- Used in case the magnetic disk fails.
- Files are backed up & stored in another storage device.
- Files copied are tagged with date & time, indicating when backup was performed the last time.

#### Log-structured file system:

- It gives better performance.
- Writes changes made in file to cache.



## **Topic - 20: Virtual File System (VFS)**

- A program which acts as a bridge between kernel & foreign file system.
- This allows the client application to access local & servers etc, which are different types of file systems.

---
