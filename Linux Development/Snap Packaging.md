# $\fbox{SNAP PACKAGING}$





## **Topic - 1: Requirements**

- Snapcraft runs on all Linux distros, MacOS & Windows.
- Recommended to use Ubuntu 22.04 (Jammy Jellyfish).
- 20 GB of storage is required too.



## **Topic - 2: Snapcraft Setup**

### <u>Snapcraft Build Environment</u>

1. Install LXD container service.

```sh
sudo snap install lxd
```

2. Give current user permission to use LXD.

```sh
sudo usermode -a -G lxd $USER
```

3. Log-in & log-out for refreshing.
4. LXD can now be initialized.

```sh
lxd init --minimal
```


### <u>Creating YAML Template</u>

1. Create a new directory for snap data.

```sh
mkdir snap
```

2. Navigate inside `snap/`.

```sh
cd snap
```

3. Initialize YAML template with snapcraft.

```sh
snapcraft init
```


### <u>Testing Snap Packaging</u>

- Let's package this empty snap package.
- The YAML template contains enough information by default to package.

```sh
snapcraft
```

- This will create a new LXD container & build a `.snap` package.



## **Topic - 3: Modify YAML File**

### <u>Introduction</u>

- `snap/snapcraft.yaml` has some default configurations.
- This default configuration is enough to build a package but is not functional.


### <u>Creating New Part</u>

- Parts are components required for snap (snapcrafted application) to function.
- Plugins are used to build & organize required external components.
- In `snap/snapcraft.yaml` replace `nil` for plugin with actual plugins.
- For example, as following.

```yaml
plugin: python
source-type: git
source: https://github.com/user/liquidctl
```
