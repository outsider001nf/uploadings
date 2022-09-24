import socket
import os
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen()
command_list = []
started = True
print("server started")
def second_thread():
    while started == True:
        command = input("SERVER_ ")
        if command == "exit":
            started = False
def main():
    while started == True:
        client, addr = s.accept()
        client.send("303".encode("utf-8"))
        LReq = client.recv(1024)
        remote_user = LReq
        def requesting():
            request_command = client.send(remote_user + "@REMOTE")
            if request_command in command_list:
                if request_command == "open_browser":
                    os.system("start www.yandex.ru")
            else:
                client.send("!WRONG COMMAND!")
                requesting()

thr1 = threading.Thread(target = main)
thr2 = threading.Thread(target = second_thread)
thr1.start()
thr2.start()