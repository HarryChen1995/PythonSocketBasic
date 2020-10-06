#!/usr/bin/env python3

import socket
import threading
class client:
    def __init__(self, ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))
        thread = threading.Thread(target= self.sendMessage)
        thread.daemon = True
        thread.start()
        while True:
            data = self.client_socket.recv(1024)
            if data == b'':
                raise RuntimeError("connection lost")
            print(data)


    def sendMessage(self):
        while True:
            message = input("Enter Message:")
            self.client_socket.send(bytes(message,"utf-8"))
if __name__ == "__main__":
    c = client("127.0.0.1", 4000)
    c.run()
