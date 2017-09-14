#How to Copy Files Between Unix servers

###In Unix, how do I use the scp command to securely transfer files between two computers?

In Unix, you can use the scp command to copy files and directories securely between remote hosts without starting an FTP session or logging into the remote systems explicitly. The scp command uses SSH to transfer data, so it requires a password or passphrase for authentication. Unlike rcp or FTP, scp encrypts both the file and any passwords exchanged so that anyone snooping on the network can't view them.

Warning: Be careful when copying between hosts files that have the same names; you may accidently overwrite them.

The syntax for the scp command is:  
`scp [options] [[user@]host1:]filename1 ... [[user@]host2:]filename2`

For example, if user dvader is on a computer called empire.gov, and wants to copy a file called file1.txt to a directory called somedir in his account on a computer called deathstar.com, he would enter:  
`scp file1.txt dvader@deathstar.com:somedir`

Likewise, if he wanted to copy the entire contents of the somedir directory on deathstar.com back to his empire.gov account, he would enter:  
`scp -r dvader@deathstar.com:somedir somedir`

Similarly, if he is working on another computer, but wanted to copy a file called file1.txt from his home directory on empire.gov to a directory called somedir in his account on deathstar.com, he would enter:  
`scp dvader@empire.gov:file1.txt dvader@deathstar.com:somedir`

When using wildcards (e.g., * and ? ) to copy multiple files from a remote system, be sure to enclose the filenames in quotes. This is because the Unix shell, not the scp command, expands unquoted wildcards.

For more information about scp, consult its man page. At the Unix prompt, enter:  
`man scp`

originally posted at: [http://kb.iu.edu/data/agye.html](http://kb.iu.edu/data/agye.html)

Remember that you would need to have your SSH public key setup on the server you want to use to connect to Vesta. If you are on connecting *from* Vesta to another server that uses SSH keys, you will need your public key for that server configured on Vesta.   