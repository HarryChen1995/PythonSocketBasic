#!/usr/bin/env python3
import socket
import threading

header_size = 1000

def encodeMessage(message):
    message_length = len(bytes(message ,"utf8"))
    header = ("{:>" + str(header_size) + "}").format(message_length)
    return bytes(header+message, "utf8")
def sendMessage(connection):
    while True:
        message = input()
        connection.send(encodeMessage(message))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 3001))


if __name__ == "__main__":
    thread = threading.Thread(target = sendMessage, args = [client_socket], daemon = True)
    thread.start()


    while True:
        header = client_socket.recv(header_size)
        if header == b"":
            print("conection lost")
            break
        size = int(header.decode("utf8"))
        data = client_socket.recv(size)
        if data == b"":
            print("connection lost")
            break
        print(data.decode("utf8"))

