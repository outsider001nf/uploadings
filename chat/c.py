import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = input("connect to ip_ ")
c.connect((addr, 20131))
while True:
	c.send(input("MSG_ ").encode("utf-8"))