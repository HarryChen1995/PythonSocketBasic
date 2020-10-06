#!/usr/bin/env python3
import socket
import threading


class server:
    def __init__(self, ip , port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen()
        self.client_lists = []

    def sendMessage(self, conn):
        while True:
            data = conn.recv(1024)
            if data ==  b"":
                self.client_lists.remove(conn)
                conn.close()
                print("an connection closed")
            for client in self.client_lists:
                if client != conn:
                    client.send(data)

    def run(self):

        while True:
            client_socket , address = self.server_socket.accept()
            cthread = threading.Thread(target = self.sendMessage, args = (client_socket,))
            cthread.deamon = True
            cthread.start()
            self.client_lists.append(client_socket)
            print(f"new connection establihsed from IP: {address[0]} and Port {address[1]}")


if __name__ == "__main__":
    s = server("127.0.0.1", 4000)
    s.run()

