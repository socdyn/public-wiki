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
