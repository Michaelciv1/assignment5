import socket 
import sys
import os

HOST = "localhost"
PORT = 5552

print (sys.argv)

with socket.socket() as s:
    s.bind((HOST, PORT))
    print("Server hostname:", HOST, "port:", PORT)

    s.listen()
    (conn, addr) = s.accept()
    while True:
        fromClient = conn.recv(1024).decode('utf-8')
        print(fromClient)