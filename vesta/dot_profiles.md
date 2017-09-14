# The python and networkx versions seem out of date...  
### AKA:

# "I need to update my bash profile"

Unix-like systems keep track of personal settings by keeping them as plain text in invisible files in your home directory `~/`
You can view hidden files by adding the `-a` option to the `ls` command:  
`% ls -la ~/`

You will see a few files whose names begin with a period. You need a .bash_profile for regular interactive mode and a .bashrc for when you use screen. These files include a setting that puts Homebrew Python (the updated one) in your search path.

The easiest way to get a working profile file is to copy one from another user with the right settings:  
`% cp /Users/cjc73/.bash_profile ~/.bash_profile`  
`% cp /Users/cjc73/.bashrc ~/.bashrc`  
`% cp /Users/cjc73/.screenrc ~/.screenrc`  

You may end up with some other settings copied too, so use at your own risk, especially if you already have these files on your account. Contact a Vesta admin for help.

#### Windows iPython users

If you are using Putty or Bitwise Client (i.e. you are on Windows), you may find that adding the following to `~.bashrc` resolves some issues with locales. The symptom of this issue is being able to `json.loads()` a UTF-8 string into a variable but getting an ASCII error when trying to view or print it.  When you type `locale` at the bash prompt, it reports the locale as `C` instead of some UTF-8 family locale. 

```bash
export LANG="en_US.UTF-8"
export LC_COLLATE="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
export LC_MESSAGES="en_US.UTF-8"
export LC_MONETARY="en_US.UTF-8"
export LC_NUMERIC="en_US.UTF-8"
export LC_TIME="en_US.UTF-8"
```
