# Viewing MongoDB data on Vesta using MongoDB Compass
1. Download the MongoDB Compass application: https://www.mongodb.com/products/compass  
2. On the Connect to Host page:    
 	A. Enter database credentials  
 	
		* Enter Host name  (e.g. 127.0.0.1)
		* Port number (default is 27017)  
		* Select Authentication -> Username/Password
		* Enter username and password for DB connection
 	B. Set up SSH Tunnel  
 	
 		* Click "Use Identity File"  
 		* SSH Hostname: vesta.soc.cornell.edu  
 		* SSH Tunnel Port: 22  
 		* SSH Username: <Vesta Username>  
 		* SSH Identity File: *select ~/.ssh/id_rsa from computer (or a custom keyfile for vesta if you created one)

 	C. Click Connect!


# Sidenote: if you're having problems logging in through the MongoDB Compass, try to SSH to Mongo first
1. Go to https://docs.mongodb.com/compass/master/connect/
2. Click on "Connect using SSH"
3. Read the section with ```ssh -L <local_port>:<mongodb_hostname>:<mongodb_port> <user>@<bastion_hostname> -fN```
4. Connect to vesta via SSH Tunnel using the script mentioned in the document
	A. We used ```ssh -N -i ~/.ssh/<ssh_key> -L localhost:27000:localhost:27017 <netid>@vesta.soc.cornell.edu```
5. Open MongoDB Compass on your local computer
6. Setup a new connection
	A. Enter `localhost` as the Hostname
	B. Enter `27000` as the Port
	C. Select `Username / Password` in Authentication and enter the relevant information
	D. Do not enter any other information for SSH in Compass
7. Click Connect!
