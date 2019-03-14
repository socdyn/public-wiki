# Using Jupyter Notebooks with Vesta

Jupyter Notebooks can be used as a way to access files & run code in Vesta.
It is a particularly useful way of doing exploratory data analysis and of
writing and debugging code, both due to the functionality of the notebooks and
because it allows you to see your files and write code in the browser on your
local machine.

You can find out more about Jupyter Notebooks
[here](http://jupyter.readthedocs.io/en/latest/index.html)

#### We are not really supporting this but it works just fine if you get the port number correct. The chat transcript below descibes the process and serves as documentation pending a rewrite

Christopher Cameron  
[12:42] As far as ipython is concerned, you would need to use a custom port number.  
The issue is that there does not seem to be good tools to automatically allocate port numbers and avoid conflicts
[12:47] 
ok, try this:  
[12:47] 
on **Vesta**, run `jupyter notebook --no-browser`  
[12:48] 
and watch for the line 
`The Jupyter Notebook is running at: http://localhost:8888/?token=****`  
[12:49] 
that `localhost:xxxx` is the port number you need to forward and it will potentially change each time you start notebook on Vesta  
[12:50] 
also note the line:

```
Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=*****
```

[12:50] 
copy and paste that URL with the token  
[12:51] 
Next, on **YOUR** computer:  
[12:52] 
`ssh -N -L localhost:8888:localhost:xxxx netID@vesta.soc.cornell.edu`  

[12:53] Where `xxxx` is the port number jupyter is using on Vesta.  
[12:54] You might need to change `8888` if you already have jupyter running locally. 8895 worked for me.  

[12:56 PM] _Finally_, Paste the **URL with token** from Vesta into your web browser. edit the port number in the URL to match the **first** port number you used in the `ssh` tunnel command


Christopher Cameron  
[1:12 PM] if you add `-f` to `ssh` command, it goes to the background. This makes it a little troublesome to quit as the port forwarding just hangs out in the background

[1:13 PM] 
run `ps aux | grep xxxx` with `xxxx` as the port forward to find the process numbers (second value on each line)  

[1:14] then `kill zzz` where `zzz` is the process ID  

[1:15] it is way more convenient (in my opinion) if you leave off the `-f` in the ssh command so it stays in the Terminal and you can `ctrl-C` to end it.  


## Using BitVise SSH Client:
Go to the C2C tab, set the first port to whatever Vesta is running Jupyter on, and the second to whatever you want to connect to (I just use the same port). That's it.

For some reason, token authentication stopped working when I did this, so I had to set up password access, which is easy:
`jupyter notebook --gen-config
jupyter notebook password`


----
### Older Stuff, Pending edit 
----

## On Vesta:

You must first open up Jupyter Notbooks in headless mode on the server using
the command: `jupyter notebook  --no-browser --port 8888`

IMPORTANT: The `8888` is a four-digit port number. To avoid port conflicts we
are setting up a document where you can each claim a port number. Please choose a number > 5k since ports below this number are reserved by the OS. If multiple
users use the same port then it will result in conflicts. The number itself is
arbitrary but must be the same in all of these commands.

Please add a line to used_ports.txt (in this directory) when you have selected a port number to use.

## On your local machine:

You must have Jupyter Notebooks installed locally. You can find instructions on
downloading the latest version [here](http://jupyter.readthedocs.io/en/latest/install.html)

You can now connect to the Notebook on your local machine using an ssh tunnel.

To connect to the notebook use the command:
`ssh -i ~/.ssh/your_private_key -f -N -L localhost:8888:localhost:8888 your_net_id@vesta.soc.cornell.edu`

You can then open up your browser and type `http://localhost.8888` to open the notebook
or alternatively if you are a Mac or Linux user type `open http://localhost.8888` into the command line to
automatically open it in your default browser.

You will see the directory where you ran the command on Vesta and can access files
as if you are logged into Vesta.

To help to speed this process up you can save these two commands in a text file and
run it as a shell script. You will need to change the permissions to make it
executable using `chmod 755 file_name`. You can then run the file in the command line by typing `./file_name`

# Kernels

You can use either Python 2 or 3 with Jupyter by using [kernels](http://ipython.readthedocs.io/en/stable/install/kernel_install.html). You can switch kernels within the Jupyter interface and the current kernel you are using will be displayed in the top right of your screen.

The current installation on Vesta should provide you with the ability to use either version but you cannot see an option to use Python 2 then you can install the kernel type the following line into command line in Vesta, `python2 -m ipykernel install --user`. You should only need to do this once.

##Troubleshooting
You may run into issues with the port on your local machine already being in use.
This can happen sometimes if you disconnect and then reconnect to the notebook
locally. To solve this you can kill the processes running on the port using the
command `sudo kill $(sudo lsof -t -i:8888)` but remember to use caution when
using `sudo`!

## Using in combination with screen:
To use it most efficiently you should also familiarize yourself with [screen](https://github.com/socdyn/wiki/blob/master/vesta/use_screen.md).
This will allow you to keep your notebook running and maintain your local
connection to Vesta even when you are not connected in the command line.
All you need to do is open a screen session on vesta, run the command to start
the headless notebook, and then detach from the screen session. This will
keep the headless notebook running in the background. It is still recommended
that you frequently save your work as any interruption of Vesta service may
cause your screen session to end.
