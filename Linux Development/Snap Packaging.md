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
4. Initialize LXD in root directory.

```sh
lxd init --minimal
```


### <u>Creating YAML Template</u>

1. Initialize YAML template with snapcraft.

```sh
snapcraft init
```

2. Navigate inside `snap/`.

```sh
cd snap
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

- But we haven't mentioned any executables yet.


### <u>Building The Part</u>

#### Parts lifecycle (build stages):

1. **<u>Pull</u>:** Retrieves all required components to built each part.
2. **<u>Build</u>:** Makes each part with all mentioned plugins.
3. **<u>Stage</u>:** Copies build components to a staging area.
4. **<u>Prime</u>:** Moves all files & directories to target locations.

 >**<u>NOTE</u>:**
 >We can stop build process anytime to take a look inside the container.

#### Snapcarfting:

1. Clean the previous snap (if any).

```sh
snapcraft clean
```

2. Snapcraft up to prime stage with a shell opened in that directory.

```sh
snapcraft prime --shell
```

3. From build shell, enter the following.

```sh
cd $HOME && ls        # Contains build stage parts & env variable.
```

4. Search for your executables.

```sh
find . -name liquidctl        # Stored at ./stage/bin
```

5. Exit the build environment shell.

```sh
exit
```



## **Topic - 4: App Section**

### <u>Introduction</u>

- Allow to use binary's location & permit it access.

```yaml
apps:
	my-snap-name:
		command: bin/liquidctl
```

- So when a user installs our snap, typing `my-snap-name` will run `bin/liquidctl`.


### <u>Installing Snap In DevMode</u>

1. Now type `snapcraft`.

```sh
snapcraft        # Creates 'my-snap-name_0.1_amd64.snap'
```

2. Try installing your snap.

```sh
sudo snap install ./my-snap-name_0.1_amd64.snap --dangerous --devmode
```

3. Run the executable `my-snap-name`.

```sh
my-snap-name
```



## **Topic - 5: Testing The Snap**

### <u>Missing Dependencies</u>

- For missing dependencies, we can add stage-packages.
- Have a look at the sample below.

```yaml
parts:
	my-part:
		plugin: python
		source-type: git
		source: http://github.com/user/liquidctl
		stage-packages:
			- python3-usb 
```

- Now we can just `snapcraft clean` & `snapcraft` again for a change in YAML file.


### <u>System Access</u>

```yaml
apps:
  my-snap-name:
    command: bin/liquidctl
    plugs:
      - raw-usb
      - uhid
      - hardware-observe
```

- Some of the permissions can't be provided by snap.
- So, a user has to manually permit it to access some special permissions.

```yaml
sudo snap connect my-snap-name:uhid
sudo snap conenct my-snap-name:raw-usb
sudo snap connect my-snap-name:hardware-observe
```



## **Topic - 6: Update Confinement**

- Grade must be `stable` to be released into stable channels.
- Confinement must be `strict` after getting right plugins & slots.

```yaml
grade: stable
confinement: strict
```



## **Topic - 7: Problems**

1. Don't know if executables will work at `bin/` normally.
2. No idea about packaging with multiple executables.

---
