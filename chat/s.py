import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 20131))
s.listen(2)
print("Server is ready to connect!")
while True:
	user, addr = s.accept()
	print("NEW USER!")
	user.send("Welcome!".encode("utf-8"))
	data = user.recv(1024)
	print(data.decode("utf-8"))