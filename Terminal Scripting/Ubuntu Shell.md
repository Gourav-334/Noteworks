# $\fbox{UBUNTU SHELL}$





## **Topic - 1: Maintenance**

### <u>Upgrading Package Manager</u>

- Once or twice a week, make sure your packages are up to date.

```sh
sudo apt update && sudo apt upgrade
```


### <u>Clean Unrequired Packages</u>

```sh
sudo apt autoremove && sudo apt autoclean
```


### <u>Proper Shutdown</u>

- Instead of closing the terminal directly, use `exit`.

```sh
exit
```



## **Topic - 2: File Operations**

### <u>Copy File</u>

```sh
cp file/to/copy path/to/put
```


### <u>Cut Paste File</u>

```sh
mv file/to/copy path/to/put
```

#### Referring to parent directories:

```sh
mv ../file_name ../..path/to/put
```


### <u>Force Remove Directory</u>

```sh
rm -rf <dir_name>
```


### <u>Rename File</u>

```sh
mv <old_name> <new_name>
```

---
