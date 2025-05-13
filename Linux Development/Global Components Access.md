# $\fbox{GLOBAL COMPONENTS ACCESS}$





## **Topic - 1: Binary Executables**

1. Modify `PATH` environment variable.

```sh
export PATH="/path/to/your/binaries:$PATH"
```

2. Now append previous command to end of `~/.bashrc` file.

```sh
echo 'export PATH="/path/to/your/binaries:$PATH"' >> ~/.bashrc
```

3. Restart the terminal or run the following command.

```sh
source ~/.bashrc
```



## **Topic - 2: Header Files**

1. Modify `PATH` environment file.

```sh
export C_INCLUDE_PATH="/path/to/your/headers:$C_INCLUDE_PATH"
export CPLUS_INCLUDE_PATH="/path/to/your/headers:$CPLUS_INCLUDE_PATH"
```

2. Now append previous command to end of `~/.bashrc` file.

```sh
echo 'export C_INCLUDE_PATH="/path/to/your/headers:$C_INCLUDE_PATH"' >> ~/.bashrc
echo 'export CPLUS_INCLUDE_PATH="/path/to/your/headers:$CPLUS_INCLUDE_PATH"' >> ~/.bashrc
```

3. Restart the terminal or run the following command.

```sh
source ~/.bashrc
```

---
