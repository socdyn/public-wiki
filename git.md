
# Git Tutorial

You will need git on your local machine. Git is a *version control* tool created by Linus Torvalds, the creator of Linux.

Git allows a group of people to contribute to a single project in an orderly way. You store the files and the project history locally on your computer, and when you make changes you push them up to the master version of the repoistory on GitHub.

## Install git

If you are using a Mac, you should be using [Homebrew](http://brew.sh/). In this case, install git with `brew install git`

If you are using Linux, use your package manager to install git. For instance, on Ubuntu you would `apt-get install git`. Maybe you use a Linux distro with yum, in which case you would `yum install git`.

If you have Windows, [go here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and install git that way.

## Git how-tos

### Repos and Cloning

Projects in git are called *repositories*, often abbreviated as *repos*.

Within a repo, you can store files and folders like you would normally on any computer. Think of a repo as containing a memory of all changes to all files for the life of the project.

The master version of the project is stored remotely on GitHub. You *clone* it to your local machine by issuing the command `git clone https://github.com/username/projectname`.

### Adding and Committing

When you want to make changes, you *add* the files you wish to change with `git add filename`. *Adding* is like telling git you want to track changes to a certain file.

When you have finished editing and want to stage your changes for incorporation into the master version of the repo, you *commit* your changes with `git commit -m 'description of changes'`. *Committing* tells git that you've made changes it should keep in its memory. Git allows you to retreive all commits made to a repo, so you can think of each commit as a stopping point with a discrete amount of work done. The commit message is quite important, it's easy to forget what you've done after awhile.

### Pushing

After you've committed changes locally, you'll want to *push* them to the master version of the repo on GitHub with `git push origin master`. "Origin" means the project's remote directory at GitHub, whereas "master" denotes the branch. Large projects will have multiple "branches", although we won't use them here. In general, branches can create huge headaches and messy merges.

After you *push*, your changes will be incorporated in the remote master directory at GitHub.

**Note: When you push from Vesta you may find that the commit does not register on your Github profile.
To ensure this does not happen you should make sure to set Vesta's Github configuration to your account
by entering the following two commands in the command line:**

```git config --global user.name "your github username"```


```git config --global user.email "the email address you use for github"```

### Pulling

Let's say you've been in Iceland for a week and you want to get caught up on the changes your colleagues have made to the repo. You'd navigate to your locally cloned repo and *pull* the latest changes from remote with `git pull origin master`. This will update all local files to match remote.

**Note: Pulls are the most common place where messy stuff happens with git.**

If you have made changes that are not incorporated into the remote master repo, pulling puts you in danger of having to do work.

Here are four scenarios that happen when you pull:

1. There are no changes. You just pull the updates! Easy peasy.
1. You have changes to files that don't exist in master, i.e. you added entirely new files. Things will be fine.
1. You have changes to existing files that don't conflict. For instance, maybe someone added some stuff to remote and you added stuff to the same file. Git will auto-merge the files to have both your additions and the remote additions in the file.
1. You have changes to existing files that conflict. For instance, maybe someone else re-wrote the same function that you also re-wrote. Git will require you to *manually* merge using a command line editor or the merge tool. This is a pain and nobody likes doing it.

**Simple rule: To avoid messy merges, pull before you edit.**

If you follow this rule, you will avoid most merge conflicts and simplify your life. You will start each editing session with the latest remote changes, and the only way you can run into a merge conflict is if someone edits the same line of code as you before you have a chance to commit your changes.

**Congrats, you are now a git pro**

## A simple workflow that won't break stuff

`clone` once to your local machine, then `pull -> add -> commit -> push`.

Code would look something like this:

```
git clone https://github.com/socdyn/wiki
```

Go to the repo with `cd /path/to/cloned/repo`.

```
git pull origin master
```

Edit your files, then

```
git add edited_file_1 edited_file_2
git commit -m 'I made changes to edited_file_1 and edited_file_2!'
git push origin master
```

**Congrats, you did it!**

# A note on storing passwords

The preferred method to cache your password with Git is the [`osxkeychain`](https://help.github.com/articles/caching-your-github-password-in-git/). This does not work on Vesta.

As a workaround you may edit your `~/.netrc` file (you probably have to create one too). The downside of this is you will have to store your password in plaintext on Vesta. This is undesirable at best and massively irresponsible at worst, depending on the repos you have access to.

However, you can use a personal access token (your profile -> settings -> personal access tokens). If you give the token `repo` access only, it will be able to push and pull repos without being able to touch other elements of your account. Plus you can revoke it remotely at any time, for any reason. This personal access token isn't perfect, but it's much better than storing a plaintext password.

You can see a [gist here](https://gist.github.com/technoweenie/1072829) for what your `.netrc` should look like. Don't forget to `chmod 600 .netrc` when you are done.

