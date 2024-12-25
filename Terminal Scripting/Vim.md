# $\fbox{VIM}$





## **Topic - 1: Configuration File**

### <u>Step - I</u>

- Creating the configuration file.

```sh
vim ~/.vimrc
```


### <u>Step - II</u>

- In the file $vimrc$, right the following.

```vim
" This is a comment!

" Initialize vim plugin
call plug#begin('~/.vim/plugged')

" Your required plugins to add
Plug 'crusoexia/vim-monokai'

" Ending vim plugin
call plug#end()

" Your defualt configurations...examples
colorscheme monokai
set number
```

- Save & close the file.


### <u>Step - III</u>

- Open Vim.

```sh
vim
```

- Write the following command.

```vim
:PlugInstall
```


### <u>Step - IV</u>

1. Restart vim.
2. Open a file in Vim & see if changes occured.



## **Topic - 2: Actions**

### <u>Undo</u>

- Enter normal mode & press `U`.
