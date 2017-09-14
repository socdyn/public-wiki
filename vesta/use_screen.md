# Use Screen to keep your session running when you disconnect from Vesta

### Keep your processes running even when you disconnect from Vesta and/or turn off your local machine
from [howtogeek.com](http://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)
and [here](http://aperiodic.net/screen/quick_reference).

Screen is like a window manager for your console. It will allow you to keep multiple terminal sessions running and easily switch between them. It also protects you from disconnects, because the screen session doesn’t end when you get disconnected. This means you can keep a process running on Vesta even if your local machine is
turned off or not connected to the internet.


This is particularly useful if you have a process that will take a long time (e.g. scraping a website or API) or
if you want to [keep a Jupyter Notebook running on the server that can then be accessed locally](https://github.com/socdyn/wiki/blob/master/vesta/jupyter.md).

Now you can start a new screen session by just typing `screen` at the command line. Hit `Enter`, and you’ll be you'll see that your window has changed into a bash-3.2 shell. You will still be in the same directory as you were before (you can verify this by typing `pwd`) but you are in a clean window. Any processes you run in this
window will remain running as long as you detach from it correctly.

We strongly recommend you give your screen session a name, you can start a new screen with a name by typing
`screen -S name` where `name` is the your chosen name.

To **disconnect** (but leave the session running)
Hit `Ctrl + A` and then `D` in immediate succession (i.e. Press and hold Ctrl and type A, release, then hit D).
You will see the message *detached*  

To **reconnect**,
If you only have one screen session running:
Type `screen -DR` *(mnemonic: screen doctor)* and you will automatically reconnect to it.
If you have multiple sessions the command will print out a list of your screen sessions and
you can reconnect to any of them using the command `screen -r name`.

To **quit** you can either type `exit` and hit Enter, type `Ctrl+A` then `:quit`,
or type `Ctrl+A` then `Ctrl+\`, which will ask if you want to quit. This will
permanently close the screen session. `Ctrl + D` will also terminate your screen.

To **view the help** for screen, type `Ctrl + A` and then `Shift+?`.
This will show you the different options available.

#### The rest of the commands are helpful, but optional:

##### Connecting

To **reconnect to an existing session**, or create a new one if none exists.
If you have multiple sessions open you will see all of them.
`screen -Dr`

To **switch** from one screen window to another  
Hit `Ctrl + A` and then `Ctrl + A` in immediate succession.
Note the red and blue bar at the bottom of the terminal window. Will show the
window you are currently located in.

To **list** open screen windows  
Hit `Ctrl + A` and then `W` in immediate succession.
Additionally, you can write `screen -ls` to list all your screens open and to know which one you are attached or detached to.

To **detach** a screen without being currently connected to it you can use `screen -d name`. This may be helpful when you are attached to multiple screens
(which may happen if you do `screen -r name` while being attached to another screen).

##### Navigation

To **create a new window** inside of a running screen session  
Hit `Ctrl + A` and then `C` in immediate succession. You will see a new prompt.

To **switch** from one screen window to another  
Hit `Ctrl + A` and then `Ctrl + A` in immediate succession.
Note the red and blue bar at the bottom of the terminal window. Will show the
window you are currently located in.

**Rename** a screen window with `Ctrl + a` then `shift + a` (*vis* `A`). Type a name that helps you recall what the window is for.

**Scroll up** in history with `Ctrl + a` then `esc`. You can then use the cursor or scroll wheel to look back at the scroll buffer. Press `esc` once or `return` twice to exit copy mode.

---
Last but not least, you should get familiar with using `man specific-command` in the terminal. This gives you detailed information of all the installed commands available in bash.
For instance, if you write `man screen` you will see a brief description of the command and all the command-line options along with other useful information. This
is EXTREMELY helpful.
