# $\fbox{Chapter 6: FILE HANDLING}$





## **Topic – 1: General information**

- `FILE` is a default `typedef` for file pointer.
- **Mode options for file -** `r`, `w`, `a`, `r+`, `w+` & `a+`.
- **Binary mode options -** `rb`, `wb`, `ab`, `wb+`, `rb+` & `ab+`.

>**<u>WARNING</u>:**
>1. Not using `fclose()` function to close the file may cause unwanted behavior.
>2. Mind cursor position when working with files, which is different for each operation.



## **Topic – 2: General Operations**

### <u>Reading From File</u>

```c
fgetc(fptr);
fgets(buffer, n, fptr);
```


### <u>Writing To File</u>

```c
fputc(c, fptr);
fputs(str, fptr);
```



## **Topic – 3: Array Based Operations**

```c
fwrite(arr, size, n, fptr);    // Writes 'n' items from 'arr' of 'size'.
fread(arr, size, n, fptr);     // Reads 'n' items from 'arr' of 'size'.
```

- Actually `fread()` returns `int` which tells how many bytes has been read.
- Giving irrelevant size to `fwrite()` or `fread()` results in some 4-digited numbers being stored in the file.
- `.dat` = data file



## **Topic – 4: Cursor Operations**

```c
feof(fptr);             // Tells if EOF reached.
ftell(fptr);            // Tells cursor's position in bytes.
fseek(fptr, n, pos);    // Moves cursor by 'n' bytes from 'pos'.
```

- Possible values for `pos` are `SEEK_SET`, `SEEK_CUR` & `SEEK_END`.



## **Topic – 5: Formatted Operations**

```c
fprintf(fptr, "Name: %s, Age: %d", name, age);    // Writing to file
fscanf(fptr, "Name: %s, Age: %d", name, age);     // Reading from file
```

---
