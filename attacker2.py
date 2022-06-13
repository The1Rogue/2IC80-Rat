import socket
import sys

def notReal(HOST, PORT, command = "ls -l"):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	try:
		s.bind((HOST, PORT))
		s.listen(0)

		conn, addr = s.accept()

		conn.sendall(command.encode())

		result = conn.recv(1024)

		conn.close()

		print("\n" + result.decode())

	except:
		print("unable to set up host: wrong ip")

try:
	sys.argv[1]
	print("attempting to connect to target...")
	notReal(sys.argv[1], int(sys.argv[2]), sys.argv[3])
except:
        pass

