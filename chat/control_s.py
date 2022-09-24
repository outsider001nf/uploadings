import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = "127.0.0.1"
port = 20131
s.bind((addr, port))
s.listen()
clients = []
nicks = []
addresses = []
while True:
	client, address = s.accept()
	client.send("303".encode("utf-8"))
	set_usr = client.recv(1024).decode("utf-8")
	cl = set_usr + "@guest_ ".encode("utf-8")