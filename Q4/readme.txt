readme for Assignment question 4 on ransomware

created by Sean Stephen

To successfully run the program, I did the following.

	1) I changed directories to the root directory and make sure there is no important.txt, key.txt or their .asc versions
	
	2) I created a file important.txt using this command > echo "get outta mah swamp" > important.txt
	
	3) I ran the ransom.py script
	
	4) First I am prompted for a key by the program to store in key.txt. I type in > shrek
	
	5) Then I am prompted by GPG for the key for important.txt.asc. As mentioned in the brief, I simply type the key I saved previously > shrek
	
		note that this is an insecure passphrase and gpg will confirm if this is the intended key when it is used.
	
	6) Then I am prompted by GPG for the key for key.txt.asc. As mentioned in the brief, I simply type the key I saved previously > shrek
	
		note that I am unclear if the public key stated is the shrek key, or a public key generated with gpg, but both ways should work

	7) From here, important.txt and key.txt are deleted by the program and the ransom message is displayed.
	
	

To decrypt:

	This displays the attacker's saved key
	
		gpg --decrypt key.txt.asc
		
			enter shrek
			
	
	Then you are free to use the same command to decrypt important.txt.asc with the contents of key.txt
	

P.S.

	I am unsure what the requirements mean by "name your script as ransom and save it together with your public key".
	Because if the program is run, key.txt is going to be deleted anyways?? Hence I have just created a file key.txt with "shrek" as its contents.

	Also I believe it would make more sense to include important.txt.asc, key.txt.asc as well as the key in plaintext to show decryption of key.txt.asc,
	then usage of the decrypted key to then decrypt important.txt.asc to obtain its original contents.