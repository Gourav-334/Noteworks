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

- `ed25519` is the encryption used when generating key.
- It will prompt question for location to store keys, prefer choosing ~/.


### <u>Step - II</u>

- An agent is used to store various keys, password or passphrases etc.
- We confirm presence of SSH key by following command.

```sh
eval "$(ssh-agent -s)"
```


### <u>Step - III</u>

- Check for presence of `config` file in the created folder.

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

### <u>Uncommit Changes</u>

```sh
git revert <commit_id>         # Hard reset (loses all progress)
git reset --soft HEAD~1        # Soft reset without losing work
git reset --all                # Unstage all changes
```


### <u>Stashing</u>

- Stashing is used for saving temporary works.

```sh
git stash save "message"        # Same as 'git stash push'.
git stash list
git stash pop
git stash drop stash@{0}        # Removes most recent stash.
```


### <u>Removing Untracked Files</u>

```sh
git clean -fd
```

- `-f` means forceful cleaning, while `-d` means including untracked directories.
- So, `-fd` together is very destructive.


### <u>Rebasing</u>

| Type                     | Example                                   | Purpose                                         |
| ------------------------ | ----------------------------------------- | ----------------------------------------------- |
| **Basic rebase**         | `git rebase main`                         | Replay current branch commits onto `main`       |
| **Interactive rebase**   | `git rebase -i HEAD~3`                    | Edit, squash, reorder last 3 commits            |
| **Onto specific commit** | `git rebase --onto newbase oldbase topic` | Move `topic` branch from `oldbase` to `newbase` |
| **Abort**                | `git rebase --abort`                      | Cancel ongoing rebase                           |
| **Continue after fix**   | `git rebase --continue`                   | Resume rebase after conflict                    |
| **Skip**                 | `git rebase --skip`                       | Ignore a problematic commit                     |



## **Topic - 6: Bisection**

### <u>Introduction</u>

- Bisection helps us finding a buggy commit that caused certain problem.
- This is done using binary search on the commit list.
- It starts bisecting the middle commit in range from first & last commit.
- Then it changes direction as per our feedback, after we manually test.


### <u>Commands</u>

#### Start:

```sh
git bisect start
```

#### Feedback loop:

```sh
git bisect bad
git bisect good <good_commit>
```

- `<good_commit>` can be commit hash, tag or reference.
- Commit hash example - `41b3a2f`
- Tag example - `v1.2.0`
- Reference - `main~10`

#### Reset to head:

```sh
git bisect reset        # After we have found faulty commit.
```



## **Topic - 7: Hooks**

### <u>Introduction</u>

- **Hooks** are used for automating Git-based operations.
- Files for hooks are found at `.git/hook/`.
- Files there are stored with `.sample` extension, which has to be removed in order to be usable.
- They use Bash script code only to run.


### <u>Files Present</u>

- `pre-commit.sample`
- `commit-msg.sample`
- `pre-push.sample`
- `pre-base.sample`
- `post-merge.sample`
- `post-checkout.sample`

>**<u>Note</u>:**
>1. Remove the extension & allow runnable permission before running them.
>2. If any file is missing, we can simply create one.
>3. Scripts can be smartly written for conditional operations.


### <u>Example</u>

- Let's say we want commits to be in format shown below.

```
feat: add login support
fix: correct typo in loader
```

- Then we can edit `commit-msg` to form shown below.

```sh
#!/bin/bash
commit_msg=$(cat "$1")

if ! grep -qE "^(feat|fix|doc|refactor): .+" <<< "$commit_msg"; then
	echo "[ERROR] Commit message must start with feat|fix|doc|refactor"
	exit 1
fi
```



## **Topic - 8: Tagging**

```sh
git tag v1.0                              # Lightweight tag
git tag -a v1.0 -m "release notes"        # Annoted '-a' tag
git push origin v1.0
git push origin --tags                    # Push all tags
```



## **Topic - 9: Submodules**

### <u>Introduction</u>

- Used for bundling a repository with its dependencies, present in different directory.
- Dependencies retain their own commit history.
- Each submodule is kept in different directory.


### <u>Commands</u>

#### Add a submodule:

```sh
git submodule add https://github.com/user/repo.git path/to/subm
```

- Directly adding submodule in root directly is not allowed by Git.

#### Getting submodules:

- This is useful when we need sub-modules that are dependencies of a cloned repository.

```sh
git submodule init
git submodule update

# OR JUST

git clone --recurse-submodules <repo>
```

#### Pull changes:

- We can pull changes to submodules using the command given below.

```sh
cd submodules/ && git pull
```


### <u>Removing Submodule</u>

```sh
# Removing entry from .gitmodules
git config -f .gitmodules --remove-section submodule.path/to/subm
rm -rf .git/modules/path/to/submodule

git rm --cached path/to/subm
rm -rf path/to/subm
```



## **Topic - 10: Miscellaneous**

### <u>Total Number Of Commits</u>

```sh
git rev-list --count HEAD
```


### <u>Log Customization</u>

```sh
git log --oneline --graph --all --decorate
```

|     Flag     | Purpose                                    |
| :----------: | ------------------------------------------ |
| `--oneline`  | Compress each commit to one line           |
|  `--graph`   | Draws ASCII commit tree (branches, merges) |
|   `--all`    | Show all branches (not just current)       |
| `--decorate` | Show branch/tag names alongside commits    |

---
