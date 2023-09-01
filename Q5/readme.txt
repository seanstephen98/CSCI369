readme file for CSCI369 Assignment Question 5

Written by Sean Stephen


Requirements:

	1) Turn on the metatploitable VM and find out metatploitable's IP address (use ifconfig -v)
	
	2) Obtain a dictionary list of words (e.g. dirs.txt from CSCI369's Moodle Site) and save it in the same directory as this program.
	
	3) Make sure your attacker machine is on the same network as metatploitable
	

This program was written on a Kali VM on a NatNetwork configured on VirtualBox, and tested to work using Visual Studio Code against a metatploitable2 VM also connected to the same NatNetwork.


Steps to run:

	1) Use a compiler like VSC or type out the compile command with this as an example
		
		"/bin/python /home/kali/Desktop/lab10/crawler_mutillidae.py"
		
	2) You will be prompted to enter the file name of your dictionary file. Enter it.
	
	
	3) You will be prompted to enter the file name of a file you would like to send the list of found subdirectories to. Enter it.
	
	4) You will be prompted to enter metatploitable's IP. Enter it. (e.g. 10.0.2.5)
	
	
Expected output:

	Terminal:


		Please enter the dictionary file name (e.g. list.txt) : subdomains.txt

		Please enter the output file name (e.g. output.txt) : output.txt

		Please enter meta ip : 10.0.2.5

		Finding subdirectories... 

		http://10.0.2.5/mutillidae/images Exists


		All dictionary words tested against target website. Program ending now...
		
	
	File output:
	
		An output file with the name you entered will be created. If there are any valid subdirectories, they will be written there.