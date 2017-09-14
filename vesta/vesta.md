# A Very Rough Guide to Using Vesta

# Logging in:

You can ssh into Vesta from the command line:
`ssh net_id@vesta.soc.cornell.edu`

If you need to create an ssh key there is a useful [tutorial here](https://help.github.com/articles/generating-an-ssh-key/)

You will need the Vesta admin to register your ssh publickey on Vesta in order to login.

Dependning on your system you may also need to specify the location of your .ssh private key before the address
e.g. `ssh ~/.ssh/id_rsa net_id@vesta.soc.cornell.edu`

# Navigating Vesta through shell commands:

Upon logging in you will be in your home directory, with the same name as your net_id

* `pwd` shows the current working directory. 
* `cd filepath` allows you to change directory
* `cd ..` allows you to go back to the previous directory
* `cd /Volumes/Server/project` takes you to your project directory, if it exists.
* `du -s -h *` will print the names of the files in the current directory and their sizes (useful to check if an output file is increasing in size).
* `df` will show the current processes running and their memory usage (useful for checking if a program is taking up a lot of memory)
* `ls -la` will show the files and folders in your current directory along with their permissions and owners.

# Use scp to transfer files between Vesta and your local machine.

The syntax to transfer a file from Vesta to your local machine is `scp filepath_on_vesta filepath_on_computer`

e.g. `scp net_id@vesta.soc.cornell.edu:/Users/net_id/filename /Users/Me/Desktop`

This saves the file filename on your desktop. 

[This link contains an explanation with additional examples](http://www.hypexr.org/linux_scp_help.php)

Generally, if you want to be transferring files to Vesta you should be using Github to push your local code
and then pull it into Vesta.
