# Remote editing on Vesta

Brief overview of your options for editing code on Vesta, with details on how to use the remote editing features of two popular editors.

One of the following methods

1. Edit a repo locally and push it to GitHub, then pull it on Vesta. This is the "brute force" method, but works just fine.
2. Use an SFTP client that support remote editing like Fetch (Mac Cornell site license), Bitvise [Windows], Filezilla? (free), or Forklift (Mac).
1. Configure your editor to connect to Vesta via SSH and edit files directly on the server. More elegant, but requires an internet connection and is more difficult to set up. **Except with BBEdit, where it is a built in feature**

## A brief history of the editor wars

[Editor wars](https://en.wikipedia.org/wiki/Editor_war) have been going on for a long time, mostly between two programs called Emacs and Vim. Both are still full-featured command line editors that have impressive communities. We assume you won't be using Emacs or Vim, though, because the learning curve is very steep for both, and more modern editors also have impressive communities with good features (but don't tell the Emacs or Vim people that).


There are other good choices:

1. [Atom](https://atom.io/) standalone [Mac, Linux, Windows]  
   **Some people like [Atom](https://atom.io/) with [Nuclide](https://nuclide.io/) [Mac, Linux].**
1. [Sublime](https://www.sublimetext.com/) [Mac, Linux, Windows]

1. [BBEdit](https://www.barebones.com/products/bbedit/) - “free forever” unlicensed use, pay to unlock pro features [Mac]
1. [Notepad++](https://notepad-plus-plus.org/) [Windows]

----
# EVERYTHING BELOW HERE IS DEPRECATED
----

## Remote editing with Atom + Nuclide [Mac, Linux]

Download [Atom](https://atom.io/). Go to Settings (`cmd + ,`) > Install. Search for "Nuclide" and click "Install"

![text](http://i.imgur.com/Vq8gU1n.png)

Go to your `~/.bash_profile` on your local machine and add this line:

```
alias vesta='ssh -p 22 YOUR_NETID@vesta.soc.cornell.edu -L 20022:[::1]:22 -L 9090:[::1]:9090'
```

Replace `YOUR_NETID` with your netid.

**Note: You may have to switch the two 9090 ports to a different number; you will get
an error message from Atom stating that "Server version is different from client version"
if this is the case. Change the numbers to the port shown in the error message**

Type `source ~/.bash_profile` to load the alias.

Go to your Terminal and type `vesta` to SSH into vesta.

Within your Terminal window connected to Vesta, open your `.bash_profile` and add this line: `export PATH=.:/usr/local/bin:$PATH`

Type `source ~/.bash_profile` to load the alias.

**You're configured!**

### How to actually edit things

Whenever you want to remotely edit a project, you will need to go to your Terminal and type `vesta` to open an SSH connection. You should leave this terminal window open in the background while you edit. You can also use this open terminal connection to do other things on Vesta like you normally would.

With the SSH connection open, go to Atom and click to add a remote project folder.

![text](http://i.imgur.com/xACPTr9.png)

Then hit the "+" button.

![text](http://i.imgur.com/PUfPU4a.png)

Finally, fill out the form like so:

![text](http://i.imgur.com/2N9Fjiv.png)

Hit "save" and you now have a profile for your remote repo. You can then connect!

You'll see a project overview.

![text](http://i.imgur.com/aQHGNd2.png)

Any changes you make locally will now be saved on Vesta! **Happy editing!**

## How to update Nuclide server

As the `brew` user: 

```
npm install -g nuclide
```
