readme for CSCI369 Assignment Q1

created by Sean Stephen

Preamble

	
	On backdoor techniques	
	
		When starting on the question, I was thinking of how to make the program usable.
		Reading up on sockets, on the victim machine, there will need to be a listener that constantly listens for messages.
		In the event that messages are no longer being sent, if the attacker sends a closing signal then the socket will close.
		Otherwise, the socket will continue listening for more messages even though the attacker is no longer sending them, causing the program to stall and not exit.
		
		Sockets also do not know when a message has finished being sent.
		Therefore, there would need to be either a fixed length message rule, with the attacker stating the number of chunks of data the victim should expect.
		Or the victim can look out for a delimeter to denote the end of a message amongst the chunks sent.
		Finally, an attacker side server program could be written but that is not part of this assessment
		Hence, I chose the delimeter route, as having to calculate number of chunks etc each time is too much work for running terminal commands.
		
		Back to letting the socket know the connection is closed, the assignment required the reverse shell to end when the & symbol is keyed.
		For sockets, this is relatively simple since I have already chosen the delimeter route anyways to scan the incoming message for it.
		However, the brief also mentioned that creating an interactive shell will be marked favourably.
		This does not work well with the delmeter method.
		An interactive shell can be spawned (e.g. typing * bash * after connecting) but entering only & (to end) will trigger an error in the shell, which if not caught in the victim program, will cause the program to crash.
		
		Another solution is to use a fifo file and piping the commands from a netcat backdoor into an interactive shell (code generated from msfconsole).
		This method creates a functioning interactive shell that works well.
		But I could not find a way to make this program parse the inputs for the & symbol.
		This method does not make use of the sockets library to launch the connection from the victim machine either.
		The interactive shell created is quite limited as well.
		
		I have spent too long on the question already.
		Time is ticking.
		I have decided to offer both options in my program.
		
	On realism of the program
	
		The program is made to be easy to use for the purposes of this assignment, but it is not reflective of a proper product.
		This is because of the two implementations of the requirements where only one can be chosen, and that even within my nat network, my dhcp ip address is dynamic and it is easier to just type in the ip address than to edit the code each time.
		As such, when the program is run, the user is prompted to first enter the attacker IP and then choose the implementation type.
		
	
	


Running the program


	initialising

		*attacker - issue the command
			
			nc -lvp 5555
			
		*victim - run the program backdoor.py (using terminal or code editor)

		You are first prompted to enter sockets or netcat to choose the options
		
			if sockets option is chosen, key in attacker's IP


	sockets option
	
		non-interactive shell - vi cannot be used at all. 
		
		syntax
		
			all commands SHOULD be encapsulated with @@
			
				e.g. @@ls -lrt@@
				
			however, any valid commands before the first @@ can run as well
			
				e.g. ls
				     @@ls -lrt@@
			results in ls being run twice
			
		
		error handling
		
			invalid commands issued before the first @@ do not return any errors
			
			invalid commands issued within the @@ encapsulation ends the program for attacker and causes the program on victim end to shutdown with an error code.
			
			
		exiting
		
			& - exits the program on both ends
			
			CTRL + C - exits the program on attacker side only
	


	netcat option
	
		
		NOTE - attacker IP needs to be manually updated in backdoor.py
		
		
		syntax
		
			no special syntax needed
			
	
		interactive shell is created but note the following: 
			netcat is finnicky. gedit is not able to be used.
			the only interactive text editor I tried to use that works is vi.
		
		
		error handling
		
			errors are echoed to our screen
			
			CTRL + C from anywhere (from what I have tested) will cause the nc connection to end, but the program will continue running on the victim's computer
			
		exiting
		
			exit - exits program in victim computer as well
			
			CTRL + C - exits program only on attacker side
			
			