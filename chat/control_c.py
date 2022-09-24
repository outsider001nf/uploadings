import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = input("IP to connect_ ")
c.connect((addr, 20131))
data = c.recv(1024).decode("utf-8")
if data == "303":
	set_usr = input("LOGIN_ ")
	c.send(set_usr)
	