# Wiki

**IMPORTANT**: before you make any changes, read this entire file. Refer to the [markdown formatting guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) liberally. Also read our [git tutorial](https://github.com/socdyn/wiki/blob/master/git.md) for an overview of best practices.

## Purpose

We are in the process of storing lab knowledge here. This includes:

1. Coding best practices
2. Vesta information (pacakges, maintenance, etc.)
3. Database information (schemas, etc.)
4. New member how-to's and tutorials
5. Other useful procedures and guidelines

Any lab member can edit the markdown (.md) files in this package! We have a purposefully open policy on editing here, so that this works like a wiki rather than a more traditional git repo with a few owners moderating pull requests.

### Note

If you copy-paste blocks of unformatted text, we may rollback your commits without warning and ask you to do it again. Please use some simple markdown formatting (click the [guide link](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)).

## Editing the wiki

If you have no idea what git is, check out our git tutorial at [git.md](https://github.com/socdyn/wiki/blob/master/git.md).

### Web editing this wiki (janky)

You can edit in a web browser by navigating to the file you want to edit and clicking the little pencil (top right). Be careful! This is not useful for long editing sessions.

### Local editing this wiki (preferred)

The preferred way to edit is to clone this repository to your local machine, then edit and push it back to GitHub.

```
cd /path/to/my/directory
git clone https://github.com/socdyn/wiki
```

Open the file you want to edit with your editor, do your thing, and then

```
git add . file_you_edited.md
git commit -m 'Descriptive commit message here'
git push origin master
```

### Local markdown editors
Mac users can get [MacDown] (https://github.com/MacDownApp/macdown) for local editing. Use the github2 style rendering for extra compatibility. 
