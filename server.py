#!/usr/bin/env python3
import socket
import threading

lock = threading.Lock()

header_size = 1000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",3001))
server_socket.listen()
socket_list = []
def recv_all(sock):
    data = b''
    while True:
        message = sock.recv(4000)
        data += message
        if len(message) < 4000:
            break
    return data

def broadcastSockets(connection):
    while True:
        data = recv_all(connection)
        if data == b"":
            print("connection lost")
            with lock:
                socket_list.remove(connection)
            connection.close()
            break
        for i in socket_list:
            if i != connection:
                i.send(data)



if __name__ == "__main__":

    while True:
        socket_connection, _ = server_socket.accept()
        socket_list.append(socket_connection)
        thread = threading.Thread(target = broadcastSockets, args = [socket_connection], daemon = True)
        thread.start()



