# $\fbox{GIT}$





## **Topic - 1: Configuring Details**

### <u>For Specific Repository</u>

```sh
git config user.name "Your Name"
git config user.email "email@gmail.com"
```


### <u>For All Repository</u>

```sh
git config --global user.name "Your Name"
git config --global user.email "email@gmail.com"
```


### <u>Removing Specific Configuration</u>

```sh
git config --global --unset user.name
git config --global --unset user.email
```


### <u>Removing All Configuration</u>

```sh
rm ~/.gitconfig
```


### <u>Verifying Changes</u>

```sh
git config --list
git config --list --local
```



## **Topic - 2: SSH Keys**

### <u>Importance</u>

- SSH keys remove the need to enter username & password each time on push, pull or clone operations.
- GitHub removes specific keys after an year.


### <u>Step - I</u>

```sh
ssh-keygen -t ed25519 -C example@gmail.com
```

- `25519` is the encryption used when generating key.
- It will prompt question for location to store keys, prefer choosing ~/.


### <u>Step - II</u>

- An agent is used to store various keys, password or passphrases etc.
- We confirm presence of SSH key by following command.

```sh
eval "$(ssh-agent -s)"
```


### <u>Step - III</u>

- Check for presence of $config$ file in the created folder.

```sh
~/.ssh/config
```

- If present, then good.
- If not, enter the following command.

```sh
touch ~/.ssh/config
vim config
```


### <u>Step - IV</u>

- Write following code in Vim terminal.

```sh
Host *
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
  UseKeyChain yes      # Write only if using passphrase
```

- Save these changes.


### <u>Step - V</u>

- Now we tell our operating system that we are adding the generated file as our SSH key.

```sh
ssh-add ~/.ssh/id_ed25519
```


### <u>Step - VI</u>

```sh
cat ~/.ssh/id_ed25519.pub
```

- Copy the output.


### <u>Step - VII</u>

1. Now open GitHub.
2. Click on your profile picture.
3. Go to **Settings** > **SSH and GPG keys** > **Add**
4. Paste the output copied in last step in **Key**.


### <u>Step - VIII</u>

- Now our final step is to set connection of our SSH key with GitHub.

```sh
ssh -T git@github.com
```

- If a question is prompted, enter $yes$ as command.



## **Topic - 3: Linking Repositories**

### <u>Linking Local To Remote</u>

```sh
git remote add origin <repo_http_url>
```


### <u>Changing Linked URL</u>

```sh
git remote set-url origin <new_repo_url>
```



## **Topic - 4: Branch**

### <u>Deletion</u>

```sh
git branch -d <branch_name>
```


### <u>Merge</u>

1. Switch to an older/safe branch.
2. Write the following command to merge the modified branch.

```sh
git checkout main
git merge <branch_name>
```

- This code merges changes in `branch1` to that in `main`.



## **Topic - 5: Tracking Changes**

### <u>Unstage Changes</u>

```sh
git reset --all
```


### <u>Uncommit Changes</u>

```sh
git revert <commit_id>
```



## **Topic - 6: Miscalleneous**

### <u>Total Number Of Commits</u>

```sh
git rev-list --count HEAD
```

---
